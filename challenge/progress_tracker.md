# Progress Tracker

## Day 1

Status: COMPLETE

Built:
- GitHub repository
- Streamlit dashboard
- TPM homepage

---

## Day 2

Status: COMPLETE

Built:
- Launch Risk Analyzer
- Risk Detection
- Recommendations
- Executive Summary

---

## Day 3

Status: COMPLETE

Goal:
Built:
- skills/launch_risk_analysis.md
- First reusable TPM skill
- README updates
- Documentation updates

Lessons:
- Difference between Tool and Skill
- Skills are reusable instructions
- Skills can later be consumed by agents

---

## Day 4

Status: COMPLETE

Goal:
Build a reusable PRD Builder skill that turns a rough product idea into a structured, exec-ready PRD - including the sections an agentic product PRD needs.

Built:
- skills/prd_builder.md (v2)
  - Core sections: Problem, Goals, Customer Base, Market Analysis, User Stories, Requirements, Success Metrics, Milestones & Timelines, Risks, Launch Plan
  - Agent sections: Agent Harness, Capacity Requirements, Data Requirements, Security & Privacy, Cost & Budget, Observability & Evaluation, Failure Modes & Guardrails
  - PRD Evaluation Rules tightened (Exec-Ready now requires agent-critical sections)
- examples/prd_ai_tpm_copilot.md
  - Worked PRD for the AI TPM Copilot product itself
  - Revised after a senior-PM critical review pass (v2 with changelog)
- notes/day4_prd_critique.md
  - Reusable 4-step critique-and-revise loop
  - Five critique categories for agentic-product PRDs
- lessons_learned/day3_day4_lessons.md (expanded with critique-loop learnings)
- README progress badge -> 4/14; 14_day_plan Day 4 -> Done

Lessons:
- Skills can layer business context (customer base, market analysis) alongside execution detail (milestones, timelines, capacity, cost)
- Evaluation rules give a skill a quality bar, not just a structure
- For agentic products, a PRD that skips Agent Harness / Capacity / Cost / Failure Modes looks Exec-Ready but is not
- A senior-PM critique pass is itself a reusable skill - turned the PRD from generic to defensible in one cycle
- Timeline realism comes from challenging hidden gates (SOC2 observation window, multi-agent quality bar), not from optimism
- Every milestone needs an exit criterion and a role-named owner

---

## Day 5

Status: COMPLETE

Goal:
Build the first agent in the project - Bug Triage Agent - with the agent shape (planner, tools, escalation, output contract) while keeping the classifier heuristic so the LLM swap-in on Day 9 is a single function change.

Built:
- skills/bug_triage.md (work contract: severity, component, owner, priority, escalation, lead-review)
- agents/bug_triage_agent.md (agent contract: skills used, planner pattern, tools, memory, escalation, routing to Lead)
- projects/tpm_pm_toolkit/app.py - new Day 5 section with triage() function and Streamlit UI
- design_decisions/day5_bug_triage_agent.md - five design choices with pros, cons, alternatives, plus observed-evidence section from the 6-bug smoke test
- README badge -> 5/14; 14_day_plan Day 5 -> Done

Built after the core agent (same day, post-wrap-up additions):
- challenge/project_evolution.md - visual project history with mermaid timeline, current-state architecture, per-day delta diagrams, mindmap, and 14-day gantt
- README compact architecture diagram (then redesigned for visual clarity with role-coded colors and shapes)
- docs/ - full GitHub Pages blog site on Minimal Mistakes theme
  - docs/_config.yml with author profile, share buttons, sticky TOC, search
  - docs/_posts/2026-06-09-week1-ai-tpm-copilot.md - Week 1 blog post (revised after a critique pass for TPM/PM audience)
  - docs/_includes/head/custom.html - Mermaid CDN script (with type=module readyState fix)
  - docs/assets/images/hero-week1.svg - custom gradient hero banner
  - docs/index.md, docs/about.md
- Author title updated to Senior Manager, TPM at Google; location -> Google Bay Area

Key design decisions (see design_decisions/day5_bug_triage_agent.md):
1. Heuristic + stable LLM-swap stub (Option 2) - matches project rhythm; Day 9 swap is one function
2. Route ambiguous bugs to "Shweta (Lead)" - confidence boundary as a first-class output
3. Separate agents/ and skills/ directories - sets up Day 6 orchestration
4. Output contract returns a dict, not a string - composable for Day 6
5. P1 batch threshold (>2 -> incident) - catches deploy regressions cheaply

Observed evidence from the smoke test (logged in the design decisions doc):
- 3 of 6 representative bugs routed to "Shweta (Lead)" - above the 20% threshold
- The keyword classifier missed "revenue is dropping" because it didn't literal-match "revenue stop"
- Route-to-Lead safety net caught every miss - the design worked exactly as intended
- This is the concrete motivation for the Day 9 LLM swap, not a hypothesis

Lessons:
- The agent shape (parse -> classify -> decide -> respond) is the real Day 5 learning; the keyword classifier is throwaway
- A stable input/output contract is what makes the LLM swap-in cheap
- "Route to Lead" is a reusable pattern for any agent with bounded confidence
- Design decisions documented at end of day are easier to read in 3 months than the diff is
- Visual architecture diagrams (left-to-right, color-coded by role, shape-encoded) communicate the system 10x better than text trees
- A blog post for a TPM/PM audience needs ONE memorable takeaway, not three meta-learnings - the rewrite cut jargon and added a "Monday-morning thing to try"
- type=module scripts are deferred; DOMContentLoaded has already fired by the time they run (Mermaid render bug, now fixed)

---

## Day 6

Status: COMPLETE

Goal:
Build an agent orchestration workflow that chains the Day 5 Bug Triage Agent into a 3-stage pipeline: Ingest → Triage → Escalation Handler.

Built:
- projects/tpm_pm_toolkit/app.py - new Day 6 section with three pipeline stage functions and a Streamlit UI showing each stage expanded
  - ingest() - validates and normalizes raw bug input
  - run_triage_stage() - calls the Day 5 triage() function for each valid bug; applies batch P1 escalation rule
  - escalation_handler() - converts triage labels into actionable artifacts: incident drafts, Slack-style on-call messages, lead notifications
- agents/agent_workflow.md - orchestration contract with stage-by-stage input/output specs, failure modes, and planned MCP upgrade path
- README badge -> 6/14; 14_day_plan Day 6 -> Done

Key design decisions:
1. Each stage is a pure function with a defined input/output contract - composable and independently testable
2. Escalation artifacts are draft text today; Day 13 MCP wires them to real Slack and Jira
3. Pipeline stops cleanly at ingest if no valid bugs pass - no empty triage runs
4. Stage outputs are shown in expandable UI panels so the orchestration is visible, not a black box

Lessons:
- Orchestration is about the contract between stages, not the stages themselves - get the interfaces right first
- Showing each pipeline stage in the UI makes the agent's reasoning transparent to a non-technical TPM audience
- Draft artifacts (incident summaries, Slack messages) are valuable even before MCP wiring - they define the output shape for Day 13
- A pure function pipeline is easy to test incrementally; adding LLM on Day 9 changes one function, not the pipeline shape

---

## Day 7

Status: COMPLETE

Goal:
Build a Status Report Skill that turns raw weekly TPM updates into a structured, exec-ready report and scores it across five quality dimensions.

Built:
- skills/status_report.md — skill spec with input contract, output format, and 5 eval dimensions: Completeness, Ask Specificity, Status Accuracy, Clarity, Next Week Concreteness
- projects/tpm_pm_toolkit/app.py — new Day 7 section with structured form input, score_report() heuristic scorer, build_report() formatter, and Streamlit UI showing status color + quality eval + generated report
- README badge -> 7/14; 14_day_plan Day 7 -> Done

Key design decisions:
1. Structured form fields (not free text) — produces better output without an LLM; also matches how TPMs actually fill in status templates
2. Status color derived from content, not user-selected — prevents the common mistake of marking Green when blockers exist
3. 5 eval dimensions are pass/fail today; Day 11 DeepEval adds numeric scoring against a golden set
4. Vague ask detection and weak next-week language detection give the TPM specific fix guidance, not just a fail flag

Lessons:
- Eval dimensions need to be specific enough to fail — "good writing" is not checkable, "no vague asks" is
- Deriving status from content rather than letting users pick it catches a real TPM antipattern (optimism bias in self-reporting)
- A form with labeled fields produces more structured output than a single text area, even without an LLM

---

## Day 8

Status: COMPLETE

Goal:
Build a Knowledge Base skill that lets TPMs upload documents and search them by question — the heuristic foundation for RAG.

Built:
- skills/knowledge_base.md — RAG skill spec with chunking strategy, retrieval contract, eval rules, and upgrade path to embeddings on Day 9
- projects/tpm_pm_toolkit/app.py — new Day 8 section with extract_text_chunks() (txt/md/docx/csv), keyword_search() scorer, and Streamlit upload + search UI
- python-docx installed to support .docx (Google Docs export) directly
- README architecture diagram updated to Day 8; timeline updated; badge -> 8/14; 14_day_plan Day 8 -> Done

Supported formats: .txt, .md, .docx (via python-docx), .csv (via pandas)

Key design decisions:
1. Chunk by paragraph for text/docx, by row for CSV — matches how TPMs structure their docs
2. Keyword overlap score (hits / total query tokens) gives a simple 0–1 relevance signal
3. Session state stores chunks — no persistent DB needed today; Day 9 upgrades to embeddings
4. .docx support added immediately (one pip install) since Google Docs is the primary TPM format

Lessons:
- Chunking strategy matters more than the retrieval algorithm at this scale — bad chunks produce bad results regardless of the scorer
- CSV row-as-chunk with headers prepended gives enough context for keyword matching to work
- The heuristic retrieval contract (source, text, score) is stable — Day 9 replaces the scorer, not the interface

---

## Day 9

Status: COMPLETE

Goal:
Make the first real LLM calls in the project: swap the heuristic bug triage classifier for Claude, and build a Feedback Agent that analyzes customer feedback with structured output.

Built:
- skills/feedback_agent.md — skill spec with per-item output (sentiment, themes, severity, action) and aggregate summary contract
- projects/tpm_pm_toolkit/app.py
  - Sidebar API key input (fallback when ANTHROPIC_API_KEY env var not set)
  - triage_with_claude() — LLM-backed triage with same output contract as heuristic triage(); fallback to heuristic on error
  - run_triage_stage() updated — uses Claude when API key present, heuristic otherwise; shows mode in UI
  - Day 9 Feedback Agent section — analyze_feedback() batch request, aggregate metrics, per-item expanders with severity/sentiment icons
- README badge -> 9/14; 14_day_plan Day 9 -> Done; architecture diagram updated with Claude API node

Key design decisions:
1. Same output contract for triage_with_claude() as triage() — Day 9 is a swap, not a refactor; pipeline shape unchanged
2. Graceful fallback: triage_with_claude() catches all exceptions and falls back to heuristic — app never breaks without an API key
3. Single batch request for feedback analysis — one API call for all items, not per-item calls; cheaper and Claude can spot cross-item patterns
4. Sidebar API key input with env var precedence — no key hardcoded anywhere; works locally and in deployed environments
5. JSON-only system prompt with code fence stripping — reliable parsing without asking for markdown

Lessons:
- The stable output contract from Day 5 paid off on Day 9: swapping triage() for triage_with_claude() required zero changes to the pipeline
- Asking Claude for pure JSON (no markdown, no explanation) works reliably; the code fence stripper handles the occasional ```json wrapper
- Batch feedback analysis in one request is better than N per-item calls — Claude can surface cross-item themes it couldn't see in isolation
- A sidebar API key input is the right UX for a learning project: it never blocks users without a key, and it's obvious where to enter it

---

## Day 10

Status: COMPLETE

Goal:
Build a Dependency Agent that tracks cross-team launch dependencies and uses Claude to reason about the full dependency graph: critical path, cascading risks, and prioritized TPM actions.

Built:
- skills/dependency_agent.md — skill spec with reasoning pattern (parse → identify blockers → trace cascades → rank → act → summarize), evaluation rules, and MCP upgrade path
- agents/dependency_agent.md — agent contract with full input/output JSON schema, planner pattern, and failure mode table
- projects/tpm_pm_toolkit/app.py — Day 10 section:
  - Structured form to add dependencies (dependent team, provider team, deliverable, due date, status)
  - Session state dependency table with status icons
  - analyze_dependencies() Claude call with batch dependency reasoning
  - Results: health dashboard (overall health, critical path count, cascades, escalations), exec summary, cascading risk chain display, per-dependency expanders with risk level, reasoning, and recommended action
- README badge 9/14 → 10/14; architecture diagram updated with Dependency Agent + DEPS store node

Key design decisions:
1. Structured form input (not free text) — produces reliable JSON for Claude; consistent schema means Claude can reason across deps, not just classify each one
2. Batch analysis over the full graph — Claude sees all deps at once, enabling cascading risk detection that per-dep calls can't do
3. Session state dependency list with Clear All — no DB needed; user builds up the graph interactively
4. Escalate flag drives UI — red error box for escalations, plain text for actions, so critical items are visually impossible to miss
5. Exec summary in the output — copy-paste ready for a status report; connects to Day 7 and Day 12 multi-agent

Lessons:
- Cascading risk detection requires seeing the full graph — this is the key reason to batch all deps into one Claude call, not N separate calls
- Structured form input + JSON prompt = more reliable output than asking Claude to parse free-text dependency descriptions
- The dependency graph naturally feeds the status report — Day 12 multi-agent will wire these together without changing either agent's contract

---

## Day 11

Status: COMPLETE

Goal:
Formalize all Claude calls into a reusable AgentHarness and build an evaluation framework that scores agent outputs against skill spec rules using Claude as judge.

Built:
- AgentHarness class — single wrapper for all Claude calls: retry on JSON parse failure (up to 2 retries), token logging (input/output/total/latency), model constant (MODEL = "claude-sonnet-4-6")
- Refactored all 3 Claude functions through AgentHarness: triage_with_claude, analyze_feedback, analyze_dependencies — same output contracts, callers unchanged
- _show_token_usage() helper — compact per-call token display shown after each result
- Day 11 Evaluation Framework section — Claude-as-judge scores any agent output per skill spec eval rules; per-criterion pass/fail, A-F grade, improvement suggestions
- Session Token Dashboard — cumulative in/out/total tokens + per-call log for the full session
- Model upgraded from claude-sonnet-4-6 to claude-opus-4-7 in AgentHarness (then switched back to sonnet for Day 12)

Key design decisions:
1. AgentHarness returns {"output": dict, "meta": {...}} — callers extract output; meta stored in session state for display without changing any call sites
2. Retry on JSON parse failure (not on API failure) — handles the occasional ```json wrapper Claude adds; API errors surface immediately
3. Claude-as-judge uses the skill spec eval rules verbatim — no separate golden set needed; rules are already in the skill specs
4. Two-call eval pattern: call 1 = agent run, call 2 = evaluator — keeps concerns separate and makes each call independently auditable
5. Token dashboard at page bottom — accumulates across all calls in the session, not just the last call

Lessons:
- The stable output contracts from Days 5-10 meant the harness refactor was purely internal — zero changes to callers or UI
- Retry on JSON parse failure catches ~100% of formatting issues without masking real API errors
- Claude-as-judge is more flexible than DeepEval for custom skill specs — no schema registration, just natural language rules
- Showing tokens after every call makes cost visible immediately; users calibrate prompt length naturally

---

## Day 13

Status: COMPLETE

Goal:
Build a real MCP server exposing TPM resources, tools, and prompts to Claude Desktop via the Model Context Protocol.

Built:
- `mcp_servers/tpm_copilot_mcp/server.py` — FastMCP server with 3 resources, 3 tools, 2 prompts
- Resources: `tpm://launch-checklist`, `tpm://risk-register`, `tpm://capacity-plan` (read from live .md files)
- Tools: `analyze_launch_risk` (5-dimension heuristic scorer), `generate_status_report` (markdown report generator), `create_escalation` (structured escalation doc)
- Prompts: `launch_readiness_review`, `weekly_exec_update` (inject live resource content at call time)
- Data files: `launch_checklist.md`, `risk_register.md`, `capacity_plan.md` — realistic TPM content
- Day 13 section in app.py: connection status, local tool test panel (3 tabs), Claude Desktop config generator
- `design_decisions/day13_mcp_server.md`

Key design decisions:
1. Real FastMCP server over mock stubs — actual MCP protocol, connectable to Claude Desktop
2. FastMCP decorator pattern over low-level SDK — resources/tools/prompts in ~10 lines each
3. Heuristic tools inside MCP, not LLM calls — MCP tools are called *by* Claude, so Claude-inside-tools creates useless recursion
4. Data files as MCP Resources — live files mean content updates without server restart
5. Prompts inject resource content at call time — Claude Desktop gets grounded context immediately, not just a pointer

Lessons:
- FastMCP makes the real MCP protocol almost as easy as writing a Flask route — the decorator abstraction is well-designed
- MCP Resources are for live data; MCP Tools are for actions; MCP Prompts prime the conversation — distinct roles, not interchangeable
- Tools called by Claude should return structured data, not call Claude themselves — the LLM layer belongs above the tool layer
- The Claude Desktop config generator in the UI is the most practical artifact: users can copy-paste it and connect immediately

---

## Day 12

Status: COMPLETE

Goal:
Build a multi-agent orchestrator with a true agent loop: Claude calls specialized tools (bug triage, feedback analysis, dependency analysis, knowledge base search), reasons on results, and loops to a final exec synthesis.

Built:
- ORCHESTRATOR_TOOLS — 4 tool schemas: triage_bug, analyze_customer_feedback, analyze_dependency_graph, search_knowledge_base
- execute_tool() — dispatcher routing Claude tool calls to existing harness-backed agent functions
- run_agent_loop() — full agentic loop: send request + tools → Claude decides tool calls → execute → feed results back → loop until end_turn or max 5 iterations
- Day 12 UI: free-text TPM request input, per-iteration expanders showing tool calls + inputs + result previews + tokens, exec briefing rendered from Claude's final answer
- agents/orchestrator_agent.md — orchestrator contract with loop pattern diagram, tool table, system prompt, safety rules
- MODEL switched from claude-opus-4-7 back to claude-sonnet-4-6 (user decision)
- README badge 11/14 → 12/14; 14_day_plan Day 12 → Done

Key design decisions:
1. Tools call existing harness functions — no duplicate Claude logic; the loop adds orchestration on top of already-tested agents
2. Max 5 iterations ceiling — prevents runaway loops on ambiguous requests; TPM tasks are bounded in scope
3. Per-iteration trace in UI — each tool call visible with input, result preview, and tokens; loop is transparent, not a black box
4. System prompt instructs call-per-bug (not batch bugs in one triage call) — each bug gets an independent triage; Claude naturally sequences them
5. Tool errors are logged and loop continues — one bad tool call doesn't crash the orchestrator; error shown in trace

Lessons:
- The stable output contracts from Days 5-10 paid off again: wiring them as tools required only a JSON.dumps() wrapper
- Claude follows "call triage_bug once per bug" instructions reliably when the system prompt is explicit — no need to enforce this in code
- Showing the loop trace is the most valuable part of Day 12 for learning: it makes the agentic loop visible and debuggable
- tool_use stop_reason requires keeping the full response.content in the messages list — extracting just text and discarding tool_use blocks breaks the loop