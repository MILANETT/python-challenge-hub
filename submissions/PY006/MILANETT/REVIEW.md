# PY006 Code Review — MILANETT

**Files reviewed:** `PY006.py` and the accompanying approach notes  
**Focus:** correctness, functions, scope understanding, testing, and readability.

## What is working well

- `calculate_average()` has one clear job, receives three marks as parameters, and returns the result.
- The same function is reused for both students, and the list of dictionaries keeps each student's name beside their average.
- The global-read, local-variable, and same-name experiments are separated from the calculator.
- The comments record actual observations and include a debugging reflection.

## Suggestions to improve

1. **Finish the global-modification experiment.** The commented `x += 1` example correctly illustrates why assignment inside a function is treated as local by default, but the challenge also asks you to test the successful version using `global`. Add a separate, clearly labelled experiment that uses it.
2. **Correct one conclusion.** “A local variable cannot be modified inside a function” is not correct. A function can create and change its own local variable. The error occurs because `x += 1` tries to read the local `x` before it has a value. Compare this with using `global x`, or with receiving a value as a parameter and returning the updated result.
3. **Expand the tests.** The two sample runs include zero marks, which is good. Also test three identical marks and marks that produce a fractional average, and record expected versus actual output.
4. **Tighten the reflection on `return`.** Explain that `return` sends a value back to the calling code; it does not itself display a message to the user. `print()` displays output.
5. **Polish formatting.** Add spaces after commas in function parameters and arguments, and keep comments aligned consistently. `name.capitalize()` is optional; be aware it can change a person's intended capitalization.

## Suggested next step

Complete the successful global-modification experiment, correct the local-variable explanation, and add the two missing test cases. The core calculator is already structured sensibly.

## Review note

This is feedback on the submitted version, not a score. Keep your own implementation and update it as you work through the suggestions.
