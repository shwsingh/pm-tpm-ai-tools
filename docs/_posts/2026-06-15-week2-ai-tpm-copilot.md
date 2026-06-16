---
title: "Building an AI made me write down something I'd known for fifteen years"
date: 2026-06-15
categories:
  - Building in Public
tags:
  - ai
  - agents
  - tpm
  - week-2
excerpt: "The AI didn't make me smarter. It made me more honest about what I actually knew — and what I'd only been pretending to know."
header:
  overlay_color: "#0f172a"
  overlay_filter: "0.6"
  overlay_image: /assets/images/hero-week1.svg
  caption: "Week 2 of 2 - Days 6-12 of 14"
  actions:
    - label: "View on GitHub"
      url: "https://github.com/shwsingh/pm-tpm-ai-tools"
    - label: "Component Reference"
      url: "https://shwsingh.github.io/pm-tpm-ai-tools/components.html"
toc: true
toc_sticky: true
toc_label: "On this page"
---

*I've spent fifteen years making decisions about complex technical systems — writing the spec, owning the plan, sequencing the work. This week I tried to build an AI that could do some of that. What I didn't expect was how much the process would expose about decisions I'd been making on autopilot.*

---

## I was calling it an agent. It wasn't.

For most of this week I was building pipelines and calling them agents. The distinction felt academic until I had both running side by side.

A pipeline does what you designed. You write the steps, you set the order, you decide what runs when. The AI executes your plan — it doesn't have one of its own. When I built the 3-stage workflow on Day 6, I felt like I'd built something intelligent. I had built something automated. Not the same thing.

> I was automating my decisions. Not delegating them.

The real shift came on Day 12. I gave Claude a free-text request and a set of tools — bug triage, feedback analysis, dependency reasoning, knowledge base search. I didn't tell it which to call or in what order. It figured that out. It called a tool, read what came back, decided what to call next, and kept going until it had enough to synthesize an answer. The sequence emerged from the reasoning. It wasn't in my code.

What made it uncomfortable wasn't that it worked. It was that it occasionally worked better than my pipeline did — using a sequence I wouldn't have chosen. I had to resist the urge to constrain it back toward what I would have designed. Staying out of the way was the hard part.

I notice I do this with teams too. The instinct to specify steps when I should be specifying outcomes. The habit of prescribing the plan when I should be clarifying the goal. Building an AI agent made me see that instinct from the outside for the first time.

---

## Fifteen years of implicit knowledge, finally written down.

The hardest thing I did this week was write the evaluation rubric for the Status Report tool. Not the code. Not the Claude prompt. The rubric — sitting down and answering honestly: what does a *good* weekly TPM status update actually look like?

I've written hundreds of status updates. I've read thousands. Coached people on them. Rewritten them at midnight before exec reviews. I had very strong intuitions about what made one good or bad. But turning those intuitions into five specific, checkable, fail-able criteria took longer than building the entire tool.

Here's what I ended up with. Completeness (are all fields filled?) became a prerequisite gate, not a quality dimension — it was form validation pretending to be judgment.

<div class="rubric-table">

| Criterion | ❌ Wrong | ✅ Right |
|-----------|---------|---------|
| **Ask Specificity** — Every ask names what leadership needs to do, who specifically, and by when. | "We need alignment on the API contract before we can proceed." | "Decision needed from VP Eng by Thursday: approve API contract v2 or we slip the integration milestone by one week." |
| **Status Accuracy** — Color is derived from content. Green = on track. Yellow = at risk with workaround. Red = blocked, no mitigation. | 🟢 Green — "Auth integration is two weeks behind and blocking the mobile launch." | 🔴 Red — "Auth integration is two weeks behind and blocking the mobile launch. No current workaround." |
| **Impact Clarity** — Every blocker and risk names its downstream consequence. Facts without consequences leave leadership unable to prioritize. | "Auth integration is delayed. API performance is a concern." | "Auth integration delayed two weeks — blocks mobile launch scheduled for Q3. API p99 at 4s under load — risks checkout abandonment on launch day." |
| **Next Week Concreteness** — Deliverables with a done state, not ongoing activities. | "Continue working on auth integration. Make progress on API performance." | "Ship auth integration to staging and complete smoke test by Friday. Deliver API load test results with mitigation options to VP Eng by Wednesday." |
| **Exec Readability** — A new VP reads it cold and knows what is happening, what is at risk, and what they are being asked to do — without follow-up questions. | "LGTM on the CL for the P0 fix — waiting on OE signoff before we can roll to prod. IAM changes still pending SIRT review." | "The critical bug fix is code-complete and approved — waiting on Operations Engineering sign-off before deploying to production. Identity and Access Management changes pending Security review, expected by end of week." |

</div>

What I ended up with isn't just an eval framework for an AI tool. It's the most precise articulation I've ever written of what I actually value in a status update — clearer than any style guide, any template, any piece of onboarding documentation I've produced in fifteen years.

The AI forced me to make the implicit explicit. I've been carrying that rubric in my head since 2012. It exists as a document now. It didn't before. That might be the most durable thing I built this week — and it has nothing to do with the code.

---

## The failures that scare me most produce no error.

Twice this week I had code that ran cleanly, produced output, and was wrong in ways I nearly shipped.

The first: the retry loop was catching every exception — including auth failures and rate limits — and retrying them with the same patience it applied to a recoverable JSON parse error. The app looked fine. It was silently burning tokens on requests that would never succeed. No stacktrace. No warning. Just slow, expensive, quietly incorrect behavior.

The second was subtler. After each tool call in the agent loop, I was keeping Claude's text response and discarding the rest. The loop kept running. Claude kept answering. But it had lost track of what it had already reasoned through — because I'd thrown away the part of the response that recorded it. The output looked complete. It was an agent with amnesia, and I almost didn't catch it.

Which is why the evaluation framework I built on Day 11 matters more than it sounds. It's a second Claude call that reads the same skill spec rules I wrote for each tool and scores any output against them — criterion by criterion, pass or fail, with a reason. Not a vibe check. A structured audit that runs automatically after every agent call.

I think about this in the context of AI systems at scale. The failure mode everyone talks about is the AI that confidently says something wrong. The failure mode I'm more worried about now is different: the AI that quietly degrades. Producing outputs that are slightly worse, for reasons that are invisible, in ways that accumulate over weeks before anyone notices.

Silent failures don't announce themselves. They wait to be found. That's what makes the evaluator — not the agent — the part worth building first.

---

**[→ Browse the Component Reference](https://shwsingh.github.io/pm-tpm-ai-tools/components.html)** — every module in the architecture with role, impact, and a link to its source.

---

### For the engineers reading this

- **Agent loop message format:** After a `tool_use` stop, append the full `response.content` list as the assistant message before sending tool results back. Extracting only text and discarding `tool_use` blocks breaks the loop silently.
- **Retry scope:** Only catch `json.JSONDecodeError` in the retry loop. Auth failures, rate limits, and network errors should surface immediately — retrying them burns tokens and masks real problems.
- **Claude-as-judge:** A second Claude call with the skill spec's evaluation rules as the prompt produces domain-specific pass/fail per criterion. No eval library needed when the rules are already written in plain English.
- **Batch over per-item:** Dependency reasoning and feedback analysis both send all items in one call. Cross-item patterns — cascading risks, aggregate themes — are only visible when Claude sees the full set.
