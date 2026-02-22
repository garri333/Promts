---
title: "Infrastructure as Code Patterns"
version: "1.0"
category: "27-devops-deployment"
tags:
  - iac
  - terraform
  - docker
  - ansible
  - infrastructure
author: "garri333"
description: "Infrastructure as Code patterns with Terraform, Docker, and Ansible for reproducible, version-controlled infrastructure"
language: "en"
created: "2026-02-22"
---

# Infrastructure as Code Patterns

## Objective

Implement **Infrastructure as Code (IaC)** best practices using Terraform, Docker, and Ansible. Cover module organization, state management, environment separation, testing, and CI/CD integration to achieve fully reproducible, version-controlled, and auditable infrastructure.

---

## Context

Infrastructure as Code replaces manual provisioning with declarative or imperative configuration files that can be versioned, reviewed, tested, and deployed like application code. The three pillars — Terraform (cloud provisioning), Docker (application packaging), and Ansible (configuration management) — together cover the full spectrum from infrastructure creation to application deployment.

---

## Prompt

You are a **Senior Infrastructure Engineer** designing an IaC strategy for a growing engineering team. Generate comprehensive patterns and templates for the following areas:

### 1. Terraform — Cloud Infrastructure

#### Module Organization

```
infrastructure/
├── modules/                    # Reusable modules
│   ├── networking/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   └── README.md
│   ├── database/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── compute/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── monitoring/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
├── environments/              # Environment-specific configurations
│   ├── dev/
│   │   ├── main.tf
│   │   ├── terraform.tfvars
│   │   └── backend.tf
│   ├── staging/
│   │   ├── main.tf
│   │   ├── terraform.tfvars
│   │   └── backend.tf
│   └── production/
│       ├── main.tf
│       ├── terraform.tfvars
│       └── backend.tf
├── global/                    # Shared resources (DNS, IAM)
│   ├── main.tf
│   └── backend.tf
└── scripts/
    ├── init-backend.sh
    └── plan-all.sh
```

#### Module Design Principles

```hcl
# modules/database/main.tf
resource "aws_db_instance" "main" {
  identifier     = "${var.project}-${var.environment}-db"
  engine         = var.engine
  engine_version = var.engine_version
  instance_class = var.instance_class

  allocated_storage     = var.allocated_storage
  max_allocated_storage = var.max_allocated_storage

  db_name  = var.db_name
  username = var.db_username
  password = var.db_password

  vpc_security_group_ids = var.security_group_ids
  db_subnet_group_name   = var.subnet_group_name

  backup_retention_period = var.environment == "production" ? 30 : 7
  multi_az               = var.environment == "production" ? true : false
  deletion_protection    = var.environment == "production" ? true : false

  tags = merge(var.common_tags, {
    Name        = "${var.project}-${var.environment}-db"
    Environment = var.environment
    ManagedBy   = "terraform"
  })
}

# modules/database/variables.tf
variable "project" {
  description = "Project name for resource naming"
  type        = string
}

variable "environment" {
  description = "Environment name (dev, staging, production)"
  type        = string
  validation {
    condition     = contains(["dev", "staging", "production"], var.environment)
    error_message = "Environment must be dev, staging, or production."
  }
}

variable "engine" {
  description = "Database engine"
  type        = string
  default     = "postgres"
}

# modules/database/outputs.tf
output "endpoint" {
  description = "Database connection endpoint"
  value       = aws_db_instance.main.endpoint
}

output "connection_string" {
  description = "Full connection string"
  value       = "postgresql://${var.db_username}:${var.db_password}@${aws_db_instance.main.endpoint}/${var.db_name}"
  sensitive   = true
}
```

Key principles:
- Every module has `variables.tf`, `outputs.tf`, and `README.md`
- Use `validation` blocks for input constraints
- Mark sensitive outputs with `sensitive = true`
- Tag all resources with `ManagedBy = "terraform"` and `Environment`
- Use conditional logic for environment-specific behavior
- Keep modules small and composable (single responsibility)

#### State Management

```hcl
# environments/production/backend.tf
terraform {
  backend "s3" {
    bucket         = "mycompany-terraform-state"
    key            = "production/terraform.tfstate"
    region         = "eu-west-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

State management rules:
- **Remote state** always (S3 + DynamoDB for AWS, GCS for GCP, Azure Blob)
- **State locking** enabled (DynamoDB table for AWS)
- **State encryption** at rest
- **One state file per environment** — never share state across environments
- **State isolation**: production state has restricted access (IAM policies)
- **Import existing resources**: `terraform import aws_instance.main i-1234567890`
- **State inspection**: `terraform state list`, `terraform state show`
- **Never edit state manually** — use `terraform state mv`, `terraform state rm`

#### Environment Separation

```hcl
# environments/production/main.tf
module "networking" {
  source      = "../../modules/networking"
  project     = "myapp"
  environment = "production"
  vpc_cidr    = "10.0.0.0/16"
  az_count    = 3
}

module "database" {
  source         = "../../modules/database"
  project        = "myapp"
  environment    = "production"
  instance_class = "db.r6g.large"
  engine_version = "16.2"
  # Production-specific: multi-AZ, 30-day backups, deletion protection
}

# environments/dev/main.tf
module "database" {
  source         = "../../modules/database"
  project        = "myapp"
  environment    = "dev"
  instance_class = "db.t4g.micro"
  engine_version = "16.2"
  # Dev-specific: single-AZ, 7-day backups, no deletion protection
}
```

Environment comparison:

| Aspect           | Dev            | Staging         | Production      |
|------------------|----------------|-----------------|-----------------|
| Instance size    | micro/small    | medium          | large/xlarge    |
| Multi-AZ         | No             | No              | Yes             |
| Backup retention | 7 days         | 14 days         | 30 days         |
| Delete protection| No             | Yes             | Yes             |
| Monitoring       | Basic          | Standard        | Enhanced + PagerDuty |
| Access           | Team-wide      | Team-wide       | Restricted IAM  |

### 2. Docker — Application Packaging

#### Multi-Stage Build Pattern

```dockerfile
# === Stage 1: Build ===
FROM python:3.12-slim AS builder

WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

COPY . .

# === Stage 2: Production ===
FROM python:3.12-slim AS production

# Security: non-root user
RUN groupadd -r appuser && useradd -r -g appuser -d /app -s /sbin/nologin appuser

WORKDIR /app

# Copy only installed dependencies
COPY --from=builder /install /usr/local
COPY --from=builder /build/app ./app

# Security: read-only filesystem where possible
RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
```

#### `.dockerignore` Pattern
```
.git
.github
__pycache__
*.pyc
.env
.env.*
node_modules
.vscode
*.md
tests/
docs/
.coverage
htmlcov/
```

### 3. Ansible — Configuration Management

#### Playbook Organization

```
ansible/
├── ansible.cfg
├── inventory/
│   ├── dev/
│   │   ├── hosts.yml
│   │   └── group_vars/
│   │       └── all.yml
│   ├── staging/
│   │   ├── hosts.yml
│   │   └── group_vars/
│   │       └── all.yml
│   └── production/
│       ├── hosts.yml
│       └── group_vars/
│           └── all.yml
├── playbooks/
│   ├── site.yml              # Master playbook
│   ├── deploy.yml            # Application deployment
│   ├── setup-server.yml      # Initial server setup
│   └── security-hardening.yml
├── roles/
│   ├── common/               # Base packages, users, SSH
│   │   ├── tasks/main.yml
│   │   ├── handlers/main.yml
│   │   ├── templates/
│   │   ├── files/
│   │   └── defaults/main.yml
│   ├── docker/               # Docker installation
│   ├── nginx/                # Nginx configuration
│   ├── app/                  # Application deployment
│   └── monitoring/           # Prometheus, node_exporter
└── vault/
    └── secrets.yml           # Encrypted with ansible-vault
```

#### Role Example

```yaml
# roles/common/tasks/main.yml
---
- name: Update package cache
  apt:
    update_cache: yes
    cache_valid_time: 3600
  become: yes

- name: Install essential packages
  apt:
    name:
      - curl
      - git
      - htop
      - ufw
      - fail2ban
      - unattended-upgrades
    state: present
  become: yes

- name: Configure automatic security updates
  template:
    src: 20auto-upgrades.j2
    dest: /etc/apt/apt.conf.d/20auto-upgrades
  become: yes

- name: Create application user
  user:
    name: "{{ app_user }}"
    shell: /bin/bash
    groups: docker
    append: yes
    create_home: yes
  become: yes

- name: Configure SSH hardening
  template:
    src: sshd_config.j2
    dest: /etc/ssh/sshd_config
    validate: "sshd -T -f %s"
  notify: restart sshd
  become: yes

- name: Configure firewall (UFW)
  ufw:
    rule: allow
    port: "{{ item }}"
    proto: tcp
  loop:
    - "22"
    - "80"
    - "443"
  become: yes

- name: Enable firewall
  ufw:
    state: enabled
    policy: deny
  become: yes
```

#### Ansible Vault for Secrets
```bash
# Encrypt secrets file
ansible-vault encrypt vault/secrets.yml

# Edit encrypted file
ansible-vault edit vault/secrets.yml

# Run playbook with vault
ansible-playbook -i inventory/production playbooks/site.yml --ask-vault-pass

# Use vault password file (CI/CD)
ansible-playbook -i inventory/production playbooks/site.yml --vault-password-file .vault_pass
```

### 4. IaC Testing Strategy

```
┌────────────┐     ┌──────────────┐     ┌──────────────┐
│   Lint     │────▶│   Unit Test  │────▶│ Integration  │
│ (tflint,   │     │ (terraform   │     │ (terratest,  │
│  hadolint, │     │  validate,   │     │  molecule)   │
│  yamllint) │     │  plan)       │     │              │
└────────────┘     └──────────────┘     └──────────────┘
```

- **Terraform**: `tflint` → `terraform validate` → `terraform plan` → `terratest`
- **Docker**: `hadolint` → `docker build` → `container-structure-test` → `trivy scan`
- **Ansible**: `ansible-lint` → `molecule test` (create → converge → verify → destroy)

### 5. CI/CD Integration

```yaml
# .github/workflows/terraform.yml
name: Terraform
on:
  pull_request:
    paths: ["infrastructure/**"]
  push:
    branches: [main]
    paths: ["infrastructure/**"]

jobs:
  plan:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        environment: [dev, staging, production]
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
      - run: terraform init
        working-directory: infrastructure/environments/${{ matrix.environment }}
      - run: terraform validate
      - run: terraform plan -out=plan.tfplan
      - name: Post plan to PR
        uses: actions/github-script@v7
        if: github.event_name == 'pull_request'
        # Post terraform plan output as PR comment

  apply:
    needs: plan
    if: github.ref == 'refs/heads/main'
    environment: ${{ matrix.environment }}
    runs-on: ubuntu-latest
    steps:
      - run: terraform apply -auto-approve plan.tfplan
```

---

## Output Format

Provide:
1. Complete directory structure for each tool
2. Template files for all modules/roles
3. CI/CD workflow for infrastructure changes
4. Environment-specific configuration examples
5. Testing setup and commands
6. Migration guide from manual infrastructure to IaC

---

## Tags

`iac` · `terraform` · `docker` · `ansible` · `infrastructure` · `state-management` · `modules` · `environments` · `testing` · `automation`
