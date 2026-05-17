"""
Runs pytest on every problem directory, prints a summary, and rewrites the
progress table in README.md between the PROGRESS markers.

Called automatically by CI on every push. Can also be run locally:
    python .github/scripts/update_progress.py
"""

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent
README = REPO_ROOT / "README.md"
MARKER_START = "<!-- PROGRESS:START -->"
MARKER_END = "<!-- PROGRESS:END -->"

DIFFICULTY = {
    "001": "Easy",
    "002": "Easy",
    "003": "Easy",
    "004": "Medium",
    "005": "Medium",
    "006": "Medium",
    "007": "Medium",
    "008": "Medium",
    "009": "Medium",
    "010": "Medium",
}


def discover_problems() -> list[Path]:
    """
    Return sorted problem directories whose names begin with a digit.

    Returns:
        list[Path]: Sorted list of problem directory paths.
    """
    return sorted(
        d for d in REPO_ROOT.iterdir()
        if d.is_dir() and d.name[0].isdigit()
    )


def run_tests(problem_dir: Path) -> bool:
    """
    Run pytest quietly on one problem and return whether all tests passed.

    Args:
        problem_dir (Path): Path to the problem directory.

    Returns:
        bool: True if pytest exited with code 0, False otherwise.
    """
    test_file = problem_dir / "test_solution.py"
    if not test_file.exists():
        return False
    result = subprocess.run(
        [sys.executable, "-m", "pytest", str(test_file), "-q", "--tb=line"],
        cwd=REPO_ROOT,
    )
    return result.returncode == 0


def prettify_name(dirname: str) -> str:
    """
    Convert a directory name like '001_two_sum' into a readable title 'Two Sum'.

    Args:
        dirname (str): Raw directory name.

    Returns:
        str: Human-readable problem title.
    """
    parts = dirname.split("_")[1:]
    return " ".join(p.capitalize() for p in parts)


def build_table(problems: list[Path]) -> str:
    """
    Run tests for every problem and build a markdown progress table.

    Args:
        problems (list[Path]): Ordered list of problem directories.

    Returns:
        str: Markdown table string.
    """
    rows = [
        "| # | Problem | Difficulty | Status |",
        "|---|---------|------------|--------|",
    ]
    solved = 0
    for problem_dir in problems:
        num = problem_dir.name.split("_")[0]
        name = prettify_name(problem_dir.name)
        difficulty = DIFFICULTY.get(num, "—")
        print(f"\n{'='*50}")
        print(f"Running: {problem_dir.name}")
        print(f"{'='*50}")
        passed = run_tests(problem_dir)
        status = "✅ Solved" if passed else "❌ Unsolved"
        if passed:
            solved += 1
        rows.append(f"| {num} | {name} | {difficulty} | {status} |")

    print(f"\n{'='*50}")
    print(f"Results: {solved}/{len(problems)} solved")
    print(f"{'='*50}\n")
    return "\n".join(rows)


def update_readme(table: str) -> None:
    """
    Replace the content between the progress markers in README.md.

    Args:
        table (str): The new markdown table to insert.
    """
    content = README.read_text(encoding="utf-8")
    new_block = f"{MARKER_START}\n{table}\n{MARKER_END}"
    updated = re.sub(
        rf"{re.escape(MARKER_START)}.*?{re.escape(MARKER_END)}",
        new_block,
        content,
        flags=re.DOTALL,
    )
    README.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    problems = discover_problems()
    print(f"Found {len(problems)} problem(s).\n")
    table = build_table(problems)
    update_readme(table)
    print("README.md progress table updated.")
