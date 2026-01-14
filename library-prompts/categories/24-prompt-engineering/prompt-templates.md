# 📋 Templates Reutilitzables de Prompts

> Templates provats i optimitzats per tasques comunes

---

## 📝 1. Template d'Anàlisi de Codi

```markdown
# TASCA: Anàlisi de Codi

## CODI A ANALITZAR
```[llenguatge]
[codi]
```

## INSTRUCCIONS
Analitza el codi anterior i proporciona:

1. **RESUM** (2-3 frases)
   - Què fa aquest codi?

2. **QUALITAT** (puntuació 1-10)
   - Llegibilitat: X/10
   - Mantenibilitat: X/10
   - Eficiència: X/10

3. **PROBLEMES DETECTATS**
   | Línia | Problema | Severitat | Solució |
   |-------|----------|-----------|---------|
   | X | Descripció | Alta/Mitjana/Baixa | Suggeriment |

4. **MILLORES SUGGERIDES**
   - [ ] Millora 1
   - [ ] Millora 2
   - [ ] Millora 3

5. **CODI REFACTORITZAT** (si aplica)
```[llenguatge]
[codi millorat]
```
```

---

## 📝 2. Template de Generació de Tests

```markdown
# TASCA: Generació de Tests

## CODI A TESTAR
```[llenguatge]
[codi de la funció/classe]
```

## REQUISITS
- Framework de testing: [Jest/Pytest/NUnit/etc.]
- Tipus de tests: [Unitaris/Integració/E2E]
- Cobertura mínima: [X%]

## GENERA
1. **Tests del camí feliç** (happy path)
2. **Tests de casos límit** (edge cases)
3. **Tests d'errors** (error handling)
4. **Tests de valors null/undefined**

## FORMAT DE SORTIDA
```[llenguatge]
// Test suite completa
```

Inclou comentaris explicant cada grup de tests.
```

---

## 📝 3. Template de Documentació d'API

```markdown
# TASCA: Documentació d'API

## ENDPOINT
- **Mètode**: [GET/POST/PUT/DELETE]
- **URL**: [/api/v1/resource]

## CODI DEL CONTROLLER
```[llenguatge]
[codi]
```

## GENERA DOCUMENTACIÓ EN FORMAT OPENAPI/SWAGGER

Inclou:
1. Descripció de l'endpoint
2. Paràmetres (path, query, body)
3. Request body schema (si aplica)
4. Responses (200, 400, 401, 404, 500)
5. Exemples de request/response
6. Notes d'autenticació

Format de sortida: YAML
```

---

## 📝 4. Template de Revisió de PR

```markdown
# TASCA: Code Review

## CONTEXT
- **PR Title**: [Títol]
- **Branch**: [feature/xxx] → [main]
- **Autor**: [Nom]

## DIFF A REVISAR
```diff
[diff del codi]
```

## CRITERIS DE REVISIÓ
- [ ] Funcionalitat correcta
- [ ] Tests adequats
- [ ] Documentació actualitzada
- [ ] Sense vulnerabilitats de seguretat
- [ ] Segueix coding standards
- [ ] Performance acceptable

## FORMAT DE FEEDBACK

### ✅ El que m'agrada
- [Aspectes positius]

### 🤔 Preguntes
- [Preguntes de clarificació]

### 💡 Suggeriments (opcional)
- [Millores no bloquejants]

### 🔴 Bloquejant (cal canviar)
- [Problemes que s'han de resoldre]

### Veredicte: [APPROVE / REQUEST_CHANGES / COMMENT]
```

---

## 📝 5. Template d'Arquitectura de Sistema

```markdown
# TASCA: Disseny d'Arquitectura

## REQUISITS
### Funcionals
- [Requisit 1]
- [Requisit 2]

### No Funcionals
- **Escalabilitat**: [X usuaris concurrents]
- **Disponibilitat**: [X% uptime]
- **Latència**: [< X ms]
- **Seguretat**: [Requisits]

### Restriccions
- **Budget**: [X €/mes]
- **Stack**: [Tecnologies preferides]
- **Cloud**: [AWS/Azure/GCP]

## GENERA

### 1. Diagrama d'Arquitectura (format Mermaid)
```mermaid
[diagrama]
```

### 2. Components
| Component | Responsabilitat | Tecnologia | Escalat |
|-----------|-----------------|------------|---------|
| [Nom] | [Funció] | [Tech] | [H/V] |

### 3. Patrons Aplicats
- [Patró 1]: [Justificació]
- [Patró 2]: [Justificació]

### 4. Trade-offs
| Decisió | Pros | Contres | Alternativa |
|---------|------|---------|-------------|
| [X] | [+] | [-] | [Alt] |

### 5. Cost Estimat Mensual
| Servei | Configuració | Cost |
|--------|--------------|------|
| [X] | [Config] | [€] |
```

---

## 📝 6. Template de Debug/Troubleshooting

```markdown
# TASCA: Debug/Troubleshooting

## SÍMPTOMA
[Descripció del problema]

## COMPORTAMENT ESPERAT
[Què hauria de passar]

## COMPORTAMENT ACTUAL
[Què passa realment]

## CONTEXT
- **Entorn**: [Dev/Staging/Prod]
- **Versió**: [X.Y.Z]
- **Últims canvis**: [Descripció]

## LOGS/ERRORS
```
[Error message o stack trace]
```

## CODI RELLEVANT
```[llenguatge]
[codi]
```

## ANALITZA

1. **DIAGNÒSTIC INICIAL**
   - Hipòtesis més probables

2. **PASSOS DE DEBUG**
   - [ ] Verificar X
   - [ ] Comprovar Y
   - [ ] Testar Z

3. **CAUSA ARREL PROBABLE**
   [Explicació]

4. **SOLUCIÓ PROPOSADA**
```[llenguatge]
[codi fix]
```

5. **PREVENCIÓ FUTURA**
   - Com evitar que torni a passar
```

---

## 📝 7. Template de Migració de Base de Dades

```markdown
# TASCA: Migració de Base de Dades

## ESTAT ACTUAL
```sql
[Esquema actual]
```

## ESTAT DESITJAT
```sql
[Nou esquema]
```

## REQUISITS
- [ ] Zero downtime
- [ ] Rollback possible
- [ ] Preservar dades existents
- [ ] Compatibilitat backward (X versions)

## GENERA PLA DE MIGRACIÓ

### Fase 1: Preparació
1. [Pas]
2. [Pas]

### Fase 2: Migració
```sql
-- Migration script UP
[SQL]
```

### Fase 3: Verificació
- [ ] Check 1
- [ ] Check 2

### Rollback Plan
```sql
-- Migration script DOWN
[SQL]
```

### Riscos i Mitigacions
| Risc | Probabilitat | Impacte | Mitigació |
|------|--------------|---------|-----------|
| [X] | [Alta/Baixa] | [Alt/Baix] | [Acció] |
```

---

## 📝 8. Template de Prompt Engineering

```markdown
# META-TASCA: Crear un Prompt Optimitzat

## OBJECTIU DEL PROMPT
[Què ha d'aconseguir el prompt]

## CONTEXT D'ÚS
- **Model**: [GPT-4/Claude/Llama]
- **Usuari típic**: [Perfil]
- **Freqüència**: [Ús únic/Repetitiu]

## INPUTS ESPERATS
[Tipus d'inputs que rebrà]

## OUTPUTS DESITJATS
[Format i contingut esperat]

## CREA EL PROMPT OPTIMITZAT

Segueix aquests principis:
1. Instruccions clares al principi
2. Delimitadors per separar seccions
3. Exemples si cal (few-shot)
4. Format de sortida explícit
5. Restriccions i guardrails

## PROMPT RESULTANT:
```
[El prompt optimitzat]
```

## TESTS DEL PROMPT
| Input | Output Esperat | ✓/✗ |
|-------|----------------|-----|
| [Test 1] | [Expectativa] | |
| [Test 2] | [Expectativa] | |
```

---

## 📝 9. Template de Conversió de Codi

```markdown
# TASCA: Conversió de Codi

## CODI ORIGINAL
- **Llenguatge**: [Python/JavaScript/etc.]
- **Framework**: [Django/React/etc.]
- **Versió**: [X.Y]

```[llenguatge_origen]
[codi original]
```

## CODI DESTÍ
- **Llenguatge**: [Go/TypeScript/etc.]
- **Framework**: [Gin/Next.js/etc.]
- **Versió**: [X.Y]

## REQUISITS DE CONVERSIÓ
- [ ] Mantenir funcionalitat idèntica
- [ ] Seguir idiomes del llenguatge destí
- [ ] Aplicar best practices del framework
- [ ] Tipus estrictes (si aplica)
- [ ] Tests equivalents

## GENERA

### Codi Convertit
```[llenguatge_desti]
[codi convertit]
```

### Notes de Conversió
| Original | Convertit | Nota |
|----------|-----------|------|
| [Patró] | [Nou patró] | [Explicació] |

### Limitacions
- [Funcionalitat que no es pot traduir directament]
```

---

## 📝 10. Template d'Explicació de Concepte

```markdown
# TASCA: Explicar Concepte Tècnic

## CONCEPTE
[Nom del concepte]

## AUDIÈNCIA
- **Nivell**: [Principiant/Intermedi/Avançat]
- **Background**: [Desenvolupador/Manager/Estudiant]
- **Objectiu**: [Entendre/Implementar/Decidir]

## GENERA EXPLICACIÓ

### 1. En Una Frase
[Definició concisa]

### 2. Analogia Simple
[Comparació amb concepte quotidià]

### 3. Explicació Tècnica
[Explicació detallada amb terminologia apropriada]

### 4. Exemple Pràctic
```[llenguatge]
[codi d'exemple]
```

### 5. Quan Usar-lo
- ✅ Casos on és útil
- ❌ Casos on NO usar-lo

### 6. Conceptes Relacionats
- [Concepte 1]: [Relació]
- [Concepte 2]: [Relació]

### 7. Recursos per Aprendre Més
- [Recurs 1]
- [Recurs 2]
```

---

*10 templates reutilitzables per tasques de desenvolupament*
