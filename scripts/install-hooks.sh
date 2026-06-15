#!/bin/bash
# Install git hooks for this repo. Run once after cloning.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
HOOKS_DIR="$SCRIPT_DIR/../.git/hooks"

cp "$SCRIPT_DIR/post-commit-hook.sh" "$HOOKS_DIR/post-commit"
chmod +x "$HOOKS_DIR/post-commit"

echo "✅ Git hooks installed:"
echo "   post-commit → scripts/post-commit-hook.sh"
echo ""
echo "The hook will warn after any 'Day N' commit if tracking files are missing."
