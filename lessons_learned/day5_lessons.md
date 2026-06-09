# Lessons Learned - Day 5

## Day 5

### Learnings

- An agent is not a skill. A skill is a markdown work contract; an agent is the runtime that decides when to use which skill, with which tools, and what to do with the result.
- The agent shape (parse -> classify -> decide -> respond) is the real learning of Day 5. The keyword classifier is throwaway; the contract survives.
- A stable input/output contract is what makes future LLM swap-in cheap. Decide the contract before the model.
- "Route to Lead when confidence is low" is a reusable pattern. It generalizes to any agent and produces an operational signal (route-to-Lead rate).
- A dict-shaped output is composable for the next agent. A string-shaped output is not.
- Design decisions documented at end of day are easier to read in 3 months than the diff is. The new design_decisions/ directory is for the future portfolio reviewer.

### Bigger learnings (post-agent additions same day)

- Visual storytelling is its own skill. A left-to-right, color-coded, shape-encoded architecture diagram communicates the system in 5 seconds; the same content as a nested directory tree takes 5 minutes to read. The redesign of the architecture diagram (yellow=UI, green=agent, blue cylinder=skill, purple=output) was the most-impact-per-minute change of the day.
- A per-day delta diagram is more readable than a full architecture diagram for understanding "what changed when". Both are useful, for different questions.
- A blog post for TPM/PM is not a craft post for AI builders. The first draft had jargon (RAG, MCP, DeepEval, agentic) and three meta-learnings. The rewrite cut jargon, anchored on ONE memorable takeaway ("if your AI tool doesn't say 'I don't know,' it's lying to you"), and added a "Monday-morning thing to try". The technical depth moved into a clearly-labeled appendix.
- Smoke tests on a heuristic should use realistic phrasing, not the keywords the heuristic was built around. The brittleness only shows up when the real test case isn't a literal keyword match.
- GitHub Pages + Minimal Mistakes via remote_theme is a small effort for a big visual upgrade. Default Minima looks like documentation; Minimal Mistakes looks like a publication.

### Issues Encountered

1. Almost merged the agent spec into skills/. Caught it during the agents/ vs skills/ split.
2. First version of the lead-routing rule only triggered on "Unknown severity". Missed the case where severity is P1 but evidence is thin - tightened the rule before writing the doc.
3. Pyright complained about `max(dict, key=dict.get)` - real fix was `key=lambda s: sev_counts[s]`. Logged in common_errors.md.
4. Streamlit Pyright "import could not be resolved" warning is back. Same known false positive from Day 1.
5. `type="module"` script with a `DOMContentLoaded` listener never ran on the live blog - module scripts are deferred, so DOMContentLoaded already fired by the time the listener attached. Mermaid diagrams stayed as raw code blocks until I added a `document.readyState` check.
6. First architecture diagram crammed day numbers into every box label - turned into visual noise. Moved day labels to a separate lookup table beneath the diagram and the picture became readable.
7. First PRD author tag said "Senior PM" - updated to "Senior Manager, TPM at Google" after the role/location update. Kept the "Senior TPM" *persona* references inside the PRD unchanged (those are about the customer, not the author).
