# PRD Builder Skill

## Purpose

Turn a rough product idea into a structured Product Requirements Document (PRD).

This skill is used by PMs and TPMs to:

* Convert a short idea into a complete PRD
* Define the problem, users, and success metrics
* Lay out milestones and timelines
* Capture customer base and market context
* Surface risks and open questions

---

## Input

A short product idea, problem statement, or feature request.

Example:

We want to build an AI assistant that helps TPMs analyze launch risks, summarize bugs, and generate weekly status reports.

---

## Output

### Product Name

Suggest a clear, short product name.

---

### Problem Statement

Describe the user problem this product solves.

---

### Goals

List the top product goals.

---

### Non-Goals

List what this product will not do.

---

### Target Users / Personas

Who this product is built for.

---

### Customer Base

Describe the customer segments this product targets.

Include:

* Primary customer segment
* Secondary customer segment
* Estimated size of the customer base
* Where these customers exist today (companies, roles, teams)

---

### Market Analysis

Describe the market opportunity for this product.

Include:

* Market category
* Existing competitors or alternatives
* Differentiation
* Market trends supporting this product
* Risks in the market

---

### User Stories

List user stories in the format:

As a [user], I want to [action], so that [benefit].

---

### Requirements

Group requirements by priority:

* P0 (Must Have)
* P1 (Should Have)
* P2 (Nice to Have)

---

### Success Metrics

List measurable success metrics.

Each metric should include:

* Metric name
* Target value
* Measurement method

---

### Milestones and Proposed Timelines

List the major delivery milestones with proposed dates.

Use this format:

* Milestone name — proposed date — owner

Suggested milestones:

* Discovery complete
* PRD approved
* Design complete
* Engineering kickoff
* Alpha release
* Beta release
* GA launch

---

### Agent Harness

Describe the AI agent harness powering the product.

Include:

* Skills used (markdown specs)
* Agents (single or multi-agent)
* Orchestration approach
* Memory and knowledge (RAG, vector store)
* Tool integrations (MCP servers, APIs)
* Evaluation framework
* Deployment model

---

### Capacity Requirements

Describe the expected load and scaling needs.

Include:

* Expected concurrent users
* Requests per second (peak and steady state)
* Latency target (p50, p95)
* Token budget per request
* Monthly token / inference volume
* Scaling strategy

---

### Data Requirements

Describe the data the agent needs to operate.

Include:

* Knowledge base sources (docs, tickets, wikis)
* RAG corpus size and refresh cadence
* Training or fine-tuning data, if any
* Data ownership and residency
* Data retention policy

---

### Security and Privacy

Describe how the agent handles sensitive information.

Include:

* Authentication and authorization model
* PII handling and redaction
* Prompt injection defenses
* Secrets and credential storage
* Compliance requirements (SOC2, GDPR, HIPAA, etc.)

---

### Cost and Budget

Describe the unit economics and operating cost.

Include:

* Model selection and per-token cost
* Estimated monthly model spend
* Infrastructure cost (vector DB, hosting, observability)
* Cost per active user or per task
* Cost ceiling and alerting

---

### Observability and Evaluation

Describe how the agent is monitored and evaluated.

Include:

* Tracing and logging
* Eval framework (DeepEval, custom evals)
* Quality metrics (accuracy, hallucination rate, task success)
* Human-in-the-loop review
* Alerting and incident response

---

### Failure Modes and Guardrails

Describe how the agent behaves when things go wrong.

Include:

* Known failure modes
* Hallucination mitigation
* Refusal patterns
* Fallback behavior when tools fail
* Manual override or escalation path

---

### Risks and Open Questions

List the top product risks and open questions.

---

### Launch Plan

Briefly describe the launch approach (internal, limited beta, GA).

---

## PRD Evaluation Rules

### Exec-Ready

Use Exec-Ready if:

* Problem, Goals, Users, Customer Base, Market Analysis, Requirements, Success Metrics, and Milestones are all filled
* Agent Harness, Capacity Requirements, Security and Privacy, and Cost and Budget are filled
* Success Metrics are measurable
* At least one P0 requirement exists
* Milestones include proposed dates

---

### Review-Ready

Use Review-Ready if:

* Problem, Goals, Users, and Requirements are filled
* Some sections (Market Analysis, Milestones, or Metrics) are incomplete

---

### Draft

Use Draft if:

* Problem or Goals are missing
* Requirements are missing
* Output is mostly empty

---

## Expected Output Format

Product Name:
...

Problem Statement:
...

Goals:
1.
2.

Non-Goals:
1.
2.

Target Users / Personas:
1.
2.

Customer Base:
- Primary:
- Secondary:
- Estimated size:
- Where they exist today:

Market Analysis:
- Category:
- Competitors:
- Differentiation:
- Trends:
- Market risks:

User Stories:
1. As a ..., I want to ..., so that ...
2.

Requirements:
P0:
1.
P1:
1.
P2:
1.

Success Metrics:
1. Metric: ... | Target: ... | Measured by: ...
2.

Milestones and Proposed Timelines:
1. ... — YYYY-MM-DD — Owner
2.

Agent Harness:
- Skills:
- Agents:
- Orchestration:
- Memory / Knowledge:
- Tool integrations:
- Evaluation:
- Deployment:

Capacity Requirements:
- Concurrent users:
- RPS (peak / steady):
- Latency (p50 / p95):
- Token budget per request:
- Monthly inference volume:
- Scaling strategy:

Data Requirements:
- Knowledge sources:
- RAG corpus size / refresh:
- Training data:
- Data ownership / residency:
- Retention policy:

Security and Privacy:
- AuthN / AuthZ:
- PII handling:
- Prompt injection defenses:
- Secrets storage:
- Compliance:

Cost and Budget:
- Model and per-token cost:
- Monthly model spend:
- Infrastructure cost:
- Cost per user / task:
- Cost ceiling:

Observability and Evaluation:
- Tracing / logging:
- Eval framework:
- Quality metrics:
- Human-in-the-loop:
- Alerting:

Failure Modes and Guardrails:
- Known failure modes:
- Hallucination mitigation:
- Refusal patterns:
- Fallback behavior:
- Escalation path:

Risks and Open Questions:
1.
2.

Launch Plan:
...

PRD Status:
DRAFT | REVIEW-READY | EXEC-READY
