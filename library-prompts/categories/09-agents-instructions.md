---
category_id: cat_009
category_name: Agents i Custom Instructions
domain: Agent Engineering & Prompt Optimization
total_prompts: 11
frameworks: [GitHub Copilot, OpenAI Agents, LangChain, AutoGen]
use_cases: [Agent Creation, Prompt Engineering, Custom Instructions, Agent Discovery]
avg_rating: 4.7
last_updated: 2026-01-12
---

# 🤖 AGENTS I CUSTOM INSTRUCTIONS

Prompts per crear agents, custom instructions i millorar prompts.

---

## 📌 Prompts Essencials (Top 3)

### 1. Creador d'Agents
```yaml
prompt_id: prompt_070
name: suggest-awesome-github-copilot-agents
domain: Agent Engineering
use_case: Agent Discovery & Recommendation
framework: [GitHub Copilot, Meta-Agent]
agent_type: Multi-Agent
techniques: [Recommendation, Knowledge Retrieval, Contextual Matching]
role: Agent ecosystem designer
task: Suggest and recommend custom agents for GitHub Copilot
format: Structured agent recommendations with use cases
tools: [agent_catalog, use_case_matcher, recommendation_engine]
metrics:
  rating: 4.9
  production_ready: true
  avg_cost: 0.03
  latency_ms: 900
  run_count: 2500
  hallucination_rate: 0.01
version: 2.2.0
created_at: 2024-09-01
updated_at: 2026-01-12
author: GitHub Copilot Team
```
**Què fa**: Suggereix i crea custom agents per GitHub Copilot
**Quan**: Per dissenyar ecosistemes d'eines d'IA
🔗 https://github.com/github/awesome-copilot/blob/main/prompts/suggest-awesome-github-copilot-agents.prompt.md

### 2. Generador d'Instructions del Codebase
```yaml
prompt_id: prompt_071
name: generate-custom-instructions-from-codebase
domain: Agent Engineering
use_case: Automatic Instruction Generation
framework: [GitHub Copilot, RAG-Agent]
agent_type: RAG-Agent
techniques: [Code Analysis, Pattern Extraction, Documentation Generation]
role: Codebase analyzer and instruction generator
task: Analyze code and generate automatic custom instructions
format: Structured custom instructions based on project patterns
tools: [code_analyzer, pattern_extractor, documentation_generator]
metrics:
  rating: 4.7
  production_ready: true
  avg_cost: 0.07
  latency_ms: 2200
  run_count: 1100
  hallucination_rate: 0.03
version: 1.9.0
created_at: 2024-09-10
updated_at: 2026-01-12
author: GitHub Copilot Team
```
**Què fa**: Analitza el codi i genera custom instructions automàtiques
**Quan**: Per crear instructions basades en el teu projecte
🔗 https://github.com/github/awesome-copilot/blob/main/prompts/generate-custom-instructions-from-codebase.prompt.md

### 3. Prompt Builder
```yaml
prompt_id: prompt_072
name: prompt-builder
domain: Prompt Engineering
use_case: Prompt Optimization & Construction
framework: [GitHub Copilot, Universal]
agent_type: Single-Agent
techniques: [Prompt Engineering, RTF Framework, Best Practices]
role: Prompt engineering expert
task: Help create well-structured, effective prompts
format: Optimized prompts with role, task, format structure
tools: [prompt_analyzer, rtf_validator, technique_suggester]
metrics:
  rating: 4.8
  production_ready: true
  avg_cost: 0.02
  latency_ms: 700
  run_count: 3200
  hallucination_rate: 0.02
version: 2.0.0
created_at: 2024-08-20
updated_at: 2026-01-12
author: GitHub Copilot Team
```
**Què fa**: Ajuda a crear prompts ben estructurats
**Quan**: Per millorar la qualitat dels teus prompts
🔗 https://github.com/github/awesome-copilot/blob/main/prompts/prompt-builder.prompt.md

---

## 📋 Tots els Prompts d'Agents

### Descobriment i Suggeriments
| Prompt | Funció | Link |
|--------|--------|------|
| suggest-awesome-github-copilot-agents | Suggereix agents | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/suggest-awesome-github-copilot-agents.prompt.md) |
| suggest-awesome-github-copilot-prompts | Suggereix prompts | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/suggest-awesome-github-copilot-prompts.prompt.md) |
| suggest-awesome-github-copilot-instructions | Suggereix instructions | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/suggest-awesome-github-copilot-instructions.prompt.md) |
| suggest-awesome-github-copilot-collections | Suggereix col·leccions | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/suggest-awesome-github-copilot-collections.prompt.md) |
| suggest-awesome-github-copilot-chatmodes | Suggereix chat modes | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/suggest-awesome-github-copilot-chatmodes.prompt.md) |

### Creació d'Agents
| Prompt | Funció | Link |
|--------|--------|------|
| create-agentsmd | Crea fitxers agents.md | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/create-agentsmd.prompt.md) |
| declarative-agents | Crea agents declaratius | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/declarative-agents.prompt.md) |

### Custom Instructions
| Prompt | Funció | Link |
|--------|--------|------|
| generate-custom-instructions-from-codebase | Genera instructions del codi | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/generate-custom-instructions-from-codebase.prompt.md) |
| copilot-instructions-blueprint-generator | Blueprints d'instructions | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/copilot-instructions-blueprint-generator.prompt.md) |

### Millora de Prompts
| Prompt | Funció | Link |
|--------|--------|------|
| prompt-builder | Constructor de prompts | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/prompt-builder.prompt.md) |
| boost-prompt | Millora prompts existents | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/boost-prompt.prompt.md) |
| finalize-agent-prompt | Finalitza i poleix prompts | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/finalize-agent-prompt.prompt.md) |
| ai-prompt-engineering-safety-review | Revisa seguretat de prompts | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/ai-prompt-engineering-safety-review.prompt.md) |

---

## 🔄 Workflow Crear Agent

```
1. suggest-awesome-github-copilot-agents → Inspira't
2. prompt-builder                         → Crea el prompt
3. finalize-agent-prompt                  → Poleix-lo
4. ai-prompt-engineering-safety-review    → Revisa seguretat
5. create-agentsmd                        → Documenta'l
```

---

*Categoria: Agents i Custom Instructions*
