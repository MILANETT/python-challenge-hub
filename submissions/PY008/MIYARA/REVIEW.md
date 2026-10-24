# PY008 Submission Review — MIYARA

**File reviewed:** `PY008.py`  
**Review status:** Revision recommended

## What is working well

- `*args` is used to receive any number of scores, and the loop accumulates the total without using the built-in `sum()`.
- The `**kwargs` example accepts named details and is called with two different sets of names.
- The default-argument examples show a default day, keyword arguments, and an overridden default.
- The commented experiment for keyword-only parameters records the expected `TypeError` and explains the rule.
- Function composition and a higher-order function are both demonstrated, and the lambda comment gives a reasonable explanation for using a short expression.
- The factorial function has a base case and is tested with both zero and a positive number.
- The menu uses `match/case`, includes a fallback case, and calls reusable functions.

## Corrections and improvements

1. **Handle empty scores before dividing.** `avg = total/count` runs before the `count == 0` check, so calling `summarize_scores()` raises `ZeroDivisionError`. Check for no scores first, then decide what result to return.
2. **Return the summary.** The challenge asks for a useful summary including count and average. At present, the function prints values but returns `None`. Returning a value makes the function easier to reuse from other code and from the menu.
3. **Return the student report.** `stu_details()` prints a fixed pair of fields rather than returning a readable report. Consider returning a formatted string built from the supplied keyword details so different details can be represented.
4. **Demonstrate both parameter rules in one signature.** The challenge asks for a small function showing positional-only and keyword-only parameters together. Your examples demonstrate each rule separately; combine `/` and `*` in one function signature and test a valid call.
5. **Add docstrings and useful design comments.** Most functions have no docstrings, and the composition functions could use a brief explanation of how the returned value from one function becomes the input to the next.
6. **Keep the script safe to import.** `run_menu()` is called at module level, so importing this file immediately starts asking for input. Put that call under `if __name__ == "__main__":`.
7. **Validate factorial input at the function boundary or clearly document its precondition.** The menu checks for negative values, but calling `factorial(-1)` directly will recurse indefinitely. The function itself should reject negative input or explicitly state the precondition.

## Commenting feedback

Your comments often explain the observed rule rather than merely narrating the syntax, especially in the parameter experiment. Keep that approach, but add docstrings and make the comments match the actual control flow. The empty-score comment should not imply the division is safe when the division currently happens first.

## Overall assessment

Most required topics are represented, and the composition, higher-order function, lambda, recursion, and menu are promising. The main correctness issue is the empty-score crash; the largest requirement gaps are returning useful results, combining both parameter restrictions in one function, and adding docstrings.

**Next step:** Fix the empty-input path, return results from the summary/report functions, and make the combined parameter-rule example explicit. This is feedback on the submitted version, not a grade.
