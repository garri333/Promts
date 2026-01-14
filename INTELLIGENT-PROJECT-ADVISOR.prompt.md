# 🎯 INTELLIGENT PROJECT ADVISOR

> El teu asistent personal per trobar els prompts i agents perfectes per al teu projecte

---

## 📋 COM FUNCIONA

1. **Descriu el teu projecte** en detall
2. **Esculls les fases** que necessites
3. **Rep 3-5 prompts/agents recomanats PER CADA FASE**
4. **Executa en ordre** per a resultat óptim

---

## 🚀 INSTRUCCIONS PER A L'IA (Copilot)

**IMPORTANT**: Copilot, quan aquest prompt es carregui:

1. **LLEGEIX** el contingut complet d'aquest fitxer
2. **ANALITZA** les taules de mapeig fase-prompts
3. **DEMANA** informació específica de l'usuari
4. **RECOMANA** 3-5 prompts + agents per CADA fase del projecte
5. **PROPORCIONA** els links directes per copiar-los
6. **DONA** un pla d'execució pas a pas

---

## 📝 FASE 1: INFORMATION GATHERING

Antes de donar recomanacions, necessito saber:

### A. Tipus de Projecte
```
Quina mena de projecte vols fer?

Selecciona una:
□ API REST / Backend
□ Frontend Web (React/Vue/Angular)
□ Full-Stack (Frontend + Backend)
□ Mobile App (iOS/Android)
□ CLI Tool / Utility
□ Desktop App (Electron/MAUI)
□ Microserveis
□ Data Processing / ML
□ DevOps / Infrastructure
□ Altre: _________________
```

### B. Stack Tecnològic
```
Quines tecnologies usaràs?

Llenguatge principal: _________________
Framework principal: _________________
Base de dades (si aplica): _________________
Cloud provider (si aplica): _________________
Testing framework preferit: _________________
```

### C. Nivell de Complexitat
```
Complexitat del projecte:
□ Beginner (< 2000 línies de codi)
□ Intermediate (2000-10000 línies)
□ Advanced (> 10000 línies, arquitectura complexa)
□ Enterprise (multi-tenant, escalabilitat crítica)
```

### D. Fases que Necessites
```
Quines fases vols cobrir?

□ FASE 1: Planning & Architecture
□ FASE 2: Development & Implementation
□ FASE 3: Testing & Quality
□ FASE 4: Documentation
□ FASE 5: Git, CI/CD & Deployment
□ TOTES (recomanat per a projectes nous)
```

---

## 🎯 FASE 2: RECOMANACIONS PER FASE

### FASE 1️⃣: PLANNING & ARCHITECTURE

**Objectiu**: Definir arquitectura, requisits i pla d'implementació

**3-5 Prompts/Agents recomanats** (segons tecnologia):

#### Opció A: Per API REST (Node.js, Python, .NET)
| # | Recurs | Tipus | Per a |
|---|--------|-------|-------|
| 1 | `structured-autonomy-plan.prompt.md` | Prompt | Planificació general |
| 2 | `api-architect.agent.md` | Agent | Disseny d'arquitectura API |
| 3 | `database-schema-design.prompt.md` | Prompt | Diseño de BD |
| 4 | `api-specification.prompt.md` | Prompt | Crear OpenAPI spec |
| 5 | `tech-stack-analyzer.prompt.md` | Prompt | Validar decisions tech |

**Workflow:**
```
1. Usa structured-autonomy-plan → Obtén overview del projecte
2. Usa api-architect agent → Disseny arquitectura
3. Usa database-schema-design → Modelat de dades
4. Usa api-specification → Documenta endpoints
5. Usa tech-stack-analyzer → Validar choices
```

#### Opció B: Per Frontend (React, Vue, Angular)
| # | Recurs | Tipus | Per a |
|---|--------|-------|-------|
| 1 | `structured-autonomy-plan.prompt.md` | Prompt | Visió general |
| 2 | `component-architecture-design.prompt.md` | Prompt | Estructura de components |
| 3 | `se-ux-ui-designer.agent.md` | Agent | UX/UI design |
| 4 | `state-management-design.prompt.md` | Prompt | Redux/Zustand/Context |
| 5 | `performance-optimization-plan.prompt.md` | Prompt | Estratègia de perf |

#### Opció C: Per Full-Stack
| # | Recurs | Tipus | Per a |
|---|--------|-------|-------|
| 1 | `structured-autonomy-plan.prompt.md` | Prompt | Master plan |
| 2 | `api-architect.agent.md` | Agent | Backend architecture |
| 3 | `component-architecture-design.prompt.md` | Prompt | Frontend structure |
| 4 | `database-schema-design.prompt.md` | Prompt | BD design |
| 5 | `system-integration-design.prompt.md` | Prompt | Com parlen front+back |

---

### FASE 2️⃣: DEVELOPMENT & IMPLEMENTATION

**Objectiu**: Generar codi de qualitat segons el pla

**3-5 Prompts/Agents recomanats** (segons stack):

#### Opció A: Node.js/JavaScript Backend
| # | Recurs | Tipus | Per a |
|---|--------|-------|-------|
| 1 | Agent `expert-nodejs-developer` | Agent | Development general |
| 2 | `structured-autonomy-implement.prompt.md` | Prompt | Implementació pas a pas |
| 3 | `express-rest-api-generator.prompt.md` | Prompt | Generar endpoints |
| 4 | `error-handling-strategy.prompt.md` | Prompt | Gestió d'errors |
| 5 | `authentication-implementation.prompt.md` | Prompt | Auth (JWT/OAuth) |

#### Opció B: Python Backend (FastAPI/Django)
| # | Recurs | Tipus | Per a |
|---|--------|-------|-------|
| 1 | Agent `expert-python-backend` | Agent | Development Python |
| 2 | `structured-autonomy-implement.prompt.md` | Prompt | Implementació |
| 3 | `fastapi-project-structure.prompt.md` | Prompt | Estructura FastAPI |
| 4 | `database-models-generation.prompt.md` | Prompt | SQLAlchemy models |
| 5 | `async-code-optimization.prompt.md` | Prompt | Async/await patterns |

#### Opció C: .NET/C#
| # | Recurs | Tipus | Per a |
|---|--------|-------|-------|
| 1 | Agent `expert-dotnet-software-engineer` | Agent | Development .NET |
| 2 | `structured-autonomy-implement.prompt.md` | Prompt | Implementació |
| 3 | `dotnet-project-setup.prompt.md` | Prompt | Estructura projecte |
| 4 | `entity-framework-models.prompt.md` | Prompt | EF Core setup |
| 5 | `dependency-injection-config.prompt.md` | Prompt | DI patterns |

#### Opció D: React/TypeScript Frontend
| # | Recurs | Tipus | Per a |
|---|--------|-------|-------|
| 1 | Agent `expert-react-frontend-engineer` | Agent | React development |
| 2 | `structured-autonomy-implement.prompt.md` | Prompt | Implementació |
| 3 | `react-component-generator.prompt.md` | Prompt | Generar components |
| 4 | `react-hooks-patterns.prompt.md` | Prompt | Custom hooks |
| 5 | `tailwind-styling-implementation.prompt.md` | Prompt | Styling amb Tailwind |

---

### FASE 3️⃣: TESTING & QUALITY ASSURANCE

**Objectiu**: Assegurar qualitat amb tests complets

**3-5 Prompts/Agents recomanats** (segons tipus de test):

#### Opció A: Backend Testing (Node.js/Python/.NET)
| # | Recurs | Tipus | Per a |
|---|--------|-------|-------|
| 1 | `breakdown-test.prompt.md` | Prompt | Estratègia de testing |
| 2 | Agent `playwright-tester` | Agent | E2E testing setup |
| 3 | `unit-test-generator.prompt.md` | Prompt | Tests unitaris |
| 4 | `integration-test-design.prompt.md` | Prompt | Tests d'integració |
| 5 | `api-testing-postman.prompt.md` | Prompt | Test API endpoints |

#### Opció B: Frontend Testing (React)
| # | Recurs | Tipus | Per a |
|---|--------|-------|-------|
| 1 | `breakdown-test.prompt.md` | Prompt | Test strategy |
| 2 | `react-component-testing.prompt.md` | Prompt | Unit tests React |
| 3 | `react-integration-testing.prompt.md` | Prompt | Tests d'integració |
| 4 | Agent `playwright-tester` | Agent | E2E testing |
| 5 | `visual-regression-testing.prompt.md` | Prompt | Visual tests |

#### Opció C: Full-Stack Testing
| # | Recurs | Tipus | Per a |
|---|--------|-------|-------|
| 1 | `breakdown-test.prompt.md` | Prompt | Master test plan |
| 2 | `unit-test-generator.prompt.md` | Prompt | Backend units |
| 3 | `react-component-testing.prompt.md` | Prompt | Frontend units |
| 4 | Agent `playwright-tester` | Agent | E2E coverage |
| 5 | `test-coverage-improvement.prompt.md` | Prompt | Augmentar coverage |

---

### FASE 4️⃣: DOCUMENTATION

**Objectiu**: Documentar codi, API, decisions i deployment

**3-5 Prompts/Agents recomanats**:

| # | Recurs | Tipus | Per a |
|---|--------|-------|-------|
| 1 | `create-readme.prompt.md` | Prompt | README complet |
| 2 | `api-documentation-generator.prompt.md` | Prompt | OpenAPI/Swagger docs |
| 3 | `architecture-decision-records.prompt.md` | Prompt | ADRs del projecte |
| 4 | `inline-code-documentation.prompt.md` | Prompt | Comments/JSDoc |
| 5 | Agent `se-technical-writer` | Agent | Documentació tècnica |

**Workflow:**
```
1. Usa create-readme → Overview + setup
2. Usa api-documentation-generator → API docs
3. Usa architecture-decision-records → Decisions tècniques
4. Usa inline-code-documentation → Comentaris al codi
5. Usa se-technical-writer agent → Review + millores
```

---

### FASE 5️⃣: GIT, CI/CD & DEPLOYMENT

**Objectiu**: Automatitzar build, test i deployment

**3-5 Prompts/Agents recomanats** (segons plataforma):

#### Opció A: GitHub Actions + Deploy
| # | Recurs | Tipus | Per a |
|---|--------|-------|-------|
| 1 | `conventional-commit-strategy.prompt.md` | Prompt | Commit guidelines |
| 2 | `create-github-action-workflow.prompt.md` | Prompt | CI workflow |
| 3 | Agent `github-actions-expert` | Agent | Optimitzar actions |
| 4 | `docker-setup-optimization.prompt.md` | Prompt | Dockerize app |
| 5 | `deployment-strategy.prompt.md` | Prompt | Deploy a producció |

#### Opció B: Azure DevOps
| # | Recurs | Tipus | Per a |
|---|--------|-------|-------|
| 1 | `conventional-commit-strategy.prompt.md` | Prompt | Commits |
| 2 | Agent `azure-iac-generator` | Agent | IaC Terraform/Bicep |
| 3 | `azure-deployment-pipeline.prompt.md` | Prompt | Azure Pipelines setup |
| 4 | Agent `platform-sre-kubernetes` | Agent | K8s deployment |
| 5 | `monitoring-alerting-setup.prompt.md` | Prompt | Observabilitat |

#### Opció C: AWS/Cloud Genèric
| # | Recurs | Tipus | Per a |
|---|--------|-------|-------|
| 1 | `conventional-commit-strategy.prompt.md` | Prompt | Git commits |
| 2 | `docker-setup-optimization.prompt.md` | Prompt | Containerization |
| 3 | Agent `devops-expert` | Agent | CI/CD strategy |
| 4 | `terraform-infrastructure.prompt.md` | Prompt | IaC setup |
| 5 | `monitoring-logging-setup.prompt.md` | Prompt | Observabilitat |

---

## 🎬 EXEMPLE COMPLET: PROJECT SETUP

### Cas: Crear una API REST Node.js + PostgreSQL + Jest Tests

**User Input:**
```
Projecte: API REST
Stack: Node.js + Express + PostgreSQL + Jest
Fases: TOTES
Nivell: Intermediate
```

**RESPOSTA INTEL·LIGENT DEL COPILOT:**

#### ✅ FASE 1: PLANNING (Estimat: 2-3 hores)
```
1️⃣ @structured-autonomy-plan.prompt.md
   → Descriu: "Node.js REST API amb PostgreSQL"
   → Obtens: Pla d'arquitectura completa

2️⃣ @api-architect.agent.md (agent)
   → Pregunta: "Quins endpoints necessito?"
   → Obtens: Disseny d'API detallat

3️⃣ @database-schema-design.prompt.md
   → Descriu: "Taules de BD necessàries"
   → Obtens: Schema SQL optimitzat

4️⃣ @api-specification.prompt.md
   → Usa el design anterior
   → Obtens: OpenAPI spec (swagger.json)

5️⃣ @tech-stack-analyzer.prompt.md
   → Valida choices de frameworks
   → Obtens: Confirmació de decisions
```

#### ✅ FASE 2: DEVELOPMENT (Estimat: 20-30 hores)
```
1️⃣ @expert-nodejs-developer.agent.md (agent)
   → "Estructura de projecte Node.js professionalcompleta"
   → Obtens: Boilerplate optimitzat

2️⃣ @structured-autonomy-implement.prompt.md
   → Usa el pla de FASE 1
   → Obtens: Plan implementació pas a pas

3️⃣ @express-rest-api-generator.prompt.md
   → Endpoints del schema de FASE 1
   → Obtens: API funcional

4️⃣ @error-handling-strategy.prompt.md
   → Estratègia consistent d'errors
   → Obtens: Error middleware

5️⃣ @authentication-implementation.prompt.md
   → "JWT per a Express + PostgreSQL"
   → Obtens: Auth funcional
```

#### ✅ FASE 3: TESTING (Estimat: 10-15 hores)
```
1️⃣ @breakdown-test.prompt.md
   → Estratègia de testing per a aquesta API
   → Obtens: Test plan complet

2️⃣ @unit-test-generator.prompt.md
   → Codi de serveis + models
   → Obtens: Jest tests per a lògica

3️⃣ @integration-test-design.prompt.md
   → Tests d'endpoints + BD
   → Obtens: Tests d'integració

4️⃣ @api-testing-postman.prompt.md
   → Endpoints de l'API
   → Obtens: Postman collection + manual

5️⃣ @test-coverage-improvement.prompt.md
   → Incrementar coverage al 80%+
   → Obtens: Plans de millora
```

#### ✅ FASE 4: DOCUMENTATION (Estimat: 5-8 hores)
```
1️⃣ @create-readme.prompt.md
   → Project overview i instruccions
   → Obtens: README.md professional

2️⃣ @api-documentation-generator.prompt.md
   → OpenAPI spec de FASE 1
   → Obtens: API docs interactiva

3️⃣ @architecture-decision-records.prompt.md
   → Decisions de FASE 1
   → Obtens: ADRs documentats

4️⃣ @inline-code-documentation.prompt.md
   → Codi de FASE 2
   → Obtens: JSDoc comments

5️⃣ @se-technical-writer.agent.md (agent)
   → Review de tota la documentació
   → Obtens: Documentació polida
```

#### ✅ FASE 5: CI/CD & DEPLOYMENT (Estimat: 3-5 hores)
```
1️⃣ @conventional-commit-strategy.prompt.md
   → Estratègia de commits
   → Obtens: Commit guidelines

2️⃣ @create-github-action-workflow.prompt.md
   → Setup per Node.js + Jest + PostgreSQL
   → Obtens: .github/workflows/ci.yml

3️⃣ @github-actions-expert.agent.md (agent)
   → Optimitzar workflows
   → Obtens: Setup profesional

4️⃣ @docker-setup-optimization.prompt.md
   → Dockerfile + docker-compose
   → Obtens: Contenidors pronts

5️⃣ @deployment-strategy.prompt.md
   → "Deploy a Heroku / Railway / DigitalOcean"
   → Obtens: Deployment guide
```

**TEMPS TOTAL ESTIMAT: 40-60 hores**
**DEPENDÈNCIES: Executar en ordre (FASE 1 → 5)**

---

## 🎯 NEXT STEPS

### Ara que tens aquest prompt:

1. **Copia'l completament** al xat de Copilot
2. **Diga informació del teu projecte** (tipus, stack, fases)
3. **Copilot te dirà els 3-5 prompts exàctes** que necessites per CADA fase
4. **Segueix les instruccions** en ordre
5. **Reutilitza els resultats** entre fases

---

## 💡 CONSELLS

✅ **DO:**
- Dona el màxim de context sobre el teu projecte
- Executa les fases en ordre (1→2→3→4→5)
- Personalitza els prompts al teu stack
- Combina prompts + agents per a millor qualitat
- Itera si la primera resposta no és perfecta

❌ **DON'T:**
- No saltes fases (testing al final = problemes)
- No modifiquis massivament els prompts
- No ignoris les recomanacions d'agents
- No preguntes a un agent de testing sobre arquitectura
- No copies cegament - sempre revisa i adapta

---

## 📞 SUPPORT

Si Copilot no entén alguna cosa:

```
"Busca a library-prompts/categories/[numero]-[categoria]/
i recomana els 3 millors prompts per [teva tasca]"
```

O:

```
"Mostra'm els agents més rellevants de library-agents/INDEX.md
per a [tipus de projecte]"
```

---

*Intelligent Project Advisor - Actualitzat 2026-01-12*
*Úsalo sempre que comencis un projecte nou o fase nova*
