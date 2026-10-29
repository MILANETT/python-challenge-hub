# PY002 Submission Review — MILANETT

## What is working well
- You convert the age and mark strings to integers before doing arithmetic.
- The running total and average are calculated correctly for the supplied marks.
- The code demonstrates comparisons, Boolean conditions, membership checks, None handling, and a final average with a bonus.
- The pass condition correctly combines an average threshold with the submission status.

## Improvements
1. The variable atLeast70avg is calculated but never used or reported. Either include it in the report or remove it if it is not required.
2. alreadySubmitted simply copies has_submitted into another Boolean variable. Since has_submitted is already Boolean, the extra variable is unnecessary unless you are deliberately demonstrating a concept.
3. Consider printing the average to a consistent number of decimal places and using consistent snake_case names such as average_mark and final_average.
4. You test for the string "89" in marks before converting the list. That is correct for the current list of strings; if you use intMarks instead, search for the integer 89, not the string "89".
5. The current data contains five marks, so division by zero is not an issue here. If the marks list becomes user-supplied, validate that it is not empty before calculating an average.

## Priority
Your core calculations and operator demonstrations are sound. Tidy the redundant/unused variables and keep the data type consistent with the list being searched.
