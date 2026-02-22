---
title: "Agent Self-Improvement — Autonomous Learning & Pattern Extraction"
version: "1.0"
category: "25-ai-skills-agents"
tags: ["skills", "agents", "ai", "self-improvement", "learning", "feedback-loop", "skill-writer", "performance"]
author: "garri333"
description: "Prompt for creating self-improving agents that analyze performance, extract patterns, codify learnings, auto-generate improvements, and maintain a feedback loop after each session."
language: "en"
---

# Agent Self-Improvement — Autonomous Learning & Pattern Extraction

## Prompt

You are an expert **AI Agent Performance Architect**. Your task is to help me create a **self-improving agent system** that automatically gets better over time by analyzing its own performance, extracting patterns from successes and failures, and codifying learnings into reusable skills.

### Context & Background

Most AI agents start fresh every session — they repeat the same mistakes, rediscover the same patterns, and never learn from experience. A self-improving agent breaks this cycle by:

1. **Analyzing** each session after completion
2. **Extracting** patterns from what worked and what didn't
3. **Codifying** learnings into persistent skills and preferences
4. **Applying** those learnings automatically in future sessions
5. **Tracking** performance improvement over time

This creates a positive feedback loop where the agent becomes measurably more effective with each interaction.

### Your Instructions

**STEP 1 — Post-Session Analysis Protocol**

After every coding session (or at the end of a significant task), run this analysis:

```markdown
## Session Analysis Report

### Session Metadata
- **Date**: <YYYY-MM-DD HH:MM>
- **Duration**: <estimated time>
- **Task**: <what was the goal>
- **Outcome**: ✅ Success / ⚠️ Partial / ❌ Failed
- **Iterations**: <how many attempts before success>

### What Worked Well
1. <specific action that produced good results>
   - **Pattern**: <generalizable pattern>
   - **Reusable?**: Yes/No
   
2. <specific action that produced good results>
   - **Pattern**: <generalizable pattern>
   - **Reusable?**: Yes/No

### What Didn't Work
1. <specific action that failed or was inefficient>
   - **Root Cause**: <why it failed>
   - **Better Approach**: <what should have been done instead>
   - **Preventable?**: Yes/No
   
2. <specific action that failed or was inefficient>
   - **Root Cause**: <why it failed>
   - **Better Approach**: <what should have been done instead>

### Tools/Approaches Used
| Tool/Approach | Effectiveness (1-5) | Notes |
|--------------|---------------------|-------|
| <tool 1> | 5 | <why it worked well> |
| <tool 2> | 2 | <why it underperformed> |

### Time Analysis
| Phase | Time Spent | Optimal Time | Gap |
|-------|-----------|--------------|-----|
| Understanding requirements | 10 min | 5 min | Slow — need better requirement parsing |
| Implementation | 20 min | 15 min | OK |
| Debugging | 30 min | 10 min | Too long — root cause found late |
| Testing | 10 min | 10 min | On target |

### Key Decisions Made
1. **Decision**: <what was decided>
   - **Alternatives considered**: <what else was considered>
   - **Rationale**: <why this was chosen>
   - **Result**: <how it turned out>
```

**STEP 2 — Pattern Extraction Engine**

Extract generalizable patterns from the session analysis:

```python
# Pattern categories to extract:

PATTERN_TYPES = {
    "solution_pattern": {
        "description": "A reusable approach to solving a class of problems",
        "example": "When building CRUD endpoints in Django, always create serializer → viewset → url → test in that order",
        "trigger": "When the user asks to create CRUD endpoints",
        "confidence": 0.0  # Increases with each successful use
    },
    "error_pattern": {
        "description": "A common mistake and how to avoid it",
        "example": "Don't use `datetime.now()` in Django — use `timezone.now()` for timezone awareness",
        "trigger": "When writing datetime code in Django",
        "prevention": "Always import from django.utils.timezone"
    },
    "optimization_pattern": {
        "description": "A way to do something faster or better",
        "example": "Use bulk_create instead of create in a loop for >10 records",
        "trigger": "When creating multiple database records",
        "improvement": "10x faster for 100+ records"
    },
    "user_preference": {
        "description": "Something the user prefers",
        "example": "User prefers function-based views over class-based views",
        "trigger": "When choosing view implementation style",
        "source": "Explicit user request on 2026-02-15"
    },
    "tool_preference": {
        "description": "Which tools/libraries work best for what",
        "example": "Use Vitest instead of Jest for Vite projects — faster, native support",
        "trigger": "When setting up testing in a Vite project",
        "evidence": "3 successful uses, 0 failures"
    }
}
```

**Pattern extraction process:**

```markdown
For each session, extract patterns by asking:

1. **Did I solve a problem that might recur?**
   → Create a SOLUTION PATTERN
   → Include: trigger condition, step-by-step solution, expected outcome

2. **Did I make a mistake I should avoid next time?**
   → Create an ERROR PATTERN
   → Include: what went wrong, root cause, prevention rule

3. **Did I find a faster/better way to do something?**
   → Create an OPTIMIZATION PATTERN
   → Include: old approach, new approach, improvement metric

4. **Did the user express a preference?**
   → Create a USER PREFERENCE
   → Include: what they prefer, context, source

5. **Did I discover which tool works best for what?**
   → Create a TOOL PREFERENCE
   → Include: tool name, best use case, evidence
```

**STEP 3 — Skill Writer — Auto-Generate New Skills**

When a pattern has been validated 3+ times, automatically generate a SKILL.md for it:

```markdown
## Skill Writer Process

### Trigger: Pattern confidence ≥ 0.8 AND validated ≥ 3 times

### Input: Extracted pattern with examples

### Process:
1. Analyze the pattern's trigger conditions → write "When to Use" section
2. Analyze the solution steps → write "Instructions" section
3. Gather all examples where this pattern was applied → write "Examples" section
4. Identify edge cases from failures → write "Boundaries" section
5. Calculate optimal token size → set in frontmatter

### Output: Complete SKILL.md file

### Quality Gate:
- Run through Skill Quality Validation (see skill-quality-validation.prompt.md)
- Must score ≥ 75/100 to be auto-installed
- If < 75, flag for human review with specific improvement suggestions
```

**Auto-generated skill template:**

```yaml
---
skill_name: "<auto-generated-from-pattern-name>"
version: "0.1.0"  # Start at 0.x until human-reviewed
description: "<from pattern description>"
author: "agent-self-improvement"
tags: <auto-extracted from pattern context>
compatible_agents: ["claude-code", "cursor", "copilot"]
triggers: <from pattern trigger conditions>
complexity: <inferred from step count>
estimated_tokens: <calculated>
last_updated: "<today>"
auto_generated: true
confidence: <pattern confidence score>
validated_count: <number of successful uses>
---

# <Pattern Name>

## Purpose
<From pattern description>

## When to Use
<From pattern trigger conditions>

## Instructions
<From pattern solution steps>

## Boundaries
<From pattern edge cases and failures>

## Examples
<From actual session examples where this pattern was applied>

## Origin
- **First observed**: <date of first occurrence>
- **Validation count**: <N successful uses>
- **Confidence**: <score>
- **Source sessions**: <list of session dates>
```

**STEP 4 — Performance Tracking Dashboard**

Track improvement metrics over time:

```markdown
## Performance Dashboard

### Overall Metrics (Last 30 Days)
| Metric | Current | Previous | Trend |
|--------|---------|----------|-------|
| Task success rate | 94% | 87% | ↑ +7% |
| Average iterations to solution | 1.3 | 2.1 | ↑ -38% |
| Average debugging time | 8 min | 22 min | ↑ -64% |
| Skills auto-generated | 7 | 3 | ↑ +133% |
| Patterns extracted | 23 | 12 | ↑ +92% |
| User satisfaction (inferred) | 4.2/5 | 3.8/5 | ↑ +11% |

### Skills Performance
| Skill | Uses | Success Rate | Avg Time Saved |
|-------|------|-------------|----------------|
| django-crud-builder | 12 | 100% | 15 min/use |
| react-form-pattern | 8 | 87.5% | 10 min/use |
| docker-compose-setup | 5 | 100% | 20 min/use |
| api-error-handling | 15 | 93% | 8 min/use |

### Error Reduction
| Error Type | Occurrences (Before) | Occurrences (After) | Reduction |
|-----------|---------------------|---------------------|-----------|
| Import errors | 8/month | 1/month | -87.5% |
| Type mismatches | 12/month | 3/month | -75% |
| Missing migrations | 5/month | 0/month | -100% |
| Wrong test assertions | 6/month | 2/month | -67% |

### Learning Velocity
- **Week 1**: 3 patterns extracted, 0 skills generated
- **Week 2**: 5 patterns extracted, 1 skill generated  
- **Week 3**: 8 patterns extracted, 3 skills generated
- **Week 4**: 7 patterns extracted, 3 skills generated
- **Trend**: Accelerating pattern recognition, stable skill generation
```

**STEP 5 — Feedback Loop Integration**

Wire the self-improvement system into your agent's workflow:

```
┌─────────────────────────────────────────────────┐
│                 AGENT SESSION                     │
│                                                   │
│  1. Load context + memories + skills              │
│  2. Execute task                                  │
│  3. ─── POST-SESSION HOOK ───                     │
│     │                                             │
│     ├─→ Run Session Analysis (Step 1)             │
│     ├─→ Extract Patterns (Step 2)                 │
│     ├─→ Update Performance Metrics (Step 4)       │
│     ├─→ Check if any pattern ready for skill      │
│     │   generation (confidence ≥ 0.8, count ≥ 3)  │
│     ├─→ If yes: Run Skill Writer (Step 3)         │
│     ├─→ If new skill: Validate quality ≥ 75       │
│     ├─→ If valid: Auto-install skill              │
│     └─→ Update memory store                       │
│                                                   │
│  4. Save session log                              │
│  5. Ready for next session (now smarter)          │
└─────────────────────────────────────────────────┘
```

**Implementation as an end-of-session prompt:**

```markdown
Before ending this session, perform a self-improvement cycle:

1. **Analyze this session**: What was the task? What was the outcome?
   Rate: success/partial/failed and count iterations.

2. **Extract patterns**: 
   - What worked well? (Create solution patterns)
   - What failed? (Create error patterns)
   - What could be faster? (Create optimization patterns)
   - Did the user express any preferences? (Create preference patterns)

3. **Update learnings file**: Append new patterns to `.agent-memory/LEARNINGS.md`

4. **Check for auto-skill generation**: 
   Any pattern with 3+ validations and 80%+ confidence? Generate a SKILL.md.

5. **Update metrics**: Log session metrics to `.agent-memory/metrics.json`

6. **Report**: Show me a brief summary of what was learned and any auto-generated skills.
```

**STEP 6 — Continuous Improvement Suggestions**

At the start of each session, proactively suggest improvements:

```markdown
## 🔄 Improvement Suggestions (Auto-Generated)

Based on your last 10 sessions, I suggest:

### High Impact (implement now)
1. **Create a "Python import fixer" skill** — You've fixed import errors in 7/10 sessions.
   Pattern is clear: check for missing `__init__.py`, verify virtual env, check PYTHONPATH.
   Confidence: 0.92 | Estimated time saved: 5 min/session

### Medium Impact (consider this week)  
2. **Standardize error response format** — 4/10 sessions involved reformatting API errors.
   Suggest creating a DRF exception handler skill.
   Confidence: 0.78 | Estimated time saved: 3 min/session

### Low Impact (backlog)
3. **Docker compose health checks** — 2/10 sessions had container startup issues.
   Pattern emerging, needs 1 more validation.
   Confidence: 0.65 | Estimated time saved: 10 min/occurrence
```

### Output Format

After each session, generate:
1. Session Analysis Report (compact, 10-15 lines)
2. Extracted Patterns (if any)
3. Auto-generated Skill (if any pattern is ready)
4. Updated Performance Metrics (key numbers only)
5. Top 3 Improvement Suggestions for next session

### Integration

Add this to your agent's system prompt or AGENTS.md:

```markdown
## Self-Improvement Protocol

At the end of each significant task:
1. Run post-session analysis
2. Extract and store patterns in .agent-memory/LEARNINGS.md
3. Update metrics in .agent-memory/metrics.json
4. Generate new skills when patterns are validated (≥3 uses, ≥80% confidence)
5. At session start, review and suggest top improvements
```

---

*Architecture: Feedback Loop with Pattern Extraction + Skill Writer. Storage: .agent-memory/ directory. Compatible with: any AI coding agent with file access.*
