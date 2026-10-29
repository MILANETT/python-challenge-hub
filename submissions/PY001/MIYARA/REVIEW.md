# PY001 Submission Review — MIYARA

## What is working well
- The manual loops for highest and lowest marks are correct.
- Your running-total loop adds each mark and calculates an average using the number of marks.
- The output labels make it clear which result is being shown.

## Improvements
1. The marks list is recreated several times even though its contents do not change. Define it once at the top and reuse it; this avoids duplication and makes future edits safer.
2. You calculate the average twice: first with sum(marks) / len(marks), then again with a manual running total. If the task is practising accumulators, keep the manual version and remove the duplicate calculation, or clearly explain why you are comparing both methods.
3. Your code assumes the list is non-empty. That is fine for the supplied data, but a reusable version should check before dividing by its length.
4. Use consistent descriptive names such as total_marks and average_mark.

## Priority
The calculations are correct. Focus on removing repeated setup and showing one clear approach to each required operation.
