# PY007 Submission Review — ShaddyMash

**Challenge:** PY007 — Inside and Outside: Understanding Scope  
**Review status:** Reviewed; minor revision recommended

## What you did well

- `G_access()` reads and prints the global `G_variable`.
- `L_access()` demonstrates a local variable, and the commented-out `print(L_variable)` keeps the deliberate error from stopping the program.
- The same-name experiment prints the local value `90` and then the unchanged global value `20`.
- `increase()` correctly uses `global count` and demonstrates two updates.
- Your `try/except UnboundLocalError` experiment keeps the no-`global` error isolated so the rest of the program can continue.
- `design(count, amount)` returns an updated value, and your final output compares it with the original global count.

## Corrections and improvements

1. **Part 1 does not need `global`.** `G_access()` only reads `G_variable`, so the declaration is unnecessary. This is not a correctness bug, but removing it makes the distinction between reading and rebinding easier to learn.
2. **Explain the error in Part 4 more precisely.** The standalone expression `s_count` neither declares the name global nor initializes a local variable. The assignment operation `s_count += 1` causes Python to treat the name as local in that function, and the increment fails because that local value has not yet been initialized.
3. **Remove the unused `U_amount` variable.** It is assigned inside `design()` but never used. Returning the updated count directly is clearer.
4. **Use more descriptive names and consistent spacing.** Names such as `session_count`, `read_global_count()`, and `increase_count()` would be easier to understand than abbreviations like `G_variable` and `s_cope`. This is a style improvement, not a functional failure.
5. **Make the final explanation explicit.** State that `design()` computes and returns a new value without changing the global `count`; the caller receives that result in `result`.

## Commenting feedback

Your comments are helpful because they explain the intention of each section. The strongest next improvement is to explain the cause of the error using Python's local-name assignment rule, rather than only saying that the code fails without `global`.

## Overall assessment

The submission covers all five required parts and demonstrates the expected behavior. The main opportunity is to simplify unused code and sharpen the explanation of why `UnboundLocalError` occurs.

**Next step:** Make the small cleanup changes, refine the Part 4 explanation, and rerun the script.
