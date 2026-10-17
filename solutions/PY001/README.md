# PY001 — Variables + Lists: Solution Approach

This guide explains the reasoning behind the reference solution. Read it alongside `solution.py`.

## 1. Start with the first mark

The list already contains all the marks:

```python
marks = [72, 45, 89, 63, 51, 94, 38]
```

Use the first item as the starting value for both the highest and lowest marks. This is safer than starting either variable at `0` or an arbitrary large number: the starting values come from the actual data.

## 2. Visit each mark

Use a loop to examine the marks one at a time.

- If the current mark is greater than the highest mark recorded so far, update the highest mark.
- If the current mark is less than the lowest mark recorded so far, update the lowest mark.
- Add the current mark to a running total.

This pattern is called **tracking a running result**. Each new value can improve the current result.

## 3. Calculate the average

Once every mark has been processed, divide the running total by the number of marks.

`average = total / len(marks)`

The length is used because it tells us how many marks are in the list. The solution deliberately avoids `sum()`, `max()`, and `min()` to practise the underlying logic.

## 4. Display the results

Print the highest mark, lowest mark, and average with clear labels. Formatting the average to two decimal places makes the result easy to read.

## Concepts used

- Lists and indexing
- Variables and assignment
- `for` loops
- Comparisons and `if` statements
- Accumulating a total
- Arithmetic and `len()`

## Common mistakes to watch for

- Initializing the highest or lowest value incorrectly.
- Forgetting to update the running total inside the loop.
- Dividing by a hard-coded number instead of the number of marks.
- Dividing before the loop has processed every mark.
- Using a prohibited built-in function.

## Test your reasoning

Try a list where all values are equal, then one where the first value is the highest and another where the last value is the lowest. The same approach should still work.

**Key idea:** Process the data systematically and keep track of what you have learned from each value.