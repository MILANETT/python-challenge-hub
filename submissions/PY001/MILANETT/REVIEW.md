# PY001 Submission Review — MILANETT

## What is working well
- You find the highest and lowest marks by starting from the first value and comparing each item.
- The running-total loop correctly accumulates all marks, and dividing by the list length produces the average.
- Formatting the average to two decimal places makes the report easier to read.

## Improvements
1. Rename the variables max and min. These names shadow Python's built-in functions, which can cause confusion if you later need to call them.
2. Consider descriptive names such as highest_mark, lowest_mark, and total_marks. The code becomes easier to understand without changing the algorithm.
3. Your approach assumes marks is non-empty because it reads marks[0] and divides by len(marks). The supplied data is non-empty, so this works for the challenge; if you turn it into a reusable program, handle an empty list before accessing the first element or calculating the average.
4. Add a brief comment explaining why the first mark is used as the initial highest/lowest candidate.

## Priority
Keep the correct loop logic and improve naming. Your solution demonstrates the intended manual maximum, minimum, and average calculations clearly.
