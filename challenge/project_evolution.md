# Project Evolution

Visual record of how the AI TPM Copilot is built up, day by day.

GitHub renders Mermaid blocks natively. Each diagram below is real Mermaid — you can edit the text and the picture updates.

---

## 1. Timeline (Day 0 → Today)

```mermaid
timeline
    title AI TPM Copilot - 14 Day Build Timeline
    Day 0  : Repo created
           : 14_day_plan.md
           : CLAUDE.md (added later)
    Day 1  : Streamlit homepage
           : app.py first version
           : venv + README
    Day 2  : Launch Risk Analyzer
           : Keyword heuristics
           : Red / Yellow / Green rubric
    Day 3  : First skill spec
           : skills/launch_risk_analysis.md
           : Skill -vs- Tool distinction learned
    Day 4  : PRD Builder skill
           : Agent-aware sections (harness, capacity, cost, security)
           : Worked PRD in examples/
           : Critique loop captured in notes/
    Day 5  : First agent (Bug Triage)
           : agents/ directory created
           : design_decisions/ directory created
           : Route-to-Lead safety net
           : Heuristic + LLM-swap stub
```

---

## 2. Architecture as it stands today (Day 5)

Read this left-to-right: a TPM pastes input, the Streamlit app routes it to the right capability, agents (when present) consume skills and return structured output. Shapes encode role — rounded = UI, rectangle = agent, cylinder = skill spec. Dashed/pink = planned for later days.

```mermaid
flowchart LR
    User(["TPM / PM<br/>user"]):::user

    subgraph APP["Streamlit App"]
        direction TB
        Home(["Homepage"]):::ui
        LRA(["Launch Risk<br/>Analyzer UI"]):::ui
        BUG(["Bug Triage UI<br/>+ triage fn"]):::ui
    end

    subgraph AGENTS["Agents"]
        BTA["Bug Triage Agent"]:::agent
    end

    subgraph SKILLS["Skills (markdown specs)"]
        S_LR[("launch_risk_analysis")]:::skill
        S_PRD[("prd_builder")]:::skill
        S_BUG[("bug_triage")]:::skill
    end

    Output["Structured output<br/>severity / risk brief / PRD"]:::output

    User --> APP
    LRA -. follows spec .-> S_LR
    BUG --> BTA
    BTA -. uses .-> S_BUG
    APP --> Output
    Output --> User

    subgraph FUTURE["Planned (Day 6 - 14)"]
        direction TB
        RAG[("RAG knowledge base<br/>Day 8")]:::future
        MCP["MCP servers<br/>Jira, GitHub<br/>Day 13"]:::future
        EVAL["DeepEval framework<br/>Day 11"]:::future
        MULTI["Multi-agent<br/>orchestration<br/>Day 12"]:::future
        LLM["Claude Sonnet swap<br/>Day 7 - 9"]:::future
    end

    AGENTS -.-> FUTURE
    SKILLS -.-> FUTURE

    subgraph META["Supporting artifacts"]
        direction TB
        EX["examples/<br/>worked PRD"]:::meta
        DD["design_decisions/<br/>per-day choices"]:::meta
        LL["lessons_learned/<br/>per-day notes"]:::meta
        NOTES["notes/<br/>reusable templates"]:::meta
    end

    AGENTS -.-> META
    SKILLS -.-> META

    classDef user fill:#1e293b,stroke:#0f172a,color:#fff,font-weight:bold
    classDef ui fill:#fef3c7,stroke:#a16207,color:#0f172a
    classDef agent fill:#dcfce7,stroke:#166534,color:#0f172a,font-weight:bold
    classDef skill fill:#dbeafe,stroke:#1e40af,color:#0f172a
    classDef output fill:#ede9fe,stroke:#6d28d9,color:#0f172a
    classDef meta fill:#f1f5f9,stroke:#94a3b8,color:#475569
    classDef future fill:#fce7f3,stroke:#9d174d,color:#831843,stroke-dasharray:5 5
```

### Legend

| Shape / colour | Means |
|---|---|
| Dark navy oval | User |
| Yellow rounded box | Streamlit UI surface |
| Green rectangle | Agent — runtime logic, consumes skills |
| Blue cylinder | Skill — markdown spec, the work contract |
| Purple rectangle | Structured output returned to the user |
| Gray box (dashed link) | Supporting artifact (lessons, design decisions, examples, notes) |
| Pink dashed box | Planned for a later day |

### When each piece was added

| Component | Day |
|---|---|
| Homepage | Day 1 |
| Launch Risk Analyzer UI | Day 2 |
| `skills/launch_risk_analysis.md` | Day 3 |
| `skills/prd_builder.md` + `examples/` + `notes/` | Day 4 |
| `skills/bug_triage.md` + `agents/` + `design_decisions/` + Bug Triage UI | Day 5 |
| RAG, MCP, DeepEval, multi-agent, LLM swap | Day 6 – 14 (planned) |

---

## 3. Per-day deltas — what each day added

Each diagram shows only the **new** boxes added that day, with arrows to what they integrate with.

### Day 0 — Repo created

```mermaid
flowchart LR
    repo["GitHub repo<br/>shwsingh/pm-tpm-ai-tools"]
    plan["challenge/14_day_plan.md"]
    license["LICENSE"]
    repo --> plan
    repo --> license
```

State at end of Day 0: empty repo with a 14-day plan and a license. No code yet.

### Day 1 — Streamlit homepage

```mermaid
flowchart LR
    venv["venv/"]
    app["projects/tpm_pm_toolkit/app.py<br/>Homepage cards"]
    readme["README.md"]
    pt["challenge/progress_tracker.md"]
    venv --> app
    app --> readme
    readme --> pt
```

Added: virtualenv, the first app.py with placeholder homepage cards for the planned modules, README, and the progress tracker.

### Day 2 — Launch Risk Analyzer

```mermaid
flowchart LR
    app["app.py<br/>(existing)"]
    lra["Day 2 section:<br/>Launch Risk Analyzer<br/>(keyword heuristic)"]
    rubric["Red / Yellow / Green rubric"]
    lessons["lessons_learned/day1_day2_lessons.md"]
    errors["lessons_learned/common_errors.md"]
    app --> lra
    lra --> rubric
    lra --> lessons
    lessons --> errors
```

Added: the first real capability, lessons file, and common-errors file.

### Day 3 — First skill

```mermaid
flowchart LR
    risk_skill["skills/launch_risk_analysis.md<br/>(first skill)"]
    contract["Skill contract:<br/>Purpose - Input - Output -<br/>Evaluation Rules"]
    risk_skill --> contract
    contract -.-> lra["Day 2 Launch Risk Analyzer<br/>(now has a spec)"]
```

Added: the very first skill spec. The Day 2 analyzer code did not change today; what changed is that the *behavior* is now documented as a reusable contract.

### Day 4 — PRD Builder + critique loop

```mermaid
flowchart TB
    prd_skill["skills/prd_builder.md"]
    agent_sections["Agent-aware sections:<br/>Harness, Capacity, Data,<br/>Security, Cost, Observability,<br/>Failure Modes"]
    example["examples/prd_ai_tpm_copilot.md<br/>(worked PRD)"]
    critique["notes/day4_prd_critique.md<br/>(reusable critique loop)"]
    lessons34["lessons_learned/day3_day4_lessons.md"]
    prd_skill --> agent_sections
    prd_skill --> example
    example --> critique
    critique --> lessons34
```

Added: second skill, worked example PRD revised through a senior-PM critique pass, and the critique loop captured as a reusable note.

### Day 5 — Bug Triage Agent (today)

```mermaid
flowchart TB
    bug_skill["skills/bug_triage.md<br/>(work contract)"]
    bug_agent["agents/bug_triage_agent.md<br/>(agent contract)"]
    app_day5["app.py<br/>Day 5 section + triage() fn"]
    dd_day5["design_decisions/day5_bug_triage_agent.md<br/>(5 design choices)"]
    lessons5["lessons_learned/day5_lessons.md"]
    lead["Route-to-Lead<br/>(safety net for ambiguous bugs)"]

    bug_skill --> bug_agent
    bug_agent --> app_day5
    bug_agent --> lead
    app_day5 --> lead
    bug_agent --> dd_day5
    dd_day5 --> lessons5
```

Added: first agent (separate from skill), the agents/ and design_decisions/ directories, route-to-Lead safety net, and a smoke test that produced real evidence (logged into the design decisions doc).

---

## 4. Mindmap of the current state

A radial view of everything that exists today, grouped by purpose.

```mermaid
mindmap
  root((AI TPM Copilot))
    Skills
      launch_risk_analysis
      prd_builder
      bug_triage
    Agents
      bug_triage_agent
    Application
      Streamlit app.py
      Homepage cards
      Launch Risk Analyzer
      Bug Triage UI
    Documentation
      README
      CLAUDE.md
      14_day_plan
      progress_tracker
      project_evolution
    Examples
      AI TPM Copilot PRD
    Design decisions
      Day 5 - Bug Triage Agent
    Lessons learned
      Day 1-2
      Day 3-4
      Day 5
      Common errors
    Notes
      Day 4 PRD critique loop
    Planned
      RAG knowledge base
      MCP server
      Multi-agent orchestration
      Evaluation framework
```

---

## 5. 14-day plan as a Gantt

```mermaid
gantt
    title 14 Day Capability Plan
    dateFormat YYYY-MM-DD
    axisFormat %d %b

    section Foundations
    Day 1 - Homepage           :done, d1, 2026-06-05, 1d
    Day 2 - Launch Risk        :done, d2, 2026-06-06, 1d
    section Skills
    Day 3 - Launch Risk Skill  :done, d3, 2026-06-07, 1d
    Day 4 - PRD Builder Skill  :done, d4, 2026-06-08, 1d
    section Agents
    Day 5 - Bug Triage Agent   :done, d5, 2026-06-09, 1d
    Day 6 - Agent Workflow     :d6,  after d5, 1d
    Day 7 - Status Report      :d7,  after d6, 1d
    section AI integration
    Day 8 - Knowledge Base     :d8,  after d7, 1d
    Day 9 - Feedback Agent     :d9,  after d8, 1d
    Day 10 - Dependency Agent  :d10, after d9, 1d
    section Evaluation
    Day 11 - Evals             :d11, after d10, 1d
    Day 12 - Multi-Agent       :d12, after d11, 1d
    Day 13 - MCP Integration   :d13, after d12, 1d
    Day 14 - Executive Copilot :d14, after d13, 1d
```

The first LLM call in the project is expected at Day 7 (Status Report needs summarization). The Bug Triage Agent flips from heuristic to LLM-backed at Day 9.

---

## 6. How to read this file in 3 months

If you are reviewing this for the portfolio:

1. **Start with Section 1** — the timeline tells you what was built and in what order.
2. **Then Section 2** — the architecture diagram shows how the pieces fit together today, with day labels so you can see what came when.
3. **Use Section 3** — when you want to understand *why* a particular file exists, look at the day delta diagram for that day.
4. **Section 4** — the mindmap is a flat inventory for quick navigation.
5. **Section 5** — the Gantt shows what is still ahead.

---

## 7. How to update this file each day

End of each day, edit Section 1 (add a timeline entry), Section 2 (drop the new boxes in), Section 3 (add a new delta diagram), Section 4 (extend the mindmap), and Section 5 (mark the day as `done`).

If a day has no architectural change (pure docs update), only Section 1 needs an entry.
