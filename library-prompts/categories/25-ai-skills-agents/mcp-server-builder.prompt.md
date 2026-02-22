---
title: "MCP Server Builder — Build Model Context Protocol Servers from Scratch"
version: "1.0"
category: "25-ai-skills-agents"
tags: ["skills", "agents", "ai", "mcp", "model-context-protocol", "server", "tools", "resources", "claude-desktop", "cursor"]
author: "garri333"
description: "Complete prompt for building MCP (Model Context Protocol) servers from scratch. Covers architecture, tool registration, resource endpoints, prompt templates, Python/TypeScript implementation, testing, deployment, and integration with Claude Desktop, Cursor, and VS Code."
language: "en"
---

# MCP Server Builder — Build Model Context Protocol Servers from Scratch

## Prompt

You are an expert MCP (Model Context Protocol) Server Engineer. Your task is to guide me through building a fully functional MCP server from scratch, including tool registration, resource endpoints, prompt templates, testing, and deployment.

### Context & Background

The **Model Context Protocol (MCP)** is an open standard (by Anthropic) that enables AI agents to interact with external data sources and tools through a unified protocol. Think of it as "USB-C for AI" — a single standard that connects any AI model to any data source or tool.

**MCP Architecture:**
```
┌──────────────────────────────────────────────────┐
│                   HOST APPLICATION                │
│              (Claude Desktop, Cursor, VS Code)    │
│                                                   │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────┐ │
│  │  MCP Client  │  │  MCP Client  │  │MCP Client│ │
│  │     (1)      │  │     (2)      │  │   (3)    │ │
│  └──────┬───────┘  └──────┬───────┘  └────┬─────┘ │
└─────────┼──────────────────┼───────────────┼──────┘
          │                  │               │
          ▼                  ▼               ▼
   ┌──────────┐      ┌──────────┐    ┌──────────┐
   │MCP Server│      │MCP Server│    │MCP Server│
   │ (Local)  │      │ (Remote) │    │ (Docker) │
   │          │      │          │    │          │
   │ • Tools  │      │ • Tools  │    │ • Tools  │
   │ • Resrc  │      │ • Resrc  │    │ • Resrc  │
   │ • Prompts│      │ • Prompts│    │ • Prompts│
   └──────────┘      └──────────┘    └──────────┘
```

**Three Core Primitives:**
1. **Tools**: Functions the AI can call (like API endpoints) — model-controlled
2. **Resources**: Data the AI can read (like GET endpoints) — application-controlled
3. **Prompts**: Reusable prompt templates — user-controlled

**Transport Options:**
- **stdio**: Local process communication (most common for local servers)
- **HTTP+SSE**: Remote servers over HTTP with Server-Sent Events
- **Streamable HTTP**: Newer, simplified HTTP transport

### Your Instructions

**STEP 1 — Define the MCP Server**

Ask me:
1. **Server purpose**: What does this server do? (e.g., "interact with my PostgreSQL database", "manage GitHub issues", "search company docs")
2. **Implementation language**: Python or TypeScript?
3. **Transport**: stdio (local) or HTTP+SSE (remote)?
4. **Tools needed**: List 3-5 specific actions the AI should be able to perform
5. **Resources needed**: What data should the AI be able to read?
6. **Target clients**: Claude Desktop / Cursor / VS Code / All

**STEP 2 — Project Setup (Python)**

```bash
# Create project structure
mkdir my-mcp-server
cd my-mcp-server

# Set up Python environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Install MCP SDK
pip install mcp[cli]

# Project structure:
# my-mcp-server/
# ├── src/
# │   └── my_mcp_server/
# │       ├── __init__.py
# │       ├── server.py        # Main server implementation
# │       ├── tools.py         # Tool definitions
# │       ├── resources.py     # Resource definitions
# │       └── prompts.py       # Prompt template definitions
# ├── tests/
# │   ├── test_tools.py
# │   └── test_server.py
# ├── pyproject.toml
# └── README.md
```

**STEP 2b — Project Setup (TypeScript)**

```bash
# Create project structure
mkdir my-mcp-server
cd my-mcp-server
npm init -y

# Install MCP SDK
npm install @modelcontextprotocol/sdk
npm install -D typescript @types/node tsx

# Create tsconfig
npx tsc --init --target es2022 --module nodenext --outDir ./dist

# Project structure:
# my-mcp-server/
# ├── src/
# │   ├── index.ts          # Main server entry point
# │   ├── tools.ts           # Tool definitions
# │   ├── resources.ts       # Resource definitions
# │   └── prompts.ts         # Prompt template definitions
# ├── tests/
# │   └── server.test.ts
# ├── package.json
# ├── tsconfig.json
# └── README.md
```

**STEP 3 — Implement the Server (Python)**

```python
# src/my_mcp_server/server.py

from mcp.server.fastmcp import FastMCP

# Create server instance
mcp = FastMCP(
    name="my-mcp-server",
    version="1.0.0",
    description="Description of what this server does"
)

# ============================================================
# TOOLS — Functions the AI can call
# ============================================================

@mcp.tool()
def search_database(query: str, limit: int = 10) -> str:
    """Search the database for records matching the query.
    
    Args:
        query: The search term to look for in the database.
        limit: Maximum number of results to return (default: 10).
    
    Returns:
        JSON string of matching records.
    """
    # Implement your search logic here
    import json
    results = perform_search(query, limit)  # Your implementation
    return json.dumps(results, indent=2)

@mcp.tool()
def create_record(name: str, data: str, category: str = "general") -> str:
    """Create a new record in the database.
    
    Args:
        name: Name/title of the record.
        data: The record data as a JSON string.
        category: Category for the record (default: "general").
    
    Returns:
        Confirmation with the new record ID.
    """
    record_id = save_to_database(name, data, category)  # Your implementation
    return f"Record created successfully. ID: {record_id}"

@mcp.tool()
def analyze_data(dataset: str, analysis_type: str) -> str:
    """Run analysis on a dataset.
    
    Args:
        dataset: Name of the dataset to analyze.
        analysis_type: Type of analysis: "summary", "trends", "anomalies".
    
    Returns:
        Analysis results as formatted text.
    """
    results = run_analysis(dataset, analysis_type)  # Your implementation
    return results

# ============================================================
# RESOURCES — Data the AI can read
# ============================================================

@mcp.resource("data://schema")
def get_schema() -> str:
    """Return the database schema for reference."""
    return """
    Tables:
    - users (id, name, email, created_at)
    - records (id, name, data, category, user_id, created_at)
    - analytics (id, record_id, metric, value, timestamp)
    """

@mcp.resource("data://records/{category}")
def get_records_by_category(category: str) -> str:
    """Return all records in a specific category."""
    import json
    records = fetch_by_category(category)  # Your implementation
    return json.dumps(records, indent=2)

@mcp.resource("data://stats")
def get_stats() -> str:
    """Return current database statistics."""
    import json
    stats = {
        "total_records": count_records(),
        "categories": list_categories(),
        "last_updated": get_last_update()
    }
    return json.dumps(stats, indent=2)

# ============================================================
# PROMPTS — Reusable prompt templates
# ============================================================

@mcp.prompt()
def analyze_prompt(dataset: str) -> str:
    """Create a prompt for comprehensive data analysis."""
    return f"""Analyze the dataset "{dataset}" and provide:
1. Summary statistics (count, mean, median, std dev)
2. Key trends over time
3. Notable anomalies or outliers
4. Actionable recommendations

Use the search_database and analyze_data tools to gather the data first."""

@mcp.prompt()
def report_prompt(category: str, time_range: str) -> str:
    """Create a prompt for generating a category report."""
    return f"""Generate a detailed report for category "{category}" 
covering the time range: {time_range}.

Steps:
1. Use get_records_by_category to fetch all records
2. Use analyze_data to identify trends
3. Format as a professional report with charts data
4. Include recommendations for improvement"""

# ============================================================
# SERVER ENTRY POINT
# ============================================================

if __name__ == "__main__":
    mcp.run()  # Runs with stdio transport by default
```

**STEP 3b — Implement the Server (TypeScript)**

```typescript
// src/index.ts

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create server instance
const server = new McpServer({
  name: "my-mcp-server",
  version: "1.0.0",
  description: "Description of what this server does"
});

// ============================================================
// TOOLS
// ============================================================

server.tool(
  "search_database",
  "Search the database for records matching the query",
  {
    query: z.string().describe("The search term to look for"),
    limit: z.number().default(10).describe("Max results to return")
  },
  async ({ query, limit }) => {
    const results = await performSearch(query, limit);
    return {
      content: [{ type: "text", text: JSON.stringify(results, null, 2) }]
    };
  }
);

server.tool(
  "create_record",
  "Create a new record in the database",
  {
    name: z.string().describe("Name/title of the record"),
    data: z.string().describe("Record data as JSON string"),
    category: z.string().default("general").describe("Category for the record")
  },
  async ({ name, data, category }) => {
    const recordId = await saveToDatabase(name, data, category);
    return {
      content: [{ type: "text", text: `Record created. ID: ${recordId}` }]
    };
  }
);

// ============================================================
// RESOURCES
// ============================================================

server.resource(
  "schema",
  "data://schema",
  async (uri) => ({
    contents: [{
      uri: uri.href,
      text: `Tables:\n- users (id, name, email)\n- records (id, name, data, category)`,
      mimeType: "text/plain"
    }]
  })
);

// ============================================================
// PROMPTS
// ============================================================

server.prompt(
  "analyze",
  "Create a data analysis prompt",
  { dataset: z.string() },
  ({ dataset }) => ({
    messages: [{
      role: "user",
      content: { type: "text", text: `Analyze dataset "${dataset}"...` }
    }]
  })
);

// ============================================================
// START SERVER
// ============================================================

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCP Server running on stdio");
}

main().catch(console.error);
```

**STEP 4 — Testing**

```python
# tests/test_server.py

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER_PATH = "src/my_mcp_server/server.py"

@pytest.mark.asyncio
async def test_list_tools():
    """Verify all tools are registered."""
    server_params = StdioServerParameters(
        command="python",
        args=[SERVER_PATH]
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            tool_names = [t.name for t in tools.tools]
            assert "search_database" in tool_names
            assert "create_record" in tool_names
            assert "analyze_data" in tool_names

@pytest.mark.asyncio
async def test_search_tool():
    """Test the search tool returns valid results."""
    server_params = StdioServerParameters(
        command="python",
        args=[SERVER_PATH]
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool("search_database", {
                "query": "test",
                "limit": 5
            })
            assert result.content[0].text  # Non-empty result

@pytest.mark.asyncio
async def test_list_resources():
    """Verify all resources are registered."""
    server_params = StdioServerParameters(
        command="python",
        args=[SERVER_PATH]
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            resources = await session.list_resources()
            uris = [r.uri for r in resources.resources]
            assert "data://schema" in [str(u) for u in uris]
```

```bash
# Quick test with MCP Inspector (visual testing tool)
npx @modelcontextprotocol/inspector python src/my_mcp_server/server.py
# Opens a web UI where you can test all tools, resources, and prompts interactively
```

**STEP 5 — Integration with Clients**

#### Claude Desktop (`claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "my-mcp-server": {
      "command": "python",
      "args": ["C:/path/to/my-mcp-server/src/my_mcp_server/server.py"],
      "env": {
        "DATABASE_URL": "postgresql://localhost:5432/mydb"
      }
    }
  }
}
```
Location:
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

#### Cursor (`.cursor/mcp.json`)
```json
{
  "mcpServers": {
    "my-mcp-server": {
      "command": "python",
      "args": ["src/my_mcp_server/server.py"],
      "env": {
        "DATABASE_URL": "postgresql://localhost:5432/mydb"
      }
    }
  }
}
```

#### VS Code (`.vscode/mcp.json`)
```json
{
  "servers": {
    "my-mcp-server": {
      "command": "python",
      "args": ["src/my_mcp_server/server.py"],
      "env": {
        "DATABASE_URL": "postgresql://localhost:5432/mydb"
      }
    }
  }
}
```

**STEP 6 — Deployment Options**

#### Option A: Local (stdio) — Default
No deployment needed. The host application spawns the server process directly.

#### Option B: Docker
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ ./src/
CMD ["python", "src/my_mcp_server/server.py"]
```

#### Option C: Remote (HTTP+SSE)
```python
# server_http.py — HTTP transport version
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="my-mcp-server",
    version="1.0.0",
    host="0.0.0.0",
    port=8080
)

# ... register tools, resources, prompts same as above ...

if __name__ == "__main__":
    mcp.run(transport="sse")  # Run with SSE transport
```

#### Option D: Publish to npm (TypeScript)
```json
{
  "name": "my-mcp-server",
  "version": "1.0.0",
  "bin": {
    "my-mcp-server": "./dist/index.js"
  },
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js"
  }
}
```
```bash
npm publish
# Users can then: npx my-mcp-server
```

**STEP 7 — Publish to MCP Marketplaces**

1. **MCP Market** (https://mcpmarket.com): Submit via their publisher portal
2. **SkillsMP** (https://skillsmp.com): Auto-indexed from npm/GitHub
3. **Skills Directory** (https://skills.directory): Submit for verification

### Output Format

Generate the complete MCP server project with all files, ready to use. Include the configuration snippet for my specific client (Claude Desktop, Cursor, or VS Code).

### Common Patterns

| Pattern | Description | Example |
|---------|-------------|---------|
| **Database bridge** | Connect AI to your database | PostgreSQL, MySQL, SQLite |
| **API wrapper** | Wrap existing REST/GraphQL API | GitHub, Jira, Slack |
| **File system** | Read/write local files with context | Code indexer, log analyzer |
| **Search engine** | Semantic search over documents | Company docs, knowledge base |
| **DevOps bridge** | Interact with infrastructure | Docker, K8s, AWS, CI/CD |

---

*Protocol: Model Context Protocol (MCP) by Anthropic. SDK: mcp[cli] (Python), @modelcontextprotocol/sdk (TypeScript). Compatible with: Claude Desktop, Cursor, VS Code, any MCP-compatible host.*
