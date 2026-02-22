---
title: "Docker Compose Production Setup"
version: "1.0"
category: "27-devops-deployment"
tags:
  - docker
  - compose
  - production
  - devops
author: "garri333"
description: "Production-grade Docker Compose orchestration"
language: "en"
created: "2026-02-22"
---

# Docker Compose Production Setup

## Objective

Design and implement a **production-grade Docker Compose** orchestration for a multi-service application stack. The configuration must cover health checks, restart policies, resource management, secrets handling, networking isolation, centralized logging, and a clear separation between development and production environments.

---

## Context

Docker Compose is the standard tool for defining and running multi-container Docker applications. In production, a naive `docker-compose.yml` is insufficient — you need health checks to ensure service availability, restart policies for resilience, volume management for data persistence, secrets for credential safety, resource limits to prevent runaway containers, and proper networking to isolate services.

---

## Prompt

You are a **Senior DevOps Engineer** specializing in containerized production deployments. Generate a complete, production-ready Docker Compose setup for the following stack:

### Services Required

| Service    | Image / Build         | Exposed Port | Internal Port | Notes                          |
|------------|-----------------------|--------------|---------------|--------------------------------|
| **nginx**  | `nginx:1.25-alpine`  | 80, 443      | 80, 443       | Reverse proxy, TLS termination |
| **frontend** | Build `./frontend`  | —            | 3000          | SPA served via nginx           |
| **backend**  | Build `./backend`   | —            | 8000          | REST API (FastAPI/Express)     |
| **db**       | `postgres:16-alpine`| —            | 5432          | Primary database               |
| **redis**    | `redis:7-alpine`    | —            | 6379          | Cache & session store          |

### Requirements for Each Service

#### 1. Health Checks
```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:PORT/health"]
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 40s
```
- **nginx**: Check HTTP 200 on `/health`
- **backend**: Check `/api/health` endpoint
- **db**: Use `pg_isready -U $POSTGRES_USER`
- **redis**: Use `redis-cli ping`
- **frontend**: Build-stage only, no runtime health check needed if served via nginx

#### 2. Restart Policies
```yaml
restart: unless-stopped   # For all production services
deploy:
  restart_policy:
    condition: on-failure
    delay: 5s
    max_attempts: 5
    window: 120s
```

#### 3. Volumes & Data Persistence
- `postgres_data:/var/lib/postgresql/data` — Named volume for database
- `redis_data:/data` — Named volume for Redis AOF/RDB persistence
- `nginx_certs:/etc/nginx/certs:ro` — TLS certificates (read-only)
- `nginx_conf:/etc/nginx/conf.d:ro` — Nginx config (read-only)
- `app_logs:/var/log/app` — Centralized log directory

#### 4. Secrets Management
```yaml
secrets:
  db_password:
    file: ./secrets/db_password.txt
  jwt_secret:
    file: ./secrets/jwt_secret.txt
  redis_password:
    file: ./secrets/redis_password.txt
```
- Never use environment variables for sensitive data in production
- Use Docker secrets or external secret managers (Vault, AWS SSM)
- Mount secrets as files: `/run/secrets/<secret_name>`

#### 5. Networking
```yaml
networks:
  frontend_net:
    driver: bridge
  backend_net:
    driver: bridge
    internal: true   # No external access
  db_net:
    driver: bridge
    internal: true   # Database isolated
```
- **nginx** → `frontend_net` + `backend_net`
- **frontend** → `frontend_net`
- **backend** → `backend_net` + `db_net`
- **db** → `db_net` only
- **redis** → `backend_net` only

#### 6. Resource Limits
```yaml
deploy:
  resources:
    limits:
      cpus: "1.0"
      memory: 512M
    reservations:
      cpus: "0.25"
      memory: 128M
```
Recommended limits:
| Service   | CPU Limit | Memory Limit | CPU Reserve | Memory Reserve |
|-----------|-----------|--------------|-------------|----------------|
| nginx     | 0.5       | 256M         | 0.1         | 64M            |
| frontend  | 0.5       | 256M         | 0.1         | 64M            |
| backend   | 1.0       | 512M         | 0.25        | 128M           |
| db        | 2.0       | 1G           | 0.5         | 256M           |
| redis     | 0.5       | 256M         | 0.1         | 64M            |

#### 7. Logging Configuration
```yaml
logging:
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "5"
    tag: "{{.Name}}/{{.ID}}"
```
- Use `json-file` driver with rotation for all services
- Alternative: `fluentd` or `gelf` driver for centralized logging (ELK/Grafana Loki)
- Add labels for log aggregation and filtering

### Production vs Development Compose Files

Generate **three** separate files:

1. **`docker-compose.yml`** — Base configuration (shared between environments)
2. **`docker-compose.override.yml`** — Development overrides (auto-loaded)
   - Bind mounts for hot reload (`./backend:/app`)
   - Exposed debug ports (5432 for db, 6379 for redis)
   - `restart: no`
   - No resource limits
   - Environment: `DEBUG=true`, `LOG_LEVEL=debug`
3. **`docker-compose.prod.yml`** — Production overrides
   - Built images with specific tags
   - Resource limits enforced
   - Secrets mounted
   - Internal networks only
   - Health checks enabled
   - Logging with rotation
   - Environment: `DEBUG=false`, `LOG_LEVEL=warning`

Usage:
```bash
# Development (uses base + override automatically)
docker compose up

# Production
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d

# Build for production
docker compose -f docker-compose.yml -f docker-compose.prod.yml build --no-cache
```

### Additional Production Checklist

- [ ] All images pinned to specific versions (no `latest`)
- [ ] Non-root users in all Dockerfiles
- [ ] `.dockerignore` in every build context
- [ ] Multi-stage builds for frontend and backend
- [ ] `depends_on` with `condition: service_healthy`
- [ ] Graceful shutdown signals (`stop_grace_period: 30s`)
- [ ] Backup strategy for `postgres_data` volume
- [ ] TLS certificates provisioned (Let's Encrypt / cert-manager)
- [ ] Environment-specific `.env` files excluded from VCS

---

## Output Format

Provide:
1. Complete `docker-compose.yml` (base)
2. Complete `docker-compose.override.yml` (dev)
3. Complete `docker-compose.prod.yml` (production)
4. Sample `nginx.conf` for reverse proxy
5. Sample `.env.production` with placeholder values
6. Directory structure diagram

---

## Tags

`docker` · `compose` · `production` · `devops` · `orchestration` · `health-checks` · `secrets` · `networking` · `resource-limits` · `logging`
