# 🎯 Tècniques Fonamentals de Prompt Engineering

> Patrons bàsics que tot enginyer de prompts ha de dominar

---

## 📌 1. Zero-Shot Prompting

El model respon sense exemples previs.

### Quan usar-lo
- Tasques simples i directes
- Quan no tens exemples disponibles
- Per instruccions clares i sense ambigüitat

### Exemple
```
Classifica el sentiment d'aquest text com a POSITIU, NEGATIU o NEUTRAL:
"El producte va arribar tard però la qualitat és excel·lent"
```

---

## 📌 2. Few-Shot Prompting

Proporciona exemples per guiar el model.

### Quan usar-lo
- Tasques amb format específic
- Quan vols consistència en les respostes
- Per classificació amb categories concretes

### Template
```
Tasca: [Descripció de la tasca]

Exemples:
Input: [Exemple 1 input]
Output: [Exemple 1 output]

Input: [Exemple 2 input]
Output: [Exemple 2 output]

Input: [Exemple 3 input]
Output: [Exemple 3 output]

Ara processa:
Input: [Nou input]
Output:
```

### Exemple pràctic
```
Extreu el nom del producte i el preu de cada text.

Text: "El nou iPhone 15 Pro costa 1.199€"
Producte: iPhone 15 Pro
Preu: 1.199€

Text: "Samsung Galaxy S24 disponible per 899€"
Producte: Samsung Galaxy S24
Preu: 899€

Text: "Oferta especial: MacBook Air M3 per només 1.299€"
Producte:
Preu:
```

---

## 📌 3. Chain-of-Thought (CoT) Prompting

Força el model a mostrar el seu raonament pas a pas.

### Quan usar-lo
- Problemes matemàtics
- Raonament lògic complex
- Quan necessites verificar el procés

### Template
```
[Problema]

Pensa pas a pas:
1. Primer, identifica...
2. Després, calcula...
3. Finalment, determina...

Mostra el teu raonament complet abans de donar la resposta final.
```

### Exemple pràctic
```
Un tren surt de Barcelona a les 9:00 viatjant a 120 km/h cap a Madrid.
Un altre tren surt de Madrid a les 9:30 viatjant a 100 km/h cap a Barcelona.
La distància entre les dues ciutats és de 620 km.
A quina hora es trobaran els trens?

Pensa pas a pas i mostra tots els càlculs.
```

---

## 📌 4. Self-Consistency

Genera múltiples respostes i selecciona la més consistent.

### Quan usar-lo
- Problemes amb múltiples solucions possibles
- Quan vols reduir errors
- Per augmentar la confiança en la resposta

### Template
```
Resol aquest problema de 3 maneres diferents:

[Problema]

Mètode 1:
[Resolució]

Mètode 2:
[Resolució]

Mètode 3:
[Resolució]

Compara les tres respostes i dona la resposta final més probable.
```

---

## 📌 5. Instruction Following

Dona instruccions clares i estructurades.

### Principis clau
1. **Sigues específic**: Evita ambigüitats
2. **Usa delimitadors**: Separa seccions clarament
3. **Especifica el format**: Output esperit
4. **Inclou restriccions**: Què NO fer

### Template
```
# TASCA
[Descripció precisa de la tasca]

# INPUT
"""
[Contingut a processar]
"""

# INSTRUCCIONS
1. [Instrucció 1]
2. [Instrucció 2]
3. [Instrucció 3]

# FORMAT DE SORTIDA
[Especifica exactament com vols l'output]

# RESTRICCIONS
- NO facis [X]
- Evita [Y]
- Limita la resposta a [Z]
```

---

## 📌 6. Role Prompting

Assigna un rol o persona al model.

### Quan usar-lo
- Per obtenir perspectives específiques
- Per ajustar l'estil de comunicació
- Per simular experts

### Template
```
Ets un [ROL] amb [ANYS] anys d'experiència en [DOMINI].

El teu estil és [CARACTERÍSTIQUES].
La teva especialitat és [ESPECIALITAT].

Respon a la següent pregunta des de la teva perspectiva professional:

[PREGUNTA]
```

### Exemple pràctic
```
Ets un arquitecte de software sènior amb 15 anys d'experiència en sistemes distribuïts.

El teu estil és pragmàtic i directe.
La teva especialitat és microserveis i escalabilitat.

Revisa aquesta arquitectura i identifica problemes potencials:

[Descripció de l'arquitectura]
```

---

## 📌 7. Output Formatting

Controla el format de sortida explícitament.

### Formats comuns

#### JSON
```
Extreu la informació i retorna-la en format JSON amb aquesta estructura:
{
  "nom": "string",
  "edat": number,
  "email": "string",
  "actiu": boolean
}

Text: "[Text a processar]"
```

#### Markdown
```
Genera la documentació en format Markdown amb:
- Títols amb ##
- Llistes amb -
- Codi amb ```
- Taules quan sigui apropiat
```

#### XML
```
Retorna la resposta en format XML:
<resposta>
  <element1>valor</element1>
  <element2>valor</element2>
</resposta>
```

---

## 📌 8. Context Window Management

Gestiona el context de manera eficient.

### Estratègies
1. **Summarization**: Resumeix context anterior
2. **Chunking**: Divideix en parts processables
3. **Prioritization**: Posa informació important al principi/final
4. **Compression**: Elimina redundàncies

### Template per context llarg
```
RESUM DEL CONTEXT ANTERIOR:
[Resum breu de la conversa/document anterior]

CONTEXT ACTUAL RELLEVANT:
[Només la informació necessària per aquesta tasca]

TASCA:
[La tasca específica a realitzar]
```

---

## 📌 9. Negative Prompting

Especifica què NO ha de fer el model.

### Template
```
[Instruccions positives]

IMPORTANT - NO FACIS:
- No inventis informació
- No donis opinions personals
- No incloguis contingut ofensiu
- No utilitzis jerga tècnica innecessària
- No excedeixis [X] paraules
```

---

## 📌 10. Prompt Chaining

Encadena múltiples prompts per tasques complexes.

### Quan usar-lo
- Tasques amb múltiples passos
- Quan cada pas depèn de l'anterior
- Per mantenir qualitat en tasques llargues

### Exemple de cadena
```
PROMPT 1: Analitza aquest codi i identifica els problemes principals
→ OUTPUT 1: Llista de problemes

PROMPT 2: Per a cada problema identificat, proposa una solució
→ OUTPUT 2: Problemes + Solucions

PROMPT 3: Implementa les solucions en codi
→ OUTPUT 3: Codi corregit

PROMPT 4: Escriu tests per verificar les correccions
→ OUTPUT 4: Suite de tests
```

---

*10 tècniques fonamentals per dominar el prompt engineering*
