# Day 13 Design Decisions — MCP Server Integration

## What we built
A real MCP server (`mcp_servers/tpm_copilot_mcp/server.py`) using the `mcp` Python SDK (FastMCP).
Exposes 3 resources, 3 tools, and 2 prompts to Claude Desktop (or any MCP client).

## Decision 1: Real MCP server (Option A) vs. mock integrations (Option B)

**Chose:** Real MCP server with FastMCP SDK.

**Alternatives considered:**
- Option B: Stub Jira/Slack tool-call wrappers in app.py (simulated, no actual MCP protocol)
- Option C: Use an existing open-source MCP server for Jira/GitHub

**Rationale:** A real working MCP server connectable to Claude Desktop is a stronger demo and a genuine learning artifact. Mock integrations would hide the actual protocol. The FastMCP abstraction makes the real thing only marginally harder than the mock.

## Decision 2: FastMCP over low-level MCP SDK

**Chose:** `FastMCP` (high-level wrapper).

**Why:** `FastMCP` lets you define resources, tools, and prompts with plain Python decorators — no manual schema wiring. At this project's scale (3+3+2) it's the right abstraction. Low-level SDK would add boilerplate without value.

## Decision 3: Heuristic tools, not LLM tools

**Chose:** `analyze_launch_risk` and `generate_status_report` use heuristic/template logic inside the MCP server, not Claude API calls.

**Why:** MCP tools are called *by* Claude (via Claude Desktop). Adding Claude API calls inside MCP tools would create Claude-calls-Claude recursion with no added value. The tools provide structured data; Claude Desktop does the reasoning on top.

## Decision 4: Data files as Resources, not hardcoded strings

**Chose:** `tpm://launch-checklist`, `tpm://risk-register`, `tpm://capacity-plan` read from `.md` files.

**Why:** Resources in MCP are meant to be live, updateable data. Pointing to files means the resource content updates automatically when files change — no server restart needed. Mirrors how real TPM data lives in wikis/docs.

## Decision 5: 2 Prompts that inject resource content at call time

**Chose:** `launch_readiness_review` and `weekly_exec_update` prompts read the data files and inject their content into the prompt text at call time.

**Why:** Prompts in MCP prime the Claude conversation with context. Injecting the actual checklist/risk register means Claude Desktop gets the live document, not a pointer to it. The user gets a grounded, data-aware conversation immediately.
