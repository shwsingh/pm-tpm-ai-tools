# Design Decisions: Agent Harness + Agent Loops (Days 11–12)

## Context

At Day 10, the curriculum has 6 live Claude calls across the app:
`triage_with_claude()`, `analyze_feedback()`, `analyze_dependencies()`, and 3 inline
system prompts. Each is ad-hoc — system prompt hardcoded inline, JSON parsing repeated,
error handling inconsistent. Days 11–12 address this with two foundational patterns.

---

## Decision 1: Add Agent Harnessing to Day 11

### What it is
An **agent harness** is the wrapper that turns a Claude call into a reusable, testable,
observable unit. It owns:
- System prompt loading (from skill spec, not inline string)
- Input schema validation
- Claude API call
- Output parsing + retry on parse failure
- Logging (input, output, latency, token usage)

### Why Day 11 (Evaluation Framework)
You cannot meaningfully evaluate an agent output if the agent is not a stable,
reproducible unit. The harness *is* what you evaluate. Before adding DeepEval scoring,
we need to ensure the same input always goes through the same harness — otherwise
evaluation results are not comparable across runs.

**Sequence:** Build harness → evaluate harness outputs → compare scores across runs.
Without the harness, evaluation is evaluating a moving target.

### What changes
- Create `AgentHarness` class in `app.py` (or a small module if the class gets large)
- Refactor all 6 Claude calls to go through `AgentHarness.run(skill, input)`
- Harness reads system prompt from the corresponding `skills/*.md` file
- Harness handles retry (up to 2 retries on JSON parse failure)
- Harness logs token usage per call (visible in Day 11 eval dashboard)

### Alternatives considered
| Option | Why rejected |
|--------|-------------|
| Keep ad-hoc calls, only add eval | Evaluation of inconsistent call patterns produces noisy results |
| Separate harness module | Overkill for a single-file Streamlit app at this stage |
| Add harness on Day 14 | Too late — Day 12 multi-agent needs it to compose agents cleanly |

---

## Decision 2: Add Agent Loops to Day 12

### What it is
An **agent loop** is the pattern where Claude drives execution rather than receiving
a single prompt and returning a single response. In a loop:
1. Claude receives the task + available tools
2. Claude calls a tool (e.g. `get_dependency_status`, `search_knowledge_base`)
3. The loop feeds the tool result back to Claude
4. Claude decides: call another tool, or return a final answer
5. Loop exits when Claude returns a final answer or max iterations reached

### Why Day 12 (Multi-Agent System)
Multi-agent means agents orchestrating other agents. Without loops, this is just
chained function calls — no real agency. With loops:
- A orchestrator agent can call the Dependency Agent, get results, then call the
  Status Report agent, get results, and synthesize a combined executive briefing
- Agents can self-correct: if the first dependency analysis is incomplete, the
  orchestrator can request clarification and re-run
- The Executive Copilot on Day 14 becomes genuinely agentic, not scripted

### What changes
- Add tool definitions for: `triage_bug`, `analyze_feedback`, `analyze_dependencies`,
  `search_knowledge_base` — these become Claude tools, not just Python functions
- Build an `OrchestratorAgent` that runs a loop, calling sub-agents as tools
- Max iterations: 5 (safety ceiling; TPM tasks are bounded)
- Loop state stored in session state so the user can see each step

### Alternatives considered
| Option | Why rejected |
|--------|-------------|
| Keep single-shot calls in Day 12 | "Multi-agent" becomes misleading — just function chaining |
| Add loops on Day 14 only | Day 14 is the demo; the pattern needs to be built and tested on Day 12 |
| Use LangChain / LlamaIndex agent loop | Adds a dependency and hides the loop mechanics; learning value is in seeing the loop directly |

---

## Curriculum Fit

```
Days 1–4   : Skills (what agents produce)
Days 5–8   : Agents + orchestration (how agents are structured)
Days 9–10  : LLM integration (Claude as classifier/reasoner)
Day 11     : Agent Harness (making Claude calls reproducible + evaluable)   ← NEW
Day 12     : Agent Loops (making Claude an active driver, not a passive responder) ← NEW
Day 13     : MCP (connecting agents to real tools)
Day 14     : Executive Copilot (harness + loops + MCP = full agentic system)
```

The two additions fill the gap between "calling Claude" (Days 9–10) and
"Claude orchestrating a workflow" (Day 14). Without them, Day 14 would require
building both patterns under demo pressure. With them, Day 14 assembles
already-tested pieces.
