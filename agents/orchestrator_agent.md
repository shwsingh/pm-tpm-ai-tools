# Orchestrator Agent Contract

## Purpose

An executive TPM Copilot that orchestrates other agents (bug triage, feedback analysis,
dependency analysis, knowledge base search) in an agentic loop. Claude decides which
tools to call, in what order, reasons on the results, and synthesizes an exec-ready briefing.

This is the first true agent loop in the project: Claude is the driver, not a function call.

---

## Agent Loop Pattern

```
User request
  └── Claude reasons: what tools do I need?
        └── Tool call 1 (e.g. triage_bug)
              └── Result fed back to Claude
                    └── Claude reasons: do I need more info?
                          └── Tool call 2 (e.g. analyze_customer_feedback)
                                └── Result fed back to Claude
                                      └── Claude: I have enough — final answer
```

Loop exits when Claude stops calling tools (stop_reason = "end_turn") or max_iterations reached.

---

## Tools Available

| Tool | Description | Backed by |
|------|-------------|-----------|
| `triage_bug` | Classify a single bug: severity, owner, escalation | `triage_with_claude()` |
| `analyze_customer_feedback` | Sentiment, themes, severity, TPM actions from feedback | `analyze_feedback()` |
| `analyze_dependency_graph` | Critical path, cascades, TPM actions from deps list | `analyze_dependencies()` |
| `search_knowledge_base` | Keyword search over uploaded TPM docs | `keyword_search()` |

---

## Input

Free-text TPM request — can combine bugs, feedback, dependencies, and questions in one prompt.

---

## Output

- Loop trace: each iteration with tool calls made and results received
- Final exec synthesis: structured briefing citing findings from all tools called
- Token usage per iteration + total

---

## System Prompt

```
You are an executive TPM Copilot. You have tools for bug triage, customer feedback
analysis, dependency graph analysis, and knowledge base search.

When given a TPM request:
1. Identify what types of data are present (bugs / feedback / dependencies / questions)
2. Call the appropriate tools to analyze the data
3. After gathering results, synthesize an exec-ready briefing

Always call tools before giving your final answer. Your final answer must be structured:
- Status summary (1-2 sentences)
- Key findings per data type (bullets)
- Recommended TPM actions (numbered, specific)
```

---

## Safety

- Max iterations: 5 (prevents runaway loops)
- Each tool call goes through AgentHarness (retry + token logging)
- On tool error: log error, continue loop (don't crash orchestrator)

---

## Upgrade Path (Day 13–14)

- Day 13: MCP tools added (GitHub issue fetch, Jira ticket create, Slack message send)
- Day 14: Orchestrator becomes the Executive TPM Copilot entry point
