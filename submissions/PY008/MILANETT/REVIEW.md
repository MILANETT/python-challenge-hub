# PY008 Submission Review — MILANETT

**File reviewed:** `PY008.py`  
**Review status:** Revision recommended

## What is working well

- The score function uses `*scores` and manually accumulates the total rather than using `sum()`.
- The empty-score case is handled without division by zero.
- The default-argument examples show both defaults and overridden values.
- `describe_session(student, /, subject, *, duration)` correctly combines positional-only and keyword-only parameters, and the valid call demonstrates the intended syntax.
- `clean_name()` and `make_greeting()` are connected, and the factorial function has a base case and recursive case.
- The menu uses `match/case`, calls functions, and includes a fallback for an unknown choice.
- Comments record several observed outputs, and the functions have docstrings, although some still contain starter-template wording.

## Corrections and improvements

1. **Return a summary rather than only printing it.** The challenge asks `summarize_scores()` to return a useful summary including count and average. It currently prints those values and returns `None`. Return a value (for example, a dictionary with `count` and `average`) and let the menu decide how to display it.
2. **Return the student report.** `build_student_report()` prints four hard-coded fields and raises `KeyError` if any are missing. A report built from the supplied `**details` should be returned as a readable string, and the function should have a deliberate behavior for an empty or partial set of details.
3. **Make the positional-only experiment demonstrate the intended error.** The commented call currently places a positional argument after a keyword argument, which is a syntax error unrelated to the positional-only rule. Use a syntactically valid call that supplies `student` by keyword, then explain that Python rejects it because `student` is positional-only.
4. **Make the higher-order function accept a function.** `apply_operation(value, operation)` currently receives strings such as `"square_value"` and selects a branch. That is ordinary conditional dispatch, not a higher-order function. Change it to accept a callable (for example, `apply_operation(3, cube)`) and invoke the supplied function.
5. **Complete Part 6 with a meaningful lambda example.** The lambda expressions are nested inside the operation function, while the dedicated lambda section is empty. Add a clear standalone use, such as sorting study-session records by duration with a lambda key, and explain why that short expression is appropriate.
6. **Return the greeting and make composition explicit.** `make_greeting()` prints instead of returning a greeting, and it calls `clean_name()` internally. Returning the greeting makes the composed result reusable and easier to test.
7. **Connect the menu to more of the toolkit.** The menu currently does not offer the score summary or student report, and it does not expose a lambda-based operation. Add choices that let users access the required functions through the menu.
8. **Improve docstrings and comments.** Remove the remaining “TODO: complete” wording from completed functions, use consistent spacing around operators and after commas, and explain the design decision rather than narrating each line. Also validate negative factorial input before calling the recursive function.

## Commenting feedback

You have recorded examples and explained the base case, which is a useful start. The positional-only comment currently describes the function's intent but attributes the wrong error to the experiment. Comments should describe what the exact code demonstrates, and expected outputs should be checked against actual behavior.

## Overall assessment

The default parameters, combined parameter restrictions, and factorial are on the right track. The main requirements still needing work are returning values, a true function-accepting higher-order function, a dedicated meaningful lambda example, and a menu that exposes the broader toolkit.

**Next step:** Refactor the summary/report/greeting functions to return values, make `apply_operation` accept a function object, then connect those pieces through the menu. This is feedback on the submitted version, not a grade.
