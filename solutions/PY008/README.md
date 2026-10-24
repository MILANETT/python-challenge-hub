# PY008 — Reference Solution and Approach

This folder contains the reference implementation in [`solution.py`](solution.py). It demonstrates the required concepts in one runnable Personal Study Toolkit while keeping each function focused.

## Run it

From the repository root, use Python 3.10 or newer:

```bash
python solutions/PY008/solution.py
```

Choose a menu option and follow the prompts. Choose `0` to exit.

## How the implementation meets the challenge

### 1. Flexible parameters: `*args` and `**kwargs`

- `summarize_scores(*scores)` accepts any number of positional scores, counts them, and calculates the average with a loop rather than the built-in `sum()`.
- With no scores, it returns a count of `0` and an average of `None`. This avoids division by zero and does not pretend that an empty collection has an average.
- `build_student_report(**details)` accepts a flexible set of named details and returns a formatted string. It does not assume every caller will supply the same fixed keys.

Examples to try in a Python shell:

```python
summarize_scores(50, 70, 90)
# {'count': 3, 'average': 70.0}

summarize_scores()
# {'count': 0, 'average': None}

print(build_student_report(name="Amina", course="Data Science"))
print(build_student_report(name="Brian", year=2, subject="Python"))
```

### 2. Default and keyword arguments

`format_session_report(student, duration=30, subject="Python")` has two defaults. Omitting them uses the defaults; passing `duration` or `subject` replaces them.

```python
format_session_report("Amina")
format_session_report("Brian", duration=50, subject="Statistics")
format_session_report("Chris", subject="Geography")
```

### 3. Positional-only and keyword-only parameters

`describe_session(student, /, subject, *, duration)` uses `/` to make `student` positional-only and `*` to make `duration` keyword-only. `subject` can be passed positionally or by keyword.

```python
describe_session("Amina", "Python", duration=45)

# Invalid: student is positional-only.
# describe_session(student="Amina", subject="Python", duration=45)

# Invalid: duration is keyword-only.
# describe_session("Amina", "Python", 45)
```

The invalid calls remain comments so the reference script can run normally.

### 4. Docstrings and explanatory comments

Every function has a docstring describing its purpose. Comments explain non-obvious design choices, such as why the empty-score average is `None`, why the factorial needs a base case, and why a function parameter makes `apply_operation()` a higher-order function.

### 5. Function composition and higher-order functions

`make_greeting()` calls `clean_name()` and uses its returned value to build the greeting. This is composition: one function's result is used by another operation.

`apply_operation(value, operation)` accepts a function object and calls it. Try both:

```python
apply_operation(4, square)  # 16
apply_operation(4, cube)    # 64
```

The function is reusable because it does not need to know the internal details of the operation it receives.

### 6. Lambda expression

Menu option 7 sorts a list of study-session tuples by duration:

```python
sorted_sessions = sorted(sessions, key=lambda session: session[1])
```

The lambda is a short, one-use key function. A named function would also work, but would add a separate definition for this simple operation.

### 7. Recursion

`factorial()` returns `1` at the base case `number == 0`. Otherwise, it returns `number * factorial(number - 1)`, moving towards the base case. It rejects negative values rather than recursing indefinitely.

Try `factorial(0)`, `factorial(1)`, and `factorial(5)`; expected results are `1`, `1`, and `120`.

### 8. Menu with `match/case`

The menu has more than four options, routes each choice to a function, repeats until the user exits, and includes a default case for unrecognised input.

## Verification checklist

- [ ] Multiple scores produce the expected count and average.
- [ ] No scores return count `0` and average `None`.
- [ ] Student reports accept different keyword details.
- [ ] Default values are used and can be overridden.
- [ ] The positional-only and keyword-only rules are understood.
- [ ] Composition returns a cleaned greeting.
- [ ] The higher-order function is tested with both `square` and `cube`.
- [ ] Lambda sorting orders sessions by duration.
- [ ] Factorial tests include `0` and an ordinary positive input.
- [ ] A valid menu choice and an invalid choice are tried.

**Learning note:** This is one valid reference implementation, not the only correct solution. Choose techniques because they make the program clearer and more reliable, not merely to demonstrate every concept.
