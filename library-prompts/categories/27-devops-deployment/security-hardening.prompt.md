---
title: "Security Hardening Guide"
version: "1.0"
category: "27-devops-deployment"
tags:
  - security
  - owasp
  - hardening
  - authentication
  - tls
author: "garri333"
description: "Comprehensive security hardening covering OWASP Top 10, dependency scanning, secrets, TLS, CORS, CSP, rate limiting, and auth best practices"
language: "en"
created: "2026-02-22"
---

# Security Hardening Guide

## Objective

Implement a **comprehensive security hardening strategy** for web applications covering the OWASP Top 10 vulnerabilities, automated dependency scanning, secret detection in code, HTTPS/TLS configuration, CORS policies, Content Security Policy (CSP), rate limiting, and authentication/authorization best practices.

---

## Context

Security is not a feature — it's a continuous process. Modern web applications face threats from injection attacks, broken authentication, sensitive data exposure, and supply chain vulnerabilities. This guide provides actionable, defense-in-depth security measures that every production application must implement, with specific code examples and configuration templates.

---

## Prompt

You are a **Senior Application Security Engineer** performing a security hardening review. Generate a complete security hardening plan with implementation details for each area:

### 1. OWASP Top 10 (2021) — Mitigation Strategies

#### A01: Broken Access Control

```python
# FastAPI example — Role-based access control
from fastapi import Depends, HTTPException, status
from app.auth import get_current_user, require_role

@app.get("/admin/users")
async def list_users(user = Depends(require_role("admin"))):
    """Only accessible by admin users"""
    return await UserService.list_all()

@app.get("/users/{user_id}/profile")
async def get_profile(user_id: int, current_user = Depends(get_current_user)):
    """Users can only access their own profile"""
    if current_user.id != user_id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Access denied")
    return await UserService.get_profile(user_id)
```

Mitigations:
- Deny by default — every endpoint requires explicit authorization
- Implement RBAC (Role-Based Access Control) or ABAC (Attribute-Based)
- Validate resource ownership on every request (IDOR prevention)
- Disable directory listing on web servers
- Log and alert on access control failures
- Rate limit authentication endpoints

#### A02: Cryptographic Failures

```python
# Password hashing with bcrypt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

# NEVER: MD5, SHA1, SHA256 without salt for passwords
# NEVER: Store passwords in plaintext
# NEVER: Use reversible encryption for passwords
```

Mitigations:
- Use bcrypt/scrypt/Argon2 for password hashing (cost factor ≥ 12)
- TLS 1.2+ for all data in transit
- AES-256-GCM for data at rest encryption
- Classify data (PII, secrets, public) and encrypt accordingly
- Rotate encryption keys annually

#### A03: Injection

```python
# SQLAlchemy — Parameterized queries (SAFE)
result = db.execute(
    text("SELECT * FROM users WHERE email = :email"),
    {"email": user_input}
)

# NEVER: String concatenation in queries
# DANGEROUS: f"SELECT * FROM users WHERE email = '{user_input}'"

# Input validation with Pydantic
from pydantic import BaseModel, EmailStr, constr

class UserCreate(BaseModel):
    email: EmailStr
    username: constr(min_length=3, max_length=50, pattern=r'^[a-zA-Z0-9_]+$')
    password: constr(min_length=8, max_length=128)
```

Mitigations:
- Always use parameterized queries / ORM
- Validate and sanitize all user input (allowlist, not blocklist)
- Use Pydantic/marshmallow for strict input validation
- Escape output in templates (Jinja2 auto-escapes by default)
- Implement WAF rules for common injection patterns

#### A04: Insecure Design

- Threat modeling during design phase (STRIDE methodology)
- Security user stories: "As an attacker, I will try to..."
- Limit resource consumption per user (rate limits, quotas)
- Implement business logic validation server-side (not client-only)

#### A05: Security Misconfiguration

```yaml
# Nginx hardening
server {
    # Remove server version
    server_tokens off;
    
    # Security headers
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "DENY" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    add_header Permissions-Policy "camera=(), microphone=(), geolocation=()" always;
    
    # Disable unnecessary HTTP methods
    if ($request_method !~ ^(GET|POST|PUT|DELETE|PATCH|OPTIONS)$) {
        return 405;
    }
}
```

- Remove default credentials and sample applications
- Disable debug mode in production (`DEBUG=False`)
- Minimize installed packages (use slim/alpine Docker images)
- Disable unnecessary HTTP methods and features
- Review cloud security groups / network ACLs

#### A06: Vulnerable and Outdated Components

→ See Section 2 (Dependency Scanning)

#### A07: Identification and Authentication Failures

→ See Section 8 (Auth Best Practices)

#### A08: Software and Data Integrity Failures

```yaml
# Verify Docker image signatures
docker trust inspect --pretty myregistry/myimage:v1.0

# Pin dependencies with hashes
# requirements.txt
flask==3.0.0 --hash=sha256:abc123...

# Verify CI/CD pipeline integrity
# Use GitHub Actions with pinned commit SHAs, not tags
- uses: actions/checkout@a5ac7e51b41094c92402da3b24376905380afc29  # v4.1.6
```

#### A09: Security Logging and Monitoring Failures

```python
import logging
import structlog

logger = structlog.get_logger()

# Log security-relevant events
logger.warning("authentication_failed", 
    username=username, 
    ip_address=request.client.host,
    user_agent=request.headers.get("user-agent"))

logger.critical("authorization_bypass_attempt",
    user_id=current_user.id,
    resource=resource_id,
    action="delete")
```

#### A10: Server-Side Request Forgery (SSRF)

```python
# Validate URLs to prevent SSRF
import ipaddress
from urllib.parse import urlparse

BLOCKED_NETWORKS = [
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("127.0.0.0/8"),
    ipaddress.ip_network("169.254.0.0/16"),  # Link-local / AWS metadata
]

def is_safe_url(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return False
    try:
        ip = ipaddress.ip_address(parsed.hostname)
        return not any(ip in network for network in BLOCKED_NETWORKS)
    except ValueError:
        # Hostname — resolve DNS and re-check
        import socket
        resolved = socket.gethostbyname(parsed.hostname)
        ip = ipaddress.ip_address(resolved)
        return not any(ip in network for network in BLOCKED_NETWORKS)
```

### 2. Dependency Scanning

#### Automated Scanning Pipeline

```yaml
# GitHub Actions — Dependency scanning
- name: Python dependency audit
  run: |
    pip install pip-audit safety
    pip-audit --strict --desc
    safety check --full-report

- name: Node.js dependency audit
  run: |
    npm audit --audit-level=high
    npx better-npm-audit audit

- name: Container vulnerability scan
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: "myapp:${{ github.sha }}"
    format: "sarif"
    output: "trivy-results.sarif"
    severity: "CRITICAL,HIGH"

- name: Upload scan results
  uses: github/codeql-action/upload-sarif@v3
  with:
    sarif_file: "trivy-results.sarif"
```

#### Dependency Management Policy

| Action              | Frequency    | Tool                        | Block Deploy? |
|---------------------|--------------|-----------------------------|---------------|
| `pip-audit`         | Every PR     | pip-audit                   | Yes (high+)   |
| `npm audit`         | Every PR     | npm audit                   | Yes (high+)   |
| Container scan      | Every build  | Trivy / Grype               | Yes (critical) |
| License compliance  | Weekly       | FOSSA / license-checker     | Yes (copyleft) |
| Dependency updates  | Weekly       | Dependabot / Renovate       | No (auto-PR)  |
| Full SBOM           | Monthly      | Syft / CycloneDX            | No             |

### 3. Secret Detection

#### Pre-Commit Hook

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks

  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.4.0
    hooks:
      - id: detect-secrets
        args: ['--baseline', '.secrets.baseline']
```

#### CI Pipeline Secret Scanning

```yaml
- name: Gitleaks scan
  uses: gitleaks/gitleaks-action@v2
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    GITLEAKS_LICENSE: ${{ secrets.GITLEAKS_LICENSE }}

- name: TruffleHog scan
  run: |
    docker run --rm -v "$PWD:/repo" trufflesecurity/trufflehog:latest \
      git file:///repo --only-verified --fail
```

#### Secret Detection Rules
```
Patterns to detect:
- API keys: [A-Za-z0-9_]{20,}
- AWS keys: AKIA[0-9A-Z]{16}
- JWT tokens: eyJ[A-Za-z0-9-_]+\.eyJ[A-Za-z0-9-_]+
- Private keys: -----BEGIN (RSA |EC |DSA )?PRIVATE KEY-----
- Connection strings: (postgres|mysql|mongodb)://[^\s]+
- Generic passwords: (password|passwd|pwd|secret)\s*[=:]\s*[^\s]{8,}
```

#### What to Do When a Secret Is Leaked

1. **Immediately rotate** the compromised credential
2. **Audit access logs** for unauthorized use
3. Run `git filter-repo` or BFG Repo-Cleaner to remove from history
4. **Never** just delete the file — the secret is in Git history
5. Add the pattern to `.gitleaks.toml` to prevent recurrence

### 4. HTTPS / TLS Configuration

#### Nginx TLS Configuration (A+ Rating)

```nginx
server {
    listen 443 ssl http2;
    server_name myapp.example.com;

    # Certificates (Let's Encrypt)
    ssl_certificate /etc/letsencrypt/live/myapp.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/myapp.example.com/privkey.pem;

    # TLS configuration
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;

    # OCSP Stapling
    ssl_stapling on;
    ssl_stapling_verify on;
    resolver 1.1.1.1 8.8.8.8 valid=300s;

    # HSTS (1 year, include subdomains, preload)
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

    # Session configuration
    ssl_session_timeout 1d;
    ssl_session_cache shared:SSL:10m;
    ssl_session_tickets off;

    # DH parameters (generate: openssl dhparam -out dhparam.pem 4096)
    ssl_dhparam /etc/nginx/dhparam.pem;
}

# Redirect HTTP to HTTPS
server {
    listen 80;
    server_name myapp.example.com;
    return 301 https://$server_name$request_uri;
}
```

Verify with: `https://www.ssllabs.com/ssltest/`

### 5. CORS Configuration

```python
# FastAPI CORS configuration
from fastapi.middleware.cors import CORSMiddleware

# PRODUCTION — Restrictive
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://myapp.example.com",
        "https://admin.myapp.example.com",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["Authorization", "Content-Type", "X-Request-ID"],
    expose_headers=["X-Request-ID", "X-RateLimit-Remaining"],
    max_age=600,  # Cache preflight for 10 minutes
)

# NEVER in production:
# allow_origins=["*"]           # Allows any origin
# allow_methods=["*"]           # Allows any method
# allow_headers=["*"]           # Allows any header
# allow_credentials=True + allow_origins=["*"]  # This is actually blocked by browsers
```

#### CORS Decision Matrix

| Scenario                  | `allow_origins`         | `allow_credentials` |
|---------------------------|-------------------------|---------------------|
| Public API (no auth)      | `["*"]`                 | `False`             |
| SPA + API (same domain)   | Not needed              | N/A                 |
| SPA + API (diff domain)   | Explicit list           | `True`              |
| Mobile app + API          | Explicit list           | `True`              |
| Third-party integrations  | Configurable allowlist  | `False`             |

### 6. Content Security Policy (CSP)

```python
# FastAPI CSP middleware
from starlette.middleware.base import BaseHTTPMiddleware

class CSPMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        
        csp_directives = [
            "default-src 'self'",
            "script-src 'self' 'nonce-{nonce}'",  # Use nonce for inline scripts
            "style-src 'self' 'unsafe-inline'",     # Consider nonce for styles too
            "img-src 'self' data: https:",
            "font-src 'self' https://fonts.gstatic.com",
            "connect-src 'self' https://api.myapp.example.com",
            "frame-ancestors 'none'",               # Prevent clickjacking
            "base-uri 'self'",
            "form-action 'self'",
            "object-src 'none'",
            "upgrade-insecure-requests",
        ]
        
        response.headers["Content-Security-Policy"] = "; ".join(csp_directives)
        return response
```

#### CSP Deployment Strategy

1. **Report-Only mode** first: `Content-Security-Policy-Report-Only`
2. Monitor reports for 1–2 weeks using a reporting endpoint
3. Fix violations and add necessary exceptions
4. Switch to enforcing mode: `Content-Security-Policy`
5. Iterate: tighten policy over time

### 7. Rate Limiting

```python
# FastAPI rate limiting with slowapi
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="redis://localhost:6379"
)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Endpoint-specific limits
@app.post("/api/auth/login")
@limiter.limit("5/minute")           # Aggressive limit on auth
async def login(request: Request):
    ...

@app.get("/api/items")
@limiter.limit("100/minute")         # Standard API limit
async def list_items(request: Request):
    ...

@app.post("/api/upload")
@limiter.limit("10/hour")            # Very limited for expensive operations
async def upload_file(request: Request):
    ...
```

#### Rate Limiting Strategy

| Endpoint Category       | Rate Limit         | Key       | Response on Exceed |
|------------------------|--------------------|-----------|-------------------|
| Authentication         | 5/min, 20/hour     | IP        | 429 + Retry-After |
| Password reset         | 3/hour             | IP + email| 429 + Retry-After |
| API (authenticated)    | 100/min            | User ID   | 429 + Retry-After |
| API (unauthenticated)  | 30/min             | IP        | 429 + Retry-After |
| File upload            | 10/hour            | User ID   | 429 + Retry-After |
| Webhook endpoints      | 1000/min           | API key   | 429               |

#### Response Headers
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 42
X-RateLimit-Reset: 1708646400
Retry-After: 30
```

### 8. Authentication Best Practices

#### JWT Configuration

```python
from datetime import datetime, timedelta, timezone
import jwt

JWT_CONFIG = {
    "algorithm": "RS256",            # Use asymmetric keys in production
    "access_token_expire": timedelta(minutes=15),     # Short-lived
    "refresh_token_expire": timedelta(days=7),        # Longer-lived
    "issuer": "myapp.example.com",
    "audience": "myapp-api",
}

def create_access_token(user_id: int, roles: list[str]) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": str(user_id),
        "roles": roles,
        "iat": now,
        "exp": now + JWT_CONFIG["access_token_expire"],
        "iss": JWT_CONFIG["issuer"],
        "aud": JWT_CONFIG["audience"],
        "jti": str(uuid.uuid4()),    # Unique token ID for revocation
    }
    return jwt.encode(payload, PRIVATE_KEY, algorithm=JWT_CONFIG["algorithm"])
```

#### Authentication Checklist

- [ ] Passwords: bcrypt with cost ≥ 12 (or Argon2id)
- [ ] JWT: RS256, short expiry (15 min), refresh token rotation
- [ ] MFA: TOTP (Google Authenticator) or WebAuthn/FIDO2
- [ ] Session: HttpOnly, Secure, SameSite=Strict cookies
- [ ] Brute force: Rate limit + account lockout (temporary, 15 min)
- [ ] Password policy: Minimum 8 chars, check against HaveIBeenPwned API
- [ ] OAuth2: Use PKCE for public clients (SPAs, mobile)
- [ ] Logout: Invalidate tokens server-side (token blacklist in Redis)
- [ ] Password reset: Time-limited tokens (1 hour), single use
- [ ] Account enumeration: Same response for "user not found" and "wrong password"

#### Security Headers Summary

```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 0  (deprecated, CSP is preferred)
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
Cache-Control: no-store (for sensitive pages)
```

### 9. Security Audit Automation

```yaml
# Complete security CI pipeline
name: Security Audit
on:
  push:
    branches: [main]
  pull_request:
  schedule:
    - cron: "0 6 * * 1"  # Weekly Monday 6 AM

jobs:
  sast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Bandit (Python SAST)
        run: pip install bandit && bandit -r app/ -f json -o bandit.json
      - name: Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: p/owasp-top-ten

  secrets:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: gitleaks/gitleaks-action@v2

  dependencies:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install pip-audit && pip-audit --strict
      - run: npm audit --audit-level=high

  container:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: docker build -t myapp:scan .
      - uses: aquasecurity/trivy-action@master
        with:
          image-ref: "myapp:scan"
          severity: "CRITICAL,HIGH"
          exit-code: 1
```

---

## Output Format

Provide:
1. OWASP Top 10 mitigation checklist with code examples
2. Security headers configuration (Nginx + application)
3. Rate limiting implementation (Redis-backed)
4. Authentication setup with JWT best practices
5. CI/CD security scanning pipeline
6. Security audit report template

---

## Tags

`security` · `owasp` · `hardening` · `tls` · `cors` · `csp` · `rate-limiting` · `authentication` · `dependency-scanning` · `secret-detection`
