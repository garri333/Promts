# 📦 Guia d'Instal·lació i Configuració

> Com configurar les bibliotecas d'agents i prompts amb GitHub Copilot Pro

## ✅ Requisits Previs

- **GitHub Account** amb Copilot Pro activat
- **VS Code** (versió 1.85+)
- **GitHub Copilot Extension** per VS Code
- **Accés a aquest repositori** (clonat o forked)

---

## 🚀 Pas 1: Instal·lar GitHub Copilot Pro

### 1.1 Activar la subscripció
1. Entra a [github.com/copilot/signup](https://github.com/copilot/signup)
2. Selecciona **Copilot Pro** ($20/mes)
3. Completa el pagament
4. Verifica que la subscripció apareix a [github.com/settings/copilot](https://github.com/settings/copilot)

### 1.2 Instal·lar l'extensió a VS Code
1. Obre VS Code
2. Vai a **Extensions** (Ctrl+Shift+X)
3. Busca "GitHub Copilot"
4. Instal·la l'extensió oficial de GitHub
5. Fes clic en **Sign in** i segueix el flux OAuth
6. Verifica que Copilot apareix a la barra inferior

---

## 🎯 Pas 2: Clonar/Descarregar la Biblioteca

### Opció A: Clonar via Git (Recomanat)

```bash
# Clona el repositori
git clone https://github.com/[tu-usuario]/PROMTS.git

# Entra a la carpeta
cd PROMTS

# Verifica l'estructura
ls -la
```

### Opció B: Descarregar ZIP

1. Ves a https://github.com/[tu-usuario]/PROMTS
2. Clica **Code → Download ZIP**
3. Descomprimeix en una carpeta
4. Obre la carpeta en VS Code

### Opció C: Usar como Submodule (Si ja tens projecte)

```bash
# Dins del teu projecte
git submodule add https://github.com/[tu-usuario]/PROMTS.git PROMTS

# Actualitza submodules
git submodule update --init --recursive
```

---

## 📂 Pas 3: Estructura de Carpetes

Un cop clonat, hauries de veure:

```
PROMTS/
├── library-agents/              # 170+ agents
│   ├── INDEX.md                 # Index complet d'agents
│   ├── agent-selector.agent.md  # Selector d'agents
│   └── README.md
│
├── library-prompts/             # 450+ prompts
│   ├── categories/              # 24 categories
│   │   ├── 01-planificacio-arquitectura/
│   │   ├── 23-chatgpt-role-prompts/  # NEW
│   │   └── 24-prompt-engineering/    # NEW
│   ├── INDEX.md                 # Index complet
│   ├── prompt-selector.prompt.md
│   └── README.md
│
├── INSTALLATION.md              # (aquest fitxer)
├── GITHUB-PRO-SETUP.md
└── README.md
```

---

## 🔧 Pas 4: Configurar VS Code

### 4.1 Configuració Recomanada

Crea o actualitza `.vscode/settings.json`:

```json
{
  "github.copilot.enable": {
    "*": true,
    "plaintext": false
  },
  "editor.suggest.showMethods": true,
  "editor.suggest.showClasses": true,
  "[markdown]": {
    "editor.wordWrap": "on",
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "files.exclude": {
    "**/.DS_Store": true,
    "**/.git": true
  }
}
```

### 4.2 Extensions Recomanades

Instal·la aquestes extensions per a millor experiència:

| Extensió | Descripció |
|----------|-----------|
| GitHub Copilot | Principal (ja instal·lada) |
| Markdown Preview Enhanced | Millor visualització de markdown |
| Prettier | Formatació de codi/markdown |
| GitLens | Integració git avançada |
| Thunder Client | Per testar APIs (opcional) |

```bash
# Instal·lar des de terminal
code --install-extension esbenp.prettier-vscode
code --install-extension yzhang.markdown-all-in-one
code --install-extension eamodio.gitlens
```

---

## ✨ Pas 5: Usar la Biblioteca amb Copilot

### 5.1 Opció A: Usar Prompts Directament

#### Mètode 1 - Copiar el contingut
```
1. Obre el fitxer del prompt que necessitis
   (ex: library-prompts/categories/01-planificacio-arquitectura/[prompt].md)

2. Copia el contingut (Ctrl+A → Ctrl+C)

3. Enganxa'l al xat de Copilot
   - Obri el xat de Copilot (Ctrl+I)
   - Enganxa el prompt (Ctrl+V)
   - Demana la tasca
```

#### Mètode 2 - Reference amb @
```
1. Obri el xat de Copilot (Ctrl+I)

2. Escriu: @[path/to/prompt.md]
   Exemple: @library-prompts/categories/01-planificacio-arquitectura/structured-autonomy-plan.prompt.md

3. Copilot carregarà automàticament el prompt
```

### 5.2 Opció B: Usar Agent Selector

```
1. Obre: library-agents/agent-selector.agent.md

2. Copia'l al xat de Copilot

3. Diga quin tipus d'agent necessites
   Exemple: "Necessito un agent expert en microserveis"

4. Copilot et dirà quin agent usar
```

### 5.3 Opció C: Usar Prompt Selector

```
1. Obre: library-prompts/prompt-selector.prompt.md

2. Segueix les preguntes interactives

3. Copilot et recomanarà els millors prompts
```

---

## 🎓 Pas 6: Workflow Recomanat per Projectes

### Projecte Web Node.js + React

```
1. PLANIFICACIÓ
   @library-prompts/categories/01-planificacio-arquitectura/structured-autonomy-plan.prompt.md
   → Descriu el teu projecte
   → Obtén plan d'arquitectura

2. GENERACIÓ DE CODI
   @library-agents/INDEX.md (busca "expert-nextjs-developer")
   → Usa l'agent NextJS
   → Genera estructura de projecte

3. TESTING
   @library-prompts/categories/03-testing/breakdown-test.prompt.md
   → Especifica els components a testar
   → Genera tests

4. DOCUMENTACIÓ
   @library-prompts/categories/04-documentacio/create-readme.prompt.md
   → Descriu el projecte
   → Genera README

5. GIT/CI
   @library-prompts/categories/10-git-cicd-github/create-github-action-workflow-specification.prompt.md
   → Configura els workflows
```

### Projecte Python + FastAPI

```
1. ARQUITECTURA
   Usa agent: expert-python-backend
   
2. GENERACIÓ
   Usa prompt: structured-autonomy-implement.prompt.md
   
3. TESTING
   Usa agent: python-mcp-expert
   
4. DOCUMENTACIÓ
   Usa prompt: create-readme.prompt.md
```

---

## 🔐 Pas 7: Configurar Accés Offline (Opcional)

Si vols accedir als prompts sense internet:

```bash
# Descarrega el repositori complet
git clone --depth=1 https://github.com/[tu-usuario]/PROMTS.git

# Genera un index local (opcional)
# Els fitxers markdown funcionen directament a l'editor
```

---

## 🐛 Troubleshooting

### ❌ Copilot no apareix al xat
**Solució:**
- Verifica que tens Copilot Pro actiu
- Reinicia VS Code
- Esborra i reinstal·la l'extensió

### ❌ Error "Cannot find module" en @references
**Solució:**
- Assegura't que el path és relatiu a VS Code
- Usa `/` en lloc de `\` fins i tot a Windows
- Prova copiant directament el contingut

### ❌ Els prompts no funcionen bé
**Solució:**
- Assegura't de seguir la versió correcta del prompt
- Prova amb GPT-4 en comptes de GPT-3.5
- Afegeix més context a la teva pregunta

---

## 📚 Passos Següents

1. ✅ Explora els INDEX.md de cada biblioteca
2. ✅ Prova 3-4 prompts/agents diferentes
3. ✅ Customitza els prompts per al teu projecte
4. ✅ Documenta els teus casos d'ús exitosos
5. ✅ Comparteix feedback amb la comunitat

---

## 🔗 Enllaços Útils

- [GitHub Copilot Docs](https://github.com/features/copilot)
- [Copilot Pro Information](https://github.com/copilot/pro)
- [VS Code Marketplace](https://marketplace.visualstudio.com)
- [Awesome Copilot GitHub](https://github.com/github/awesome-copilot)

---

*Última actualització: 2026-01-12*
*Per preguntes o problemes, crea una issue al repositori*
