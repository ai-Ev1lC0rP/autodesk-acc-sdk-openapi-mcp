"""Regression test for README endpoint checklist sync."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "update_readme_checklist.py"
README = REPO_ROOT / "README.md"


def test_readme_checklist_up_to_date() -> None:
    """Ensure running the update script leaves README unchanged."""
    subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO_ROOT, check=True)
    diff = subprocess.run(
        ["git", "diff", "--name-only", str(README)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        assert diff.stdout.strip() == "", "README.md is out of date. Run scripts/update_readme_checklist.py"
    finally:
        subprocess.run(["git", "checkout", "--", str(README)], cwd=REPO_ROOT)

