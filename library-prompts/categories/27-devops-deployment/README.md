# 27 - DevOps & Deployment 2026

> Production-grade DevOps, deployment, infrastructure, and security prompts for modern software delivery.

---

## Category Overview

This category covers the full spectrum of DevOps and deployment practices — from container orchestration and CI/CD pipelines to infrastructure as code, incident response, and security hardening. Each prompt provides actionable, production-ready patterns with real code examples.

---

## Prompts Index

| #  | Prompt                                                                  | Description                                                                                              |
|----|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 1  | [docker-compose-production.prompt.md](docker-compose-production.prompt.md) | Production Docker Compose setup with multi-service orchestration (frontend, backend, db, Redis, nginx), health checks, restart policies, volumes, secrets, networking isolation, resource limits, and logging configuration. Includes dev vs prod compose file separation. |
| 2  | [github-actions-ci-cd.prompt.md](github-actions-ci-cd.prompt.md)         | Complete GitHub Actions CI/CD pipeline with matrix builds, dependency caching, secrets management, environment protection rules, approval gates, artifact management, reusable workflows, and CodeQL security scanning. |
| 3  | [railway-deployment.prompt.md](railway-deployment.prompt.md)             | Railway.app deployment guide covering `railway.toml` configuration, environment variable scoping, PostgreSQL/Redis provisioning, custom domains with TLS, auto-deploy from GitHub, PR preview environments, and scaling strategies. |
| 4  | [infrastructure-as-code.prompt.md](infrastructure-as-code.prompt.md)     | Infrastructure as Code patterns using Terraform (module organization, state management, environment separation), Docker (multi-stage builds, security), and Ansible (playbook structure, roles, vault). Includes CI/CD integration and testing strategies. |
| 5  | [incident-response-runbook.prompt.md](incident-response-runbook.prompt.md) | Incident response framework with P0–P4 severity classification, escalation matrix, on-call rotation, communication templates (internal + customer-facing), root cause analysis (5 Whys), and structured blameless post-mortem generation. |
| 6  | [security-hardening.prompt.md](security-hardening.prompt.md)             | Comprehensive security hardening covering OWASP Top 10 mitigations with code examples, dependency scanning pipelines, secret detection (pre-commit + CI), HTTPS/TLS configuration (A+ rating), CORS policies, Content Security Policy, rate limiting, and JWT auth best practices. |

---

## Quick Start

1. **New project deployment?** Start with [docker-compose-production](docker-compose-production.prompt.md) + [railway-deployment](railway-deployment.prompt.md)
2. **Setting up CI/CD?** Use [github-actions-ci-cd](github-actions-ci-cd.prompt.md)
3. **Infrastructure provisioning?** Follow [infrastructure-as-code](infrastructure-as-code.prompt.md)
4. **Going to production?** Run through [security-hardening](security-hardening.prompt.md) checklist
5. **Preparing for incidents?** Set up [incident-response-runbook](incident-response-runbook.prompt.md)

---

## Technology Coverage

| Technology / Tool    | Prompts                                          |
|----------------------|--------------------------------------------------|
| Docker / Compose     | docker-compose-production, infrastructure-as-code |
| GitHub Actions       | github-actions-ci-cd                             |
| Railway.app          | railway-deployment                               |
| Terraform            | infrastructure-as-code                           |
| Ansible              | infrastructure-as-code                           |
| Nginx                | docker-compose-production, security-hardening    |
| PostgreSQL           | docker-compose-production, railway-deployment    |
| Redis                | docker-compose-production, railway-deployment    |
| TLS / HTTPS          | security-hardening                               |
| OWASP                | security-hardening                               |
| PagerDuty / Alerting | incident-response-runbook                        |

---

## Related Categories

- **26 - Testing & Quality** — Unit, integration, and E2E testing strategies
- **28 - Monitoring & Observability** — Metrics, logging, tracing, alerting
- **25 - Architecture & Design** — System design and architectural patterns

---

## Contributing

To add a new prompt to this category:

1. Create a `.prompt.md` file in this directory
2. Include YAML frontmatter with: `title`, `version`, `category`, `tags`, `author`, `description`, `language`
3. Follow the established structure: Objective → Context → Prompt → Output Format → Tags
4. Update this README with the new prompt entry
5. Submit a PR for review

---

*Category: 27-devops-deployment · Author: garri333 · Language: en · Last updated: 2026-02-22*
