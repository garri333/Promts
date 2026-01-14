# 🚀 Patrons Avançats de Prompt Engineering

> Tècniques avançades per tasques complexes i raonament sofisticat

---

## 🌳 1. Tree of Thoughts (ToT)

Explora múltiples camins de raonament simultàniament.

### Quan usar-lo
- Problemes amb múltiples solucions
- Planificació estratègica
- Decisions complexes

### Template
```
Problema: [Descripció del problema]

EXPLORACIÓ DE CAMINS:

## Camí A: [Enfocament 1]
- Pas 1: [Acció]
  - Avaluació: [Pros/Contres]
- Pas 2: [Acció]
  - Avaluació: [Pros/Contres]
- Resultat probable: [Predicció]
- Puntuació: [1-10]

## Camí B: [Enfocament 2]
- Pas 1: [Acció]
  - Avaluació: [Pros/Contres]
- Pas 2: [Acció]
  - Avaluació: [Pros/Contres]
- Resultat probable: [Predicció]
- Puntuació: [1-10]

## Camí C: [Enfocament 3]
- Pas 1: [Acció]
  - Avaluació: [Pros/Contres]
- Pas 2: [Acció]
  - Avaluació: [Pros/Contres]
- Resultat probable: [Predicció]
- Puntuació: [1-10]

SELECCIÓ: Basant-me en l'anàlisi, el millor camí és [X] perquè...
```

---

## 🔄 2. ReAct (Reasoning + Acting)

Combina raonament amb accions concretes.

### Quan usar-lo
- Agents que interactuen amb eines
- Tasques que requereixen cerca d'informació
- Resolució de problemes iterativa

### Template
```
Tasca: [Descripció de la tasca]

Eines disponibles:
- search(query): Cerca informació
- calculate(expression): Fa càlculs
- code(snippet): Executa codi

Procés:

Thought 1: [Raonament sobre què fer primer]
Action 1: [Eina a usar i paràmetres]
Observation 1: [Resultat de l'acció]

Thought 2: [Raonament sobre el següent pas]
Action 2: [Eina a usar i paràmetres]
Observation 2: [Resultat de l'acció]

Thought 3: [Raonament final]
Answer: [Resposta final]
```

### Exemple pràctic
```
Tasca: Quantes calories té un Big Mac comparat amb les calories diàries recomanades?

Thought 1: Necessito saber les calories d'un Big Mac
Action 1: search("Big Mac calories")
Observation 1: Un Big Mac té 563 calories

Thought 2: Ara necessito les calories diàries recomanades
Action 2: search("recommended daily calorie intake adult")
Observation 2: 2000-2500 calories per adult

Thought 3: Ara puc calcular el percentatge
Action 3: calculate(563 / 2000 * 100)
Observation 3: 28.15%

Answer: Un Big Mac (563 cal) representa aproximadament el 28% de les calories diàries recomanades (2000 cal).
```

---

## 🎭 3. Persona Pattern

Crea persones detallades per respostes contextualitzades.

### Template
```
# PERSONA: [Nom]

## Perfil
- Professió: [Rol]
- Experiència: [Anys i àrees]
- Estil de comunicació: [Formal/Informal, Tècnic/Accessible]
- Valors: [Què prioritza]
- Limitacions: [Què NO sap o fa]

## Coneixements
- Expert en: [Àrees d'expertesa]
- Familiar amb: [Coneixements secundaris]
- Desconeix: [Àrees fora del seu domini]

## Comportament
- Davant preguntes fora del seu domini: [Com respon]
- Davant incertesa: [Com ho gestiona]
- Estil de resolució: [Enfocament típic]

---

Ara, com a [Nom], respon a:
[Pregunta]
```

---

## 🔍 4. Retrieval-Augmented Generation (RAG) Pattern

Estructura per integrar informació recuperada.

### Template
```
# CONTEXT RECUPERAT
Les següents són fonts rellevants per respondre la pregunta:

## Font 1: [Títol/Font]
"""
[Contingut recuperat]
"""

## Font 2: [Títol/Font]
"""
[Contingut recuperat]
"""

## Font 3: [Títol/Font]
"""
[Contingut recuperat]
"""

# INSTRUCCIONS
Basant-te NOMÉS en el context proporcionat:
1. Respon la pregunta de manera precisa
2. Cita les fonts quan facis afirmacions
3. Si la informació no és suficient, indica-ho
4. NO inventis informació que no estigui al context

# PREGUNTA
[Pregunta de l'usuari]

# RESPOSTA
```

---

## 🎯 5. Least-to-Most Prompting

Descompon problemes complexos en subproblemes.

### Quan usar-lo
- Problemes que es poden dividir
- Aprenentatge progressiu
- Tasques de composició

### Template
```
PROBLEMA COMPLEX:
[Descripció del problema]

DESCOMPOSICIÓ EN SUBPROBLEMES:

## Subproblema 1 (més simple):
[Pregunta/Tasca simple]
Solució: [Resposta]

## Subproblema 2 (usant #1):
[Pregunta que depèn de #1]
Solució: [Resposta]

## Subproblema 3 (usant #1 i #2):
[Pregunta que depèn dels anteriors]
Solució: [Resposta]

## SOLUCIÓ FINAL:
Combinant les solucions anteriors:
[Resposta completa al problema original]
```

---

## 🔄 6. Self-Refinement / Iterative Refinement

El model millora la seva pròpia resposta.

### Template
```
TASCA: [Descripció]

## INTENT 1:
[Primera resposta del model]

## AUTO-CRÍTICA 1:
Punts forts:
- [Què està bé]

Punts febles:
- [Què es pot millorar]

Suggeriments:
- [Com millorar-ho]

## INTENT 2 (REFINAT):
[Resposta millorada incorporant la crítica]

## AUTO-CRÍTICA 2:
[Repeteix el procés si cal]

## RESPOSTA FINAL:
[Versió final després de refinaments]
```

---

## 📊 7. Structured Output with Schema

Força sortides estructurades amb esquema.

### Template JSON Schema
```
Analitza el següent text i extreu informació en el format JSON especificat.

TEXT:
"""
[Text a analitzar]
"""

ESQUEMA DE SORTIDA (segueix-lo exactament):
{
  "entitats": [
    {
      "nom": "string",
      "tipus": "PERSONA | ORGANITZACIÓ | LLOC",
      "mencions": ["string"]
    }
  ],
  "relacions": [
    {
      "subjecte": "string",
      "predicat": "string",
      "objecte": "string"
    }
  ],
  "sentiment": {
    "general": "POSITIU | NEGATIU | NEUTRAL",
    "puntuació": 0.0  // -1 a 1
  },
  "resum": "string (màx 100 paraules)"
}

Retorna NOMÉS el JSON, sense explicacions.
```

---

## 🧪 8. Hypothesis Testing Pattern

Per validar afirmacions o hipòtesis.

### Template
```
HIPÒTESI A TESTAR:
"[Afirmació a verificar]"

## ANÀLISI

### Evidència A FAVOR:
1. [Argument/Dada que suporta]
2. [Argument/Dada que suporta]
3. [Argument/Dada que suporta]

### Evidència EN CONTRA:
1. [Argument/Dada que contradiu]
2. [Argument/Dada que contradiu]
3. [Argument/Dada que contradiu]

### LIMITACIONS DE L'ANÀLISI:
- [Informació que falta]
- [Possibles biaixos]
- [Supòsits fets]

### VEREDICTE:
- Conclusió: [CONFIRMAT / REFUTAT / INCONCLUSIU]
- Confiança: [ALTA / MITJANA / BAIXA]
- Raonament: [Explicació breu]
```

---

## 🎓 9. Socratic Method Pattern

Guia l'aprenentatge amb preguntes.

### Template
```
TEMA: [Concepte a explorar]
OBJECTIU: Ajudar a entendre [X] mitjançant preguntes guiades

En lloc de donar la resposta directament, faré preguntes que guiïn el raonament:

1. [Pregunta inicial per establir coneixement base]
   → Resposta de l'usuari → 
   
2. [Pregunta que construeix sobre la resposta anterior]
   → Resposta de l'usuari →
   
3. [Pregunta que introdueix un nou aspecte]
   → Resposta de l'usuari →
   
4. [Pregunta que connecta conceptes]
   → Resposta de l'usuari →
   
5. [Pregunta final que porta a la comprensió desitjada]

SÍNTESI FINAL:
Basant-nos en les respostes, ara podem concloure que...
```

---

## 🔀 10. Multi-Agent Debate Pattern

Múltiples "agents" debaten per arribar a una conclusió.

### Template
```
QÜESTIÓ: [Tema a debatre]

## RONDA 1

### Agent A (Advocat de [Posició 1]):
[Argument inicial]

### Agent B (Advocat de [Posició 2]):
[Argument inicial]

### Agent C (Escèptic/Devil's Advocate):
[Preguntes i objeccions]

## RONDA 2

### Agent A (Resposta a objeccions):
[Contra-arguments]

### Agent B (Resposta a objeccions):
[Contra-arguments]

### Agent C (Anàlisi):
[Avaluació dels arguments]

## SÍNTESI

### Moderador (Síntesi final):
Després del debat:
- Punts de consens: [X]
- Punts de desacord: [Y]
- Conclusió més robusta: [Z]
- Nivell de confiança: [ALTA/MITJANA/BAIXA]
```

---

*10 patrons avançats per desafiar els límits del prompting*
