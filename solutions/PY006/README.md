# PY006 — Reusable Functions: Solution Approach

This guide explains the reference solution using the concepts intended for PY006. Read it alongside `solution.py`.

## 1. Write the calculation once

Define `calculate_average` with three parameters. Inside the function, calculate the average using arithmetic and return the result.

The function should focus on one job: calculating an average. It should not ask for input or print the student's report. Separating calculation from interaction makes the function easier to reuse.

## 2. Call the same function for both students

For each student, collect a name and three marks. Convert the entered marks to numeric values, then pass those values as arguments to `calculate_average`.

Store the returned average in a variable and display it with the student's name. The same function works for both students because its inputs are supplied at the time of each call.

## 3. Understand `return` and `print()`

`print()` displays information to the screen. `return` sends a result back to the code that called the function.

Because the average is returned, the calling code can store it, format it, compare it, or use it in another calculation. If a function reaches its end without returning a value, the result of that call is `None`.

## 4. Investigate scope with small experiments

The scope examples are separate from the student calculator so they cannot interfere with its results.

- **Global variable:** A variable created outside a function can be read inside the function when the function does not create a local variable with the same name.
- **Local variable:** A variable created inside a function is available within that function. Trying to use it directly outside its scope produces a `NameError`.
- **Same name in both places:** Assigning to a name inside a function creates a local variable in that function. The global variable with the same name remains unchanged.
- **Parameters and return values:** A function can receive a value, calculate a result, and return it without modifying a global variable.

To observe the local-variable error without adding exception handling, leave the failing access as a commented line and uncomment it only for that experiment. Run the program to observe the error, then comment it again before running the full script.

This version intentionally avoids `try`/`except` and the `global` keyword so the core solution stays within the intended PY006 concepts. Modifying global variables can be explored separately when that syntax has been taught.

## 5. Test the calculator

Test different marks for the two students. Include a mark of zero, three identical marks, and marks that produce a fractional average. Check each result with a manual calculation.

## Concepts used

- `def` and function calls
- Parameters and arguments
- `return` and `print()`
- Variables and assignment
- Numeric type conversion
- Local and global scope
- f-strings and two-decimal formatting
- Testing and debugging

## Common mistakes to watch for

- Printing the average inside the function instead of returning it.
- Forgetting to store or use the returned value.
- Passing fewer or more than three arguments.
- Leaving entered marks as strings.
- Expecting a local variable to be available outside its function.
- Assuming that a local variable with the same name changes the global variable.
- Adding advanced syntax before it has been covered in the learning roadmap.

**Key idea:** A reusable function receives information through parameters, performs one focused task, and returns a result that the rest of the program can use.