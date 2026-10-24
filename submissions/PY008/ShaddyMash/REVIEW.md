# PY008 Submission Review — ShaddyMash

**File reviewed:** `Problem8.py`  
**Review status:** Strong overall; targeted refinements recommended

## What is working well

- `summarize_scores()` handles empty input before division and returns both the count and average. Returning `(0, None)` for no scores is a deliberate, usable choice.
- `student_report()` accepts different keyword details and returns a readable report string.
- The study-session function has a default parameter, and the menu's test option demonstrates default and overridden values.
- `study_plan(subject, /, *, minutes)` demonstrates positional-only and keyword-only rules together. Both invalid-call examples are isolated in comments and explain the expected errors.
- The two conversion functions are composed in `add_break(to_minutes(2))`.
- `apply_function()` accepts a function argument and is tested with two different functions.
- The lambda is used as a sorting key, and the comment explains why a short anonymous function fits.
- The recursive factorial has a base case and a recursive step; the tests include zero and a positive number.
- The menu has multiple choices, an invalid-choice fallback, and a test option covering many of the requirements.

## Corrections and improvements

1. **Add the missing menu/function docstrings.** The challenge asks for a docstring for each function. Several helpers have docstrings, but the menu loop is at module level and there is no documented `main()` function. Move the loop into `main()`, give it a docstring, and protect execution with `if __name__ == "__main__":`.
2. **Guard factorial at the function boundary.** The menu restricts values to 0–10, but the recursive function itself does not reject a negative argument. Calling `factorial(-1)` directly would recurse until Python stops it. Add a negative-input guard or clearly enforce the precondition in the function.
3. **Return the study-session report if you want it to be reusable.** `study_session()` prints directly. That is valid for a display helper, but returning a formatted string would make it consistent with `student_report()` and easier to test without capturing terminal output.
4. **Make the lambda test evidence explicit.** The lambda sorting test is present under the menu's “Tests” option. Consider including a brief expected-order comment so a learner can compare actual and expected output.
5. **Keep comments focused on why.** Most comments are useful, but a few narrate the next line (for example, announcing that the program asks for a choice). Prefer comments that explain a design decision or the behavior an experiment is intended to show.

## Overall assessment

This is the most complete submission of the group in terms of coverage and runnable menu structure. The core requirements are represented, including returned summaries, flexible keyword reports, combined parameter restrictions, composition, higher-order functions, lambda, recursion, and menu fallback. The main refinements are adding a documented entry point, guarding the recursive function itself, and polishing a few comments.

**Next step:** Wrap the menu in a documented `main()`, add a negative-factorial guard, and make the lambda test's expected behavior easy to verify. This is feedback on the submitted version, not a grade.
