# PY011 Submission Review — YVONNE

**File reviewed:** `PY011.py`  
**Submission PRs:** #121 (README) and #122 (solution)  
**Review status:** Revision recommended

## What is working well

- The supplied member records are reproduced correctly.
- The final report in Q5 uses a list comprehension for active members, a dictionary comprehension for study hours, a set comprehension for distinct topics, and a generator expression for members with at least 200 study minutes.
- The set explanation correctly identifies that sets prevent duplicate values.
- The second generator in Q4 uses the correct fewer-than-six condition.

## Corrections and improvements

1. **Use the required list comprehensions in Q1.** Lines 31–47 use nested loops and print statements for all three lists. The challenge explicitly asks for list comprehensions. The list comprehension in Q5 does not replace the three separate Q1 tasks; create the three requested lists in Q1 and display them.

2. **Use dictionary comprehensions in Q2 and correct the study-time units.** Lines 53–76 build dictionaries with loops and `update()`, rather than dictionary comprehensions. More importantly, lines 62–67 store raw minutes in `studyTime_dict`, although the task asks for hours. Convert each member's minutes by dividing by 60. The correct dictionary-comprehension approach is already demonstrated later in Q5 at lines 158–161.

3. **Use set comprehensions in Q3.** Lines 83–100 create empty sets and update them in loops. The task specifically asks for set comprehensions. The nested set comprehension in Q5 at lines 165–169 is a suitable pattern to apply to the Q3 topic collection; use a separate set comprehension for the first letters.

4. **Keep the one-at-a-time output tied to the filtered generator.** Lines 108–111 correctly create and consume the generator for members with at least 200 study minutes. Lines 116–123 then create a different generator containing every member and call `next()` on it, so that output does not demonstrate one-at-a-time retrieval from the filtered generator. The earlier `for` loop already processes the filtered generator one value at a time; keep the demonstration focused on that generator. `next()` is not listed among the PY011 topics and is planned for later work.

5. **Complete the exhaustion demonstration.** Lines 135–145 contain only commented-out retrieval attempts. The code does not execute a second retrieval after the fewer-than-six generator has been consumed at lines 130–131. Iterate over that same generator a second time and show that no values are produced. This can be done with a loop; no exception-handling syntax is needed.

6. **Expand the AI note if assistance was used.** Line 106 only says that generator expressions were learned with AI assistance. Briefly describe what the tool helped explain and how you adapted or checked the result, following the group's disclosure guidance.

## Overall assessment

Q5 shows that the core comprehension patterns are understood, and the generator filters are mostly correct. However, Q1–Q3 do not use the specific comprehension types required by those questions, Q2's study-time dictionary contains minutes instead of hours, and Q4's exhaustion demonstration is commented out.

**Next step:** Rework Q1–Q3 using the requested comprehension forms, correct the study-time conversion, and complete Q4's exhaustion demonstration using a second loop over the consumed generator. No `try/except` or `raise` technique is needed for this challenge.
