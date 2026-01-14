# 📚 BIBLIOTECA DE PROMPTS - MULTI-PLATAFORMA

Aquesta biblioteca conté una col·lecció organitzada de **450+ prompts** de 9 fonts principals (GitHub Copilot, OpenAI, Claude, Awesome Claude, Reddit ChatGPT Genius, Reddit PromptEngineering, DiffusionDB, Awesome ChatGPT Prompts, Awesome Prompt Engineering), dissenyada per trobar ràpidament els millors prompts segons el tipus de projecte i necessitat.

## 🆕 SISTEMA DE METADADES (Nou!)

Aquesta biblioteca utilitza **YAML frontmatter** per afegir metadades estructurades a cada prompt, permetent:

✅ **Búsqueda multi-dimensional** per domini, framework, tècniques i métriques  
✅ **Reutilització amb diferents frameworks** (OpenAI Agents, LangChain, AutoGen, CrewAI)  
✅ **Tracking de rendiment** amb ratings, costos i latència  
✅ **Versionat i auditoría** amb historial complet  
✅ **A/B testing** entre versions de prompts  

📖 **Llegeix**: [METADATA-SCHEMA.md](METADATA-SCHEMA.md) per detalls complets  
🔍 **Cerca**: Usa [scripts/search_prompts.py](scripts/search_prompts.py) per búsquedas avançades  

## 🚀 Com utilitzar aquesta biblioteca

### Opció 1: Usa el Prompt Selector (Recomanat)
1. Obre el fitxer [`prompt-selector.prompt.md`](prompt-selector.prompt.md)
2. Diga a Copilot quin tipus de projecte vols fer
3. Et recomanarà els millors prompts per cada fase

### Opció 2: Búsqueda per Metadades (Nou!)
```python
# Exemple: Trobar prompts production-ready amb rating alt
python scripts/search_prompts.py

# Búsqueda avançada:
# - Per domini: Planning, Testing, Documentation, etc.
# - Per framework: GitHub Copilot, LangChain, OpenAI Agents
# - Per qualitat: rating >= 4.5, production_ready
# - Per cost/latència: optimització de rendiment
```

### Opció 3: Consulta l'INDEX
1. Obre el fitxer [`INDEX.md`](INDEX.md) per veure tots els prompts classificats
2. Busca per categoria o per funcionalitat
3. Clica directament al link del prompt que necessitis

### Opció 4: Navega per Categories
Entra a la carpeta de la categoria que necessitis:
- `📁 01-planificacio-arquitectura/` - Planificació i disseny de projectes
- `📁 02-sql-databases/` - Optimització SQL i bases de dades
- `📁 03-testing/` - Tests unitaris, integració i e2e
- `📁 04-documentacio/` - README, ADR, tutorials
- `📁 05-dotnet-csharp/` - Desenvolupament .NET/C#
- `📁 06-java-kotlin-spring/` - Desenvolupament Java/Kotlin
- `📁 07-python/` - Desenvolupament Python
- `📁 08-cloud-azure/` - Azure i cloud
- `📁 09-agents-instructions/` - Agents i custom instructions
- `📁 10-git-cicd-github/` - Git, CI/CD i GitHub Actions
- `📁 11-refactoring/` - Refactoring i code review
- `📁 12-mcp-servers/` - Model Context Protocol servers
- `📁 13-power-platform/` - Power Apps, Power BI
- `📁 14-utilitats/` - Utilitats diverses
- `📁 15-blueprints/` - Generadors de blueprints
- `📁 16-openai-examples/` - Prompts d'OpenAI (30+ exemples pràctics)
- `📁 17-claude-prompt-library/` - Prompts de Claude (60+ prompts versàtils)
- `📁 23-chatgpt-role-prompts/` - 🆕 "Act as X" prompts (80+ rols - 142k⭐)
- `📁 24-prompt-engineering/` - 🆕 Tècniques PE, patrons avançats, tools

## 🎯 Workflow recomanat per projectes nous

```
1. PLANIFICACIÓ → structured-autonomy-plan.prompt.md
2. GENERACIÓ DE CODI → structured-autonomy-generate.prompt.md  
3. IMPLEMENTACIÓ → structured-autonomy-implement.prompt.md
4. TESTING → breakdown-test.prompt.md + [framework-test].prompt.md
5. DOCUMENTACIÓ → create-readme.prompt.md
6. GIT/CI → conventional-commit.prompt.md + create-github-action-workflow-specification.prompt.md
```

## 📎 Com afegir prompts al teu projecte

1. **Copia el link** del prompt que necessitis
2. **Enganxa'l al xat de Copilot** amb @
3. Copilot carregarà el prompt automàticament

### Exemple:
```
@https://github.com/github/awesome-copilot/blob/main/prompts/structured-autonomy-plan.prompt.md
Necessito planificar una API REST amb Node.js
```

## 🔗 Fonts Originals
- GitHub Awesome Copilot: https://github.com/github/awesome-copilot/tree/main/prompts
- OpenAI Examples: https://platform.openai.com/examples
- Claude Prompt Library: https://docs.anthropic.com/claude/prompt-library
- Awesome ChatGPT Prompts: https://github.com/f/awesome-chatgpt-prompts (142k⭐)
- Awesome Prompt Engineering: https://github.com/promptslab/Awesome-Prompt-Engineering

---
*Biblioteca creada el 2026-01-11*
*Actualitzada amb ChatGPT Role Prompts i Prompt Engineering el 2026-01-12*
