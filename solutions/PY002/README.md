# PY002 — Student Performance Checker: Solution Approach

This guide explains the design of the reference solution. Read it alongside `solution.py`.

## 1. Inspect the starting data

The age and marks are supplied as strings:

```python
age = "20"
marks = ["72", "45", "89", "63", "51"]
```

Strings are text, even when they look like numbers. Convert the age to an integer and each mark to a numeric value before performing arithmetic.

Keep in mind that converting a value for calculation does not change the original string automatically. That matters later when checking whether the original list contains the string `"89"`.

## 2. Calculate the total and average

Build a running total by adding each converted mark. Divide the total by the number of marks to calculate the average. Do not use `sum()`.

The expected total is `320`, and the average is `64.00`.

## 3. Use operators for checks

Create Boolean results for the required checks:

- Compare the age with `18` to check adulthood.
- Compare the average with `50` and `70` for the performance thresholds.
- Use `and` to decide whether the student passed: the average must be at least 50 **and** the student must have submitted the work.
- Use `in` to check membership in the original string list.
- Use `is None` to check whether the bonus has no value yet.

Membership is a good example of why data types matter: `"89"` is a string, whereas `89` is an integer. They are not the same value for a membership check.

## 4. Handle the bonus

If the bonus is `None`, assign it the value `5`. Then use an augmented assignment operator such as `+=` to add it to the average.

The final average is `69.00`. Keep the original average and final average conceptually distinct: the bonus changes the reported final result, not the original marks.

## 5. Build the report from variables

Print the report using the values your program calculated. Do not type the expected results directly into the report. Use two decimal places for the averages.

## Concepts used

- `str`, `int`, `float`, `bool`, and `None`
- Type conversion
- Arithmetic and comparison operators
- Logical operator `and`
- Assignment and augmented assignment
- Membership: `in`
- Identity: `is`
- Formatted output

## Common mistakes to watch for

- Trying to add numeric strings without converting them.
- Checking for integer `89` in a list that still contains string `"89"`.
- Confusing `is None` with ordinary value equality.
- Calculating the pass result without checking submission status.
- Printing hard-coded results instead of calculated variables.

**Key idea:** Choose operations based on the kind of value you actually have, not how that value looks when printed.