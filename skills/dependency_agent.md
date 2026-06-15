# Dependency Agent Skill

## Purpose

Track cross-team dependencies for a launch or project. Given a list of dependencies
(who needs what from whom, by when, and current status), Claude reasons about the
critical path, cascading risks, and recommends specific TPM actions.

This goes beyond classification — the agent reasons across the full dependency graph
to surface chains where one blocked dependency cascades into others.

---

## Input

A list of dependency records, each with:
- **Dependent team** — the team that needs the deliverable
- **Provider team** — the team responsible for delivering it
- **Deliverable** — what needs to be handed off
- **Due date** — when it's needed by
- **Status** — On Track | At Risk | Blocked

---

## Output

### Per dependency:
- Risk level: Low | Medium | High | Critical
- Reasoning: why this risk level was assigned
- Recommended TPM action: one specific, actionable step
- Escalate flag: true if requires immediate TPM intervention

### Aggregate:
- Overall dependency health: Green | Yellow | Red
- Critical path dependencies (blocking the launch)
- Cascading risk chains (A blocks B which blocks C)
- Top 3 prioritized TPM actions
- Exec-ready summary (2–3 sentences)

---

## Evaluation Rules

A dependency analysis is **Good** when:
- [ ] Critical path is correctly identified (blocked deps that gate the launch)
- [ ] Cascading risks are surfaced, not just individual dep status
- [ ] TPM actions are specific: "Schedule sync between Auth and Checkout by EOD Friday" not "follow up"
- [ ] Exec summary is usable in a status report as-is
- [ ] Low-risk, on-track deps are not over-escalated

---

## Agent Reasoning Pattern

```
1. Parse all dependencies and their statuses
2. Identify direct blockers (Blocked or At Risk)
3. Trace cascading chains: if dep A feeds dep B, and A is blocked, flag B as at-risk
4. Rank by launch impact (due date proximity + downstream dependencies)
5. Generate specific, role-named actions for each critical item
6. Produce exec summary citing the top risk and recommended escalation
```

---

## Upgrade Path

- Day 12: Multi-agent — Dependency Agent feeds risk findings to the Status Report agent
- Day 13: MCP integration — pull dependency status directly from Jira / Linear
