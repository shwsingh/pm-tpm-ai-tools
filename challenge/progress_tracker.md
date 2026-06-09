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
- design_decisions/day5_bug_triage_agent.md - five design choices with pros, cons, alternatives
- README badge -> 5/14; 14_day_plan Day 5 -> Done

Key design decisions (see design_decisions/day5_bug_triage_agent.md):
1. Heuristic + stable LLM-swap stub (Option 2) - matches project rhythm; Day 9 swap is one function
2. Route ambiguous bugs to "Shweta (Lead)" - confidence boundary as a first-class output
3. Separate agents/ and skills/ directories - sets up Day 6 orchestration
4. Output contract returns a dict, not a string - composable for Day 6
5. P1 batch threshold (>2 -> incident) - catches deploy regressions cheaply

Lessons:
- The agent shape (parse -> classify -> decide -> respond) is the real Day 5 learning; the keyword classifier is throwaway
- A stable input/output contract is what makes the LLM swap-in cheap
- "Route to Lead" is a reusable pattern for any agent with bounded confidence
- Design decisions documented at end of day are easier to read in 3 months than the diff is