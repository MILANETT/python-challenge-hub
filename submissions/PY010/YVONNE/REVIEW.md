# PY010 Submission Review — YVONNE

**File reviewed:** `PY010.py`  
**Submission PRs:** #113 (README) and #114 (solution)  
**Review status:** Revision recommended

## What is working well

- The while-loop advances its index correctly, and the for-loop version processes each student.
- The nested-dictionary work correctly identifies active students, finds students taking Python, and counts students by department.
- `calculate_average` uses `*args` and returns `None` for empty input. `register_session` correctly uses positional-only and keyword-only parameters.
- The name-processing functions are composed in the right order, and `apply_operation` correctly accepts a function. The alphabetical sort and recursive structure are also present.
- The submission stays within the PY001–PY008 concepts expected for PY010; no later-phase processing tools are needed.

## Corrections and improvements

1. **Complete Q1(d).** Lines 16–17 describe only one mistake (failing to increment the index). The question asks for two different mistakes. Add another distinct example, such as incrementing by 2 and skipping records, or resetting the index and repeating records.

2. **Repair the transaction function.** Lines 45–52 contain the main Q2 issue:
   - The parameter `amount` is ignored; the loop iterates over the global `amounts` list at line 46.
   - The `amount <= 0` check at lines 47–48 runs before the sentinel check at lines 50–51. Since `-999` is negative, it is skipped and never stops the loop, so 90 and 150 are processed incorrectly.
   - The function prints amounts but does not return the required count.
   
   Iterate over the function argument, check for `-999` first, skip other non-positive values, increment the count for valid amounts, and return that count.

3. **Finish Q3's requested output and explanation.** In lines 89–98, the department, ID, and name are printed on separate lines. Print the three fields together for each student so their relationship is clear. The Q3(e) explanation is also missing after the department-count loop (lines 122–128); explain that the outer dictionary gives department keys and inner dictionaries, not each student's individual fields.

4. **Implement the required report function.** Lines 153–159 define `student_details` instead of `build_report`. The function prints fixed `dept` and `avg` entries, rather than accepting arbitrary named details and returning a report string. It also cannot handle a call with no extra details. Implement `build_report(name, **kwargs)`, return the completed string, and test it both with and without extra details.

5. **Fix the greeting separator.** Line 194 joins `"Hello"`, an empty string, and the name, producing output such as `HelloaMINA wanjiku`. Include a space (and suitable punctuation) between the greeting and the name. The overall composition order at lines 200–201 is correct.

6. **Correct the score sort and test the recursion base case.** Line 231 sorts scores in ascending order because it omits `reverse=True`, despite the task and comment requiring highest-to-lowest order. Add `reverse=True`. The recursive function at lines 242–246 uses 0 as its base case, but the tests at lines 248–250 do not test 0; include that base-case test and state the intended input range.

7. **Complete Q7 and Q8 explanations/tests.**
   - Q7's identity explanation at lines 274–276 restates the general idea but does not give a concrete practical situation. For example, explain checking whether a function result `is None`.
   - Q8 defines `find_first_positive(*numbers)` twice (lines 295–311), whereas the challenge asks for a function that receives a list. Keep one definition with the expected list parameter. The final definition is tested only with a positive result at line 312; run the required positive, no-positive, and empty-list tests against that final definition. The explanations for the no-positive case and for the difference between `return`, `continue`, and `print` are also missing (lines 288–293).

8. **Add the final reflection.** The challenge asks for a short reflection on the most difficult concept, a mistake you can now recognise, what you would check first when a loop or recursive function fails, and what still needs practice. It is not included in the submitted file; it can be added as a short comment section or in the README.

## Overall assessment

There is a good foundation in the nested-dictionary work and several of the function exercises. However, Q2, Q4(B), and Q6(A) have substantive requirement or correctness gaps, and Q8's final function does not use the requested list interface or complete the required tests and explanations.

**Next step:** Prioritise the transaction function, report function, descending score sort, and final Q8 implementation. Then complete the missing explanations and reflection. This is feedback on the submitted version, not a grade.
