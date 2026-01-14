# 🚀 GUIA RÀPIDA: SISTEMA DE METADADES

> Com utilitzar el nou sistema de metadades YAML per búsquedas avançades

---

## ⚡ INICI RÀPID (5 minuts)

### 1. Instal·lar Python i dependències

```bash
# Verifica que tens Python 3.9+
python --version

# Opcional: crear virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instal·lar PyYAML si no el tens
pip install pyyaml
```

### 2. Executar búsquedas

```bash
# Anar a la carpeta de scripts
cd library-prompts/scripts

# Executar exemples de búsqueda
python search_prompts.py
```

---

## 📋 EXEMPLES DE BÚSQUEDA

### Exemple 1: Trobar prompts per domini

```python
from search_prompts import PromptDatabase

db = PromptDatabase()

# Tots els prompts de Planning
planning_prompts = db.search_by_domain("Planning")

# Tots els prompts de Testing
testing_prompts = db.search_by_domain("Testing")

# Tots els prompts d'Agent Engineering
agent_prompts = db.search_by_domain("Agent Engineering")

for prompt in planning_prompts:
    print(f"{prompt.name}: {prompt.use_case}")
```

### Exemple 2: Prompts compatibles amb frameworks

```python
# Prompts que funcionen amb LangChain
langchain_prompts = db.search_by_framework("LangChain")

# Prompts d'OpenAI Agents
openai_prompts = db.search_by_framework("OpenAI Agents")

# Prompts universals (funcionen amb qualsevol framework)
universal_prompts = db.search_by_framework("Universal")

# Prompts compatibles amb múltiples frameworks
multi_fw = db.search_multi_framework(["LangChain", "AutoGen", "CrewAI"])
```

### Exemple 3: Prompts production-ready amb alta qualitat

```python
# Només els millors prompts
best_prompts = db.advanced_search(
    min_rating=4.7,
    production_ready=True
)

for prompt in best_prompts:
    rating = prompt.metrics.get('rating')
    print(f"{prompt.name}: ⭐ {rating}/5.0")
```

### Exemple 4: Optimització de costos

```python
# Prompts barats i ràpids
cheap_fast = db.advanced_search(
    max_cost=0.05,        # Màxim 5 cèntims per execució
    max_latency=1500      # Màxim 1.5 segons
)

for prompt in cheap_fast:
    cost = prompt.metrics.get('avg_cost')
    latency = prompt.metrics.get('latency_ms')
    print(f"{prompt.name}: ${cost:.3f}, {latency}ms")
```

### Exemple 5: Prompts per tècniques específiques

```python
# Tots els prompts que usen Chain-of-Thought
cot_prompts = db.search_by_technique("Chain-of-Thought")

# Prompts amb ReAct
react_prompts = db.search_by_technique("ReAct")

# Prompts amb Reflection
reflection_prompts = db.search_by_technique("Reflection")
```

### Exemple 6: Búsqueda combinada complexa

```python
# Cas d'ús: Trobar el millor prompt per generar tests E2E
# amb Playwright, production-ready, baix cost

e2e_testing_prompts = db.advanced_search(
    domain="Testing",
    use_case="E2E",
    framework="Playwright",
    min_rating=4.5,
    production_ready=True,
    max_cost=0.10,
    max_latency=2000
)

if e2e_testing_prompts:
    best = e2e_testing_prompts[0]
    print(f"✅ Recomanat: {best.name}")
    print(f"   Rating: {best.metrics.get('rating')}/5.0")
    print(f"   Cost: ${best.metrics.get('avg_cost')}")
    print(f"   Latency: {best.metrics.get('latency_ms')}ms")
    print(f"   Arxiu: {best.file_path}")
```

---

## 🎯 CASOS D'ÚS REALS

### Cas 1: Nou projecte React amb testing

```python
db = PromptDatabase()

# 1. Planning
planning = db.advanced_search(
    domain="Planning",
    use_case="Project Planning",
    min_rating=4.7
)[0]
print(f"1. Planning: {planning.name}")

# 2. Testing strategy
testing_strategy = db.advanced_search(
    domain="Testing",
    use_case="Test Strategy",
    min_rating=4.5
)[0]
print(f"2. Testing Strategy: {testing_strategy.name}")

# 3. E2E tests amb Playwright
e2e = db.advanced_search(
    domain="Testing",
    framework="Playwright",
    production_ready=True
)[0]
print(f"3. E2E Testing: {e2e.name}")

# 4. Documentation
docs = db.advanced_search(
    domain="Documentation",
    production_ready=True
)[0]
print(f"4. Documentation: {docs.name}")
```

### Cas 2: Migrar de OpenAI a LangChain

```python
# Trobar tots els prompts que funcionen amb ambdós frameworks
compatible = db.search_multi_framework(["OpenAI Agents", "LangChain"])

print(f"Prompts compatibles amb OpenAI i LangChain: {len(compatible)}")
for prompt in compatible:
    print(f"  - {prompt.name}")
    print(f"    Frameworks: {', '.join(prompt.framework)}")
```

### Cas 3: Optimitzar costos d'agents

```python
# Trobar els agents més econòmics mantenint qualitat
cost_effective = db.advanced_search(
    agent_type="Single-Agent",
    min_rating=4.5,
    max_cost=0.05,  # Màxim 5 cèntims
    production_ready=True
)

# Ordenar per cost
sorted_by_cost = sorted(
    cost_effective, 
    key=lambda p: p.metrics.get('avg_cost', 999)
)

print("Top 5 agents més econòmics (alta qualitat):")
for i, prompt in enumerate(sorted_by_cost[:5], 1):
    print(f"{i}. {prompt.name}")
    print(f"   Cost: ${prompt.metrics.get('avg_cost'):.3f}")
    print(f"   Rating: {prompt.metrics.get('rating')}/5.0")
```

### Cas 4: Trobar agents amb baixa taxa d'al·lucinacions

```python
# Agents fiables amb mínimes al·lucinacions
reliable = db.search_low_hallucination(max_rate=0.03)

print(f"Agents amb <3% al·lucinacions: {len(reliable)}")
for prompt in reliable[:5]:
    halluc = prompt.metrics.get('hallucination_rate', 0)
    print(f"  - {prompt.name}: {halluc*100:.1f}%")
```

---

## 📊 ESTADÍSTIQUES I ANÀLISI

### Generar report complet

```python
db = PromptDatabase()
stats = db.get_statistics()

print("=" * 60)
print("ESTADÍSTIQUES DE LA BIBLIOTECA")
print("=" * 60)

print(f"\n📦 Total prompts: {stats['total_prompts']}")
print(f"⭐ Rating mitjà: {stats['avg_rating']:.2f}/5.0")
print(f"✅ Production ready: {stats['production_ready_count']}")
print(f"💰 Cost mitjà: ${stats['avg_cost']:.3f}")
print(f"⚡ Latència mitjana: {stats['avg_latency']:.0f}ms")

print("\n📁 Distribució per domini:")
for domain, count in sorted(stats['by_domain'].items(), 
                            key=lambda x: x[1], 
                            reverse=True)[:10]:
    print(f"  {domain}: {count} prompts")

print("\n🔧 Distribució per framework:")
for fw, count in sorted(stats['by_framework'].items(), 
                       key=lambda x: x[1], 
                       reverse=True)[:10]:
    print(f"  {fw}: {count} prompts")

print("\n🧠 Tècniques més utilitzades:")
for tech, count in sorted(stats['by_technique'].items(), 
                         key=lambda x: x[1], 
                         reverse=True)[:10]:
    print(f"  {tech}: {count} prompts")
```

---

## 🔍 BÚSQUEDA AVANÇADA AMB FILTRES

### Exemple complet: Dashboard de recomanacions

```python
def recommend_prompts_for_project(
    project_type: str,
    preferred_framework: str = None,
    budget_per_run: float = 0.10,
    max_latency_ms: int = 3000
):
    """
    Recomana els millors prompts per un tipus de projecte
    considerant framework, pressupost i latència
    """
    db = PromptDatabase()
    
    # Mapa de projecte a domini
    domain_map = {
        'web_app': 'Planning',
        'api': 'Planning',
        'data_pipeline': 'Data Analysis',
        'ml_project': 'Data Analysis',
        'testing': 'Testing'
    }
    
    domain = domain_map.get(project_type, 'Planning')
    
    # Búsqueda amb criteris
    prompts = db.advanced_search(
        domain=domain,
        framework=preferred_framework,
        min_rating=4.5,
        production_ready=True,
        max_cost=budget_per_run,
        max_latency=max_latency_ms
    )
    
    # Ordenar per rating
    sorted_prompts = sorted(
        prompts,
        key=lambda p: p.metrics.get('rating', 0),
        reverse=True
    )
    
    return sorted_prompts[:5]


# Ús:
recommendations = recommend_prompts_for_project(
    project_type='web_app',
    preferred_framework='LangChain',
    budget_per_run=0.08,
    max_latency_ms=2000
)

print("🎯 Prompts recomanats:")
for i, prompt in enumerate(recommendations, 1):
    print(f"\n{i}. {prompt.name}")
    print(f"   Domain: {prompt.domain}")
    print(f"   Use case: {prompt.use_case}")
    print(f"   Rating: {prompt.metrics.get('rating')}/5.0")
    print(f"   Cost: ${prompt.metrics.get('avg_cost'):.3f}")
    print(f"   Latency: {prompt.metrics.get('latency_ms')}ms")
    print(f"   Frameworks: {', '.join(prompt.framework)}")
```

---

## 🛠️ SCRIPTS PERSONALITZATS

### Script 1: Export a CSV

```python
import csv
from search_prompts import PromptDatabase

db = PromptDatabase()

with open('prompts_export.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([
        'ID', 'Name', 'Domain', 'Use Case', 'Framework', 
        'Agent Type', 'Rating', 'Cost', 'Latency', 'Version'
    ])
    
    for prompt in db.prompts:
        writer.writerow([
            prompt.prompt_id,
            prompt.name,
            prompt.domain,
            prompt.use_case,
            ', '.join(prompt.framework),
            prompt.agent_type,
            prompt.metrics.get('rating', ''),
            prompt.metrics.get('avg_cost', ''),
            prompt.metrics.get('latency_ms', ''),
            prompt.version
        ])

print("✅ Exportat a prompts_export.csv")
```

### Script 2: Comparar versions

```python
def compare_prompt_versions(prompt_id: str):
    """Compara diferents versions d'un prompt"""
    db = PromptDatabase()
    
    # Trobar totes les versions del prompt
    versions = [p for p in db.prompts if p.prompt_id == prompt_id]
    
    if len(versions) < 2:
        print(f"Només hi ha 1 versió de {prompt_id}")
        return
    
    # Ordenar per versió
    versions.sort(key=lambda p: p.version)
    
    print(f"\n📊 Comparació de versions: {prompt_id}")
    print("=" * 60)
    
    for v in versions:
        print(f"\nVersió {v.version} ({v.updated_at}):")
        print(f"  Rating: {v.metrics.get('rating')}/5.0")
        print(f"  Cost: ${v.metrics.get('avg_cost'):.3f}")
        print(f"  Latency: {v.metrics.get('latency_ms')}ms")
        print(f"  Hallucination: {v.metrics.get('hallucination_rate', 0)*100:.1f}%")
        print(f"  Runs: {v.metrics.get('run_count')}")

# Ús:
compare_prompt_versions("prompt_001")
```

---

## 📚 RECURSOS ADDICIONALS

- **Esquema complet**: [METADATA-SCHEMA.md](../METADATA-SCHEMA.md)
- **Codi del buscador**: [search_prompts.py](search_prompts.py)
- **README principal**: [README.md](../README.md)
- **INDEX de prompts**: [INDEX.md](../INDEX.md)

---

## ❓ PREGUNTES FREQÜENTS

**P: Com afegeixo un nou prompt amb metadades?**  
R: Afegeix un bloc YAML entre ` ```yaml ` i ` ``` ` dins del fitxer de categoria. Segueix l'estructura de METADATA-SCHEMA.md

**P: Puc cercar sense Python?**  
R: Sí! Les metadades són llegibles i pots buscar manualment dins dels fitxers .md

**P: Com actualitzo les mètriques d'un prompt?**  
R: Edita el bloc YAML del prompt i actualitza els valors dins de `metrics:`

**P: On puc veure tots els prompts disponibles?**  
R: Al fitxer INDEX.md o executant `db.prompts` al script Python

---

*Guia Ràpida v1.0 - Última actualització: 2026-01-12*
