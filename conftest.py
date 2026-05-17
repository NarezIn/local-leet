"""
Root conftest for the local-leet practice environment.

Each problem directory contains a solution.py that the test file imports as
'from solution import <function>'. Since all test files share the same basename
(test_solution.py) and the same import name (solution), this hook ensures that
before each test module is loaded, its own problem directory is first on sys.path
and any cached 'solution' module from a previous problem is evicted.
"""

import sys


def pytest_pycollect_makemodule(module_path, parent):
    """
    Prepare sys.path so that 'from solution import X' resolves to the correct
    solution.py sibling, not a cached one from an earlier problem directory.

    Args:
        module_path: Path to the test module about to be imported.
        parent: The pytest collector that owns this module.
    """
    if module_path.name == "test_solution.py":
        problem_dir = str(module_path.parent)
        sys.modules.pop("solution", None)
        if problem_dir in sys.path:
            sys.path.remove(problem_dir)
        sys.path.insert(0, problem_dir)
