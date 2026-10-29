# PY004 Submission Review — MIYARA

## What is working well
- You use a for loop to collect a chosen number of student records and a nested while loop to repeat mark entry until the mark is in range.
- The grade boundaries are mutually exclusive and correctly classify marks into A–E.
- The parallel names, marks, and grades lists are populated together, and the final report uses matching indices.
- Accumulators track the total and grade counts, and the highest/lowest calculations use loops.

## Important improvements
1. If the user enters 0 for the number of students, marks[0] raises an IndexError and the average calculation would divide by zero. Reject non-positive student counts or handle the empty case before calculating statistics.
2. The prompt says marks should be between 1 and 100, but the condition accepts 0. Decide whether 0 is a valid mark and make the prompt and validation agree.
3. Non-numeric input for the student count or mark causes ValueError because int() is called directly. Add input validation appropriate to the concepts allowed for the challenge.
4. Consider using a single grade-count dictionary later, but the individual counters are understandable at this stage and are not inherently wrong.
5. Add a space after report labels and format the average to a consistent number of decimal places.

## Priority
The loop and grade logic are well structured. First protect the program against an empty class and make the allowed mark range consistent with the prompt.
