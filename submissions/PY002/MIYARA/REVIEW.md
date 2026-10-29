# PY002 Submission Review — MIYARA

## What is working well
- You inspect the original types and demonstrate converting the age and marks from strings to integers.
- The total and average calculations are correct for the supplied data.
- You demonstrate comparisons, Boolean logic, membership operators, and the None value.
- The pass expression correctly requires both an average of at least 50 and a submitted assignment.

## Improvements
1. The messages say “greater than 50” and “greater than 70”, but the conditions use >=, which means “greater than or equal to”. Update the wording or use the strict > operator if that is what you intend.
2. The average is calculated using the running total, which is useful practice. Keep the variable names consistent and descriptive (for example, total_marks and average_mark).
3. Your membership tests correctly search the original string list. If you later search the converted integer list, search for 89 and 100 as integers rather than strings.
4. You set bonus to 0 when it is None and then add 5. This works; a short comment could explain that None means no bonus value was supplied, so the program applies the default bonus.
5. As with any average calculation, a future version that accepts an arbitrary list should check that the list is not empty before dividing.

## Priority
The program covers the intended types and operators well. The main correction is aligning the comparison messages with the actual >= conditions.
