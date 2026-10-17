# PY006 Code Review — MIYARA

**File reviewed:** `PY006.py`  
**Focus:** correctness, naming, scope experiments, testing, and readability.

## What is working well

- `calculate_avg()` receives three marks and returns the average.
- Student details and averages are stored together as tuples in a list, then displayed with two-decimal formatting.
- The voter example demonstrates reading a global variable, and the local-variable and same-name experiments are useful.
- You included two concrete debugging examples and explained why those errors occurred.
- You compare a global-state function with a parameter-based function that returns a result.

## Suggestions to improve

1. **Avoid replacing the student list.** You first use `students` for the list of records, then later assign `students = 3` for the global-variable experiment. That replaces the list with an integer. Give the experiment a distinct name, such as `student_count`, so each variable keeps one meaning.
2. **Rename the function `sum()`.** `sum` is already the name of Python's built-in summation function. Defining your own function with that name shadows it and can cause confusing behaviour later. Choose a name that describes this experiment instead.
3. **Make the prompts friendlier.** `range(2)` starts at zero, so the prompts currently say “student0” and “student1.” Display `i + 1` in the prompt so they read “student 1” and “student 2.”
4. **Complete the testing section.** Add explicit calculator tests for a zero mark, identical marks, and a fractional average. Compare the results with manual calculations.
5. **Show the global-assignment contrast clearly.** You document the `UnboundLocalError` caused by assigning without `global`, then demonstrate the successful version. Keep these as two clearly labelled, separate experiments and state why the first fails.
6. **Improve spacing and names.** For example, use consistent spaces after commas and around operators, and keep function names descriptive. This will make your reasoning easier to follow.

## Suggested next step

Rename the two conflicting identifiers, improve the prompts, and add the missing test cases. Your scope experiments cover many of the required ideas; the main improvements are clearer naming and more systematic testing.

## Review note

This is feedback on the submitted version, not a score. Keep your own implementation and update it as you work through the suggestions.
