---
title: "14 days, 14 capabilities, one AI TPM Copilot — what I actually built"
date: 2026-06-16
categories:
  - Building in Public
tags:
  - ai
  - agents
  - tpm
  - mcp
  - challenge-complete
excerpt: "The challenge is done. Here's what I shipped, what surprised me, and what I'd do differently if I started again."
header:
  overlay_color: "#0f172a"
  overlay_filter: "0.6"
  overlay_image: /assets/images/hero-week1.svg
  caption: "14 / 14 — Challenge Complete"
  actions:
    - label: "View on GitHub"
      url: "https://github.com/shwsingh/pm-tpm-ai-tools"
    - label: "Interactive Timeline"
      url: "https://shwsingh.github.io/pm-tpm-ai-tools/timeline_gitbranch.html"
    - label: "Component Reference"
      url: "https://shwsingh.github.io/pm-tpm-ai-tools/components.html"
toc: true
toc_sticky: true
toc_label: "On this page"
---

*14 days ago I opened a blank repo. Today I have a working multi-agent AI copilot, a real MCP server connectable to Claude Desktop, and a clearer picture of what "AI engineering" actually means for a TPM. Here's what I built — and what I learned.*

---

## What shipped

### Days 13–14: The protocol layer

The final two days were about connecting the copilot to the outside world.

**Day 13 — MCP Server.** I built a real [Model Context Protocol](https://modelcontextprotocol.io) server using the FastMCP Python SDK. It exposes three things to Claude Desktop:

- **Resources** — live TPM data files (launch checklist, risk register, capacity plan) that Claude can read on demand
- **Tools** — `analyze_launch_risk`, `generate_status_report`, `create_escalation` — actions Claude can call
- **Prompts** — conversation starters that inject your actual TPM data into Claude before you type a word

Before Day 13: you paste your risk register into Claude. After Day 13: you say "check my risks" and Claude fetches the file. The difference is who does the copy-pasting.

**Day 14 — Executive TPM Copilot.** The capstone pulls everything together: live GitHub commit data feeds into Claude, which synthesises a velocity analysis, milestone summary, and exec briefing — GREEN / YELLOW / RED with specific next actions. The MCP config now includes both the TPM Copilot server and the GitHub MCP server, so Claude Desktop has access to your internal data *and* your repo in a single conversation.

---

## The full build map

| Phase | Days | What got built |
|-------|------|---------------|
| Foundation | 0–4 | Repo, dashboard, launch risk analyzer, first skill spec, PRD builder |
| Skills & Agents | 5–8 | Bug triage agent, 3-stage pipeline, status report skill, knowledge base |
| LLM & Orchestration | 9–12 | Feedback agent + first Claude calls, dependency agent, AgentHarness + evals, multi-agent orchestrator |
| Protocol | 13–14 | MCP server (resources/tools/prompts), executive copilot + GitHub live feed |

---

## What actually surprised me

**The output contract was the most important decision I made.** On Day 5, before writing a single line of agent code, I defined exactly what the bug triage agent would return — severity, owner, escalate flag, confidence. That decision paid dividends through Day 12. When I swapped heuristics for Claude on Day 9, nothing downstream changed. When I wired agents as tools in the Day 12 orchestrator, the JSON wrappers were trivial. Design the contract first.

**Claude orchestrating itself is genuinely different from code orchestrating Claude.** Days 1–11 are code calling Claude. Day 12 is Claude calling tools, reasoning on results, and deciding whether to loop. The transition is subtle in the code — one `while` loop and a `tool_use` stop reason check — but the behaviour is qualitatively different. You stop writing "call triage, then call feedback" and start writing "here are the tools, figure it out."

**MCP is simpler than I expected.** FastMCP makes a real MCP server — actual protocol, connectable to Claude Desktop — almost as easy as writing a Flask route. A `@mcp.resource()` decorator, a `@mcp.tool()` decorator, a `@mcp.prompt()` decorator, and `mcp.run()`. The hard part wasn't the code; it was understanding the right role for each primitive: Resources for data, Tools for actions, Prompts for conversation priming.

**Heuristics first was the right call.** The Day 2 launch risk analyzer uses keyword matching. No LLM. I was tempted to add Claude immediately — it would have been two extra lines. I didn't, and I'm glad. Proving the output contract with fast, free, deterministic code meant I knew exactly what "correct" looked like before I asked an LLM to do it.

---

## What I'd do differently

**Add evals on Day 3, not Day 11.** I wrote the skill spec on Day 3 but didn't build the evaluation framework until Day 11. Eight days of Claude outputs with no systematic scoring. In a real project those eight days are where silent regressions live.

**Name the output files by their role, not their day.** `app.py` has grown to 2,000+ lines. The append-per-day pattern was great for learning — each day's section is immediately findable — but production code would split this into modules by capability, not chronology.

**Build the MCP server earlier.** I built it on Day 13 as if it were an advanced topic. It's not. FastMCP is simple enough to introduce on Day 5 alongside the first agent. Starting with MCP from the beginning would have made the resource/tool/prompt distinction clearer from the start.

---

## By the numbers

- **14 days, 14 capabilities** shipped and committed
- **5 agents** built (bug triage, feedback, dependency, orchestrator, MCP tools)
- **2 MCP servers** connected to Claude Desktop (TPM Copilot + GitHub)
- **1 eval framework** running Claude-as-judge against skill spec rules
- **0 external databases** — session state, markdown files, and chunked text all the way

---

## What's next

The copilot works. The next questions are about making it real:

1. **Live data** — swap the markdown risk register for a Jira query. The MCP tool interface stays identical; only the data source changes.
2. **Persistent memory** — right now every session starts fresh. A simple SQLite store for past triage decisions would make the agents learn from history.
3. **Evaluation in CI** — run Claude-as-judge on every commit, not just on demand.

---

*The repo, all design decisions, and per-day lessons are at [github.com/shwsingh/pm-tpm-ai-tools](https://github.com/shwsingh/pm-tpm-ai-tools). The interactive timeline is [here](https://shwsingh.github.io/pm-tpm-ai-tools/timeline_gitbranch.html).*

*Built by Shweta Singh — Senior Manager, TPM at Google.*
