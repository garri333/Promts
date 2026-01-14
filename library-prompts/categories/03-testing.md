---
category_id: cat_003
category_name: Testing i Qualitat
domain: Testing & Quality Assurance
total_prompts: 12
frameworks: [xUnit, NUnit, MSTest, JUnit, Jest, pytest, Playwright]
use_cases: [Unit Testing, Integration Testing, E2E Testing, Test Coverage]
avg_rating: 4.5
last_updated: 2026-01-12
---

# 🧪 TESTING I QUALITAT

Prompts per crear tests unitaris, d'integració, e2e i estratègies de testing.

---

## 📌 Prompts Essencials (Top 3)

### 1. Estratègia de Testing
```yaml
prompt_id: prompt_020
name: breakdown-test
domain: Testing
use_case: Test Strategy & Planning
framework: [GitHub Copilot, Multi-framework]
agent_type: Single-Agent
techniques: [Strategic Planning, Coverage Analysis, Best Practices]
role: Testing strategist
task: Create comprehensive testing strategies (unit, integration, e2e)
format: Structured test plan with coverage matrix
tools: [test_analyzer, coverage_mapper, framework_selector]
metrics:
  rating: 4.7
  production_ready: true
  avg_cost: 0.05
  latency_ms: 1500
  run_count: 890
  hallucination_rate: 0.03
version: 1.5.0
created_at: 2024-07-20
updated_at: 2026-01-12
author: GitHub Copilot Team
```
**Què fa**: Crea estratègies de testing completes (unit, integration, e2e)
**Quan**: Per planificar tests d'un projecte
🔗 https://github.com/github/awesome-copilot/blob/main/prompts/breakdown-test.prompt.md

### 2. Tests E2E amb Playwright
```yaml
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
```
**Què fa**: Genera tests automatitzats de navegador
**Quan**: Per testejar UI i fluxos d'usuari
🔗 https://github.com/github/awesome-copilot/blob/main/prompts/playwright-generate-test.prompt.md

### 3. Cobertura Pytest (Python)
```yaml
prompt_id: prompt_022
name: pytest-coverage
domain: Testing
use_case: Python Unit Testing & Coverage
framework: [pytest, GitHub Copilot]
agent_type: Single-Agent
techniques: [Code Generation, Coverage Analysis, Fixture Optimization]
role: Python test generator
task: Improve test coverage for Python projects with pytest
format: Python test files with fixtures and assertions
tools: [pytest, coverage_py, fixture_generator]
metrics:
  rating: 4.6
  production_ready: true
  avg_cost: 0.04
  latency_ms: 1300
  run_count: 950
  hallucination_rate: 0.04
version: 1.8.0
created_at: 2024-07-15
updated_at: 2026-01-12
author: GitHub Copilot Team
```
**Què fa**: Millora la cobertura de tests en Python
**Quan**: Per projectes Python amb pytest
🔗 https://github.com/github/awesome-copilot/blob/main/prompts/pytest-coverage.prompt.md

---

## 📋 Tests per Llenguatge

### C# / .NET
| Prompt | Framework | Link |
|--------|-----------|------|
| csharp-xunit | xUnit | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/csharp-xunit.prompt.md) |
| csharp-nunit | NUnit | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/csharp-nunit.prompt.md) |
| csharp-mstest | MSTest | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/csharp-mstest.prompt.md) |
| csharp-tunit | TUnit (modern) | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/csharp-tunit.prompt.md) |

### Java
| Prompt | Framework | Link |
|--------|-----------|------|
| java-junit | JUnit | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/java-junit.prompt.md) |

### JavaScript / TypeScript
| Prompt | Framework | Link |
|--------|-----------|------|
| javascript-typescript-jest | Jest | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/javascript-typescript-jest.prompt.md) |

### Python
| Prompt | Framework | Link |
|--------|-----------|------|
| pytest-coverage | pytest | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/pytest-coverage.prompt.md) |

---

## 📋 Tests E2E (Playwright)

| Prompt | Funció | Link |
|--------|--------|------|
| playwright-generate-test | Genera tests e2e | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/playwright-generate-test.prompt.md) |
| playwright-explore-website | Explora i documenta webs | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/playwright-explore-website.prompt.md) |
| playwright-automation-fill-in-form | Automatitza formularis | [Link](https://github.com/github/awesome-copilot/blob/main/prompts/playwright-automation-fill-in-form.prompt.md) |

---

## 🔄 Workflow de Testing

```
1. breakdown-test              → Crea estratègia de tests
2. [framework-test]            → Escriu tests unitaris
3. playwright-generate-test    → Escriu tests e2e
4. pytest-coverage / cobertura → Verifica cobertura
```

---

*Categoria: Testing i Qualitat*
