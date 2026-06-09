# Day 4 Note — PRD Critique-and-Revise Loop

A working note from Day 4. Captures the flow that turned a generic-looking PRD into an Exec-Ready one in a single review cycle, so I can re-use it on future PRDs.

---

## Why this matters

A PRD written from a template hits the structural bar but rarely the quality bar. Templates ensure all sections exist; they do not ensure the sections are honest, evidence-based, or schedulable. The critique-and-revise loop is what closes that gap.

For an agentic product specifically, the gap is larger. Standard PRDs do not cover Agent Harness, Capacity Requirements, Cost and Sensitivity, Failure Modes, or Multi-Agent Fallback. Without those, the PRD looks Exec-Ready but is not.

---

## The loop (use this as a checklist)

### Step 1 — Draft from the skill

Use `skills/prd_builder.md` to generate the first draft. Fill every section. Mark PRD Status optimistically.

### Step 2 — Run a senior-PM critical review pass

Re-read the draft as if you were the senior PM reviewer in the approval meeting. Tag each issue with severity:

- **Blocker** — must fix before Exec-Ready.
- **Major** — must fix before Beta.
- **Minor** — can defer.

### Step 3 — Force a fix for every Blocker

Do not lower the status from Exec-Ready to Review-Ready and call it done. Fix the Blockers. The point of the loop is to produce an Exec-Ready PRD, not to relabel a Draft.

### Step 4 — Re-status only after fixes land

Run the PRD Evaluation Rules from the skill spec again. Only then update the PRD Status field.

---

## The critique categories that actually matter

These are the categories where my Day 4 v1 PRD failed and where most agentic-product PRDs fail. Use this as a self-review checklist before the human review.

### Strategic / framing

- Problem statement has evidence (interview count, time data, a representative quote). Assertion is not evidence.
- Customer base sized bottom-up with the methodology visible. Top-down TAM is a red flag.
- Differentiation ranked by honest defensibility. Features are not moats.
- Pricing model defined, even directionally. "Open question" is not Exec-Ready.
- Distribution / GTM motion specified. A cost model assuming 5,000 users with no acquisition plan is a fiction.

### Metrics

- Each metric is measurable in practice, not just in theory.
- Self-report bias and telemetry blind spots are called out.
- Leading indicators preferred over lagging.
- Eval methodology specified (set size, labeler count, agreement floor).

### Plan and timeline

- The hidden gating constraint identified (SOC2 observation window, model capacity, hiring, vendor RFP).
- Every milestone has an exit criterion, not just a name.
- Every milestone has a role-named owner. Author owning every milestone is a credibility tell.
- Go/no-go criteria for milestones with technical risk.

### Agent / technical sections

- Agent Harness layers documented (skills, agents, orchestration, memory, tools, eval, deployment).
- Capacity sized from a usage model with the math shown, not round numbers.
- Cost forecast has line items (model, retries, eval, RAG refresh, infra) and a sensitivity table.
- Multi-agent has a Plan B with a measurable fallback trigger.

### Missing sections to check for

- Team and staffing plan.
- External dependencies (model capacity, MCP server availability, eval-labeling vendor, audit firm).
- Compliance and legal roadmap.
- Customer support model and incident escalation for hallucinated outputs.
- Sunset / data deletion on churn.
- Agent anti-goals (what the agent will explicitly refuse to do).

---

## What "Exec-Ready" actually requires for an agentic product

The skill's Exec-Ready rule was updated in Day 4 to include Agent Harness, Capacity Requirements, Security and Privacy, and Cost and Budget. The lived lesson: even with those sections filled, the PRD is not Exec-Ready until:

1. The numbers in those sections have visible methodology.
2. The timeline accommodates compliance gates that have fixed observation windows.
3. There is a Plan B for any technical capability the team has never shipped before.

---

## When to skip the loop

- Internal RFCs with no exec audience.
- Pre-discovery scoping docs where evidence does not yet exist.
- Hackathon-style prototypes where the PRD is documenting a working demo, not authorizing investment.

Everywhere else, run the loop.

---

## Related artifacts

- Skill spec: `skills/prd_builder.md`
- Worked example PRD (after one critique cycle): `examples/prd_ai_tpm_copilot.md`
- Day 4 lessons: `lessons_learned/day3_day4_lessons.md`
