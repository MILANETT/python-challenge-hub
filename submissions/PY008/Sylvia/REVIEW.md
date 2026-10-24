# PY008 Submission Review — Sylvia

**File reviewed:** `problem8.py`  
**Review status:** Revision recommended; script currently stops before reaching the menu

## What is working well

- `*args` is used with multiple scores, and the function deliberately checks whether any scores were supplied.
- The `**kwargs` function loops through the supplied dictionary, so it can display different keys and values.
- The study-session examples show default values and overridden values using keyword arguments.
- `describe_session(student, /, subject, *, duration)` combines positional-only and keyword-only parameters. The invalid call is commented out and its error is explained.
- `clean_name()` and `make_greeting()` are used together, and `apply_operation()` shows a function being passed as an argument.
- The factorial function has a base case and is tested with zero and positive inputs.

## Corrections and improvements

1. **Fix the call that stops the script.** This line is executed before `main()`:
   `print(apply_operation(make_greeting(clean_name(" sylvia "))))`
   It calls `make_greeting()` immediately and passes its result as the only argument to `apply_operation()`, which requires two arguments. Python raises `TypeError`, so the program never reaches the menu. Pass the function itself as one argument and the value as the other, for example `apply_operation(make_greeting, clean_name(" sylvia "))`.
2. **Return values instead of returning `print()`.** `return print(...)` returns `None`, because `print()` displays text but does not return the displayed string. The outer `print(summarize_scores(...))` therefore prints `None` after the output. Have the function return a useful result and print it at the call site, or print inside the function without wrapping the call in another `print()`.
3. **Include the count and define the empty-score result.** The summary currently reports total and average but not count. With no scores, it prints “No score was supplied” and then reports a total of 0 and average of 0; that makes an empty set look like it has a meaningful average. Return a deliberate result such as count 0 and average `None`.
4. **Add docstrings to every function.** The challenge requires them, but the current functions do not have docstrings. Briefly explain purpose, parameters where useful, and return values.
5. **Strengthen the lambda example.** Sorting numbers with `key=lambda number: number` is effectively the same as sorting them directly, so the lambda adds little value. Use a more meaningful key (for example, sorting study-session tuples by duration) and explain why the short expression fits.
6. **Expand the menu.** The menu has four cases and a default, but it accepts only one choice and then ends. Make it repeat until an explicit exit choice, and include an actual valid/invalid menu test.
7. **Test the higher-order function with two different functions.** The corrected call should pass the function object rather than call it first. Then demonstrate a second function argument so the requirement is unambiguous.

## Commenting feedback

The recursion comment correctly identifies why a base case is necessary. Keep comments focused on the rule or design decision, and add the required function docstrings. Also remove the duplicate `print()` wrappers where the called function already prints.

## Overall assessment

The script demonstrates several key concepts, but the current incorrect higher-order-function call causes a runtime failure before the menu. The main gaps are that failure, the summary's return behavior and missing count, absent docstrings, and the weak lambda demonstration.

**Next step:** Fix the crashing call first, then make the summary return a clear count/average result, add docstrings, and improve the menu and lambda tests. This is feedback on the submitted version, not a grade.
