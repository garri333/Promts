# 🚀 GitHub Copilot Pro - Guia de Setup i Optimització

> Guia completa per maximitzar GitHub Copilot Pro amb aquestes bibliotecas

---

## 🎯 Avantatges de GitHub Copilot Pro

| Característica | Copilot Free | Copilot Pro |
|----------------|--------------|------------|
| **Chats illimitades** | 60 per dia | ✅ Illimitades |
| **Accés a GPT-4 Turbo** | ❌ | ✅ Mode predeterminat |
| **Context window** | 2k tokens | ✅ 8k tokens |
| **Priority en servers** | ❌ | ✅ Cua prioritària |
| **Web access search** | ❌ | ✅ Inclòs |
| **Custos estimats** | $0 | $20/mes |

---

## 💳 Pas 1: Subscripció a GitHub Copilot Pro

### 1.1 Activar la subscripció

```
1. Entra a github.com
2. Cli a la teva foto de perfil (arriba a la dreta)
3. Selecciona "Settings"
4. Vai a "Billing and plans"
5. Clica "Upgrade to Copilot Pro"
6. Completa el pagament
```

### 1.2 Verificar l'activació

```
1. Entra a github.com/settings/copilot
2. Hauries de veure "Your Copilot plan: Pro"
3. Apareixerà la data de renovació
```

### 1.3 Billeting i costos

- **Cost**: $20 USD/mes (es renova automàticament)
- **Facturació**: Es carrega al teu mètode de pagament registrat
- **Cancel·lació**: Pots cancel·lar en qualsevol moment a [github.com/settings/billing](https://github.com/settings/billing)
- **Probes**: Primer mes a preu reduït si tens promoció

---

## 🔐 Pas 2: Seguretat i Privacitat

### 2.1 Configurar els Teus Secrets

**MOLT IMPORTANT**: No comparteixis secrets en els prompts!

```markdown
❌ MAL:
"Crea una connexió a BD amb aquesta contrasenya: abc123"

✅ BÉ:
"Crea una connexió a BD amb secrets.DB_PASSWORD"
```

### 2.2 Configurar .gitignore

Assegura't que el teu `.gitignore` inclou:

```plaintext
# Secrets
.env
.env.local
.env.*.local
secrets/
private/

# Logs
*.log
logs/

# Build
dist/
build/
node_modules/

# IDE
.vscode/
.idea/
*.swp
```

### 2.3 Permissos de Repositori

Si fas public el repositori:

```bash
# Fes el repositori privat si conté secrets
git config --local user.name "Tu Nom"  # No public al repo

# O fes public sols les bibliotecas, privat els secrets
# Estructura recomanada:
# - PROMTS/library-agents → Public
# - PROMTS/library-prompts → Public
# - PROMTS/secrets/ → Private (a .gitignore)
```

---

## 🎛️ Pas 3: Optimitzar VS Code per Copilot Pro

### 3.1 Activa el Mode GPT-4

Per defecte, Copilot Pro usa **GPT-4 Turbo** per chats.

Per assegurar-te:

1. Obri el xat de Copilot (Ctrl+I)
2. Clica els **...** (settings del xat)
3. Verifica que diu "**GPT-4 Turbo**" (no GPT-3.5)

### 3.2 Configurar Keyboard Shortcuts

Afegeix aquests shortcuts al `~/.vscode/keybindings.json`:

```json
[
  {
    "key": "ctrl+shift+i",
    "command": "github.copilot.openSymbolFromEditor"
  },
  {
    "key": "ctrl+k ctrl+i",
    "command": "github.copilot.interactive.explain"
  },
  {
    "key": "ctrl+shift+;",
    "command": "github.copilot.comment"
  }
]
```

### 3.3 Configurar la Mida del Context

Al `.vscode/settings.json`:

```json
{
  "github.copilot.chat.maxContextLength": 8000,
  "editor.suggest.maxVisibleSuggestions": 5,
  "editor.inlineSuggest.enabled": true
}
```

---

## 📖 Pas 4: Setup de la Biblioteca

### 4.1 Crear estructura local

```bash
# Clona el repositori a una ubicació accessible
git clone https://github.com/[tu-usuario]/PROMTS.git ~/PROMTS

# Crea un symlink per accés ràpid (opcional)
ln -s ~/PROMTS ~/Documents/PROMTS
```

### 4.2 Crea favorites/bookmarks

A VS Code, obri el File Explorer i:

1. Clica el **+** al lateral per afegir folder
2. Selecciona `~/PROMTS`
3. Ara veuràs totes les categories al lateral

### 4.3 Crea snippets personalitzats

Crea `~/.config/Code/User/snippets/prompts.json`:

```json
{
  "Use Structured Plan": {
    "prefix": "plan",
    "body": "@library-prompts/categories/01-planificacio-arquitectura/structured-autonomy-plan.prompt.md\n$1",
    "description": "Usa el prompt de planificació estructurada"
  },
  "Use Agent Selector": {
    "prefix": "agent",
    "body": "@library-agents/agent-selector.agent.md\n$1",
    "description": "Usa el selector d'agents"
  }
}
```

---

## 🎯 Pas 5: Workflow Recomanat amb Copilot Pro

### 5.1 Workflow per a desenvolupament sènior

```
FASE 1: EXPLORACIÓ
├─ Obri el xat (Ctrl+I)
├─ @agent-selector.agent.md
├─ "Necessito un expert en [X]"
└─ Copilot et recomana l'agent

FASE 2: PLANIFICACIÓ
├─ @structured-autonomy-plan.prompt.md
├─ Descriu el projecte en detall
├─ Copilot genera un pla complet
└─ Itera i refina el pla

FASE 3: IMPLEMENTACIÓ
├─ Usa l'agent recomanat directament
├─ @expert-[tecnologia]-developer.agent.md
├─ "Implementa [tarea] segons [pla]"
└─ Copia el codi generat

FASE 4: TESTING
├─ @breakdown-test.prompt.md
├─ Especifica els test cases
├─ Genera suite de tests
└─ Integra a CI/CD

FASE 5: DOCUMENTACIÓ
├─ @create-readme.prompt.md
├─ Usa el codi generat
└─ Copilot documenta automàticament
```

### 5.2 Workflow per a debugging ràpid

```
PROBLEMA DETECTAT
    ↓
Obri xat (Ctrl+Shift+I)
    ↓
@library-prompts/categories/06-debugging/...
    ↓
Enganxa l'error i el codi
    ↓
"Debugging: [descripció del problema]"
    ↓
Aplica la solució suggerida
```

---

## ⚡ Pas 6: Optimitzacions de Velocitat

### 6.1 Usar Context Intel·ligent

En lloc de compartir 1000 línies, comparteix només:

```markdown
// File: src/api/handler.ts
// Lines: 45-75 (excerpt)

// El context complet que Copilot necessita
```

### 6.2 Usar Sessions de Context

Copilot Pro manté context entre missatges:

```
Missatge 1: "Sóc desenvolupa Node.js amb 5 anys d'experiència"
Missatge 2: "Necesito crear un endpoint POST"
→ Copilot recorda que ets sènior en Node.js!
```

### 6.3 Cache Eficient

Reutilitza els mateixos prefixes:

```
Bona pràctica:
1. Define l'agent una vegada
2. Fer múltiples tasques dins la mateixa sessió
3. Canvia d'agent només quan necessari
```

---

## 🔄 Pas 7: Mantenir la Biblioteca Actualizada

### 7.1 Pull updates regularment

```bash
cd ~/PROMTS

# Verifica si hi ha actualitzacions
git status

# Si hi ha canvis remots
git pull origin main

# Crea una branca per les teves customitzacions (opcional)
git checkout -b mi-customizaciones
```

### 7.2 Crear les teves versions customitzades

```bash
# Dins de la teva branca
mkdir library-prompts/categories/99-mis-prompts/

# Crea els teus prompts
cat > library-prompts/categories/99-mis-prompts/mi-prompt.md <<EOF
# Mi Prompt Custom

[Contingut del teu prompt]
EOF

# Commit
git add .
git commit -m "Add: Custom prompts for my use case"
```

---

## 💡 Pas 8: Best Practices amb Copilot Pro

### ✅ DO

- ✅ **Sigues específic**: "Crea un validador de email en TypeScript amb regex" (no "valida coses")
- ✅ **Dona context**: Include versions de frameworks, requirements especifiques
- ✅ **Usa agents especialitzats**: No preguntes a un agent genèric sobre .NET
- ✅ **Comparteix codi rellevant**: Només el necessari per entendre el problema
- ✅ **Solicita explicacions**: "Explica aquest codi linia per linia"
- ✅ **Iteració**: Refina respostes gradually

### ❌ DON'T

- ❌ **Preguntes vagues**: "Ajuda'em amb el codi" (massa ampli)
- ❌ **Compartir secrets**: Mai API keys, passwords, tokens
- ❌ **Copiar cegament**: Sempre revisa i entén el codi
- ❌ **Usar agent equivocat**: No preguntes a un agent frontend sobre DevOps
- ❌ **Contexto excessiu**: No copies 5000 línies si només 50 són rellevants
- ❌ **Ignorar errors**: Si Copilot genera codi trencat, pregunta per a corregir-lo

---

## 📊 Monitorizzar el Teu Us

### Quota d'ús mensual (Pro = Illimitada)

```
Entra a github.com/settings/copilot per veure:
- Chats usats aquesta facturació
- Commits assistits per Copilot
- Estadístiques d'ús
```

### Costos adicionals (si n'hi ha)

Copilot Pro és $20/mes fix. No hi ha costos adicionals per:
- Chats
- Commit suggestions
- Prompts reutilitzats

---

## 🎓 Recursos d'Aprenentatge

| Recurs | Tipus | Link |
|--------|-------|------|
| Copilot Documentation | Oficial | [github.com/features/copilot](https://github.com/features/copilot) |
| Copilot Tips & Tricks | Blog | [github.blog/copilot](https://github.blog) |
| VS Code Settings | Docs | [code.visualstudio.com/docs](https://code.visualstudio.com/docs) |
| Keyboard Shortcuts | Cheat Sheet | [cheat.sh/vscode](https://cheat.sh/vscode) |

---

## 🆘 Contacte i Suport

### Problemes Comuns

| Problema | Solució |
|----------|---------|
| Copilot no funciona | Reinstal·la l'extensió, reinicia VS Code |
| Auth error | Logout a GitHub, tornar a login |
| Respostes pobres | Usa context més específic, prova agent diferent |
| Limite de tokens | Usa context window de 8k més efectivament |

### Suport Oficial

- [GitHub Copilot Support](https://support.github.com/contact/github-copilot)
- [Community Discussions](https://github.com/orgs/community/discussions)
- [VS Code Issues](https://github.com/microsoft/vscode/issues)

---

## 📈 Metriques de ROI (Retorn d'Inversió)

### Cost anual
- Copilot Pro: $20 × 12 = **$240/any**

### Estalvi de temps aproximat
- Si uses correctament: **10-15 hores/setmana** (estimat)
- Valor per hora: $50-100 USD (sou de Sr. Developer)
- **Estalvi estimat: $26,000-52,000/any**

### **ROI: +10,000%** 🚀

---

## ✅ Checklist d'Instal·lació

- [ ] He comprat Copilot Pro
- [ ] He verificat l'accés al xat de Copilot
- [ ] He configurat VS Code amb els settings recomanats
- [ ] He clonat el repositori PROMTS
- [ ] He afegit les extensions recomanades
- [ ] He creat els snippets personalitzats
- [ ] He testat un prompt bàsic
- [ ] He llegit la guia de best practices
- [ ] He entès el workflow recomanat

---

*Guia actualitzada: 2026-01-12*
*Per actualitzacions, consultau el repositori principal*
