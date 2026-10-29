# PY003 Submission Review — MIYARA

## What is working well
- You collect all four profile fields with input().
- String methods demonstrate capitalization changes, and the report includes useful derived information such as the name length and first/last characters.
- The report is separated into clear sections.

## Improvements
1. A blank name makes name[0] raise an IndexError. Check that the stripped name is not empty before accessing its first or last character, or ask the user to enter it again.
2. Apply strip() to every text input before formatting. Course and favourite language currently keep surrounding spaces, and university is uppercased without trimming.
3. Prefer stripping before applying title() or upper(), so the normalization sequence is consistent and easier to read.
4. Add spaces after labels in the formatted output, such as “Name: Amina”, to improve readability.
5. Keep the prompt capitalization and output labels consistent; this is a small presentation improvement rather than a logic issue.

## Priority
The main flow is clear. Handle an empty name first because it is the input edge case that can crash the program, then normalize all fields consistently.
