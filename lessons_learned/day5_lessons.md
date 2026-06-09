# Lessons Learned - Day 5

## Day 5

### Learnings

- An agent is not a skill. A skill is a markdown work contract; an agent is the runtime that decides when to use which skill, with which tools, and what to do with the result.
- The agent shape (parse -> classify -> decide -> respond) is the real learning of Day 5. The keyword classifier is throwaway; the contract survives.
- A stable input/output contract is what makes future LLM swap-in cheap. Decide the contract before the model.
- "Route to Lead when confidence is low" is a reusable pattern. It generalizes to any agent and produces an operational signal (route-to-Lead rate).
- A dict-shaped output is composable for the next agent. A string-shaped output is not.
- Design decisions documented at end of day are easier to read in 3 months than the diff is. The new design_decisions/ directory is for the future portfolio reviewer.

### Issues Encountered

1. Almost merged the agent spec into skills/. Caught it during the agents/ vs skills/ split.
2. First version of the lead-routing rule only triggered on "Unknown severity". Missed the case where severity is P1 but evidence is thin - tightened the rule before writing the doc.
3. Pyright complained about `max(dict, key=dict.get)` - real fix was `key=lambda s: sev_counts[s]`. Logged in common_errors.md.
4. Streamlit Pyright "import could not be resolved" warning is back. Same known false positive from Day 1.
