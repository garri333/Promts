# 📚 PROMTS - Librería Colaborativa de Prompts & Agents

Repositorio compartido con **450+ prompts** y **170+ agents** especializados para trabajar con IA (OpenAI, Claude, GitHub Copilot).

## 🎯 Contenido

### 📖 library-prompts/ (450+ prompts)
24 categorías temáticas:
- **01-planificacio-arquitectura** - Planning, design, blueprints
- **02-sql-databases** - SQL optimization, PostgreSQL, CosmosDB
- **03-testing** - Jest, pytest, Playwright, xUnit
- **04-documentacio** - README, ADR, tutorials
- **05-dotnet-csharp** - Async, best practices, MCP
- **06-java-kotlin-spring** - Spring Boot, refactoring
- **07-python** - MCP servers, pytest, async patterns
- **08-cloud-azure** - Bicep, Terraform, Logic Apps
- **09-agents-instructions** - Custom agents, MCP patterns
- **10-git-cicd-github** - GitHub Actions, conventional commits
- **11-refactoring** - Code review, patterns, cleanup
- **12-mcp-servers** - Model Context Protocol
- **13-power-platform** - Power Apps, Power BI
- **14-utilitats** - Diverse utilities
- **15-blueprints** - Code exemplars
- **16-openai-examples** - OpenAI API examples (30+)
- **17-claude-prompt-library** - Claude specialist prompts (60+)
- **18-awesome-claude-prompts** - Community prompts (80+)
- **19-reddit-chatgpt-prompts** - Community Reddit
- **20-specialized-niches** - Domain-specific prompts
- **21-prompt-engineering-r** - Técnicas de prompt engineering (50+)
- **22-diffusiondb-image** - Image generation prompts
- **23-chatgpt-role-prompts** - "Act as X" roles (80+)
- **24-prompt-engineering** - Advanced techniques & patterns

### 🤖 library-agents/ (170+ agents)
Agentes especializados categorizados por dominio tecnológico.

### 🛠️ CHATGPT5/
Plantillas y metaprompts para crear nuevos prompts.

### 📊 scripts/
- `search_prompts.py` - Búsqueda avanzada por metadatas

---

## 🚀 Cómo Usar

### Opción 1: Clonar el repo
```bash
git clone https://github.com/tu-usuario/PROMTS.git
cd PROMTS
```

### Opción 2: Navegar por categorías
```
PROMTS/
└── library-prompts/
    └── categories/
        ├── 07-python/ (solo Python)
        ├── 03-testing/ (solo Testing)
        └── ...
```

### Opción 3: Buscar con script
```bash
python scripts/search_prompts.py --category python --tag async
```

---

## ✏️ Cómo Contribuir

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para instrucciones detalladas.

**Flujo rápido:**
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
author: "Tu Nombre"
description: "Breve descripción"
language: "ca" # Catalan / en / es
---

# Contenido del Prompt
```

---

## 📈 Estadísticas

- **Total prompts**: 450+
- **Total agents**: 170+
- **Categorías**: 24
- **Lenguajes**: Catalan, English, Spanish
- **Últimas actualización**: [Ver commits](../../commits/main)

---

## 📝 Licencia

MIT - Libre para usar, compartir y modificar.

---

## 💡 Recursos Adicionales

- **INDEX.md** - Catálogo completo con referencias
- **QUICK-REFERENCE.md** - Guía rápida
- **METADATA-SCHEMA.md** - Especificación de metadatas YAML

---

¿Preguntas? Abre un [Issue](../../issues) o contáctame.

**Happy Prompting! 🚀**
