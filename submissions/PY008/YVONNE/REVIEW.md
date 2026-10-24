# PY008 Submission Review — YVONNE

**File reviewed:** `PY008.py`  
**Review status:** Revision recommended

## What is working well

- The default-argument examples show both an unchanged default and an overridden value.
- `POSITIONALvsKEYWORD()` combines positional-only, flexible, and keyword-only parameters in one signature, and the commented experiment attempts an invalid call.
- The two sorting functions are passed into `output()`, which is a clear higher-order-function demonstration.
- The lambda expression is used for a short filtering operation, and the comment explains the general idea of an anonymous function.
- `sum_Recursion()` solves a defined problem (sum of digits), uses a base case, and includes an explanation of the recursive step.
- The `match/case` statement includes a fallback case and calls earlier functions.

## Corrections and improvements

1. **Handle an empty `*args` call.** `average` is assigned only inside the loop. If `summarize_scores()` receives no scores, returning `average` raises `UnboundLocalError`. Add an explicit empty-input path before calculating the average.
2. **Include the count and return a useful summary.** The challenge asks for the count and average. The current function returns only the average, and it does not demonstrate the empty case. Return a consistent result for both empty and non-empty input.
3. **Avoid shadowing the built-in `sum`.** Naming a variable `sum` hides Python's built-in function in that scope. Use a name such as `total` instead.
4. **Make the student report use the supplied details.** `student_Details()` receives `**details`, but calculates the displayed average from hard-coded scores instead of the supplied details. Keep the report tied to its arguments and avoid hard-coding an unrelated calculation inside it.
5. **Add actual docstrings to every function.** The section labelled “DOCSTRINGS AND USEFUL COMMENTS” only prints a heading. A heading is not a substitute for docstrings in the functions themselves. Add a short purpose-focused docstring to each function.
6. **Demonstrate function composition explicitly.** `ascend_NOs()` and `descend_NO()` are separate sorting operations, and `output()` passes a function in as an argument. That demonstrates a higher-order function, but the submission does not clearly compose the returned result of one function into another. Add two small functions and a nested call that shows this data flow.
7. **Improve the menu.** It asks for one choice only, so it is not a repeated menu. The fallback message says “1-3” although there is also a choice 4. Put the menu in a loop with an exit option and make the fallback message match the actual choices.
8. **Add a direct empty-score test and test the menu fallback.** These would expose the main current failure and verify the menu's invalid-choice behavior.

## Commenting feedback

You explain several parameter rules and the recursive digit-sum calculation well. Some comments contain spelling errors or describe a concept only generally; revise them so they explain the specific design or observed behavior. Avoid including personal registration details in a public repository unless they are genuinely necessary for the challenge.

## Overall assessment

The parameter syntax, higher-order function, lambda, and recursive digit-sum example show good engagement with the topics. The main issues are the missing empty-input behavior, the incomplete summary result, the hard-coded report calculation, missing docstrings, and a menu that runs only once.

**Next step:** Make the summary consistent for zero or more scores, return the count and average, add docstrings, and complete the composition and menu tests. This is feedback on the submitted version, not a grade.
