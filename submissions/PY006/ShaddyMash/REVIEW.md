# PY006 Code Review — ShaddyMash

**File reviewed:** `py006.py`  
**Focus:** function reuse, input handling, scope, testing, and keeping the solution maintainable.

## What is working well

- `calculate_average()` is focused and reusable.
- You check names and mark ranges, and you test several cases including zero marks.
- The scope experiments are labelled and supported by comments.
- The parameter-and-return example clearly shows that the original value remains unchanged while the function returns a new result.
- The reflection records mistakes and explains how you corrected them.

## Suggestions to improve

1. **Reduce repeated code.** The mark-validation loop is repeated for each of the six marks. That makes the program long and increases the chance of inconsistent fixes. Once comfortable with the current concepts, look for a small reusable input function or a loop over the subject prompts.
2. **Avoid bare `except:`.** It catches far more than invalid numeric input. When exception handling is part of your taught material, catch the specific `ValueError` raised by converting invalid text to a number. If `try/except` has not been covered yet, treat this as an extension rather than a required PY006 concept.
3. **Simplify the name loop.** The `continue` after a valid name is unnecessary: the loop will check its condition again naturally. Also consider whether a name containing only spaces should count as empty.
4. **Make the local-scope experiment more precise.** Your test correctly triggers an error when it tries to use local `x` outside the function. The exception handler lets the rest of the file continue, but catching all exceptions can hide unrelated bugs. Keep the experiment isolated and explain the specific error you expect.
5. **Add the required manual comparison.** The four direct function tests are useful. Also record at least one manual calculation and actual output, including a fractional average and three identical marks.
6. **Check the length against the learning goal.** Most of the file is devoted to repeating input validation. Prioritize the required function and scope concepts first; extra validation is useful, but it should not bury the main learning objective.
7. **AI-use disclosure.** If you used AI after the initial 30 minutes, add the required comment explaining where it helped and what you changed or learned. I can't infer AI use from the code itself.

## Suggested next step

Keep the strong tests and scope notes, then shorten the repeated input-validation sections and make error handling more specific when you're ready to use it.

## Review note

This is feedback on the submitted version, not a score. Keep your own implementation and update it as you work through the suggestions.
