---
title: "Agent Memory Patterns — Persistent Triple Memory System"
version: "1.0"
category: "25-ai-skills-agents"
tags: ["skills", "agents", "ai", "memory", "persistence", "lancedb", "git-notes", "embeddings", "context-window"]
author: "garri333"
description: "Prompt for implementing persistent memory in AI agents using triple memory system (LanceDB + Git-Notes + File-based). Covers session state persistence, context window management, memory categories, and semantic retrieval."
language: "en"
---

# Agent Memory Patterns — Persistent Triple Memory System

## Prompt

You are an expert AI Memory Systems Architect. Your task is to help me implement **persistent memory** in my AI agent so it retains knowledge, preferences, and learnings across sessions. You will guide me through building a triple memory system using LanceDB, Git-Notes, and file-based storage.

### Context & Background

AI agents lose all context between sessions. This is a fundamental limitation — every new chat starts from zero. Persistent memory solves this by storing and retrieving relevant information across sessions.

The **Triple Memory System** combines three complementary storage mechanisms:

| Layer | Technology | Purpose | Speed | Capacity |
|-------|-----------|---------|-------|----------|
| **L1: Semantic Memory** | LanceDB (vector DB) | Semantic search over past interactions | Fast | Unlimited |
| **L2: Structured Memory** | Git-Notes | Version-controlled structured knowledge | Medium | Per-repo |
| **L3: File Memory** | Markdown files | Human-readable persistent context | Fast | Unlimited |

### Your Instructions

**STEP 1 — Assess Memory Requirements**

Ask me:
1. **Agent platform**: Claude Code / Codex / Cursor / Custom
2. **Project type**: Single repo / Multi-repo / Organization-wide
3. **Memory scope**: Project-specific / User-global / Team-shared
4. **Key memory categories needed** (select all that apply):
   - Facts (project architecture, tech stack, conventions)
   - Preferences (coding style, naming conventions, tool preferences)
   - Decisions (architectural decisions, trade-offs made, reasons)
   - Learnings (what worked, what failed, patterns discovered)
   - Context (current sprint goals, open issues, blockers)

**STEP 2 — Implement Layer 1: Semantic Memory (LanceDB)**

Set up vector-based semantic search for past interactions:

```python
# memory_semantic.py — LanceDB Semantic Memory Layer

import lancedb
import os
from datetime import datetime

# Initialize LanceDB
DB_PATH = os.path.expanduser("~/.agent-memory/semantic")
db = lancedb.connect(DB_PATH)

# Define memory schema
SCHEMA = {
    "id": "str",           # Unique memory ID
    "content": "str",      # The memory content (text)
    "category": "str",     # fact | preference | decision | learning | context
    "project": "str",      # Project identifier
    "tags": "str",         # Comma-separated tags
    "importance": "float", # 0.0 to 1.0
    "created_at": "str",   # ISO 8601 timestamp
    "updated_at": "str",   # ISO 8601 timestamp
    "source": "str",       # Where this memory came from
    "vector": "vector(384)" # Embedding vector (all-MiniLM-L6-v2)
}

def store_memory(content: str, category: str, project: str, 
                 tags: list, importance: float = 0.5) -> str:
    """Store a new memory with automatic embedding generation."""
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    memory_id = f"mem_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{hash(content) % 10000}"
    embedding = model.encode(content).tolist()
    
    table_name = f"memories_{project}"
    if table_name not in db.table_names():
        table = db.create_table(table_name, [{
            "id": memory_id,
            "content": content,
            "category": category,
            "project": project,
            "tags": ",".join(tags),
            "importance": importance,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "source": "agent-session",
            "vector": embedding
        }])
    else:
        table = db.open_table(table_name)
        table.add([{
            "id": memory_id,
            "content": content,
            "category": category,
            "project": project,
            "tags": ",".join(tags),
            "importance": importance,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "source": "agent-session",
            "vector": embedding
        }])
    
    return memory_id

def recall_memories(query: str, project: str, top_k: int = 5, 
                    category: str = None) -> list:
    """Retrieve relevant memories using semantic search."""
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    table_name = f"memories_{project}"
    if table_name not in db.table_names():
        return []
    
    table = db.open_table(table_name)
    query_embedding = model.encode(query).tolist()
    
    results = table.search(query_embedding).limit(top_k)
    if category:
        results = results.where(f"category = '{category}'")
    
    return results.to_list()
```

**STEP 3 — Implement Layer 2: Structured Memory (Git-Notes)**

Use Git-Notes for version-controlled, structured knowledge:

```bash
# Store a memory as a git note attached to the current commit
git notes --ref=agent-memory add -m '{
  "category": "decision",
  "content": "Chose PostgreSQL over MySQL for JSONB support and better concurrent writes",
  "importance": 0.9,
  "tags": ["database", "architecture"],
  "date": "2026-02-22"
}'

# Retrieve all agent memories
git notes --ref=agent-memory list

# Search memories
git log --notes=agent-memory --all | grep -A5 "database"

# Export all memories
git notes --ref=agent-memory list | while read blob commit; do
  echo "=== Commit: $commit ==="
  git notes --ref=agent-memory show $commit
done
```

```python
# memory_git.py — Git-Notes Memory Layer

import subprocess
import json
from datetime import datetime

def store_git_memory(content: str, category: str, tags: list, 
                     importance: float = 0.5) -> bool:
    """Store a memory as a git note on the current HEAD."""
    memory = {
        "category": category,
        "content": content,
        "importance": importance,
        "tags": tags,
        "timestamp": datetime.now().isoformat(),
        "source": "agent-session"
    }
    
    try:
        # Append to existing note or create new
        existing = subprocess.run(
            ["git", "notes", "--ref=agent-memory", "show", "HEAD"],
            capture_output=True, text=True
        )
        
        if existing.returncode == 0:
            # Append to existing
            memories = json.loads(f"[{existing.stdout}]") if existing.stdout.strip() else []
            memories.append(memory)
            note_content = json.dumps(memories, indent=2)
            subprocess.run(
                ["git", "notes", "--ref=agent-memory", "add", "-f", "-m", note_content, "HEAD"],
                check=True
            )
        else:
            # Create new
            subprocess.run(
                ["git", "notes", "--ref=agent-memory", "add", "-m", json.dumps([memory], indent=2), "HEAD"],
                check=True
            )
        return True
    except subprocess.CalledProcessError:
        return False

def recall_git_memories(category: str = None, limit: int = 20) -> list:
    """Retrieve memories from git notes."""
    try:
        result = subprocess.run(
            ["git", "log", "--notes=agent-memory", "--format=%H %N", f"-{limit}"],
            capture_output=True, text=True, check=True
        )
        
        memories = []
        for line in result.stdout.strip().split('\n'):
            if line.strip():
                try:
                    parts = line.split(' ', 1)
                    if len(parts) > 1 and parts[1].strip():
                        parsed = json.loads(parts[1])
                        if isinstance(parsed, list):
                            for m in parsed:
                                if category is None or m.get("category") == category:
                                    m["commit"] = parts[0]
                                    memories.append(m)
                except json.JSONDecodeError:
                    continue
        return memories
    except subprocess.CalledProcessError:
        return []
```

**STEP 4 — Implement Layer 3: File Memory (Markdown)**

Create human-readable memory files:

```
Project Root/
├── .agent-memory/
│   ├── CONTEXT.md          # Current project context (loaded every session)
│   ├── PREFERENCES.md      # User preferences and coding style
│   ├── DECISIONS.md        # Architectural decision log
│   ├── LEARNINGS.md        # Patterns and lessons learned
│   └── sessions/
│       ├── 2026-02-22.md   # Today's session log
│       └── 2026-02-21.md   # Yesterday's session log
```

**CONTEXT.md** (loaded at start of every session):
```markdown
# Project Context — Auto-Updated by Agent

## Project
- **Name**: <project-name>
- **Stack**: <tech stack>
- **Status**: <current phase>

## Current Sprint
- **Goal**: <sprint goal>
- **Key Tasks**: 
  - [ ] <task 1>
  - [ ] <task 2>

## Recent Changes (Last 5 Sessions)
1. <change 1> — <date>
2. <change 2> — <date>

## Active Decisions
- <decision 1>: <rationale>

## Known Issues
- <issue 1>: <status>

---
*Last updated: <timestamp> by agent*
```

**PREFERENCES.md**:
```markdown
# User Preferences — Persistent

## Coding Style
- **Language**: TypeScript preferred over JavaScript
- **Formatting**: Prettier with 2-space indent
- **Naming**: camelCase for variables, PascalCase for components
- **Comments**: JSDoc for public functions only

## Communication
- **Response length**: Concise, code-first
- **Explanations**: Only when asked
- **Language**: English for code, Catalan for comments

## Tool Preferences
- **Package manager**: pnpm
- **Test runner**: Vitest
- **Linter**: ESLint + Biome
```

**STEP 5 — Context Window Management**

Implement smart context loading to avoid exceeding the agent's context window:

```python
# context_manager.py — Smart Context Loading

MAX_CONTEXT_TOKENS = 8000  # Reserve for memory loading

def load_session_context(project: str, query: str = None) -> str:
    """Load the most relevant context for this session."""
    context_parts = []
    token_budget = MAX_CONTEXT_TOKENS
    
    # Priority 1: Always load CONTEXT.md (project state) — ~500 tokens
    context_md = load_file_memory("CONTEXT.md")
    if context_md:
        context_parts.append(("## Current Project Context", context_md))
        token_budget -= estimate_tokens(context_md)
    
    # Priority 2: Always load PREFERENCES.md — ~300 tokens
    prefs = load_file_memory("PREFERENCES.md")
    if prefs:
        context_parts.append(("## User Preferences", prefs))
        token_budget -= estimate_tokens(prefs)
    
    # Priority 3: If query provided, semantic recall — ~200 tokens each
    if query and token_budget > 1000:
        memories = recall_memories(query, project, top_k=5)
        for mem in memories:
            mem_text = f"- [{mem['category']}] {mem['content']}"
            mem_tokens = estimate_tokens(mem_text)
            if token_budget - mem_tokens > 0:
                context_parts.append(("## Relevant Memories", mem_text))
                token_budget -= mem_tokens
    
    # Priority 4: Recent decisions — ~100 tokens each
    if token_budget > 500:
        decisions = recall_git_memories(category="decision", limit=5)
        for d in decisions:
            d_text = f"- {d['content']}"
            d_tokens = estimate_tokens(d_text)
            if token_budget - d_tokens > 0:
                context_parts.append(("## Recent Decisions", d_text))
                token_budget -= d_tokens
    
    return format_context(context_parts)

def estimate_tokens(text: str) -> int:
    """Rough token estimate: ~4 chars per token."""
    return len(text) // 4
```

**STEP 6 — Memory Categories Reference**

| Category | What to Store | When to Store | Retention |
|----------|--------------|---------------|-----------|
| **Facts** | Project architecture, file structure, API schemas | When discovered or changed | Permanent |
| **Preferences** | Code style, tool choices, communication style | When user expresses preference | Permanent |
| **Decisions** | Architecture choices, trade-offs, rationale | When a decision is made | Permanent |
| **Learnings** | What worked, what failed, patterns | End of each session | Permanent |
| **Context** | Sprint goals, current tasks, blockers | Start/end of session | Rolling (last 5) |

**STEP 7 — Session Lifecycle**

```
SESSION START:
1. Load CONTEXT.md (always)
2. Load PREFERENCES.md (always)
3. If user provides a task → semantic recall of relevant memories
4. Inject loaded context into agent's system prompt

DURING SESSION:
5. Detect and store new facts, preferences, decisions
6. Track important code changes
7. Note any errors and their resolutions

SESSION END:
8. Update CONTEXT.md with new state
9. Append to session log (sessions/YYYY-MM-DD.md)
10. Store new learnings in LanceDB
11. Commit git-notes with session summary
12. Remove stale context entries (> 30 days, low importance)
```

### Output Format

Generate the complete memory system setup for my specific project, including:
1. Directory structure
2. Configuration files
3. Python helper scripts
4. Initial CONTEXT.md and PREFERENCES.md templates
5. Integration instructions for my specific AI agent

---

*Architecture: Triple Memory System (LanceDB + Git-Notes + File-based). Compatible with: Claude Code, Codex CLI, Cursor, any file-aware AI agent.*
