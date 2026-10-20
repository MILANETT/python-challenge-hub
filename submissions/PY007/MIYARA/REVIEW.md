# PY007 Submission Review — MIYARA

**Challenge:** PY007 — Inside and Outside: Understanding Scope  
**Review status:** Reviewed; revision recommended

## What you did well

- `read_std()` reads the global `std_sess` without changing it.
- `local_var()` demonstrates a local variable and your comments correctly identify the expected `NameError` if `age` is accessed outside the function.
- The same-name experiment clearly shows `"Miyara"` inside the function and `"Monicah"` outside it.
- `inc_global()` correctly declares `global count` and increments the global count from 7 to 8 and then 9.
- `receive(count, amount)` returns an updated value without changing the global `count`.

## Corrections to make

1. **Correct the explanation in Part D.** You wrote that a function can read a global variable but cannot modify it. That is too broad: a function can rebind a module-level name when it declares that name with `global`. Without that declaration, an assignment such as `count += 1` makes `count` local in that function and raises `UnboundLocalError` because the local value is read before being initialized.
2. **Use “shadows” rather than “overrides” in Part C.** The local `name` shadows the global name inside `lname()`; it does not replace the global variable.
3. **Strengthen the Part E comparison.** Explain that `receive()` calculates and returns a value using its parameters. It does not itself change the global `count`; the caller decides what to do with the returned value.
4. Fix the small typo in `"Updted count"` if you want the displayed output to be polished.

## Commenting feedback

Your output comments are useful, and you explain the observed behavior rather than only pasting code. Focus on making the explanations technically precise: describe the Python rule that causes the behavior, not just the result.

## Overall assessment

All five required experiments are present and the code logic is broadly correct. The main revision is conceptual accuracy in the explanation of `global` and clearer language about local names shadowing global names.

**Next step:** Update the comments in Parts C, D, and E, then run the script again to confirm the examples still behave as expected.
