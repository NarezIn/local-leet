# Local LeetCode Practice

10 LeetCode-style problems for offline practice.

## Structure

Each problem lives in its own subdirectory:
- `description.md` — problem statement, examples, constraints
- `solution.py` — your solution goes here (fill in the function body)
- `test_solution.py` — pytest test cases that validate your solution

## How to start

### 1. Clone the repository

```bash
git clone https://github.com/NarezIn/local-leet.git
cd local-leet
```

### 2. Create and activate a virtual environment

**macOS / Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

You should see `(.venv)` appear at the start of your terminal prompt once the environment is active.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Pick a problem

Open a problem directory and read its `description.md` before writing any code:

```bash
cd 001_two_sum
```

### 5. Write your solution

Open `solution.py` in your editor. You will find a function with a docstring and a `pass` placeholder — replace `pass` with your implementation:

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    # your code here
    pass
```

### 6. Run the tests

From inside the problem directory:
```bash
pytest test_solution.py -v
```

A failing test looks like this:
```
FAILED test_solution.py::test_example_1 - assert ...
```

A passing test looks like this:
```
PASSED test_solution.py::test_example_1
```

Keep iterating until all tests show `PASSED`.

### 7. Move to the next problem

Once all tests pass, navigate to the next problem and repeat:
```bash
cd ../002_palindrome_number
```

## How to run tests

From within a problem directory:
```
cd 001_two_sum
pytest test_solution.py -v
```

Or run all problems from the root:
```
pytest -v
```

## Problems

| # | Title | Difficulty |
|---|-------|------------|
| 001 | Two Sum | Easy |
| 002 | Palindrome Number | Easy |
| 003 | Valid Parentheses | Easy |
| 004 | Longest Substring Without Repeating Characters | Medium |
| 005 | Longest Palindromic Substring | Medium |
| 006 | Container With Most Water | Medium |
| 007 | 3Sum | Medium |
| 008 | Group Anagrams | Medium |
| 009 | Product of Array Except Self | Medium |
| 010 | Coin Change | Medium |

## Tips

- Read `description.md` carefully before writing any code.
- Try to solve it on your own before looking up hints.
- Run `pytest test_solution.py -v` often to see which cases pass.
- All test files import from `solution.py` in the same directory.
