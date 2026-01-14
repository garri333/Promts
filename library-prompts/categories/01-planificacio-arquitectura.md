---
category_id: cat_001
category_name: Planificació i Arquitectura
domain: Planning & Architecture
total_prompts: 14
frameworks: [GitHub Copilot, OpenAI Agents, LangChain, AutoGen]
use_cases: [Project Planning, Code Generation, Architecture Design, Task Breakdown]
avg_rating: 4.6
last_updated: 2026-01-12
---

# 🏗️ PLANIFICACIÓ I ARQUITECTURA

Prompts per planificar projectes, crear arquitectures i dividir tasques.

---

## 📌 Prompts Essencials (Top 3)

### 1. Planificador de Projectes
```yaml
prompt_id: prompt_001
name: structured-autonomy-plan
domain: Planning
use_case: Project Planning
framework: [GitHub Copilot, OpenAI Agents, LangChain]
agent_type: Single-Agent
techniques: [ReAct, Chain-of-Thought, Structured Output]
role: Planning Agent that creates implementation plans
task: Create implementation plans divided into commits without writing code
format: Structured JSON with commits, files, and dependencies
tools: [code_analyzer, file_mapper, dependency_tracker]
metrics:
  rating: 4.8
  production_ready: true
  avg_cost: 0.04
  latency_ms: 1200
  run_count: 1500
  hallucination_rate: 0.02
version: 2.1.0
created_at: 2024-06-15
updated_at: 2026-01-12
author: GitHub Copilot Team
```
**Què fa**: Agent de planificació que crea plans dividits en commits sense escriure codi
**Quan**: Quan tens un problema difús i no saps els passos a seguir
🔗 https://github.com/github/awesome-copilot/blob/main/prompts/structured-autonomy-plan.prompt.md

### 2. Generador de Codi Llarg
```yaml
prompt_id: prompt_002
name: structured-autonomy-generate
domain: Code Generation
use_case: Autonomous Code Generation
framework: [GitHub Copilot, OpenAI Agents]
agent_type: Single-Agent
techniques: [Chain-of-Thought, Self-Consistency, Structured Output]
role: Autonomous code generator
task: Generate complete, production-ready code without supervision
format: Complete files with imports, types, tests, and documentation
tools: [code_generator, syntax_validator, style_checker]
metrics:
  rating: 4.7
  production_ready: true
  avg_cost: 0.12
  latency_ms: 3500
  run_count: 2300
  hallucination_rate: 0.05
version: 2.0.0
created_at: 2024-06-15
updated_at: 2026-01-12
author: GitHub Copilot Team
```
**Què fa**: Genera codi complet copy-paste ready sense supervisió
**Quan**: Per crear codi llarg i complex de manera autònoma
🔗 https://github.com/github/awesome-copilot/blob/main/prompts/structured-autonomy-generate.prompt.md

### 3. Implementador de Codi
```yaml
prompt_id: prompt_003
name: structured-autonomy-implement
domain: Implementation
use_case: Plan Execution
framework: [GitHub Copilot, OpenAI Agents]
agent_type: Single-Agent
techniques: [Instruction Following, Structured Output, Verification]
role: Implementation executor
task: Implement exactly what the generated plan specifies
format: Code files following the plan structure
tools: [file_writer, plan_parser, validation_checker]
metrics:
  rating: 4.9
  production_ready: true
  avg_cost: 0.08
  latency_ms: 2100
  run_count: 1800
  hallucination_rate: 0.01
version: 2.1.0
created_at: 2024-06-15
updated_at: 2026-01-12
author: GitHub Copilot Team
```
**Què fa**: Implementa exactament el que diu el pla generat
**Quan**: Després de tenir un pla d'implementació
🔗 https://github.com/github/awesome-copilot/blob/main/prompts/structured-autonomy-implement.prompt.md

---

## 📋 Tots els Prompts de la Categoria

| Prompt | Funció | Link |
|--------|--------|------|
| structured-autonomy-plan | Planifica projectes en commits | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/structured-autonomy-plan.prompt.md) |
| structured-autonomy-generate | Genera codi llarg autònom | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/structured-autonomy-generate.prompt.md) |
| structured-autonomy-implement | Implementa segons el pla | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/structured-autonomy-implement.prompt.md) |
| architecture-blueprint-generator | Crea blueprints d'arquitectura | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/architecture-blueprint-generator.prompt.md) |
| breakdown-feature-implementation | Divideix features en tasques | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/breakdown-feature-implementation.prompt.md) |
| create-implementation-plan | Plans detallats d'implementació | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/create-implementation-plan.prompt.md) |
| update-implementation-plan | Actualitza plans existents | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/update-implementation-plan.prompt.md) |
| breakdown-epic-arch | Descomposa epics arquitectònicament | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/breakdown-epic-arch.prompt.md) |
| breakdown-epic-pm | Descomposa epics com PM | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/breakdown-epic-pm.prompt.md) |
| breakdown-plan | Divideix plans complexos | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/breakdown-plan.prompt.md) |
| breakdown-feature-prd | Descomposa PRD | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/breakdown-feature-prd.prompt.md) |
| create-specification | Crea especificacions de features | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/create-specification.prompt.md) |
| update-specification | Actualitza especificacions | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/update-specification.prompt.md) |
| create-technical-spike | Crea spikes tècnics | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/create-technical-spike.prompt.md) |

---

## 🔄 Workflow Recomanat

```
1. structured-autonomy-plan      → Planifica el projecte
2. breakdown-feature-implementation → Divideix en tasques
3. create-specification          → Documenta requisits
4. structured-autonomy-generate  → Genera el codi
5. structured-autonomy-implement → Implementa tot
```

---

*Categoria: Planificació i Arquitectura*
