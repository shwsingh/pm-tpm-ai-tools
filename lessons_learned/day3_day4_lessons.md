# Lessons Learned - Day 3 and Day 4

## Day 3

### Learnings

- A skill is not a tool. A tool runs code; a skill is a reusable instruction spec.
- Skills are markdown files, not Python files.
- A good skill has a contract: Purpose, Input, Output, Evaluation Rules, Expected Output Format.
- Skills written today become inputs for agents in later days.

### Issues Encountered

1. Confused "skill" with "function" early on.
2. Forgot to sync README, 14_day_plan.md, and progress_tracker.md together.

---

## Day 4

### Learnings

- A PRD skill is more than a template. Evaluation rules give it a quality bar.
- Customer Base and Market Analysis turn a feature spec into a product spec.
- Milestones with proposed dates force the PRD to be schedulable, not just descriptive.
- Reusing the Day 3 skill structure made Day 4 fast. Skills compound.

### Bigger learnings (from the critique-and-revise loop)

- For an agentic product, the PRD must include Agent Harness, Capacity, Data, Security, Cost, Observability, and Failure Modes. Skipping these is how an "Exec-Ready" PRD silently turns into a Draft.
- A senior-PM critical review pass is itself a reusable skill. Running it against my own PRD took it from generic-looking to actually defensible in one cycle.
- "Show your work" beats round numbers. Bottom-up sizing, cost line items, and capacity math from a usage model are what make a PRD survive review.
- Differentiation has to be ranked by honest defensibility. "Agentic, not chat" is not a moat. Workflow-specific evals and cross-workflow context sharing are.
- Timeline realism comes from challenging the hidden gates. SOC2 Type II observation period and multi-agent quality bars set the GA date, not optimism.
- Every milestone needs an exit criterion. "RAG knowledge base online" is not a milestone; "retrieval recall@5 >= 80% on the eval set" is.
- Every milestone needs a role-named owner. Listing the author as the owner of every milestone is a credibility tell.

### Issues Encountered

1. Tempted to add LLM calls inside the skill - the skill is markdown only, agents come later.
2. Almost skipped the badge bump on README.
3. First PRD draft used bullet points everywhere - it read as a checklist, not a senior-PM document. Prose for narrative sections, bullets only for genuine lists.
4. First PRD claimed Exec-Ready status without evidence, sourced sizing, or pricing. Marking it Exec-Ready prematurely would have wasted a real review meeting.
5. First timeline put GA in 4 months while including SOC2 Type II, which has a 6-month observation window. The constraint was sitting in the doc the whole time and I missed it on the first pass.
