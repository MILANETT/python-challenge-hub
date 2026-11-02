# PY007 Submission Review — Sylvia

**File reviewed:** `problem7.py`  
**Review status:** Small revision recommended

## What is working well

- `displaySessionCount()` reads the global session counter and returns its value without changing it.
- `addNo()` creates a local variable, and the commented-out `print(add)` line records the attempted access from outside the function.
- `displayCarDetails()` creates a local `car` with the same name as the global variable. Printing both values demonstrates that the local assignment does not replace the global value.
- `increaseCount()` uses `global` to update the session counter, and the two calls show the count increasing repeatedly.
- `increaseSession()` demonstrates the alternative parameter-and-return design. The comparison comment correctly identifies why this approach is easier to reuse for different counts.

## Corrections and improvements

1. **Display the local variable inside its function.** Part 2 asks you to create a local variable and display it inside the function. At present, `addNo()` returns `add`, and the caller displays the returned value at line 20, but the function itself does not display the local variable. Add a `print(add)` inside `addNo()`; you can keep the return as well to show both behaviours.
2. **Avoid relying on global inputs in the local-variable experiment.** Lines 9–14 make `addNo()` read `num1` and `num2` from global scope. Passing them as parameters would make the function's inputs explicit while keeping `add` as the local variable being investigated.
3. **Use the starter's session-counter variable.** The starter provides `completed_sessions = 0`, while this submission creates `sessionCount = 1`. The scope experiment still works, but using the supplied variable would keep the solution aligned with the task setup.
4. **Make the same-name explanation more precise.** In the README, the statement that you tried changing the global variable using the function is a little unclear. Explain that assigning `car` inside `displayCarDetails()` creates a local variable and leaves the global `car` unchanged. The two printed values in the code demonstrate this.
5. **Clarify the missing-`global` observation.** Your comment at lines 39–40 has the right idea. You can make it more precise: without `global`, Python treats `sessionCount` as local inside the function, and `sessionCount += 1` tries to use that local variable before it has been assigned.

## Overall assessment

The main scope behaviours are represented correctly, and the comparison between modifying global state and returning an updated value is useful. The main requirement gap is that the local variable is returned to the caller but is not displayed inside its own function as requested.

**Next step:** Add the display inside `addNo()`, then refine the short explanations of local shadowing and the `global` keyword. This is feedback on the submitted version, not a grade.
