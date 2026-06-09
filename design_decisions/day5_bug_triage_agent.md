# Day 5 — Bug Triage Agent: Design Decisions

**Date:** 2026-06-09
**Day:** 5 of 14
**Capability:** Bug Triage Agent (first agent in the project)
**Lead:** Shweta Singh

This document records the design choices made on Day 5 along with the reasoning and tradeoffs, so that the choices can be revisited during the portfolio review.

---

## Decision 1 — Build the agent heuristically with a stable LLM-swap stub (Option 2)

### Choice

Implement the `triage()` function with rule-based heuristics today, but freeze its input/output contract so that the Day 9 swap-in to a Claude-Sonnet-backed implementation is a single function replacement.

### Reasoning

The 14-day plan introduces LLM integration mid-challenge (Day 7 status report, Day 8 RAG, Day 9 feedback agent). Introducing the Anthropic SDK on Day 5 would have pulled forward work that is already scheduled and would have skipped the *agent shape* learning — planner, executor, escalation, output contract — that Day 5 is meant to teach.

Choosing the stable-contract heuristic forces the contract decision to happen before the LLM call, which is the right order. By Day 9 the only question will be *"can the LLM hit this contract"* — not *"what should the contract be."*

### Alternatives considered

- **Option 1 — Pure markdown spec, no Streamlit code.** Rejected. Skills are already markdown specs (Day 3, Day 4). Day 5 needs to demonstrate *execution*, not just specification.
- **Option 3 — Real LLM agent from day one.** Rejected. Introduces SDK setup, API key management, prompt engineering, JSON-mode handling, and cost concerns all on the same day. Violates the project's incremental rhythm and CLAUDE.md's explicit guardrail about not introducing LLM SDKs ahead of schedule.

### Pros

- Matches the project's incremental rhythm (Days 1–4 were all heuristic / spec-only).
- Stable contract means Day 9 swap-in is a 5-line change.
- The agent shape (parse → classify → decide → respond) is the real learning of Day 5, and it does not require an LLM.
- Demo runs deterministically — useful for the portfolio walkthrough.
- Zero API cost, zero rate-limit risk.

### Cons

- Not "truly agentic" yet — the classifier is rule-based, not reasoning-based.
- Heuristic keyword lists will miss bugs that use synonyms.
- The agent cannot handle multi-bug reasoning (e.g., "are these two bugs the same root cause?") until LLM swap-in.
- Demo viewers may underestimate the system if they see only the Day 5 version.

### When to revisit

Day 9, when the Feedback Agent is built LLM-first. At that point, swap `triage()` to a Claude call that returns the same dict shape.

### Observed evidence (2026-06-09 smoke test)

Ran six representative bugs through `triage()` and the brittleness predicted in the Cons section showed up immediately. Findings:

| Bug | Heuristic verdict | What went wrong |
|---|---|---|
| `"500 errors... revenue is dropping"` | P1 → Lead | "revenue is dropping" did not match the literal `"revenue stop"` keyword; the case landed on a single P1 hit ("500 error") and triggered the thin-evidence rule. |
| `"Minor UI glitch... Safari"` | P2 (not P3) | "minor" lives in `P2_KEYWORDS` and is checked before `P3_KEYWORDS`, so cosmetic bugs that include "minor" land as P2. |
| `"PII may be leaking..."` | Unknown → Lead | "pii leak" did not literal-match "PII may be leaking"; severity classifier fell through to Unknown. |

The good news is that every miss routed to Lead instead of mis-classifying. The route-to-Lead rule is doing exactly the safety-net job it was designed for.

The bad news is the brittleness is worse than expected — three of six test cases route to Lead, which is well above the 20% Lead-routing threshold flagged in Decision 2. If this rate held in production, it would mean the heuristic is below the bar for daily use.

This is now the concrete motivation for the Day 9 LLM swap rather than just a hypothesis.

---

## Decision 2 — Route ambiguous bugs to "Shweta (Lead)" instead of guessing

### Choice

When the heuristic cannot triage confidently — ambiguous wording, conflicting signals, unknown component, thin P0/P1 evidence — the agent sets the owner to "Shweta (Lead) — needs discussion", overrides the next action to "Reach out to Shweta as the lead for triage discussion", and tags the summary `[NEEDS LEAD]`.

### Reasoning

A confident wrong triage is worse than a hedged correct one. A false P0 escalation pages on-call at 2am for a typo; a false P3 buries a real outage in the backlog. The Lead-routing rule is the agent's explicit acknowledgment of its own confidence bound.

It also creates a useful operational signal: if more than 20% of bugs route to Lead in a week, the heuristic rules need tightening. The route-to-Lead rate is a real metric.

### Alternatives considered

- **Always pick best-guess severity.** Rejected. False escalations have higher cost than human review delay.
- **Drop ambiguous bugs.** Rejected. Silent drops are worse than visible escalations.
- **Route to a generic queue.** Rejected. "Reach out to Shweta as the lead" gives a named person, which gets acted on. A queue does not.

### Pros

- Honest confidence boundary.
- Generates a useful signal (route-to-Lead rate) for tuning the rules.
- Names a real owner, so the routed bug does not sit in limbo.
- Will translate cleanly to the LLM version — the LLM can be prompted to return a `needs_lead` flag when its confidence is low.

### Cons

- Adds a hop in the workflow — every Lead-routed bug needs human time.
- "Shweta as Lead" is hard-coded in v1. Multi-tenant version needs configurable lead routing.
- Without a confidence score, the Lead-routing rule is itself a heuristic (counting keyword hits is a proxy for confidence).

### When to revisit

Day 9 LLM swap-in — replace the keyword-hit-count proxy with an actual confidence score from the model. Multi-tenant version (post-GA) needs configurable Lead routing per team.

---

## Decision 3 — Two artifacts (skill + agent), separate directories

### Choice

Create `skills/bug_triage.md` (the work contract) **and** `agents/bug_triage_agent.md` (the agent contract). Two new files, two directories.

### Reasoning

A skill answers *what good triage looks like.* An agent answers *when to do triage, which tools to use, and what to do with the result.* Conflating them would have been faster today but would have made Day 6 (Agent Workflow) harder, because orchestration needs the agent as a separable unit.

This is also the right shape for Day 12 (Multi-Agent System) — agents are composable, skills are agent inputs.

### Alternatives considered

- **Single markdown file mixing skill and agent.** Rejected. Conflates the work contract with the runtime contract.
- **Put the agent spec inside `skills/` for simplicity.** Rejected. Naming gets confused; future readers will not be able to tell what is a skill and what is an agent.

### Pros

- Clean separation of concerns: skills are stateless contracts, agents are runtime behavior.
- Sets up Day 6 orchestration cleanly.
- Matches industry convention (skills, tools, and agents are distinct concepts in MCP and Anthropic Agent SDK terminology).
- The portfolio reader sees the architecture, not just the demo.

### Cons

- Two files to keep in sync if the contract changes.
- Project structure grows — more directories to navigate.
- Risk of over-engineering for a 14-day challenge.

### When to revisit

If by Day 10 the agents/ directory has fewer than three files, the convention may be over-architected and we should reconsider folding agent specs into a different structure.

---

## Decision 4 — Output contract returns a dict, not a string

### Choice

`triage()` returns a Python `dict` with stable keys (`severity`, `component`, `owner`, `priority`, `next_action`, `escalate`, `escalate_reason`, `needs_lead`, `needs_lead_reason`, `summary`).

### Reasoning

A dict is what an orchestrator needs to compose multiple agents. A string is what a user reads. Today the UI renders the dict; tomorrow another agent will consume it. The dict shape is the contract.

### Alternatives considered

- **Return a formatted string.** Rejected. The Day 6 workflow agent needs structured fields, not text to re-parse.
- **Return a Pydantic model.** Rejected for v1 — adds a dependency for a project that explicitly does not yet have a requirements.txt. Revisit when LLM swap-in lands.

### Pros

- Direct consumption by future agents.
- Easy to test (assert on dict keys).
- Easy to log and to evaluate (DeepEval, Day 11).
- LLM swap-in will return the same shape via JSON mode.

### Cons

- No schema validation today — a typo in a key name fails silently.
- Less self-documenting than a typed model.

### When to revisit

Day 9 LLM swap-in — add Pydantic at the same time the SDK is introduced. Schema validation matters more when the producer is a probabilistic model.

---

## Decision 5 — Use a "P1 batch threshold" rule for incident detection

### Choice

If more than two bugs in a single triage batch are classified P1, all P1 bugs in that batch are auto-escalated to incident with the reason "possible broader regression."

### Reasoning

A single P1 is rarely an incident. Three P1s arriving together usually means a deploy broke something. This is a cheap heuristic that catches the most common multi-bug incident pattern.

### Alternatives considered

- **No batch logic.** Rejected. Misses the most common regression pattern.
- **More sophisticated clustering.** Deferred to the LLM version, which can actually reason about whether bugs share a root cause.

### Pros

- Catches deploy-regression incidents cheaply.
- Trivially explainable to a reviewer.

### Cons

- Three unrelated P1 bugs would falsely escalate.
- The threshold (>2) is arbitrary.

### When to revisit

Day 9 LLM swap-in — let the model cluster bugs by likely root cause instead of counting.

---

## Things explicitly deferred to later days

- LLM-backed classification (Day 9).
- Jira / GitHub MCP integration for real ticket reads and writes (Day 13).
- RAG over past bugs and runbooks (Day 8).
- DeepEval golden set scoring (Day 11).
- Multi-agent root-cause clustering across agents (Day 12).
- Configurable Lead routing per team (post-GA).

---

## Summary for portfolio revision

The Day 5 build is intentionally shallow on intelligence and deep on architecture. The shape — agent contract, skill contract, stable dict output, Lead-routing for ambiguous cases — is the artifact that survives into the LLM-backed version. The keyword lists are throwaway.

The Lead-routing rule is the most reusable design decision: it generalizes to any agent whose confidence is bounded, and it produces an operational signal (route-to-Lead rate) that is independently useful.
