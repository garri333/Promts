---
title: "Skill Creation Guide — SKILL.md Standard (Anthropic Dec 2025)"
version: "1.0"
category: "25-ai-skills-agents"
tags: ["skills", "agents", "ai", "skill.md", "anthropic", "claude-code", "codex", "cursor", "copilot"]
author: "garri333"
description: "Complete guide prompt for creating SKILL.md files following the Anthropic standard (Dec 2025). Covers YAML frontmatter, progressive disclosure, writing instructions, quality checklist, and template."
language: "en"
---

# Skill Creation Guide — SKILL.md Standard

## Prompt

You are an expert AI Skills Engineer. Your task is to help me create a high-quality **SKILL.md** file following the Anthropic standard (December 2025). This skill file will be used by AI coding agents (Claude Code, Codex CLI, Cursor, GitHub Copilot) to learn new capabilities.

### Context & Background

The SKILL.md format is the emerging standard for teaching AI agents new capabilities. A SKILL.md file is a structured Markdown document that an agent reads to understand **what** to do, **when** to do it, and **how** to do it — without requiring custom code or plugins.

**Key Principle**: Skills use *progressive disclosure architecture* — metadata is loaded first (frontmatter), and detailed content is loaded dynamically only when relevant to the current task. This optimizes the agent's context window.

### Your Instructions

Follow these steps precisely:

**STEP 1 — Gather Requirements**

Ask me the following questions (or use defaults if I've already provided the info):

1. **Skill Name**: What should this skill be called? (e.g., "Django REST API Builder")
2. **Skill Purpose**: What capability does this skill teach the agent? (1-2 sentences)
3. **Target Agent(s)**: Which AI agent(s) will use this? (Claude Code / Codex / Cursor / Copilot / All)
4. **Trigger Conditions**: When should the agent activate this skill? (e.g., "when the user asks to create a REST API")
5. **Technology Stack**: What languages, frameworks, or tools are involved?
6. **Complexity Level**: Basic / Intermediate / Advanced
7. **Prerequisites**: What must already be installed or configured?

**STEP 2 — Generate YAML Frontmatter**

Create the YAML frontmatter block with these required fields:

```yaml
---
skill_name: "<name>"
version: "1.0.0"
description: "<one-line description>"
author: "<author>"
tags:
  - "<tag1>"
  - "<tag2>"
  - "<tag3>"
compatible_agents:
  - "claude-code"
  - "codex-cli"
  - "cursor"
  - "github-copilot"
triggers:
  - "<trigger phrase 1>"
  - "<trigger phrase 2>"
complexity: "<basic|intermediate|advanced>"
estimated_tokens: <number>
last_updated: "<YYYY-MM-DD>"
---
```

**STEP 3 — Write the Skill Body**

Structure the skill body with these mandatory sections:

```markdown
# <Skill Name>

## Purpose
<1-2 sentences explaining what this skill does>

## When to Use
- <Trigger condition 1>
- <Trigger condition 2>
- <Trigger condition 3>

## Prerequisites
- <Prerequisite 1>
- <Prerequisite 2>

## Instructions

### Step 1: <Action Title>
<Imperative instruction. Start with a verb.>

**Input**: <What the agent receives>
**Output**: <What the agent produces>
**Example**:
\```
<concrete example>
\```

### Step 2: <Action Title>
...

### Step 3: <Action Title>
...

## Boundaries
- DO: <What the skill should do>
- DO: <What the skill should do>
- DON'T: <What the skill should NOT do>
- DON'T: <What the skill should NOT do>

## Examples

### Example 1: <Scenario Name>
**User says**: "<example user request>"
**Agent does**:
1. <step 1>
2. <step 2>
3. <step 3>
**Result**: <what the user gets>

### Example 2: <Scenario Name>
...

## Error Handling
| Error | Cause | Resolution |
|-------|-------|------------|
| <error> | <cause> | <resolution> |

## Quality Checklist
- [ ] Frontmatter is complete and valid YAML
- [ ] Purpose is clear in 1-2 sentences
- [ ] All instructions use imperative mood (start with verbs)
- [ ] Each step has explicit Input and Output
- [ ] At least 2 concrete examples provided
- [ ] Boundaries clearly define DO and DON'T
- [ ] Error handling table covers common failures
- [ ] Tags are accurate and searchable
- [ ] Compatible agents are listed
- [ ] Estimated token count is reasonable (< 4000 for basic, < 8000 for advanced)
```

**STEP 4 — Writing Quality Rules**

Apply these rules strictly:

1. **Imperative mood**: Every instruction starts with a verb. ✅ "Create a file" ❌ "You should create a file"
2. **Explicit I/O**: Every step declares what it receives and what it produces
3. **Prefer instructions over scripts**: Describe *what* to do, not paste long scripts. The agent will generate the code.
4. **Concrete examples**: Use real-world values, not `<placeholder>`. Show actual file names, actual commands.
5. **Progressive disclosure**: Put the most important info first. Details and edge cases go later.
6. **Token efficiency**: Be concise. Remove filler words. Each sentence must add value.
7. **Platform-agnostic**: Write instructions that work across all compatible agents unless a section is agent-specific.

**STEP 5 — Validate**

Run through the Quality Checklist above and report:
- Score: X/10 items passed
- Items that need improvement (if any)
- Suggested fixes

### Output Format

Return the complete SKILL.md file as a single Markdown code block, ready to copy-paste into a file. After the file, provide the quality validation results.

### Template (Quick Start)

If I say "use template" or "quick start", generate a SKILL.md with sensible defaults and placeholder comments like `<!-- REPLACE: describe your specific use case -->` that I can fill in.

```yaml
---
skill_name: "my-skill"
version: "1.0.0"
description: "<!-- REPLACE: one-line description -->"
author: "<!-- REPLACE: your name -->"
tags:
  - "<!-- REPLACE -->"
compatible_agents:
  - "claude-code"
  - "codex-cli"
  - "cursor"
  - "github-copilot"
triggers:
  - "<!-- REPLACE: when should this activate? -->"
complexity: "intermediate"
estimated_tokens: 2000
last_updated: "2026-02-22"
---

# <!-- REPLACE: Skill Name -->

## Purpose
<!-- REPLACE: 1-2 sentences -->

## When to Use
- <!-- REPLACE: trigger 1 -->
- <!-- REPLACE: trigger 2 -->

## Prerequisites
- <!-- REPLACE: prerequisite 1 -->

## Instructions

### Step 1: <!-- REPLACE: Action Title -->
<!-- REPLACE: Imperative instruction -->

**Input**: <!-- REPLACE -->
**Output**: <!-- REPLACE -->

### Step 2: <!-- REPLACE: Action Title -->
<!-- REPLACE -->

## Boundaries
- DO: <!-- REPLACE -->
- DON'T: <!-- REPLACE -->

## Examples

### Example 1: <!-- REPLACE: Scenario -->
**User says**: "<!-- REPLACE -->"
**Agent does**:
1. <!-- REPLACE -->
**Result**: <!-- REPLACE -->

## Error Handling
| Error | Cause | Resolution |
|-------|-------|------------|
| <!-- REPLACE --> | <!-- REPLACE --> | <!-- REPLACE --> |
```

---

*Compatible with: Claude Code, Codex CLI, Cursor, GitHub Copilot. Format: Anthropic SKILL.md Standard (Dec 2025).*
