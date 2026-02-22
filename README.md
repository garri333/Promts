# 📚 PROMTS — Librería Colaborativa de Prompts & Agents para IA

[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Prompts: 480+](https://img.shields.io/badge/Prompts-480%2B-blue)](library-prompts/)
[![Agents: 180+](https://img.shields.io/badge/Agents-180%2B-orange)](library-agents/)
[![Categories: 28](https://img.shields.io/badge/Categories-28-purple)](library-prompts/categories/)
[![Last Updated](https://img.shields.io/badge/Updated-Feb%202026-red)]()
[![Compatible](https://img.shields.io/badge/Compatible-OpenAI%20|%20Claude%20|%20Copilot%20|%20Cursor-brightgreen)]()

Repositorio compartido con **480+ prompts** y **180+ agents** especializados para trabajar con IA — OpenAI (GPT-5.2), Claude (Opus 4.6), GitHub Copilot, Cursor, Codex, Gemini y más.

> **Actualización Feb 2026:** Nuevas categorías de AI Skills & Agents, ML/AI Models 2026, DevOps avanzado, y navegador del ecosistema de skills. 8 nuevos agentes especializados.

---

## 🌟 Novedades Febrero 2026

| Novedad | Descripción |
|---------|-------------|
| **4 nuevas categorías de prompts** | 25-ai-skills-agents, 26-ml-ai-models, 27-devops-deployment, 28-ecosystem-navigator |
| **8 nuevos agentes especializados** | skill-architect, multi-agent-orchestrator, codebase-analyst, security-guardian, ml-pipeline-engineer, devops-deployer, ecosystem-scout, release-manager |
| **Prompts para GPT-5.2** | Guía de migración desde GPT-4o (retiro 13 feb 2026) |
| **Prompts para Claude Opus 4.6** | Optimización de prompts para el nuevo modelo |
| **Prompts para Voxtral** | Transcripción open-source local (Mistral AI) |
| **Ecosystem navigator** | Prompts para navegar SkillsMP (66K+), MCP Market (31K+) |

---

## 🎯 Contenido

### 📖 library-prompts/ (480+ prompts)

**28 categorías temáticas:**

| # | Categoría | Descripción | Prompts |
|---|-----------|-------------|---------|
| 01 | `planificacio-arquitectura` | Planning, design, blueprints | ~20 |
| 02 | `sql-databases` | SQL optimization, PostgreSQL, CosmosDB | ~15 |
| 03 | `testing` | Jest, pytest, Playwright, xUnit | ~20 |
| 04 | `documentacio` | README, ADR, tutorials | ~15 |
| 05 | `dotnet-csharp` | Async, best practices, MCP | ~20 |
| 06 | `java-kotlin-spring` | Spring Boot, refactoring | ~15 |
| 07 | `python` | MCP servers, pytest, async patterns | ~25 |
| 08 | `cloud-azure` | Bicep, Terraform, Logic Apps | ~15 |
| 09 | `agents-instructions` | Custom agents, MCP patterns | ~20 |
| 10 | `git-cicd-github` | GitHub Actions, conventional commits | ~15 |
| 11 | `refactoring` | Code review, patterns, cleanup | ~20 |
| 12 | `mcp-servers` | Model Context Protocol | ~10 |
| 13 | `power-platform` | Power Apps, Power BI | ~10 |
| 14 | `utilitats` | Diverse utilities | ~15 |
| 15 | `blueprints` | Code exemplars | ~10 |
| 16 | `openai-examples` | OpenAI API examples | 30+ |
| 17 | `claude-prompt-library` | Claude specialist prompts | 60+ |
| 18 | `awesome-claude-prompts` | Community prompts | 80+ |
| 19 | `reddit-chatgpt-prompts` | Community Reddit | ~20 |
| 20 | `specialized-niches` | Domain-specific prompts | ~15 |
| 21 | `prompt-engineering-r` | Técnicas de prompt engineering | 50+ |
| 22 | `diffusiondb-image` | Image generation prompts | ~15 |
| 23 | `chatgpt-role-prompts` | "Act as X" roles | 80+ |
| 24 | `prompt-engineering` | Advanced techniques & patterns | ~20 |
| 25 | `ai-skills-agents` 🆕 | Creación de skills, orquestación multi-agente, MCP | 9 |
| 26 | `ml-ai-models` 🆕 | GPT-5.2, Claude Opus 4.6, HuggingFace, LoRA, Voxtral | 8 |
| 27 | `devops-deployment` 🆕 | Docker, GitHub Actions, Railway, IaC, seguridad | 6 |
| 28 | `ecosystem-navigator` 🆕 | SkillsMP, MCP Market, GitHub Topics, herramientas AI | 5 |

### 🤖 library-agents/ (180+ agents)

Agentes especializados categorizados por dominio tecnológico:

| Agente | Descripción | Dominio |
|--------|-------------|---------|
| `agent-selector` | Selecciona el mejor agente para la tarea | Meta |
| `skill-architect` 🆕 | Crea SKILL.md profesionales (estándar Anthropic) | Skills |
| `multi-agent-orchestrator` 🆕 | Coordina múltiples agentes especializados | Orchestration |
| `codebase-analyst` 🆕 | Analiza salud del codebase y deuda técnica | Quality |
| `security-guardian` 🆕 | Auditoría de seguridad OWASP, CVE, compliance | Security |
| `ml-pipeline-engineer` 🆕 | Pipeline ML completo con HuggingFace | ML/AI |
| `devops-deployer` 🆕 | Docker, CI/CD, Railway, Vercel, monitoring | DevOps |
| `ecosystem-scout` 🆕 | Descubre skills y herramientas AI emergentes | Discovery |
| `release-manager` 🆕 | Gestión de releases: semver, changelog, publish | Release |

### 📊 scripts/

- `search_prompts.py` — Búsqueda avanzada por metadatas

---

## 🚀 Cómo Usar

### Opción 1: Clonar el repo
```bash
git clone https://github.com/garri333/Promts.git
cd Promts
```

### Opción 2: Navegar por categorías
```
Promts/
└── library-prompts/
    └── categories/
        ├── 07-python/           (solo Python)
        ├── 03-testing/          (solo Testing)
        ├── 25-ai-skills-agents/ (Skills & Agents IA)   🆕
        ├── 26-ml-ai-models/     (ML/AI Models 2026)    🆕
        ├── 27-devops-deployment/ (DevOps & Deploy)      🆕
        ├── 28-ecosystem-navigator/ (Ecosystem tools)   🆕
        └── ...
```

### Opción 3: Buscar con script
```bash
python scripts/search_prompts.py --category python --tag async
python scripts/search_prompts.py --category ai-skills-agents --tag multi-agent
python scripts/search_prompts.py --category ml-ai-models --tag gpt5
```

### Opción 4: Usar agentes directamente
```markdown
Copia el contenido de cualquier archivo .agent.md y úsalo como
system prompt o instrucciones de agente en tu herramienta favorita.
```

---

## 🆕 Nuevas categorías (Feb 2026)

### 25. AI Skills & Agents Development (9 prompts)

Basado en el ecosistema de skills que ha explotado en 2026 con 100K+ skills disponibles en marketplaces.

| Prompt | Descripción |
|--------|-------------|
| `skill-creation-guide` | Guía completa para crear SKILL.md (estándar Anthropic dic 2025) |
| `multi-agent-orchestration` | Configurar workflows multi-agente (Codex Desktop Feb 2026) |
| `skill-discovery-optimization` | Encontrar las mejores skills en SkillsMP, MCP Market, skills.sh |
| `agent-memory-patterns` | Triple memoria: LanceDB + Git-Notes + File-based |
| `mcp-server-builder` | Construir servidores MCP desde cero (Python/TypeScript) |
| `openskills-universal-installer` | Instalar skills en todos los agentes con OpenSkills |
| `skill-quality-validation` | Validar calidad de skills (score 0-100) |
| `agent-self-improvement` | Agentes que aprenden de sus propios errores |
| `skill-marketplace-navigator` | Referencia rápida para los 6 principales marketplaces |

### 26. ML/AI & Models 2026 (8 prompts)

Prompts actualizados para los modelos y herramientas de febrero 2026.

| Prompt | Descripción |
|--------|-------------|
| `gpt5-migration-guide` | Migración GPT-4o → GPT-5.2 (retiro 13 feb 2026) |
| `claude-opus-optimization` | Optimización para Claude Opus 4.6 (3 feb 2026) |
| `huggingface-ml-pipeline` | Pipeline ML completo: datasets → training → deploy |
| `model-evaluation-benchmark` | Benchmarks: GLUE, SuperGLUE, MMLU, HumanEval, SWE-bench |
| `lora-finetuning` | Fine-tuning LoRA/QLoRA paso a paso |
| `gemini-integration` | Google Gemini 2.0 Flash: API, multimodal, plugins |
| `voxtral-voice-to-text` | Voxtral Transcribe 2: open-source local, <200ms |
| `model-comparison-2026` | Comparativa: GPT-5.2 vs Claude 4.6 vs Gemini vs DeepSeek |

### 27. DevOps & Deployment 2026 (6 prompts)

Prompts de producción para infraestructura moderna.

| Prompt | Descripción |
|--------|-------------|
| `docker-compose-production` | Multi-servicio con health checks, secrets, monitoring |
| `github-actions-ci-cd` | CI/CD completo: matrix, caching, CodeQL, approvals |
| `railway-deployment` | Railway.app: config, DB, dominios, PR environments |
| `infrastructure-as-code` | Terraform + Docker + Ansible: IaC patterns |
| `incident-response-runbook` | Runbooks de respuesta: P0-P4, RCA, post-mortem |
| `security-hardening` | OWASP Top 10, dependency scanning, TLS, CORS, CSP |

### 28. Ecosystem & Tools Navigator (5 prompts)

Navegación eficiente del ecosistema de skills y herramientas AI en 2026.

| Prompt | Descripción |
|--------|-------------|
| `skillsmp-explorer` | SkillsMP: 66,541+ skills, categorías, búsqueda eficiente |
| `mcp-market-guide` | MCP Market: 31,000+ skills, leaderboards, trending |
| `github-topics-monitor` | Monitorización sistemática de GitHub Topics |
| `ai-tools-comparison-2026` | Comparativa: Claude Code vs Codex vs Cursor vs Copilot |
| `community-resources-finder` | Reddit, Twitter/X, awesome lists, docs oficiales |

---

## ✏️ Cómo Contribuir

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para instrucciones detalladas.

Flujo rápido:

1. Fork el repositorio
2. Crea una rama: `git checkout -b feat/nuevo-prompt`
3. Añade tu prompt en la categoría correcta
4. Commit: `git commit -m "feat(categoria): descripcion"`
5. Push: `git push origin feat/nuevo-prompt`
6. Abre un Pull Request

---

## 📊 Estructura de Metadatas

Cada prompt tiene metadatas YAML para búsqueda avanzada:

```yaml
---
title: "Título del Prompt"
version: "1.0"
category: "07-python"
tags: ["python", "async", "patterns"]
author: "garri333"
description: "Breve descripción"
language: "en"  # en / es / ca
---

# Contenido del Prompt
```

---

## 📈 Estadísticas

| Métrica | Valor |
|---------|-------|
| Total prompts | **480+** |
| Total agents | **180+** |
| Categorías prompts | **28** |
| Categorías nuevas (Feb 2026) | **4** (25-28) |
| Agentes nuevos (Feb 2026) | **8** |
| Lenguajes | Catalan, English, Spanish |

### Desglose de fuentes:

| Fuente | Contribución |
|--------|-------------|
| Prompts propios | ~150 |
| OpenAI examples | 30+ |
| Claude prompt library | 60+ |
| Awesome claude prompts | 80+ |
| ChatGPT role prompts | 80+ |
| Prompt engineering | 50+ |
| AI Skills & Agents 🆕 | 9 |
| ML/AI Models 🆕 | 8 |
| DevOps Deployment 🆕 | 6 |
| Ecosystem Navigator 🆕 | 5 |

---

## 🔗 Repositorios hermanos

| Repositorio | Descripción | Skills |
|-------------|-------------|--------|
| [garri333/Skills](https://github.com/garri333/Skills) | 245+ skills reutilizables para agentes IA | 21 categorías |

> Los prompts de este repo complementan las skills del repo Skills. Usa prompts para instrucciones puntuales y skills para conocimiento persistente que el agente carga automáticamente.

---

## 🔍 Ecosistema de referencia (Feb 2026)

| Recurso | URL | Descripción |
|---------|-----|-------------|
| SkillsMP | [skillsmp.com](https://skillsmp.com) | 66,541+ skills indexadas |
| MCP Market | [mcpmarket.com](https://mcpmarket.com) | 31,000+ skills con leaderboards |
| anthropics/skills | [GitHub](https://github.com/anthropics/skills) | Skills oficiales Anthropic (14K+ ⭐) |
| openai/skills | [GitHub](https://github.com/openai/skills) | Skills oficiales OpenAI Codex |
| huggingface/skills | [GitHub](https://github.com/huggingface/skills) | Skills ML/AI HuggingFace |
| skills.sh | [skills.sh](https://skills.sh) | Directorio con leaderboard |
| r/ClaudeAI | [Reddit](https://reddit.com/r/ClaudeAI) | Comunidad principal de Claude |
| r/ClaudeCode | [Reddit](https://reddit.com/r/ClaudeCode) | Comunidad técnica de Claude Code |

---

## 📝 Licencia

MIT — Libre para usar, compartir y modificar.

---

## 💡 Recursos Adicionales

- [INDEX.md](library-prompts/INDEX.md) — Catálogo completo con referencias
- [QUICK-REFERENCE.md](library-prompts/QUICK-REFERENCE.md) — Guía rápida
- [METADATA-SCHEMA.md](library-prompts/METADATA-SCHEMA.md) — Especificación de metadatas YAML
- [CONTRIBUTING.md](CONTRIBUTING.md) — Cómo contribuir
- [INSTALLATION.md](INSTALLATION.md) — Guía de instalación detallada
- [COPILOT.INSTRUCTIONS.md](COPILOT.INSTRUCTIONS.md) — Instrucciones para GitHub Copilot

---

¿Preguntas? Abre un [Issue](https://github.com/garri333/Promts/issues) o contáctame.

*Última actualización: Febrero 2026 · [garri333](https://github.com/garri333)*

Happy Prompting! 🚀
