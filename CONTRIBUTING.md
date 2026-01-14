# 🤝 Guía de Contribución - PROMTS

¡Gracias por querer contribuir! Esta guía explica cómo añadir prompts, editar existentes y mantener el repositorio organizado.

---

## 📋 Requisitos Previos

### Software necesario
- **Git** [Descargar](https://git-scm.com/download/win)
- **Cuenta GitHub** (si no la tienes, crea una gratis)
- **Editor de texto** (VS Code, Notepad++, etc.)

### Verificar instalación
```powershell
git --version
```

---

## 🚀 Flujo de Contribución (5 pasos)

### Paso 1: Fork del Repositorio
Ve a [appdieta/PROMTS](https://github.com/appdieta/PROMTS) y clica **Fork** (arriba a la derecha).

Esto crea tu propia copia del repo.

### Paso 2: Clonar tu Fork
```powershell
cd C:\ruta\donde\quieras
git clone https://github.com/TU_USUARIO/PROMTS.git
cd PROMTS
```

### Paso 3: Crear una Rama Feature
```powershell
git checkout -b feat/nombre-descriptivo
```

**Ejemplos:**
- `feat/python-async-patterns`
- `feat/testing-jest-examples`
- `feat/sql-optimization-queries`

### Paso 4: Hacer Cambios

#### Añadir nuevo prompt:
1. Identifica la categoría (ej: `07-python`)
2. Crea archivo: `categories/07-python/nuevo-prompt.md`
3. Usa plantilla YAML + contenido

**Plantilla (copiar):**
```markdown
---
title: "Título del Prompt"
version: "1.0"
category: "07-python"
tags: ["python", "async", "patterns"]
author: "Tu Nombre"
created: "2026-01-14"
updated: "2026-01-14"
language: "ca"
---

# [Título]

## Descripción

Explicación breve del prompt y cuándo usarlo.

## Prompt

[Tu prompt aquí]

## Ejemplos

[Ejemplos de uso]

## Tags

- **Tecnología**: Python
- **Función**: Async patterns
- **Nivel**: Intermedio
```

#### Editar prompt existente:
1. Navega al archivo
2. Haz cambios
3. Actualiza `updated: "YYYY-MM-DD"`

### Paso 5: Commit y Push

```powershell
# Ver cambios
git status

# Añadir cambios
git add .

# Commit con mensaje descriptivo
git commit -m "feat(07-python): add async retry pattern prompt"

# Push a tu rama
git push origin feat/nombre-descriptivo
```

**Convención de commits:**
```
[tipo](categoría): descripción breve

Tipos: feat, fix, docs, refactor, improve
```

---

## 📤 Enviar Pull Request

1. Ve a tu fork en GitHub
2. Clica **Compare & pull request**
3. Escribe descripción:
   - Qué añades
   - Por qué es útil
   - Categoría del prompt

Ejemplo:
```
## ¿Qué?
Añado prompt para async retry patterns en Python

## Por qué
Falta un ejemplo de retry logic con backoff exponencial

## Categoría
07-python (async patterns)
```

4. Clica **Create Pull Request**
5. ¡Espera review! Haremos cambios si es necesario.

---

## ✅ Checklist Antes de Pushear

- [ ] Nombre de archivo descriptivo (ej: `async-retry-pattern.md`)
- [ ] Metadatas YAML completas (title, tags, author, language)
- [ ] Contenido en Markdown bien formateado
- [ ] Prompt es claro y reutilizable
- [ ] Ejemplos incluidos
- [ ] Sin archivos de Office (.docx) - solo .md
- [ ] Rama creada desde `main` actualizado

---

## 📝 Reglas de Nomenclatura

### Nombres de archivo
- Minúsculas
- Separar palabras con guiones: `async-retry-pattern.md`
- Descriptivos y cortos

### Nombres de rama
- `feat/descripcion` - Nuevo prompt
- `fix/descripcion` - Corregir prompt existente
- `docs/descripcion` - Documentación
- `improve/descripcion` - Mejora

**Ejemplo:**
```
feat/python-dataclass-validation
fix/testing-jest-async-bug
docs/contributing-guide-update
improve/sql-query-optimization
```

---

## 🔄 Sincronizar tu Fork (Importante!)

Si otros han hecho cambios y tu fork está desactualizado:

```powershell
# Añadir repositorio original como "upstream"
git remote add upstream https://github.com/appdieta/PROMTS.git

# Traer cambios
git fetch upstream

# Actualizar tu rama main
git checkout main
git merge upstream/main

# Pushear a tu fork
git push origin main
```

---

## ❓ Preguntas Frecuentes

### P: ¿Puedo editar directamente sin fork?
**R**: No recomendado. Fork garantiza que mantienes versión sincronizada.

### P: ¿Qué si mi PR no es aceptado?
**R**: Podemos hacer cambios. Es colaborativo. No es rechazo, es mejora.

### P: ¿Puedo añadir múltiples prompts en una rama?
**R**: Sí, pero mejor separar cambios temáticos en ramas diferentes.

### P: ¿Cómo contacto si tengo dudas?
**R**: Abre un [Issue](../../issues) con etiqueta `question` o `help wanted`.

---

## 🎓 Recursos Útiles

- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F)
- [GitHub Pull Requests](https://docs.github.com/en/pull-requests)
- [Markdown Guide](https://www.markdownguide.org/)

---

## 📊 Historial de Cambios

GitHub rastreará automáticamente:
- **Quién** cambió cada línea
- **Cuándo** se cambió
- **Por qué** (en el mensaje de commit)
- **Qué** exactamente cambió

Pestaña: **History** en cada archivo.

---

**¡Gracias por contribuir! 🎉**

Si tienes preguntas, abre un Issue o contacta al mantenedor.
