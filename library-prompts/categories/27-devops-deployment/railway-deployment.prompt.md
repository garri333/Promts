---
title: "Railway.app Deployment Guide"
version: "1.0"
category: "27-devops-deployment"
tags:
  - railway
  - deployment
  - paas
  - cloud
author: "garri333"
description: "Complete Railway.app deployment guide covering configuration, databases, scaling, and PR environments"
language: "en"
created: "2026-02-22"
---

# Railway.app Deployment Guide

## Objective

Provide a **complete, actionable guide** for deploying full-stack applications on Railway.app — covering project configuration, environment variables, database provisioning, custom domains, auto-deploy workflows, PR preview environments, scaling strategies, and production best practices.

---

## Context

Railway.app is a modern PaaS that simplifies deployment with Git-based workflows, built-in databases, automatic HTTPS, and generous free-tier resources. It is an excellent choice for small-to-medium projects that need rapid deployment without managing infrastructure. Understanding `railway.toml`, environment variable scoping, and Railway's service model is critical for reliable production deployments.

---

## Prompt

You are a **Platform Engineer** experienced with Railway.app deployments. Generate a comprehensive deployment setup for a full-stack application with the following architecture:

### Application Architecture

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│  Frontend    │────▶│   Backend    │────▶│  PostgreSQL   │
│  (Vite/React)│     │  (FastAPI)   │────▶│  (Railway DB) │
└─────────────┘     └──────────────┘     └──────────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    Redis     │
                    │ (Railway DB) │
                    └──────────────┘
```

### 1. `railway.toml` Configuration

```toml
[build]
builder = "nixpacks"
buildCommand = "pip install -r requirements.txt"

[deploy]
startCommand = "uvicorn app.main:app --host 0.0.0.0 --port $PORT"
healthcheckPath = "/api/health"
healthcheckTimeout = 300
restartPolicyType = "on_failure"
restartPolicyMaxRetries = 5
numReplicas = 1

[deploy.resources]
# Memory and CPU configuration
# Adjust based on your plan limits
```

Provide separate `railway.toml` for:
- **Backend service** — Nixpacks Python build, Uvicorn start, health check
- **Frontend service** — Nixpacks Node build, static serve or Caddy
- **Worker service** (optional) — Celery/ARQ background tasks

### 2. Environment Variables

#### Variable Scoping Strategy

```
Project-level variables (shared across all services):
  APP_ENV=production
  LOG_LEVEL=warning

Service-specific variables:
  Backend:
    DATABASE_URL=${{Postgres.DATABASE_URL}}      # Railway reference variable
    REDIS_URL=${{Redis.REDIS_URL}}               # Railway reference variable
    JWT_SECRET=<generated>
    CORS_ORIGINS=https://myapp.example.com
    PORT=${{PORT}}                                # Auto-provided by Railway

  Frontend:
    VITE_API_URL=https://api.myapp.example.com
    VITE_APP_ENV=production
```

#### Railway Reference Variables
```
${{service_name.VARIABLE_NAME}}   — Reference another service's variable
${{Postgres.DATABASE_URL}}        — Auto-generated database connection string
${{Redis.REDIS_URL}}              — Auto-generated Redis connection string
${{shared.VARIABLE_NAME}}         — Shared variable group
```

Best practices:
- Use Railway reference variables (`${{...}}`) instead of hardcoding connection strings
- Set `APP_ENV` / `NODE_ENV` at the project level
- Sensitive values: generate via Railway CLI or dashboard (never commit)
- Use `.env.example` in repo for documentation purposes only

### 3. Database Provisioning

#### PostgreSQL
```bash
# Via Railway CLI
railway add --plugin postgresql

# Via Dashboard: Project → New → Database → PostgreSQL
```

Configuration:
- Railway auto-provisions PostgreSQL 16 with connection pooling
- `DATABASE_URL` is automatically injected as a service variable
- Enable **point-in-time recovery** on Pro plan
- Connection string format: `postgresql://user:pass@host:port/dbname`

#### Redis
```bash
railway add --plugin redis
```

Configuration:
- Auto-provisioned Redis 7 with persistence
- `REDIS_URL` injected automatically
- Configure `maxmemory-policy` via Redis CLI if needed

#### Database Migrations
```bash
# Run migrations on deploy via build command or release command
[deploy]
startCommand = "python -m alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port $PORT"
```

Alternative — use a **release command** pattern:
```toml
[deploy]
releaseCommand = "python -m alembic upgrade head"
startCommand = "uvicorn app.main:app --host 0.0.0.0 --port $PORT"
```

### 4. Custom Domains

```bash
# Via Railway CLI
railway domain add myapp.example.com

# DNS Configuration (at your domain registrar):
# Type: CNAME
# Name: myapp (or @ for root)
# Value: <generated>.up.railway.app
```

Setup checklist:
- [ ] Add custom domain in Railway dashboard → Service → Settings → Domains
- [ ] Configure CNAME record at DNS registrar
- [ ] Wait for DNS propagation (5–60 minutes)
- [ ] Railway auto-provisions Let's Encrypt TLS certificate
- [ ] Verify HTTPS is working: `curl -I https://myapp.example.com`
- [ ] Configure backend CORS to allow the custom domain
- [ ] Update frontend `VITE_API_URL` to use custom API domain

Multiple domains per service:
```
myapp.example.com          → Frontend service
api.myapp.example.com      → Backend service
admin.myapp.example.com    → Admin panel (optional)
```

### 5. Auto-Deploy Configuration

```
GitHub Integration:
  Repository: github.com/user/myapp
  Branch: main
  Auto-deploy: ON
  Root directory: /backend (for monorepo)
```

#### Monorepo Setup
```
# Service 1 — Backend
Root Directory: /backend
Watch Paths: /backend/**

# Service 2 — Frontend
Root Directory: /frontend
Watch Paths: /frontend/**

# Service 3 — Shared changes trigger all
Watch Paths: /shared/**, /libs/**
```

#### Deploy Triggers
- **Auto**: Push to `main` branch triggers deploy
- **Manual**: Via dashboard or `railway up` CLI command
- **Rollback**: One-click rollback to any previous deployment in dashboard
- **Redeploy**: Trigger rebuild without code change (useful for env var updates)

### 6. PR Preview Environments

```
GitHub Integration → Enable PR Environments

Each PR automatically gets:
  - Isolated environment with all services
  - Separate database instance
  - Unique URL: pr-<number>-<project>.up.railway.app
  - Auto-destroyed when PR is closed/merged
```

Configuration:
- Enable in Project Settings → Environments → Enable PR Environments
- Each PR environment inherits variables from the base environment
- Override variables per PR environment if needed
- Seed database with test data via migration or seed script

#### PR Environment Workflow
```
1. Developer opens PR → Railway creates isolated environment
2. All services deployed with PR code
3. Fresh database provisioned and migrated
4. Preview URL posted as PR comment
5. Team reviews with live preview
6. PR merged → environment destroyed
7. Main branch auto-deploys to production
```

### 7. Scaling Strategies

#### Horizontal Scaling
```toml
[deploy]
numReplicas = 3    # Multiple instances (Pro plan)
```

#### Vertical Scaling
- Adjust memory/CPU in Service → Settings → Resources
- Monitor usage via Railway Metrics dashboard
- Start small, scale up based on observed metrics

#### Scaling Decision Matrix

| Traffic Level     | Replicas | Memory  | CPU    | Database Plan |
|-------------------|----------|---------|--------|---------------|
| Development       | 1        | 512MB   | 0.5    | Starter       |
| Low (< 1K RPM)   | 1        | 1GB     | 1.0    | Starter       |
| Medium (1-10K RPM)| 2        | 2GB     | 2.0    | Pro           |
| High (> 10K RPM) | 3+       | 4GB     | 4.0    | Pro + Pooling |

#### Performance Optimization
- Enable Railway's built-in **connection pooling** for PostgreSQL
- Use Redis for session storage and API response caching
- Configure Uvicorn workers: `--workers $(nproc)`
- Enable gzip compression in the backend
- Use CDN (Cloudflare) in front of Railway for static assets

### 8. Railway CLI Essentials

```bash
# Install
npm install -g @railway/cli

# Login
railway login

# Link to existing project
railway link

# Deploy from local
railway up

# View logs
railway logs

# Open dashboard
railway open

# Run command in service context
railway run python manage.py migrate

# Set environment variable
railway variables set KEY=value

# List services
railway service list

# Switch environment
railway environment staging
```

### 9. Monitoring & Observability

- **Railway Metrics**: CPU, memory, network, disk usage per service
- **Logs**: `railway logs -f` for real-time log streaming
- **Alerts**: Set up via Railway dashboard or integrate with:
  - Sentry (error tracking)
  - Better Uptime / UptimeRobot (availability monitoring)
  - Grafana Cloud (metrics visualization)

### 10. Production Checklist

- [ ] All services have health checks configured
- [ ] Custom domains with TLS active
- [ ] Environment variables scoped correctly (no secrets in code)
- [ ] Database backups enabled (Pro plan)
- [ ] PR environments enabled for team workflow
- [ ] Monitoring and alerting configured
- [ ] Auto-deploy on `main` branch only
- [ ] Resource limits set appropriately
- [ ] CORS configured for production domains
- [ ] Rate limiting enabled on API endpoints

---

## Output Format

Provide:
1. Complete `railway.toml` for each service
2. Environment variable configuration table
3. Step-by-step deployment guide (first deploy + ongoing)
4. DNS configuration instructions
5. Monitoring setup recommendations

---

## Tags

`railway` · `deployment` · `paas` · `cloud` · `auto-deploy` · `preview-environments` · `scaling` · `database` · `custom-domains`
