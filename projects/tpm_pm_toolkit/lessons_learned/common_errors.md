# Common Errors and Fixes

| Error | Meaning | Fix |
|---|---|---|
| Import "streamlit" could not be resolved | VS Code/Pylance is using wrong interpreter | Select venv Python interpreter |
| ModuleNotFoundError: No module named streamlit | Streamlit not installed in active environment | Activate venv and install Streamlit |
| File does not exist: app.py | Running command from wrong folder | cd into projects/tpm_pm_toolkit |
| zsh: command not found | Typed code into terminal | Put Python code inside app.py |
| GitHub push rejected due to private email | Git commit used private email | Configure GitHub noreply email |
| non-fast-forward push rejected | Local and remote branches diverged | Run git pull origin main --rebase |
