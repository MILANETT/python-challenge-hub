# PY007 — Inside and Outside: Solution Approach

This README explains the reference implementation in [`solution.py`](solution.py). It follows the five experiments in the PY007 challenge and keeps the deliberately failing examples isolated so the main program runs normally.

## Run the solution

From the repository root, run:

```bash
python solutions/PY007/solution.py
```

The script prints the current session count, demonstrates local scope and same-name variables, increments the global counter twice, and compares that approach with returning an updated value.

## 1. Read a global variable

`completed_sessions` is defined outside all functions. `show_completed_sessions()` can read it without declaring it `global`, because the function does not assign a new value to that name.

**Key distinction:** reading a global name is allowed; assigning to a global name from inside a function requires a `global` declaration when the function intends to rebind that name.

## 2. Create a local variable

`demonstrate_local_scope()` creates `local_note`. It is available inside that function, but it is not a module-level name.

The attempted outside access is left commented out:

```python
# print(local_note)
```

Uncommenting it at module level causes a `NameError`, because no variable named `local_note` exists in that scope. It is commented out in the normal run so the remaining experiments can execute.

## 3. Use the same name in two scopes

The global `study_goal` and the local `study_goal` inside `demonstrate_same_name()` are different bindings. Assigning the local name does not replace the global value. The program prints the global value before and after the function call so this is easy to verify.

## 4. Modify global state with `global`

`increment_completed_sessions()` declares:

```python
global completed_sessions
```

That declaration tells Python that the assignment targets the module-level name. Calling the function twice changes the global count from `0` to `1`, then to `2`.

### Experiment: remove the declaration

If you remove or comment out the `global completed_sessions` line and call the function, Python treats `completed_sessions` as a local name because the function assigns to it. The augmented assignment also tries to read that local name before it has a value, so Python raises `UnboundLocalError`.

Restore the declaration after the experiment. The reference solution leaves this failing variant as an explanation rather than making the full program stop.

## 5. Compare parameters and return values

`updated_count(count, amount)` receives values through parameters and returns `count + amount`. With `trial_count = 10` and `amount = 3`, it returns `13` while leaving `trial_count` unchanged and not touching `completed_sessions`.

This is generally easier to test and reuse than changing global state: the inputs and result are visible at the function call, and the function does not silently alter a separate variable.

## Commenting choices

The comments focus on **why** an experiment behaves a certain way and how to reproduce it. They avoid narrating obvious syntax line by line. The docstrings briefly describe each function's purpose.

For your own work, comments should be accurate, useful, and placed beside the behavior they explain. Update them whenever the code changes.

## Quick verification checklist

- [ ] The global counter is initially `0`.
- [ ] Reading the counter from a function does not change it.
- [ ] The local-variable access experiment is understood; its failing line stays commented during the normal run.
- [ ] The local `study_goal` does not change the global `study_goal`.
- [ ] The global counter reaches `1` and then `2` after two increment calls.
- [ ] Removing `global` produces the expected `UnboundLocalError` experiment.
- [ ] `updated_count(10, 3)` returns `13`, while the original count remains `10`.

## Concepts used

- Function definitions and calls
- Global and local scope
- Name shadowing
- The `global` keyword
- Parameters and arguments
- Return values
- Docstrings, comments, and isolated experiments

**Main takeaway:** prefer passing information through parameters and returning results when practical. Use global state only when there is a clear reason to share and modify that state.
