# PY007 Submission Review — YVONNE

**Challenge:** PY007 — Inside and Outside: Understanding Scope  
**Review status:** Reviewed; minor revision recommended

## What you did well

- `add_NOs()` correctly reads the global values `x` and `y`.
- The local-access experiment demonstrates that `a` is not available as a module-level name after being created inside `subtract_NOs()`; the failing line is safely commented out.
- The same-name experiment compares the global product `9 * 3 = 27` with the local product `4 * 2 = 8`.
- `counter()` correctly increments the global `count` three times using `global count`.
- `update_counter(count, amount)` returns a new value without modifying the global variable inside the function.
- The accompanying README gives a useful plain-language summary of your approach.

## Corrections and improvements

1. **Explain the global access rule.** `add_NOs()` only reads `x` and `y`, so it does not need a `global` declaration. Reading a global name and assigning to a global name are different operations.
2. **Explain the no-`global` error by its cause.** When a function assigns to `count`, Python treats that name as local within the function unless it is declared global. The increment tries to read the local value before it has been initialized, producing `UnboundLocalError`.
3. **Clarify the final comparison.** `update_counter()` itself does not change the global `count`. In your script, however, the caller assigns each returned value back to `count` at module level, which does update the global name. This is an important distinction and a good point to explain in your comments.
4. **Polish spelling and naming.** Correct typos such as `varible` and `udate_counter`, and keep function names consistent (for example, `update_counter`).
5. **Keep the error demonstration easy to follow.** The traceback comments are useful evidence, but add a short explanation directly beside them so the reader understands the underlying rule.

## Commenting feedback

Your section headings make the script easy to navigate, and the final comment is a good start. Be especially clear about the difference between a function returning a value and the caller assigning that value to a global name.

## Overall assessment

All five required experiments are represented, and the code demonstrates the main scope behaviors correctly. Your parameter-and-return example is useful; explain the caller's assignment carefully so it does not appear that the function itself mutates global state.

**Next step:** Refine the comments around global access and the final comparison, correct the typos, and rerun the script.
