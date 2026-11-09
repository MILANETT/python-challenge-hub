# PY011 Submission Review — MIYARA

**File reviewed:** `PY011.py`  
**Submission PR:** #120  
**Review status:** Minor revisions recommended

## What is working well

- Q1's list comprehensions correctly apply all three conditions.
- Q2's dictionary comprehensions correctly map names to challenge counts, convert study minutes to hours, and filter members with at least seven completed challenges.
- Q3 correctly uses set comprehensions for distinct topics and name initials, and the explanation identifies the duplicate-removal benefit of sets.
- Q4 creates the required generators. The first generator uses the correct inclusive `>= 200` condition and is consumed one value at a time with a loop.
- Q5 includes all four requested report elements and uses a generator expression for the final member list.

## Corrections and improvements

1. **Correct the second generator's recorded output.** Lines 86–89 filter for members with fewer than six completed challenges. The actual names produced are **Brian** and **David**. The output comment at lines 91–97 incorrectly includes Amina, Carol, and Esther; it also shows a generator-object line that the code does not print. Update or remove this stale output.

2. **Demonstrate exhaustion explicitly.** The `chall_six` generator is consumed at lines 86–89, but the code does not attempt another iteration afterward. Add a second loop over the same generator and show that it produces no values. This is enough to demonstrate exhaustion; exception handling is not required.

3. **Make the AI note more informative.** Line 53 only says `Used Ai`. If AI assistance was used, briefly state what it helped explain and how you checked or adapted the result, in line with the group's disclosure guidance.

## Overall assessment

This is a good, largely complete PY011 solution. The list, dictionary, and set comprehensions are correct, and the report is complete. The main outstanding requirement is the explicit generator-exhaustion demonstration; the second generator's recorded output also needs correction.

**Next step:** Correct the Q4 output comments and add a second pass over the exhausted generator. No `try/except` or `raise` technique is needed for this challenge.
