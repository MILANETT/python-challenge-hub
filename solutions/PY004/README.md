# PY004 — Student Performance Analyzer: Solution Approach

This guide describes how to organize the reference solution for the analyzer. Read it alongside `solution.py`.

## 1. Plan the information to track

The program needs to process multiple students and then produce a class summary. Keep a clear plan for:

- Each student's name and mark.
- The number of students processed.
- A count for each grade.
- A running total of marks.
- The highest and lowest marks seen so far.

Initialize counters and the running total before processing students. Initialize the highest and lowest values from the first valid mark, or use another approach that correctly handles the first mark. Avoid arbitrary starting values that could distort the result.

## 2. Repeat for each student

Ask how many students will be entered, then use a loop to process that number of students.

For each student:
1. Read their name.
2. Ask for a mark.
3. Check that the mark is between 0 and 100.
4. If invalid, ask again rather than including it in the statistics.
5. Determine the grade.
6. Display the student's result.
7. Update the appropriate counters and summary values.

The grade conditions should be checked in descending bands: A (70–100), B (60–69), C (50–59), D (40–49), and E (below 40). Validate the upper and lower limits before assigning a grade.

## 3. Validate before counting

An invalid mark must not affect the grade counts, total, highest mark, lowest mark, or average. Only update the summary after a valid mark has been obtained.

A loop is useful for repeating the prompt until a valid mark is entered. Be careful not to update any counters before validation succeeds.

## 4. Update the class summary

For each valid mark:

- Increase the counter for the assigned grade.
- Add the mark to the running total.
- Update the highest mark if the current mark is larger.
- Update the lowest mark if the current mark is smaller.

After all students have been processed, calculate the average by dividing the running total by the number of valid marks. The design should ensure the program does not divide by zero if no valid marks were processed.

## 5. Use control flow for a reason

This challenge practises conditions, loops, counters, accumulators, and loop-control statements. Each construct should have a clear role in the algorithm. In particular, avoid adding a nested loop, `break`, `continue`, or `pass` where it makes the program less understandable; be prepared to explain the purpose of each construct required by the challenge.

## 6. Test the boundaries

Test marks at 40, 50, 60, 70, and 100, as well as a value below 0 and above 100. Check both the individual grade and the final counts. Include marks from several grade bands to test the summary.

## Concepts used

- `if`, `elif`, and `else`
- `for` and `while` loops
- Comparisons and nested conditions
- Input validation
- Counters and accumulators
- Running highest and lowest values
- `break`, `continue`, and `pass` where appropriate
- Boundary testing

## Common mistakes to watch for

- Assigning the wrong grade at a boundary.
- Counting a mark before validating it.
- Updating the total but forgetting a grade counter.
- Calculating the average using the number requested rather than the number of valid marks, if those counts differ.
- Forgetting to initialize highest and lowest correctly.
- Making the algorithm more complicated just to include a particular statement.

**Key idea:** Separate the job into stages—validate, classify, update, and summarize—so each part can be checked independently.