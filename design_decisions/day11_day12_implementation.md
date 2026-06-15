# Design Decisions: Days 11–12 Implementation

## Day 11 — Agent Harness + Evaluation Framework

### Decision 1: Harness returns {"output", "meta"}, callers extract output

**Choice:** `AgentHarness.run()` returns a dict with two keys. Each caller extracts
`result["output"]` and stores `result["meta"]` in session state. Callers' return
signatures stay identical to what they were before.

**Why:** Changing the return type of `triage_with_claude()`, `analyze_feedback()`,
and `analyze_dependencies()` would require updating 8+ call sites in the UI. By
keeping the functions returning the same dict as before, the refactor is purely
internal — zero UI changes required.

**Alternative rejected:** Return the full `{"output", "meta"}` from every function
and update all callers → cascading changes, higher diff risk, same end result.

---

### Decision 2: Retry only on JSON parse failure, not on API errors

**Choice:** The retry loop in `AgentHarness.run()` catches `json.JSONDecodeError`
and retries up to 2 times. Other exceptions (API errors, auth failures, network
timeouts) surface immediately.

**Why:** JSON parse failures are recoverable — Claude occasionally wraps output in
markdown code fences despite being told not to. API errors are not recoverable by
retrying immediately (rate limits need backoff; auth failures need user action). Masking
API errors with retries hides real problems.

**Anti-pattern avoided:** Catching all exceptions and retrying blindly — this hides
real API errors and wastes tokens on futile retries.

---

### Decision 3: Claude-as-judge instead of DeepEval

**Choice:** The evaluation framework uses a second Claude call (with the skill spec's
eval rules as the prompt) to score agent outputs. No DeepEval dependency.

**Why:** DeepEval requires a separate installation, account setup, and schema
registration per metric. The skill specs already contain evaluation rules in plain
English — a Claude-as-judge call can use them directly. For a learning project with
custom TPM-domain eval criteria, Claude-as-judge is faster to set up and easier to
customize.

**Trade-off:** DeepEval provides standardized metrics (faithfulness, answer relevancy,
etc.) useful for comparing across models. Claude-as-judge produces domain-specific
pass/fail per criterion. For Day 11's purpose (demonstrating evaluation), the latter
is more instructive.

---

## Day 12 — Multi-Agent System + Agent Loops

### Decision 4: Tools call existing harness functions (no duplicate logic)

**Choice:** `execute_tool()` calls `triage_with_claude()`, `analyze_feedback()`,
`analyze_dependencies()`, and `keyword_search()` — the exact same functions used
by the standalone Day 5, 9, 10 sections.

**Why:** Reuse over duplication. The tool definitions are just wrappers that
serialize/deserialize JSON around the existing functions. No new Claude prompt
engineering — the sub-agents' system prompts are already battle-tested from
Days 9–10. Adding tools to the orchestrator required ~10 lines of dispatch code.

---

### Decision 5: Max 5 iterations, errors continue loop

**Choice:** The agent loop exits after 5 iterations or on `end_turn`. Tool errors
are caught, formatted as error strings, fed back to Claude as tool results, and the
loop continues.

**Why:** 5 iterations handles any realistic TPM request (3–4 tool calls + synthesis).
Stopping on tool errors would mean a bad knowledge base query crashes a briefing that
has already triaged 3 bugs. Claude can reason around a failed tool if it knows what
failed — the error message in the tool result gives it that information.

**Anti-pattern avoided:** Silently swallowing tool errors and passing empty results
back to Claude — Claude would then synthesize a briefing missing key data without
knowing why, producing hallucinated output that looks correct.

---

### Decision 6: Per-iteration trace in UI (not just final answer)

**Choice:** Each loop iteration is shown as an expander with tool name, input,
result preview, and token count. The final synthesis is shown separately.

**Why:** The loop trace is the primary learning artifact of Day 12. Without it,
"multi-agent" is indistinguishable from a single Claude call that returns a long
answer. Showing each tool call makes the agentic reasoning process visible and
debuggable — TPMs can see which tool Claude decided to call and why.

---

## Anti-Patterns Introduced in Days 11–12

| Anti-Pattern | What Goes Wrong | Fix Applied |
|-------------|-----------------|-------------|
| Catching all exceptions in retry loop | Masks API auth/rate errors; retries forever | Only catch `json.JSONDecodeError` in retry; let others surface |
| Calling `anthropic.Anthropic()` inside a tight loop | New client per iteration = connection overhead | Client created once per `AgentHarness.run()` call, not per retry |
| Discarding `response.content` after tool_use | Loop breaks — tool_use blocks must stay in messages | Append full `response.content` to messages, not just text blocks |
| Running evaluator and agent in the same prompt | Conflicts between "produce output" and "score output" | Two separate harness calls: agent first, evaluator second |
| Asking Claude to call all bugs in one triage call | Triage contract expects one bug; batch input produces malformed output | System prompt explicitly says "call triage_bug once per bug report" |
