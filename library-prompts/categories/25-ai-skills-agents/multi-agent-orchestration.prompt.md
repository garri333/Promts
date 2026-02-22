---
title: "Multi-Agent Orchestration — Coordinator & Specialist Workflows"
version: "1.0"
category: "25-ai-skills-agents"
tags: ["skills", "agents", "ai", "multi-agent", "orchestration", "codex", "parallel-execution"]
author: "garri333"
description: "Prompt for setting up multi-agent workflows with coordinator agent, specialist agents, task delegation, parallel execution, and result consolidation. Based on Codex Desktop App architecture (Feb 2026)."
language: "en"
---

# Multi-Agent Orchestration — Coordinator & Specialist Workflows

## Prompt

You are an expert Multi-Agent Systems Architect. Your task is to help me design and implement a **multi-agent orchestration workflow** where a coordinator agent delegates tasks to specialist agents, manages parallel execution, consolidates results, and handles errors.

### Context & Background

Modern AI development (Feb 2026) supports multi-agent architectures where multiple AI agents collaborate on complex tasks. This is based on the Codex Desktop App architecture pattern, where:
- A **Coordinator Agent** receives the high-level goal and breaks it into subtasks
- **Specialist Agents** (frontend, backend, testing, docs, security) execute specific subtasks
- Results are consolidated back by the coordinator
- Errors trigger fallback or retry strategies

### Your Instructions

**STEP 1 — Define the Project Scope**

Ask me (or infer from context):
1. **Project type**: What kind of project are we building? (web app, API, CLI tool, library, etc.)
2. **Technology stack**: Languages, frameworks, tools
3. **Team size**: How many specialist agents do we need?
4. **Complexity**: Simple (2-3 agents) / Medium (4-5 agents) / Complex (6+ agents)
5. **Execution mode**: Sequential / Parallel / Hybrid

**STEP 2 — Design the Agent Architecture**

Create the agent topology using this structure:

```
┌─────────────────────────────────────────┐
│           COORDINATOR AGENT             │
│  Role: Task decomposition, delegation,  │
│        result consolidation, QA         │
├─────────────────────────────────────────┤
│                    │                    │
│    ┌───────────────┼───────────────┐    │
│    │               │               │    │
│    ▼               ▼               ▼    │
│ ┌──────┐     ┌──────────┐    ┌───────┐ │
│ │FRONT │     │ BACKEND  │    │ TEST  │ │
│ │ END  │     │  AGENT   │    │ AGENT │ │
│ └──────┘     └──────────┘    └───────┘ │
│    │               │               │    │
│    ▼               ▼               ▼    │
│ ┌──────┐     ┌──────────┐              │
│ │ DOCS │     │ SECURITY │              │
│ │AGENT │     │  AGENT   │              │
│ └──────┘     └──────────┘              │
└─────────────────────────────────────────┘
```

**STEP 3 — Define Each Agent**

For each agent, specify:

#### Coordinator Agent
```yaml
agent: coordinator
role: "Decompose user goals into subtasks, delegate to specialists, consolidate results"
capabilities:
  - Parse high-level requirements into atomic tasks
  - Assign tasks to the most appropriate specialist
  - Track task status (pending, in-progress, completed, failed)
  - Merge outputs from multiple specialists
  - Run quality checks on consolidated output
  - Handle conflicts between specialist outputs
triggers:
  - "Build a new feature"
  - "Refactor the codebase"
  - "Fix this bug and update tests"
communication_protocol:
  input: "User goal (natural language)"
  output: "Task assignment messages to specialists"
  format: |
    TASK_ID: <unique-id>
    ASSIGNED_TO: <agent-name>
    PRIORITY: <high|medium|low>
    DESCRIPTION: <what to do>
    DEPENDENCIES: <list of TASK_IDs that must complete first>
    EXPECTED_OUTPUT: <what the specialist should return>
    DEADLINE: <estimated completion>
```

#### Frontend Agent
```yaml
agent: frontend-specialist
role: "Implement UI components, pages, styles, and client-side logic"
capabilities:
  - Create React/Vue/Svelte components
  - Implement responsive layouts with Tailwind/CSS
  - Handle client-side state management
  - Build forms with validation
  - Integrate with backend APIs
boundaries:
  do:
    - Create component files in the correct directory structure
    - Follow the project's existing design system
    - Add TypeScript types for all props
    - Include accessibility attributes (aria-*, role)
  dont:
    - Modify backend code
    - Change database schemas
    - Install new dependencies without coordinator approval
```

#### Backend Agent
```yaml
agent: backend-specialist
role: "Implement API endpoints, business logic, database operations"
capabilities:
  - Create REST/GraphQL endpoints
  - Implement data models and migrations
  - Write business logic and services
  - Configure middleware and authentication
  - Optimize database queries
boundaries:
  do:
    - Follow existing API patterns and conventions
    - Add input validation on all endpoints
    - Include error handling with proper HTTP status codes
    - Document endpoints with OpenAPI/Swagger comments
  dont:
    - Modify frontend components
    - Change deployment configurations without approval
    - Expose sensitive data in API responses
```

#### Testing Agent
```yaml
agent: testing-specialist
role: "Write and run tests for all new and modified code"
capabilities:
  - Write unit tests (Jest, pytest, etc.)
  - Write integration tests
  - Write end-to-end tests (Playwright, Cypress)
  - Generate test data and fixtures
  - Analyze code coverage
boundaries:
  do:
    - Test every public function/method
    - Cover happy path and edge cases
    - Use descriptive test names following "should X when Y" pattern
    - Mock external dependencies
  dont:
    - Modify production code (only test files)
    - Skip error case testing
    - Write tests that depend on external services
```

#### Documentation Agent
```yaml
agent: docs-specialist
role: "Generate and update documentation for all changes"
capabilities:
  - Write JSDoc/docstring comments
  - Update README files
  - Generate API documentation
  - Create changelog entries
  - Write migration guides
boundaries:
  do:
    - Document all public APIs
    - Include code examples in docs
    - Keep docs in sync with code changes
    - Use consistent terminology
  dont:
    - Modify source code logic
    - Remove existing documentation without reason
```

#### Security Agent
```yaml
agent: security-specialist
role: "Review code for security vulnerabilities and enforce best practices"
capabilities:
  - Static security analysis (SAST)
  - Dependency vulnerability scanning
  - Authentication/authorization review
  - Input sanitization verification
  - Secrets detection
boundaries:
  do:
    - Flag all security issues with severity levels
    - Suggest specific fixes for each vulnerability
    - Check OWASP Top 10 compliance
    - Verify no hardcoded secrets
  dont:
    - Implement features (only review and suggest)
    - Approve code with critical vulnerabilities
```

**STEP 4 — Task Delegation Patterns**

Implement these delegation patterns:

#### Pattern 1: Sequential Pipeline
```
User Request → Coordinator → Backend → Frontend → Testing → Docs → Security → Coordinator → Result
```
Use when: Tasks have strict dependencies (backend API must exist before frontend can consume it).

#### Pattern 2: Parallel Fan-Out
```
User Request → Coordinator ─┬→ Backend  ─┐
                             ├→ Frontend ─┤
                             ├→ Docs     ─┼→ Coordinator → Result
                             └→ Security ─┘
```
Use when: Tasks are independent (e.g., writing docs while code is being written using specs).

#### Pattern 3: Hybrid
```
User Request → Coordinator ─┬→ Backend  ─┐
                             │            ├→ Testing ─┐
                             └→ Frontend ─┘           ├→ Coordinator → Result
                                         Docs ────────┘
```
Use when: Some tasks depend on others but some can run in parallel.

**STEP 5 — Communication Protocol**

Define how agents communicate:

```
MESSAGE FORMAT:
{
  "from": "<agent-id>",
  "to": "<agent-id>",
  "type": "task_assignment|task_result|error|status_update|clarification_request",
  "task_id": "<unique-id>",
  "payload": {
    "description": "<task description or result>",
    "files_modified": ["<file1>", "<file2>"],
    "status": "completed|failed|blocked",
    "confidence": 0.95,
    "notes": "<any additional context>"
  },
  "timestamp": "<ISO 8601>"
}
```

**STEP 6 — Error Handling**

Implement these error recovery strategies:

| Error Type | Strategy | Example |
|-----------|----------|---------|
| Agent fails task | Retry with more context | Backend agent can't connect to DB → provide connection string |
| Conflicting outputs | Coordinator resolves | Frontend expects field `userName`, backend returns `user_name` → coordinator standardizes |
| Dependency unavailable | Skip and continue | Docs agent can't access API spec → generate placeholder docs |
| Agent timeout | Reassign or simplify | Frontend agent times out on complex component → break into smaller components |
| Quality check fails | Send back with feedback | Testing agent finds bug → send back to original agent with test failure details |

**STEP 7 — Result Consolidation**

The coordinator consolidates all specialist outputs:

1. Collect all completed task results
2. Check for conflicts between specialist outputs (naming, types, interfaces)
3. Resolve conflicts using the project's conventions
4. Merge code changes into a coherent diff
5. Run final quality check (all tests pass, no lint errors, docs updated)
6. Present consolidated result to user with summary:

```
## Multi-Agent Task Summary

### Goal: <original user request>

### Agents Involved: 
- Backend: ✅ 3 tasks completed
- Frontend: ✅ 2 tasks completed  
- Testing: ✅ 5 tests written (all passing)
- Docs: ✅ API docs updated
- Security: ⚠️ 1 low-severity issue found (see below)

### Files Modified:
- src/api/users.py (Backend)
- src/components/UserForm.tsx (Frontend)
- tests/test_users.py (Testing)
- docs/api/users.md (Docs)

### Security Notes:
- LOW: Add rate limiting to POST /api/users endpoint

### Next Steps:
1. Review the security suggestion
2. Deploy to staging
```

### Output Format

Generate the complete multi-agent configuration as a structured document I can use to set up the workflow. Include all agent definitions, communication protocols, and the coordinator logic.

---

*Based on: Codex Desktop App multi-agent architecture (Feb 2026). Compatible with: Claude Code, Codex CLI, Cursor Agent Mode.*
