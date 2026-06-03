# Lessons Learned - Day 1 and Day 2

## Day 1 - Setup and First App

### What Worked
- Created GitHub repository.
- Cloned repo locally.
- Created Python virtual environment.
- Installed Streamlit.
- Built first TPM/PM dashboard.
- Ran app locally.
- Committed and pushed code.

### Issues Found

| Issue | Root Cause | Fix |
|---|---|---|
| Streamlit import could not be resolved | VS Code was not using the venv interpreter | Select venv interpreter in VS Code |
| Streamlit not found globally | Streamlit was installed inside venv, not global Python | Activate venv before running app |
| GitHub push rejected due to email privacy | Git used private/local email | Set GitHub noreply email |
| Branch diverged after fixing commit author | Local and remote history had different commits | Used git pull origin main --rebase |

### Key Learnings
- The terminal runs commands; app.py stores Python code.
- Virtual environments isolate project dependencies.
- GitHub only gets what is committed and pushed.
- README turns code into a portfolio story.

---

## Day 2 - Launch Risk Analyzer

### What Worked
- Built on top of existing Day 1 app.
- Added Launch Risk Analyzer as a new section.
- Added text input for launch notes.
- Added keyword-based risk detection.
- Added launch health output: Green, Yellow, Red.
- Added risks, blockers, recommendations, and executive summary.

### Issues Found

| Issue | Root Cause | Fix |
|---|---|---|
| Typed Python code in terminal | Confused terminal commands with source code | Paste Python code inside app.py |
| app.py file not found | Ran Streamlit from repo root instead of app folder | cd into projects/tpm_pm_toolkit |
| Pylance warning persisted | VS Code interpreter mismatch | Ignore if app runs, or select venv interpreter |

### Key Learnings
- Current working directory matters.
- Streamlit must be run from the folder containing app.py or with full file path.
- Day 2 feature is rule-based today; future version can use a real LLM.
- Vibe coding still requires debugging and understanding where code belongs.
