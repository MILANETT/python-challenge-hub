# PY007 Submission Review — MILANETT

**Challenge:** PY007 — Inside and Outside: Understanding Scope  
**Review status:** Reviewed; revision recommended

## What you did well

- `read_globalSession()` correctly reads the global counter without changing it.
- `display_my_var()` demonstrates a local variable, and the attempted outside access is commented out so the script remains runnable.
- The `rate` experiment shows that the local value `"30%"` and global value `"20%"` remain distinct.
- `add_completed_sessions()` correctly declares `global completed_sessions` and increments the global counter twice.
- `mod_completed_sessions()` correctly calculates and returns an updated value using parameters without changing the global counter.

## Corrections and improvements

1. **Clarify scope versus lifetime.** The comment says the local variable “dies immediately the function finishes executing.” More precisely, the local name is normally no longer accessible after the function call ends. The object it referred to may continue to exist if other references still point to it.
2. **Explain `global` precisely.** Rather than saying it makes the function “know that it is a global variable,” explain that `global completed_sessions` tells Python that assignments to this name inside the function refer to the module-level name.
3. **Strengthen Part 5.** Your call `mod_completed_sessions(0, 5)` followed by printing `completed_sessions` is a useful demonstration that the global remains unchanged. For a stronger test, also pass the current counter and an increment, store the returned value in a separate variable, and show that the global counter is still unchanged.
4. **Polish names and comments.** Use consistent naming such as `read_completed_sessions()` rather than `read_globalSession()`. Explain that the global `rate` retains its original value because the local assignment inside `display_rate()` binds a different local name.

## Commenting feedback

You have comments beside the deliberate error and the observed outputs, which is a good habit. The next step is to explain the underlying rule more precisely and avoid wording that could teach an inaccurate model of variable lifetime.

## Overall assessment

All five experiments are present and the main code behavior is correct. The key improvements are more precise explanations of local scope and the `global` declaration, plus a slightly stronger Part 5 test.

**Next step:** Refine the comments, strengthen the parameter-and-return experiment, and rerun the script.
