# PY006 Code Review — Sylvia

**Files reviewed:** `problem6.py` and `README.md`  
**Focus:** function results, variable scope, program flow, and completion of the challenge requirements.

## What is working well

- `calculate_average()` uses parameters, arithmetic, and `return` correctly.
- The loop collects information for two students, and the average is formatted to two decimal places.
- The fruit example is a clear demonstration that a local variable can share a name with a global variable without changing the global value.
- You recorded a real debugging mistake and attempted to compare functions with and without `return`.

## Important fixes

1. **Calculate each average once.** Inside the student loop, `calculate_average(sub1, sub2, sub3)` is called and its result discarded, then called a second time for printing. Store the first result in a variable and use that value in the report.
2. **Pass the name into `displayName()`.** At present, the function relies on the global `name` left over from the loop, so it displays the last student's name. A function that accepts the name as a parameter is more reusable and avoids this hidden dependency.
3. **Avoid relying on global marks in `calculate()`.** The function reads `sub1` and `sub2` from the surrounding program. It will only work after those variables have been assigned, and it ignores the third mark. Pass the values as arguments instead.
4. **Clarify the `product()` experiment.** The function calculates `a * b` but has no `return`, so `print(product(...))` displays `None`. That is a useful experiment, but label it explicitly as an intentional demonstration and compare it with the version that returns the product.
5. **Complete the global-modification investigation.** The fruit example tests a local/global name collision, but it does not test changing a global variable from inside a function using `global`. Add that as a separate experiment.
6. **Keep the challenge focused.** The default parameters in `_Product(a=15, b=13)` are a preview of a later topic, not a PY006 requirement. It's fine to be curious, but make sure the core PY006 tasks are complete first.
7. **Improve the README's accuracy.** It says the code tests changing a global variable inside a function, but the shown fruit experiment only creates a local variable with the same name. Update the explanation to match the actual code.
8. **Finish the testing evidence.** Add the requested zero-mark, identical-mark, and fractional-average cases, and document the expected and actual results.

## Suggested next step

Fix the hidden global dependencies first, store the average once, then finish the global-modification and testing sections. These changes will make the program easier to understand and reuse.

## Review note

This is feedback on the submitted version, not a score. Keep your own implementation and update it as you work through the suggestions.
