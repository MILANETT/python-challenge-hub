# PY010 Submission Review — MIYARA

**File reviewed:** `PY0010.py`  
**Submission PR:** #115  
**Review status:** Minor revisions recommended

## What is working well

- Q1 correctly advances the while-loop index and provides a working for-loop alternative. The two examples of mistakes that can skip or repeat records are relevant.
- The Q2 function checks the sentinel before skipping non-positive values, uses `continue` and `break` correctly, and returns the valid-item count.
- The nested-dictionary loops correctly display student details, identify active students, find students taking Python, and count students by department.
- `calculate_average` handles empty input without using `sum()`. `build_report` returns a string and supports different keyword details, including no additional details.
- The name-processing pipeline and higher-order function are correctly composed. Both lambda sorts use the required ordering, and the recursive function has a base case and a step towards it.
- The required PY010 test cases for `find_first_positive` are present. The AI-assisted recursion explanation is disclosed in the code.
- The solution stays within the PY001–PY008 progression; no later-phase processing tools are introduced.

## Corrections and improvements

1. **Enforce positional-only parameters in Q4(C).** Line 200 defines `register_session(session_name, duration, *, instructor, room="Lab 1")`. The `*` correctly makes `instructor` and `room` keyword-only, but the required `/` is missing. As written, `session_name` and `duration` can still be passed by keyword, so the first example labelled invalid would actually be accepted. Use `def register_session(session_name, duration, /, *, instructor, room="Lab 1")`.

2. **Correct the Q7 membership explanation.** Line 333 combines the meanings of `in` and `not in` in one unclear statement. Explain them separately: `in` is true when a value is present; `not in` is true when it is absent. The identity explanation and the practical `value is None` example are good.

3. **Make the Q8 return explicit.** Lines 338–344 still contain the original print-based ending. When no positive number is found, the function prints a message and implicitly returns `None`. The comment at line 354 correctly suggests an explicit `return None`, but that change has not been made. Add the explicit return and remove the print so the function communicates its result through its return value. The three requested list tests at lines 346–348 are already present.

4. **Show the recursion base-case test.** The function at lines 293–296 supports non-negative inputs and uses `n <= 0` as its base case. The tests at lines 299–301 cover 1, 5, and 10, but not 0. Add a call with `recursive_sum(0)` so the base case itself is demonstrated.

5. **Remove the repeated Q7 setup.** The `first`, `second`, `third`, and `target` variables are initialized twice at lines 309–318. This does not change the result, but one setup is sufficient and makes the section easier to follow.

6. **Include the final reflection.** The challenge asks for a short reflection on the most difficult concept, a mistake you can now recognise, what you would check first when a loop or recursive function fails, and what still needs practice. That reflection is not present in the submitted file; add it as a short comment section or in the README.

## Overall assessment

This is a strong and mostly complete PY010 attempt. The control-flow, nested-dictionary, flexible-report, composition, sorting, and recursion work is generally sound. The main functional requirement gap is the missing positional-only marker in Q4(C); Q8 also needs the explicit return-based correction rather than leaving the original print-based ending in place.

**Next step:** Add the `/` to `register_session`, make Q8 return `None` explicitly when no positive value exists, correct the Q7 explanation, and finish the base-case test and reflection. This is feedback on the submitted version, not a grade.
