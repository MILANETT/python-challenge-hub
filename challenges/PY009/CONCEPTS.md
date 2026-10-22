# PY009 — Concepts Reference (PY001–PY008)

This file defines the programming knowledge you may rely on for PY009. It is a reference boundary, not a list of techniques you must use in the solution. Choose concepts based on the problem, and do not add a technique just to demonstrate that you know it.

## PY001 — Values, variables, lists, and basic calculations

- Variables and assignment
- Integer and other basic values
- Lists and accessing list elements
- Iterating through a list
- Comparisons and arithmetic
- Tracking a running total or count
- Finding a highest or lowest value through basic logic rather than relying on built-ins introduced as prohibited in the challenge

## PY002 — Types, conversions, and operators

- Basic data types and checking values
- Converting between strings and numeric values
- Arithmetic, comparison, logical, assignment, membership, and identity operators
- Combining conditions to make decisions
- Handling optional values such as `None` where appropriate

## PY003 — Input, output, strings, and debugging

- `input()` and `print()`
- String formatting and manipulation
- Converting user input into an appropriate type
- Reading error messages and investigating unexpected behavior
- Using comments to record observations and explain fixes
- Testing with different inputs

## PY004 — Conditions and loops

- `if`, `elif`, and `else`
- `for` and `while` loops
- Nested decisions and repeated operations
- Comparisons and logical conditions
- Controlling program flow
- Checking a condition before performing an operation

## PY005 — Data structures and organization

- Lists, indexing, slicing, and list methods
- Tuples and their immutability
- Sets, uniqueness, membership, and set operations
- Dictionaries, keys, values, and dictionary methods
- Nested data structures
- Mutability and immutability
- References, assignment, and copying, including shallow and deep copies
- Choosing a suitable structure for the information and operations required

## PY006 — Functions and reusable logic

- Defining and calling functions with `def`
- Parameters and arguments
- Returning values with `return` versus displaying output with `print()`
- Reusing a function with different inputs
- Keeping calculations separate from reporting
- Testing and debugging functions

## PY007 — Scope

- Local and global variables
- Accessing variables inside and outside functions
- Local and global variables with the same name
- The `global` keyword and its effect
- Passing information through parameters and returning results instead of relying unnecessarily on global state

## PY008 — Flexible and composable functions

- Default and keyword arguments
- Arbitrary positional arguments (`*args`)
- Arbitrary keyword arguments (`**kwargs`)
- Positional-only parameters (`/`) and keyword-only parameters (`*`)
- Function docstrings and useful explanatory comments
- Function composition
- Higher-order functions that accept another function
- Lambda expressions for small operations
- Recursion, base cases, and recursive cases
- `match/case` selection, including a default case (Python 3.10+)

## Boundaries for this challenge

Stay within the concepts above. In particular, PY009 does not require:

- Classes or object-oriented programming
- Reading or writing files, databases, or other persistent storage
- External libraries or packages
- Exception handling with `try/except`
- Modules or concepts taught after PY008

For quantity input, validate the text before converting it to an integer. For example, the string method `.isdigit()` can help determine whether the input contains digits; you must still check that the resulting quantity is greater than zero.

You are not expected to use every concept listed here. The challenge assesses your ability to select and combine appropriate tools to solve an unfamiliar problem.
