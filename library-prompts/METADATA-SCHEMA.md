# 📊 ESQUEMA DE METADADES - BIBLIOTECA DE PROMPTS

> Sistema de metadades YAML per búsqueda multi-dimensional i tracking de rendiment

---

## 🎯 OBJECTIU

Aquesta biblioteca utilitza **YAML frontmatter** per afegir metadades estructurades a cada prompt i categoria, permetent:

✅ **Búsqueda per problema de negoci** (no només per model)  
✅ **Reutilització amb diferents frameworks** (OpenAI Agents, LangChain, AutoGen, CrewAI)  
✅ **Mesura de rendiment** i versionat de canvis  
✅ **A/B testing** entre versions  
✅ **Auditorías** i depuració amb històric complet  

---

## 📋 ESTRUCTURA DE METADADES

### 1. METADADES DE CATEGORIA

Cada fitxer de categoria inclou al començament:

```yaml
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
```

**Camps:**
- `category_id`: Identificador únic de la categoria
- `category_name`: Nom en català
- `domain`: Domini de negoci (anglès)
- `total_prompts`: Número total de prompts en aquesta categoria
- `frameworks`: Frameworks compatibles
- `use_cases`: Casos d'ús principals
- `avg_rating`: Rating mitjà de tots els prompts
- `last_updated`: Data última actualització

---

### 2. METADADES DE PROMPT

Cada prompt destacat inclou un bloc YAML amb:

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

---

## 🔍 CAMPS DETALLATS

### IDENTITAT
| Camp | Descripció | Exemple |
|------|------------|---------|
| `prompt_id` | ID únic del prompt | `prompt_001` |
| `name` | Nom tècnic del prompt | `structured-autonomy-plan` |

### CONTEXT
| Camp | Descripció | Valors Possibles |
|------|------------|------------------|
| `domain` | Domini de negoci | Planning, Testing, Documentation, Coding, Data Analysis, Support, Operations |
| `use_case` | Cas d'ús específic | Project Planning, SQL Optimization, E2E Testing, etc. |
| `agent_type` | Tipus d'agent | Single-Agent, Multi-Agent, Tool-Centric, RAG-Agent |
| `framework` | Frameworks compatibles | GitHub Copilot, OpenAI Agents, LangChain, AutoGen, CrewAI, Semantic Kernel |

### ESTRUCTURA RTF+TOOLS
| Camp | Descripció |
|------|------------|
| `role` | Persona/rol de l'agent |
| `task` | Tasca específica que ha de fer |
| `format` | Format exacte de la sortida |
| `tools` | Llista de tools/funcions disponibles |

### TÈCNIQUES DE PROMPTING
| Camp | Descripció | Valors Possibles |
|------|------------|------------------|
| `techniques` | Tècniques utilitzades | ReAct, Chain-of-Thought, Reflection, Self-Consistency, Tool-Choice, Few-Shot, Prompt-Chaining, System-Prompt, Structured Output, Verification |

### MÈTRIQUES OPERATIVES
| Camp | Descripció | Unitat |
|------|------------|--------|
| `rating` | Valoració humana | 1.0 - 5.0 |
| `production_ready` | Llest per producció | true/false |
| `avg_cost` | Cost mitjà per execució | $ (USD) |
| `latency_ms` | Latència mitjana | milliseconds |
| `run_count` | Número d'execucions | número |
| `hallucination_rate` | Taxa d'al·lucinacions | 0.00 - 1.00 |

### VERSIONAT
| Camp | Descripció | Format |
|------|------------|--------|
| `version` | Versió del prompt | Semantic Versioning (X.Y.Z) |
| `created_at` | Data de creació | YYYY-MM-DD |
| `updated_at` | Data última actualització | YYYY-MM-DD |
| `author` | Autor o equip | text |

---

## 🎨 VALORS ESTÀNDARD

### Dominis de Negoci
```yaml
domains:
  - Planning & Architecture
  - Code Generation
  - Testing & Quality Assurance
  - Documentation
  - Data Analysis
  - Cloud & DevOps
  - Database Management
  - Agent Engineering
  - Marketing
  - Support
  - Operations
```

### Tipus d'Agent
```yaml
agent_types:
  - Single-Agent      # Un sol rol/responsabilitat
  - Multi-Agent       # Múltiples agents col·laborant (planner, executor, reviewer)
  - Tool-Centric      # El valor està en les eines/funcions
  - RAG-Agent         # Agents amb recuperació de coneixement (Retrieval)
```

### Frameworks
```yaml
frameworks:
  - GitHub Copilot
  - OpenAI Agents SDK
  - LangChain
  - LangGraph
  - AutoGen
  - CrewAI
  - Semantic Kernel
  - Prompt Flow
  - Universal          # Compatible amb tots
```

### Tècniques de Prompting
```yaml
techniques:
  - ReAct              # Reasoning + Acting
  - Chain-of-Thought   # Pensament pas a pas
  - Reflection         # Auto-revisió i millora
  - Self-Consistency   # Múltiples respostes + consens
  - Tool-Choice        # Selecció intel·ligent d'eines
  - Few-Shot           # Exemples en el prompt
  - Prompt-Chaining    # Encadenar múltiples prompts
  - System-Prompt      # Instruccions de sistema
  - Structured Output  # Sortida JSON/YAML estructurada
  - Verification       # Verificació de resultats
  - Instruction Following  # Seguir instruccions exactes
  - Code Generation    # Generació de codi
  - Coverage Analysis  # Anàlisi de cobertura
  - Best Practices     # Seguir millors pràctiques
```

---

## 📈 CASOS D'ÚS DE LES METADADES

### 1. BÚSQUEDA PER PROBLEMA DE NEGOCI
```python
# Trobar prompts per optimitzar SQL
prompts = search(domain="Data Analysis", use_case="SQL Optimization")
```

### 2. REUTILITZACIÓ AMB DIFERENTS FRAMEWORKS
```python
# Trobar prompts compatibles amb LangChain
prompts = search(framework="LangChain")
```

### 3. FILTRATGE PER QUALITAT
```python
# Només prompts production-ready amb rating alt
prompts = search(
    production_ready=True, 
    rating__gte=4.5
)
```

### 4. A/B TESTING
```python
# Comparar versions
v1 = get_prompt("prompt_001", version="1.0.0")
v2 = get_prompt("prompt_001", version="2.1.0")
compare_metrics(v1, v2)
```

### 5. AUDITORÍA I DEBUGGING
```python
# Veure historial de canvis
history = get_changelog("prompt_001")
# Qui va crear/modificar?
author = get_author("prompt_001")
# Quan es va actualitzar?
last_update = get_last_updated("prompt_001")
```

### 6. OPTIMITZACIÓ DE COSTOS
```python
# Trobar prompts barats i ràpids
prompts = search(
    avg_cost__lt=0.05,
    latency_ms__lt=1000
)
```

### 7. ANÀLISI DE RENDIMENT
```python
# Prompts amb menys al·lucinacions
prompts = search(
    hallucination_rate__lt=0.05,
    order_by="rating"
)
```

---

## 🔄 WORKFLOW AMB METADADES

### Crear nou prompt:
1. Assignar `prompt_id` únic
2. Emplenar camps de context (domain, use_case, framework)
3. Definir RTF (role, task, format)
4. Afegir tècniques utilitzades
5. Inicialitzar mètriques (rating estimat, production_ready=false)
6. Versió 1.0.0, dates de creació

### Actualitzar prompt:
1. Modificar contingut del prompt
2. Actualitzar `updated_at`
3. Incrementar `version` (patch/minor/major segons canvi)
4. Afegir nota al changelog si existeix
5. Recalcular mètriques si disponible

### Mesurar rendiment:
1. Executar prompt en casos reals
2. Recollir mètriques: cost, latència, errors
3. Valoració humana (rating)
4. Actualitzar `metrics` al YAML
5. Incrementar `run_count`

---

## 📊 ESTADÍSTIQUES DISPONIBLES

Amb aquest sistema pots generar:

- **Prompts per domini**: Quants prompts tens de cada domini
- **Framework coverage**: Quins frameworks tens més coberts
- **Quality metrics**: Distribució de ratings i production-ready
- **Cost analysis**: Costos mitjans per categoria/domini
- **Performance trends**: Evolució de latència i precisió
- **Technique usage**: Quines tècniques s'utilitzen més
- **Version history**: Velocitat de canvis i millores

---

## 🛠️ EINES RECOMANADES

### Parsing YAML
```python
import yaml
from pathlib import Path

def load_prompt_metadata(file_path):
    content = Path(file_path).read_text()
    if content.startswith('---'):
        parts = content.split('---', 2)
        metadata = yaml.safe_load(parts[1])
        markdown_content = parts[2]
        return metadata, markdown_content
    return None, content
```

### Búsqueda avançada
```python
def search_prompts(criteria):
    results = []
    for file in Path('categories').glob('*.md'):
        metadata, _ = load_prompt_metadata(file)
        if metadata and matches_criteria(metadata, criteria):
            results.append(metadata)
    return results
```

### Generador de reports
```python
def generate_report():
    stats = {
        'total_prompts': 0,
        'by_domain': {},
        'by_framework': {},
        'avg_rating': 0,
        'production_ready': 0
    }
    # Processar tots els fitxers...
    return stats
```

---

## 📚 EXEMPLES COMPLETS

### Exemple 1: Prompt de Planning
```yaml
---
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
---
# Structured Autonomy Plan
Contingut del prompt...
```

### Exemple 2: Prompt de Testing
```yaml
---
prompt_id: prompt_021
name: playwright-generate-test
domain: Testing
use_case: E2E Browser Testing
framework: [Playwright, GitHub Copilot]
agent_type: Tool-Centric
techniques: [Code Generation, Selector Optimization, Best Practices]
role: E2E test generator
task: Generate automated browser tests with Playwright
format: TypeScript/JavaScript Playwright test files
tools: [playwright, selector_generator, assertion_builder]
metrics:
  rating: 4.8
  production_ready: true
  avg_cost: 0.06
  latency_ms: 1800
  run_count: 1200
  hallucination_rate: 0.02
version: 2.0.0
created_at: 2024-08-10
updated_at: 2026-01-12
author: GitHub Copilot Team
---
# Playwright E2E Test Generator
Contingut del prompt...
```

---

## ✅ BENEFICIS DEL SISTEMA

| Benefici | Abans | Després |
|----------|-------|---------|
| **Búsqueda** | Manual per carpetes | Multi-dimensional (domain, framework, use_case) |
| **Qualitat** | Sense mètriques | Ratings, costs, latència tracked |
| **Versionat** | Sense historial | Versions semàntiques + changelog |
| **Reutilització** | Framework específic | Multi-framework amb compatibilitat clara |
| **Optimització** | Sense visibilitat | A/B testing + anàlisi de costos |
| **Auditoría** | Impossible | Historial complet amb autor i dates |

---

*Esquema de Metadades v1.0.0 - Última actualització: 2026-01-12*
*Sistema basat en les recomanacions de "Bases de Datos de Prompts para Agentes"*
