---
title: "GitHub Actions CI/CD Pipeline"
version: "1.0"
category: "27-devops-deployment"
tags:
  - github-actions
  - ci-cd
  - automation
author: "garri333"
description: "Complete GitHub Actions CI/CD pipeline with matrix builds, caching, security scanning, and deployment automation"
language: "en"
created: "2026-02-22"
---

# GitHub Actions CI/CD Pipeline

## Objective

Design a **comprehensive GitHub Actions CI/CD pipeline** that covers the full software delivery lifecycle — from code quality checks and testing through security scanning to automated deployment with environment protection and approval gates.

---

## Context

GitHub Actions is the native CI/CD platform for GitHub repositories. A production pipeline must go beyond simple "build and test" — it needs matrix builds for cross-platform/version compatibility, aggressive caching for speed, secure secrets management, environment protection rules, artifact management, reusable workflows for DRY pipelines, and integrated security scanning via CodeQL.

---

## Prompt

You are a **Senior DevOps Engineer** building a production CI/CD pipeline for a full-stack application (Python backend + Node.js frontend). Generate complete GitHub Actions workflow files for the following pipeline stages:

### Pipeline Architecture

```
Push/PR → Lint & Format → Test (Matrix) → Security Scan → Build → Deploy
                                                              ↓
                                              staging (auto) → production (manual approval)
```

### 1. Matrix Builds

```yaml
strategy:
  fail-fast: false
  matrix:
    os: [ubuntu-latest, windows-latest]
    python-version: ["3.11", "3.12", "3.13"]
    node-version: ["18", "20", "22"]
    exclude:
      - os: windows-latest
        python-version: "3.11"
```

- Test backend across Python 3.11, 3.12, 3.13
- Test frontend across Node.js 18, 20, 22
- Cross-platform validation on Ubuntu and Windows
- Use `fail-fast: false` to see all failures, not just the first
- Include/exclude combinations for efficiency

### 2. Caching Strategy

```yaml
- name: Cache pip dependencies
  uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements*.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-

- name: Cache node_modules
  uses: actions/cache@v4
  with:
    path: |
      ~/.npm
      frontend/node_modules
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

- Cache pip, npm, Docker layers, and build artifacts
- Use `hashFiles()` for cache key generation
- Implement fallback restore keys for partial cache hits
- Cache Docker buildx layers with `actions/cache` or registry-based caching

### 3. Secrets Management

```yaml
env:
  DATABASE_URL: ${{ secrets.DATABASE_URL }}
  JWT_SECRET: ${{ secrets.JWT_SECRET }}

# Environment-scoped secrets
jobs:
  deploy-prod:
    environment: production   # Secrets scoped to this environment
    steps:
      - name: Deploy
        env:
          DEPLOY_TOKEN: ${{ secrets.PROD_DEPLOY_TOKEN }}
```

- Repository secrets for shared credentials
- Environment-specific secrets for deployment tokens
- Use `GITHUB_TOKEN` for GitHub API operations (auto-provided)
- Never echo secrets — use `::add-mask::` for dynamic values
- Rotate secrets quarterly with documented procedure

### 4. Environment Protection Rules

```yaml
jobs:
  deploy-staging:
    environment:
      name: staging
      url: https://staging.example.com
    # Auto-deploys on merge to main

  deploy-production:
    environment:
      name: production
      url: https://app.example.com
    needs: [deploy-staging]
    # Requires manual approval
```

Configure in GitHub Settings:
- **staging**: Auto-deploy, wait 5 min after staging tests pass
- **production**: Required reviewers (2+), wait timer (10 min), branch restriction (`main` only)
- **Deployment branch rules**: Only `main` can deploy to production
- **Required status checks**: All tests must pass before deploy

### 5. Approval Gates

```yaml
  deploy-production:
    needs: [deploy-staging, integration-tests]
    environment:
      name: production
    runs-on: ubuntu-latest
    steps:
      - name: Verify staging health
        run: |
          STATUS=$(curl -s -o /dev/null -w "%{http_code}" https://staging.example.com/health)
          if [ "$STATUS" != "200" ]; then
            echo "::error::Staging health check failed"
            exit 1
          fi
      - name: Deploy to production
        run: ./scripts/deploy.sh production
```

- Staging smoke tests must pass before production deployment
- Manual approval required from designated reviewers
- Automatic rollback on failed health checks post-deploy
- Slack/Teams notification on approval request

### 6. Artifacts Management

```yaml
- name: Upload test results
  uses: actions/upload-artifact@v4
  if: always()
  with:
    name: test-results-${{ matrix.os }}-py${{ matrix.python-version }}
    path: |
      reports/junit.xml
      reports/coverage.xml
      reports/htmlcov/
    retention-days: 30

- name: Upload build artifacts
  uses: actions/upload-artifact@v4
  with:
    name: docker-image-${{ github.sha }}
    path: build/image.tar
    retention-days: 5
```

- Upload test reports (JUnit XML, coverage) for every matrix combination
- Upload built Docker images as artifacts for deployment jobs
- Set appropriate retention periods (30 days for test results, 5 for builds)
- Use `actions/download-artifact@v4` in downstream jobs

### 7. Reusable Workflows

```yaml
# .github/workflows/reusable-test.yml
name: Reusable Test Workflow
on:
  workflow_call:
    inputs:
      python-version:
        required: true
        type: string
      run-integration:
        required: false
        type: boolean
        default: false
    secrets:
      DATABASE_URL:
        required: true

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ inputs.python-version }}
      - run: pip install -r requirements.txt
      - run: pytest --junitxml=reports/junit.xml
      - if: ${{ inputs.run-integration }}
        run: pytest tests/integration/ --junitxml=reports/integration.xml
```

Caller workflow:
```yaml
jobs:
  test:
    uses: ./.github/workflows/reusable-test.yml
    with:
      python-version: "3.12"
      run-integration: true
    secrets:
      DATABASE_URL: ${{ secrets.DATABASE_URL }}
```

- Extract common patterns into reusable workflows (`workflow_call`)
- Parameterize with inputs and secrets
- Share across repositories with `org/repo/.github/workflows/reusable.yml@main`
- Version reusable workflows with tags for stability

### 8. CodeQL Security Scanning

```yaml
- name: Initialize CodeQL
  uses: github/codeql-action/init@v3
  with:
    languages: python, javascript
    queries: +security-extended,security-and-quality

- name: Autobuild
  uses: github/codeql-action/autobuild@v3

- name: Perform CodeQL Analysis
  uses: github/codeql-action/analyze@v3
  with:
    category: "/language:${{ matrix.language }}"
```

- Run CodeQL on every PR and weekly on `main`
- Scan both Python and JavaScript/TypeScript
- Use `security-extended` query suite for comprehensive coverage
- Block PRs with high/critical severity findings
- Additional tools: `trivy` for container scanning, `gitleaks` for secret detection

### Complete Workflow Files to Generate

1. **`.github/workflows/ci.yml`** — Lint, test (matrix), coverage
2. **`.github/workflows/security.yml`** — CodeQL + dependency review + container scan
3. **`.github/workflows/deploy.yml`** — Build, push to registry, deploy staging → production
4. **`.github/workflows/reusable-test.yml`** — Reusable test workflow
5. **`.github/workflows/reusable-docker.yml`** — Reusable Docker build & push
6. **`.github/dependabot.yml`** — Automated dependency updates

### Performance Targets

| Metric                    | Target      |
|---------------------------|-------------|
| CI pipeline (lint + test) | < 5 minutes |
| Full pipeline to staging  | < 10 minutes|
| Cache hit rate             | > 80%       |
| Matrix combinations        | ≤ 12        |

---

## Output Format

Provide all workflow YAML files with inline comments explaining each decision, plus a `README-CI.md` documenting the pipeline architecture and how to add new services.

---

## Tags

`github-actions` · `ci-cd` · `automation` · `matrix-builds` · `caching` · `codeql` · `security` · `reusable-workflows` · `deployment`
