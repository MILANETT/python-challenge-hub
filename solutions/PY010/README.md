# PY010 — Reference Solution

This folder contains a complete implementation for the PY010 refinement challenge.

## Run it

From the repository root, use Python 3.10 or newer:

    python solutions/PY010/solution.py

The implementation uses built-in Python features and the concepts covered in the group's Phase 0–4 progression. It does not use `try`, `except`, or `raise`.

## Design notes

- **Question 1:** The while-loop increments its index after printing each name. The for-loop version processes each item directly.
- **Question 2:** The sentinel check comes before the non-positive check so that `-999` stops processing. Other zero and negative values are skipped. The function returns the number of positive values printed.
- **Question 3:** Two nested loops navigate departments and their student dictionaries. The functions use the dictionary's current contents, so additional departments and students are processed without rewriting the loops.
- **Question 4:** `calculate_average(*args)` handles an empty argument collection and calculates the total manually. `build_report(name, **kwargs)` accepts flexible named details. `register_session()` uses positional-only and keyword-only parameters exactly as required.
- **Question 5:** The name-processing functions each perform one operation and return a value. `make_clean_greeting()` composes them in order. `apply_operation()` demonstrates passing a function as an argument.
- **Question 6:** The lambda expressions provide sorting keys. `recursive_sum()` uses zero as its base case and reduces the input by one on each call.
- **Question 7:** Equality compares list contents; identity checks whether two names refer to the same object. The two separately created lists are equal but not identical.
- **Question 8:** The revised function returns the first positive value and explicitly returns `None` when no positive value exists, including for an empty list.

## Important learning points

- A sentinel must be checked before other rules that might skip it.
- `break` ends a loop, `continue` skips to the next iteration, and `return` ends the function.
- Nested dictionaries require navigating each level to reach individual student records.
- A function should return a result when its caller needs to use that result; printing is not a substitute for returning.
- Recursive functions need a base case and a step that moves towards it.
- Equality and identity answer different questions.

This is one valid implementation. Alternative solutions are welcome when they satisfy the challenge requirements and remain readable.
