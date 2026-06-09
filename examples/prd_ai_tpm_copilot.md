# PRD: AI TPM Copilot

**Author:** Shweta Singh (Senior Manager, TPM at Google)
**Status:** Exec-Ready (v2 — revised after first review pass)
**Last updated:** 2026-06-08
**Generated using:** `skills/prd_builder.md`
**Reviewers:** Eng Lead, Security Lead, GTM Lead, Finance partner

---

## 1. Problem Statement

We ran sixteen one-hour interviews with Senior TPMs and PMs across nine companies between April and May 2026 (six FAANG-adjacent, three mid-stage SaaS). Twelve of the sixteen independently described the same weekly loop: pull status from Jira and Slack on Monday and Tuesday, write a launch risk brief on Wednesday, triage bugs on Thursday, and produce an executive update on Friday. Self-reported time on this loop ranged from 11 to 19 hours per week, with a median of 14. One Director of Engineering, reading the same TPM rollups across six programs, told us bluntly: *"I cannot compare these. Each TPM grades risk differently. I do not trust the green."*

The consequence is not just lost hours. It is late risk surfacing. In post-launch retros from three of the interviewed companies, the most-cited root cause of slipped milestones was "blocker visible in Slack/Jira earlier, did not reach the readiness review." This is exactly the gap an agentic system can close — not a chat box bolted onto Jira, but a copilot that owns the recurring TPM workload end-to-end with a consistent severity rubric.

Open caveat: the interview sample is biased toward companies that already invest in TPM as a discipline. The pain may be smaller at companies under 200 engineers, which is part of why we scope the ICP narrowly below.

---

## 2. Goals

Our primary goal is to reduce time-on-TPM-loop by 50% on a hard metric (paste-to-brief, paste-to-status) for design-partner TPMs within ninety days of activation. We intentionally chose a smaller, harder, *measurable* number rather than the directional "70%" we drafted first.

Secondarily, we want to lift cross-program risk consistency. We will measure this by having the same Director rescore TPM briefs against our rubric and tracking inter-program agreement before and after rollout.

Third, we want to be cross-workflow from day one. A TPM should not need three tools for risk, triage, and reporting. Sharing context and a single severity model across workflows is what makes us defensible against single-feature competitors.

---

## 3. Non-Goals

We are not replacing Jira or Linear. We will not auto-execute writes against production systems — humans approve every write. We will not provide generic chat, generic code assistance, or generic writing — every workflow is scoped to TPM and PM use cases. We will not train a foundation model, and we will not fine-tune in v1.

**Agent anti-goals** (explicit refusals the agent will enforce): no writes to prod systems without an approval handshake; no generation of code; no summarization of HR, legal, or compensation data; no inferring individual performance from telemetry.

---

## 4. Target Users and Personas

The primary persona is the **Senior TPM** at a company with 200+ engineers, running multi-team launches every quarter and writing one to three exec updates a week. Their pain scales linearly with program complexity and they have no leverage point today.

The secondary persona is the **Product Manager** who needs PRD scaffolding fast and consistently. Lower frequency, but a high-conversion entry point for self-serve.

The consuming personas — **Engineering Managers** and **Directors of Engineering** — do not log in daily but are the budget owners and the reason exec-readability matters.

---

## 5. Customer Base (Bottom-Up Sizing)

We size from the bottom up rather than top-down to avoid the "TAM theatre" problem.

**ICP at GA:** US and EU technology companies with 200+ engineers that have at least one dedicated TPM. From LinkedIn and Crunchbase, we count approximately 4,200 such companies. Average TPM density at this size is 1 TPM per 30–50 engineers (interview data + public org charts), which gives us ~12,000–18,000 TPMs in the ICP. Including PMs (heavier on the PRD use case) adds ~35,000–50,000 seats.

**Serviceable obtainable market (3-year):** We assume 8% logo penetration of ICP companies and 40% seat penetration within a customer (TPMs first, PMs second). That gives roughly 340 customer logos and 20,000–28,000 paid seats. At our target ACV (Section 12) this is a meaningful business but not a billion-dollar standalone category — which is why bundling-resistance (Section 6) matters more than raw TAM.

**Open data risk:** Our TPM density estimate is based on twelve org charts. We will validate against a paid LinkedIn Talent Insights pull in Q3.

---

## 6. Market Analysis and Defensibility

The category — AI productivity for technical program and product management — is forming, not formed. Our competitive set splits into two groups.

The **incumbent productivity suites** (Atlassian Intelligence, Linear AI, Productboard AI, Notion AI) have distribution we cannot match. Their AI today is single-doc summarization and ticket auto-write — not multi-step agentic workflows with eval and rubric enforcement. We expect them to close this gap in 12–18 months. Our wedge is to be obviously better at TPM workflows specifically before they generalize.

The **horizontal enterprise AI** group (Glean, in-house copilots, Anthropic/OpenAI assistants) is powerful but workflow-agnostic. They do not know what a launch readiness review is.

**Our defensibility, ranked honestly:**
1. **Workflow-specific evals and rubrics** (strongest). Atlassian will not invest in a TPM-specific severity rubric or a curated golden eval set. This is a long-tail integration of domain expertise, not a model feature.
2. **Multi-workflow context sharing.** Once a TPM uses us for launch risk *and* status reporting, the cross-workflow context makes single-feature alternatives feel narrow. Switching cost grows with usage.
3. **MCP-native integration portfolio.** Real but copyable in 6–12 months once MCP standardizes.
4. **"Agentic, not chat"** (weakest as a moat). This is a product choice, not a defensible position. We will stop using this in external pitches.

**Strategic risk to the wedge:** If Atlassian ships a TPM-pack inside Intelligence within 9 months of our beta, our defensibility narrows from "purpose-built" to "best-of-breed against a default-bundled alternative." Our mitigation is to land 10 design partners by Sept 2026 and convert at least 6 to paid by GA, locking in switching cost before bundling lands.

---

## 7. User Stories

1. As a Senior TPM, I want to paste raw launch notes and receive a structured risk brief in under 60 seconds, so that I can flag blockers before the readiness review.
2. As a TPM, I want to generate a weekly exec status report from Jira and Slack, so that I save four or more hours every Friday afternoon.
3. As a PM, I want to turn a rough idea into a structured PRD in under a day, so that I can move into design review the same week.
4. As an Engineering Manager, I want to see dependency risks across teams, so that I can unblock my team before a milestone slips.
5. As a Director of Engineering, I want a consistent severity rubric across all my TPMs, so that I can compare program risk without translating each TPM's idiom.

---

## 8. Requirements

### P0 — Must Have for GA

1. Launch Risk Analyzer with Red/Yellow/Green output and a documented, versioned rubric.
2. PRD Builder skill producing an Exec-Ready PRD from a short idea.
3. Bug Triage agent that classifies and prioritizes incoming bugs.
4. Weekly Status Report skill with exec-quality summary.
5. MCP integrations with Jira and GitHub.
6. Evaluation framework: golden sets per skill, nightly regression, dashboards.

### P1 — Should Have Shortly After GA

1. Dependency Agent tracking cross-team blockers.
2. Customer Feedback Agent clustering and prioritizing inbound feedback.
3. RAG knowledge base over TPM docs, runbooks, and past launches.
4. Multi-agent orchestration across launch, bug, and dependency agents.
5. Slack integration for inline summaries and escalation flows.

### P2 — Nice to Have

1. Voice input for hands-free status capture.
2. Auto-generated launch retros from incident data.
3. Per-team dashboards with trend lines.
4. Customer-specific fine-tuned variants.

---

## 9. Success Metrics

We track a small, high-signal set, and we are explicit about which metrics have measurement limitations.

| Metric | Target | Measurement | Known limitation |
|---|---|---|---|
| Median paste-to-brief latency (Launch Risk) | ≤ 60s end-to-end | Server traces | None |
| Median time-to-Review-Ready (PRD) | ≤ 1 working day | PRD status transitions | None |
| Risk-catch leading indicator | ≥ 70% of risks the AI flagged are confirmed in the readiness review | Confirmed-or-rejected click on each AI-flagged risk by the TPM in-app | TPM bias toward confirming AI output — we sample 10% for human review |
| TPM time saved | ≥ 4 hours/week (self-report) AND ≥ 30% reduction in median paste-to-brief time (telemetry) | Quarterly self-report survey + telemetry | Self-report biased upward; telemetry only sees in-app time |
| Hallucination rate on factual outputs | < 3% | Golden eval set of 500 labeled outputs, three labelers, Cohen's kappa ≥ 0.7 required for the set to count | Eval set is curated, not representative; we resample quarterly |
| WAU among activated TPMs | ≥ 70% by month 3 post-activation | Product analytics, weekly active over a 4-week trailing window | Rebased from MAU because TPM use is naturally weekly |

We dropped the original "8 hours/week saved" and "80% risk-catch" because neither was measurable with the rigor a board would accept.

---

## 10. Pricing and Go-to-Market

### Pricing

Three-tier seat-based, billed annually, with a usage cap per seat to protect margin.

- **Team** — $39/seat/month, includes Launch Risk + PRD + Status skills, 1 MCP integration, shared org RAG (up to 5k docs). Targets PM-led teams and design partners converting.
- **Enterprise** — $79/seat/month, adds Bug Triage and Dependency agents, all MCP integrations, SOC2 reporting, SSO, per-tenant RAG (up to 50k docs).
- **Enterprise Plus** — custom, adds VPC deployment, EU residency, dedicated eval set with quarterly tuning.

Target blended ACV: $35k in year 1 (median customer ~50 seats on Enterprise). Target gross margin: 72% at scale (Section 13).

### GTM motion

Hybrid PLG-into-sales, not pure top-down enterprise.

- **Entry point (PLG):** Free PRD Builder skill via the web app with a 5-PRD/month cap. Designed for individual PMs to bring in.
- **Land:** Team tier self-serve credit card for the first 25 seats of a customer.
- **Expand:** Sales-assisted upgrade to Enterprise once a customer reaches 25 seats or requests SSO. AE-led from there.
- **Channel:** Anthropic and MCP ecosystem partnerships for inbound; targeted outbound to Senior TPMs at top 200 ICP accounts.

Acquisition target by GA: 30 paying customer logos, ~1,200 seats, $1.0M ARR run-rate.

---

## 11. Milestones, Owners, and Exit Criteria

Owners are listed by role; named individuals to be filled in by the staffing plan (Section 15). Every milestone has an explicit go/no-go criterion. **We rebased the original Oct 2026 GA to Feb 2027** to make SOC2 Type II feasible and to give multi-agent quality a real shot at meeting bar. The eng lead and security lead concur with this rebase.

| # | Milestone | Proposed Date | Owner | Exit Criterion |
|---|---|---|---|---|
| 1 | Discovery complete | 2026-06-15 | PM | 16 interviews coded, ICP narrowed, top 3 use cases ranked |
| 2 | PRD approved (this doc, v2) | 2026-06-22 | PM | Eng, Security, GTM, Finance signoff |
| 3 | Skills layer complete | 2026-07-20 | Eng Lead | All P0 skills hit ≥ 85% accuracy on golden set; latency p50 ≤ 2s |
| 4 | Single-agent harness (Bug Triage agent) | 2026-08-17 | Eng Lead | Task success rate ≥ 75% on 100-task eval; refusal rate < 8% |
| 5 | RAG knowledge base | 2026-09-14 | Eng Lead | Retrieval recall@5 ≥ 80% on 200-query eval; nightly refresh stable for 7 days |
| 6 | MCP integrations (Jira + GitHub) | 2026-10-12 | Eng Lead | End-to-end status report from real Jira data passes 10/10 manual review |
| 7 | Alpha — internal dogfood | 2026-10-26 | PM | 5 internal TPMs use it weekly for 4 weeks; NPS ≥ 30 |
| 8 | Multi-agent orchestration | 2026-11-23 | Eng Lead | A2A task success ≥ 70%; if not met, GA ships single-agent (Section 14) |
| 9 | SOC2 Type II observation period starts | 2026-08-01 | Security Lead | Audit firm engaged, controls baselined |
| 10 | Beta with 10 design partners | 2026-12-14 | GTM Lead | 8+ partners onboarded, weekly NPS ≥ 30, < 3% hallucination rate |
| 11 | SOC2 Type II report issued | 2027-02-01 | Security Lead | Audit firm issues Type II report (6-month observation) |
| 12 | GA launch | 2027-02-28 | PM | All beta exit criteria met + 6 design partners converted to paid contracts |

---

## 12. Agent Harness

The harness is layered for composability and independent eval. At the bottom sit markdown **skills** (`launch_risk_analysis`, `prd_builder`, `status_report`, `bug_triage`, `dependency_tracker`, `feedback_analyzer`), each with input/output contracts and evaluation rules. Skills are version-controlled and inspectable, which is what makes them surviveable in enterprise governance review.

**Agents** sit on top of skills and add tool access and planner-executor orchestration. Bug Triage, Dependency, Feedback, and Status Report agents each compose one or more skills with MCP-backed tool calls.

**Multi-agent (A2A)** is used only for cross-domain queries that require composing two or more agents (e.g., "launch risk given current bugs and dependencies"). This is the highest-risk capability and has an explicit fallback path in Section 14.

**Memory** is split: a per-tenant **RAG corpus** (10k–50k docs) over launch docs, runbooks, and retros, and per-user **episodic memory** so the agent does not re-ask the same questions.

**Tools** are exposed exclusively via MCP — Jira, GitHub, Slack, Confluence, Google Docs at GA. Read-mostly; writes require explicit user confirmation.

**Evaluation** is wired in from day one. DeepEval for skill-level evals, an internal harness for agent task success. Every skill has a versioned golden set; nightly regression blocks model or prompt changes that drop quality.

**Models:** Claude Sonnet as default; Haiku for triage/classification where speed wins; Opus reserved for exec-summary fallbacks. Selection is per-skill and configurable per tenant.

**Deployment:** Streamlit prototype today, then containerized API behind enterprise SSO. VPC deployment available as Enterprise Plus.

---

## 13. Capacity Requirements (with the math)

Capacity is sized from a usage model, not round numbers.

**Usage assumptions:** A Senior TPM does ~5 skill calls and ~2 agent tasks per workday. A PM does ~2 PRD-related calls per workday. We assume an 8-hour active window and 50% utilization within that window (i.e., 4 active hours per user per day).

**Beta (Dec 2026):** 10 design partners × ~50 seats = 500 paid seats. Active concurrency at peak ≈ 500 × (4/8) × 0.3 (peak-to-active ratio) ≈ **75 concurrent users**. Peak RPS ≈ 75 × (7 calls / 4hr / 3600s) ≈ **0.04 RPS per user**, ~**3 RPS peak**. We over-provision to **15 RPS peak / 4 RPS steady** for safety.

**GA Year 1 (end of 2027):** 1,200 paid seats. Same model → ~**180 concurrent peak**, **9 RPS peak / 2.5 RPS steady**. Over-provision to **50 RPS peak / 12 RPS steady**.

**Latency targets:** p50 ≤ 8s, p95 ≤ 25s for agent tasks; p50 ≤ 2s, p95 ≤ 6s for skill-only calls. These targets are derived from "should feel real-time during a meeting" (~10s perceived ceiling).

**Token budget per request:** skill calls ~15k input + 3k output; agent tasks ~50k input + 8k output. Multi-agent ~120k input + 12k output.

**Monthly inference volume:** beta ≈ 50M input tokens; GA Year 1 ≈ 350M input tokens. (Lower than our original 750M projection — the previous number was top-down and inflated.)

**Scaling strategy:** stateless API tier behind autoscaling; per-tenant rate limits; queue-backed long-running agent tasks so a slow MCP call cannot block the user-facing request.

---

## 14. Multi-Agent Fallback Plan

Multi-agent orchestration is the single largest technical risk. We commit to a Plan B before milestone 8.

**Quality bar to ship multi-agent at GA:** task success ≥ 70% on a 200-task A2A eval, hallucination rate < 3%, p95 latency ≤ 25s.

**Fallback if the bar is not met by 2027-01-15:** GA ships with **single-agent tool-chaining** instead of A2A. In this mode, the launch-risk agent calls Jira/GitHub directly rather than delegating to a Dependency Agent. We lose ~15% of the cross-domain answer quality (estimated from internal eval) but ship a reliable product. Multi-agent moves to v2 with a dedicated quarter.

This fallback is a real product, not a placeholder. The eng lead has signed off that it can be built on the same infra.

---

## 15. Team, Staffing, and External Dependencies

### Team (target headcount at GA)

- 1 PM (author)
- 3 backend / agent engineers (1 hired, 2 to hire by 2026-08)
- 1 ML / eval engineer (to hire by 2026-09)
- 1 security engineer (50% allocation, shared with platform)
- 1 designer (50% allocation)
- 0.5 GTM lead (shared with another product through beta; dedicated at GA)

### External dependencies

- **Anthropic** model capacity (committed quota for Sonnet + Haiku + Opus by 2026-09). Risk: tier upgrade processing time.
- **MCP servers** for Jira, GitHub, Slack — community + first-party. Risk: Jira MCP completeness; mitigated by maintaining a fork.
- **Eval labeling vendor** for golden-set expansion — Surge AI or Scale (RFP in July 2026).
- **SOC2 audit firm** — engaged by 2026-08 to start observation period.

---

## 16. Data Requirements

**Sources:** Jira tickets, GitHub PRs/issues, Confluence/Notion docs, opt-in Slack channels, historical launch retros (the highest-value corpus for the risk skill).

**RAG corpus:** 10k–50k docs per tenant, refreshed nightly with delta indexing. Embeddings stored in a per-tenant vector namespace.

**Eval data:** sampled from real customer outputs with consent, labeled by a vendor + internal review.

**Ownership and residency:** customers own all data. US and EU regions at GA; no cross-region replication without explicit consent. EU customers default to EU region.

**Retention:** prompts and outputs retained 30 days for debugging by default; opt-out to 7 days available. Eval data anonymized before entering golden sets. Customer churn triggers 30-day data deletion SLA.

---

## 17. Security, Privacy, and Compliance

Security is a procurement gate, not a feature.

**AuthN/AuthZ:** enterprise SSO (Okta, Azure AD); per-workspace RBAC; least-privilege scopes on every MCP integration.

**PII:** redaction pass before persistence; no PII in eval datasets; no PII echoed back in summaries (enforced as a guardrail).

**Prompt injection:** input/output filters; tool-call allowlists; strict agent boundary preventing arbitrary code execution; documented threat model reviewed quarterly.

**Secrets:** vault-backed; MCP credentials never sent to the model context.

**Compliance roadmap:** SOC2 Type II report by 2027-02 (observation starts 2026-08, audit firm engaged 2026-07). GDPR-ready by beta. HIPAA explicitly out of scope for v1. AI governance: model cards, eval reports, and prompt change log available to customer security teams on request.

---

## 18. Cost, Budget, and Sensitivity

### Forecast at GA Year 1 (1,200 seats)

| Line item | Monthly | Notes |
|---|---|---|
| Sonnet inference | ~$95k | 60% of calls, default model |
| Haiku inference | ~$8k | 30% of calls, triage/classification |
| Opus fallback | ~$22k | 10% of calls, exec summary quality |
| Agent retries | ~$11k | Modeled at 12% retry rate on agent tasks |
| Eval workload (nightly regression) | ~$6k | Golden sets across all skills |
| RAG embedding refresh | ~$4k | Delta indexing nightly |
| Vector DB + hosting + observability | ~$12k | Pinecone or pgvector + GCP/AWS |
| **Total infra + model** | **~$158k/month** | |

### Sensitivity

The forecast is most exposed to Opus fallback rate and retry rate. A swing in those two changes total cost by ±25%.

| Scenario | Opus fallback | Retry rate | Total infra+model/month |
|---|---|---|---|
| Base case | 10% | 12% | $158k |
| Pessimistic | 18% | 18% | $200k |
| Optimistic | 6% | 8% | $128k |

### Margin math

ARR target at GA Year 1: $1.0M. Annualized cost: ~$1.9M. **Year 1 gross margin is negative as expected for a new agentic product.** Path to 72% gross margin by end of Year 2 requires either (a) Sonnet cost reductions, (b) routing more traffic to Haiku, or (c) doubling seat count without doubling infra cost. (c) is the realistic lever — agentic products have meaningful operating leverage at scale because RAG, eval, and MCP costs are amortized across tenants.

### Controls

- Hard alert at 120% of monthly forecast.
- Per-tenant spend caps configurable by the customer.
- Circuit breaker degrades Sonnet → Haiku for low-priority skills when a tenant exceeds budget.

---

## 19. Observability and Evaluation

OpenTelemetry traces on every skill and agent call. Prompts and responses logged with 30-day retention. DeepEval for skill evals, internal harness for agent task success. Golden sets are versioned in git alongside the skill specs.

Quality metrics monitored: skill accuracy, hallucination rate, task success rate, latency, refusal rate, cost per task. Every UI output has thumbs-up/thumbs-down; 10% of outputs receive weekly sampled human review. Alerts on latency, error rate, hallucination spike, and cost anomaly route to PagerDuty.

---

## 20. Failure Modes, Guardrails, and Customer Support

**Known failure modes:** hallucinated Jira ticket IDs, over-confident risk ratings on thin evidence, stale RAG context.

**Mitigations:** citation-required outputs for facts pulled from RAG (UI shows the source doc); golden eval set blocks regressions; explicit "confidence: low — needs human review" tag when retrieval recall is below threshold.

**Refusal patterns:** no writes to external systems without explicit confirmation; no PII echo; no inference of individual performance from telemetry; refuses requests outside scope per Section 3 agent anti-goals.

**Fallback behavior:** on tool failure, return partial output with explicit "tool unavailable" notice; never silently drop data; failed agent runs surface an "Escalate to human" action that pre-fills a ticket with the context and trace ID.

**Customer support model:** Tier-1 in-app help and docs; Tier-2 chat support with 4-business-hour response for Enterprise, 1-hour for Enterprise Plus. **Incident escalation for hallucination affecting an exec output:** customer can flag any output as "broken on exec output" and we commit to a root-cause within 24 business hours.

---

## 21. Sunset and Migration

When a customer churns, we delete their RAG corpus, traces, and prompts within 30 days. Customer can request export of their golden eval set and any saved PRDs as markdown before deletion. We will not retain anonymized data without explicit opt-in.

---

## 22. Risks and Open Questions

**Strategic risks**

1. Atlassian or Linear ship a comparable in-suite copilot before our beta. Mitigation: lock in switching cost with 10 design partners by Sept 2026.
2. Enterprise AI procurement compresses our window. Mitigation: PLG entry point bypasses procurement for the first 25 seats.

**Execution risks**

1. Multi-agent orchestration quality. Mitigated by Plan B in Section 14.
2. Sonnet cost durability. Mitigated by Haiku routing and per-tenant caps.
3. SOC2 timeline. Observation period starts 2026-08 and is the gating constraint on GA; any slip cascades.

**Open questions to resolve before milestone 4**

1. EU residency: do we commit to EU region at GA, or behind a 90-day waitlist?
2. Self-serve vs sales-assisted threshold: 25 seats or 50?

---

## 23. Launch Plan

Internal dogfood through alpha (Oct 2026) on this team's own programs, including the Day 14 demo of this repo. Limited beta (Dec 2026 – Feb 2027) with 10 TPM design-partner teams selected from interview pipeline. GA launches Feb 28, 2027 with Jira + GitHub + Slack MCP integrations, SOC2 Type II, SSO, US + EU residency. Post-GA: Dependency and Feedback agents to v2; on-premises / VPC option for Enterprise Plus customers whose security review requires it.

---

**PRD Status:** EXEC-READY

**Changelog from v1:**
- Added evidence to problem statement (16 interviews, quotes, time range).
- Replaced top-down sizing with bottom-up SOM/SAM/SOM.
- Rewrote differentiation as ranked moats with honest defensibility.
- Added pricing tiers and GTM motion.
- Rebased success metrics to be measurable; dropped "8hr saved" and "80% risk-catch."
- Specified hallucination eval methodology (set size, labeler count, kappa).
- Moved GA from 2026-10-31 to 2027-02-28 to make SOC2 Type II feasible.
- Added exit criteria to every milestone; named owners by role.
- Added multi-agent Plan B (Section 14).
- Added team, staffing, external dependencies (Section 15).
- Rebuilt cost forecast with line items and sensitivity (Section 18).
- Added customer support model, sunset / migration, agent anti-goals.
