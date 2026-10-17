# PY006 Code Review — YVONNE

**Files reviewed:** `YvonnePY006.py`, `YvonnePY006b.py`, and `YvonnePY006scopes.py`  
**Focus:** reusable functions, variable scope, naming, and alignment with the current learning phase.

## What is working well

- The average calculation adds the marks and divides by the number of marks.
- The student details are collected interactively, and the average is formatted in the first version.
- The scope file compares local values with global values and includes a parameter-based subtraction function.
- You have made separate attempts at the calculator and scope experiments, which makes it easier to identify what each file is practising.

## Suggestions for `YvonnePY006.py`

1. **Use only the function features currently being studied.** `*marks` (arbitrary positional arguments) is a later topic in the roadmap. For PY006, use the three explicit mark parameters so the function matches the challenge requirement and reinforces the concept being taught.
2. **Do not name a variable `sum`.** It shadows Python's built-in `sum()`. Use a name such as `total` instead.
3. **Define functions outside the student loop.** The functions do not need to be recreated for each student. Define them once, then call them for each student's data.
4. **Avoid hidden dependencies.** `display_StudentDetails()` reads `student_name` and the mark variables from the surrounding scope. Passing the information it needs as arguments would make the function easier to reuse and test.
5. **Add the missing reflection and tests.** Explain `return` versus `print()`, and test zero marks, identical marks, and a fractional average.

## Suggestions for `YvonnePY006b.py`

1. **Reduce the global variables.** Declaring each student's name and marks as global makes the functions depend on shared state. Prefer collecting the values locally and passing them to the calculation and display functions.
2. **Use the returned average.** The call to `calculate_avg(...)` inside the loop currently discards its result; `display_StudentDetails()` calculates it again. Calculate once, store the result, and display it.
3. **Format the average consistently.** Use two decimal places as required by the challenge.
4. **Keep the function parameters explicit for PY006.** The `*marks` feature belongs to a later challenge, so it is better to practise three named parameters here.

## Suggestions for `YvonnePY006scopes.py`

1. **The local/global name experiment is useful.** `add_No()` uses local `x` and `y`, while the expressions outside the function use the global values.
2. **Correct the final comment.** Assigning `x = 30` and `y = 10` at the top level changes the global variables directly; it does not demonstrate changing them from inside a function.
3. **Add the missing modification experiment.** Try reassigning a global from inside a function without `global`, observe the local-variable error, then compare it with a separate version using `global`.
4. **Explain the parameter example.** `subtract_No(100, 30)` is a good example: `x` and `y` are parameters in the definition, while `100` and `30` are arguments in the call.

## Suggested next step

Start with `YvonnePY006.py`: use explicit parameters, move function definitions outside the loop, and avoid global dependencies. Then use the scopes file to complete the global-modification experiment and correct its final comment.

## Review note

This is feedback on the submitted versions, not a score. Keep your own implementation and update it as you work through the suggestions.
