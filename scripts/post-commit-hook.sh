#!/bin/bash
# Day wrap checker — runs automatically after every commit.
# Warns if a "Day N" commit is missing required tracking file updates.

MSG=$(git log -1 --format="%s")

# Only enforce on Day N commits
if ! echo "$MSG" | grep -qE "^Day [0-9]+"; then
    exit 0
fi

DAY=$(echo "$MSG" | grep -oE "Day [0-9]+" | head -1)
CHANGED=$(git diff-tree --no-commit-id -r --name-only HEAD)
MISSING=()

echo "$CHANGED" | grep -q "challenge/progress_tracker.md" || MISSING+=("challenge/progress_tracker.md  — add Day N section (status, built, decisions, lessons)")
echo "$CHANGED" | grep -q "challenge/14_day_plan.md"     || MISSING+=("challenge/14_day_plan.md        — mark Day N ✅ Done")
echo "$CHANGED" | grep -q "README.md"                    || MISSING+=("README.md                       — badge, current app table, build timeline, architecture diagram")

# Warn if no design decision file for this day
DAY_NUM=$(echo "$DAY" | grep -oE "[0-9]+")
if ! echo "$CHANGED" | grep -qE "design_decisions/day${DAY_NUM}"; then
    MISSING+=("design_decisions/day${DAY_NUM}_*.md       — design decisions with rationale and alternatives")
fi

if [ ${#MISSING[@]} -eq 0 ]; then
    echo ""
    echo "✅ $DAY wrap complete — all tracking files updated."
    echo ""
else
    echo ""
    echo "⚠️  $DAY committed but these tracking files are missing:"
    echo ""
    for f in "${MISSING[@]}"; do
        echo "   • $f"
    done
    echo ""
    echo "Update the files above, then run:"
    echo "   git add <files> && git commit --amend --no-edit"
    echo ""
fi
