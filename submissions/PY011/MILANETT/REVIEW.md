# PY011 Submission Review — MILANETT

**File reviewed:** `PY011.py`  
**Submission PR:** #118  
**Review status:** Minor revisions recommended

## What is working well

- Q1 uses list comprehensions correctly for the three requested member lists.
- Q2 correctly builds the challenge-count dictionary, converts minutes to hours, and filters members with at least seven completed challenges.
- Q3 uses nested set-comprehension logic to flatten the members' topic lists and correctly collects name initials. The explanation of why sets remove duplicates is clear.
- Q5 brings the required datasets together in a readable report and creates a fresh generator for the final list of members.
- The AI-assistance comments identify where help was used.

## Corrections and improvements

1. **Use the inclusive threshold in Q4.** Line 52 uses `> 200`, but the challenge asks for members who studied for **at least** 200 minutes, so use `>= 200`. The supplied records do not contain exactly 200 minutes, which is why the current output appears correct; a boundary test would expose the difference.

2. **Keep Q4 within the listed PY011 concepts.** Lines 57–59 use `next()`, which is not among the concepts listed for PY011 and is planned for later work. A `for` loop already retrieves generator values one at a time, so it is sufficient for this challenge.

3. **Actually demonstrate generator exhaustion.** The attempted retrieval at line 61 is commented out, so it never runs. Also, the second generator at lines 65–66 is created but never consumed. Consume that second generator with a loop, then iterate over it again to show that it produces no further values. This demonstrates exhaustion without requiring exception-handling syntax.

4. **Tidy the formatting.** Add consistent spaces around assignment and comparison operators, and keep comments separated from code. This will make the otherwise correct comprehensions easier to scan.

## Overall assessment

The comprehension work in Q1–Q3 and the integrated report in Q5 are strong and meet the main requirements. The remaining gaps are concentrated in Q4: one boundary condition is incorrect, the exhaustion demonstration is commented out, and the second generator is unused.

**Next step:** Correct the Q4 threshold, use loops for one-at-a-time consumption, and demonstrate that a consumed generator produces no further values. No `try/except` or `raise` technique is needed for this challenge.
