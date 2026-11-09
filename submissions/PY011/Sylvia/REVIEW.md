# PY011 Submission Review — Sylvia

**File reviewed:** `problem11.py`  
**Submission PR:** #119  
**Review status:** Minor improvements recommended

## What is working well

- Q1 correctly uses list comprehensions for all three requested member lists.
- Q2 uses dictionary comprehensions correctly, including the conversion from study minutes to hours.
- Q3 uses nested set-comprehension logic to collect distinct topics and a separate set comprehension for initials.
- Q4 creates both required generators with the correct conditions. The loops consume the generated names one at a time.
- The second pass over `names6` at lines 53–55 produces no names, which is a valid demonstration that the generator has already been exhausted.
- Q5 reuses the earlier results and creates a fresh generator for the final report.

## Corrections and improvements

1. **Clarify the set explanation.** Lines 42–43 refer to getting the “unique names of the topic.” The intended point is that a set stores unique **topic values**, so revise the wording to make that distinction clear.

2. **Make the exhaustion demonstration easier to interpret.** The second loop at lines 53–55 is appropriate and does not need exception handling. Add a short comment after it explaining that no values appear because the generator was already consumed by the first loop.

3. **Improve naming and spacing.** Names such as `names_7_` and `fLetter` could be more descriptive (for example, `active_member_names` and `first_letters`). Consistent spaces around assignments and comparisons would also improve readability.

4. **Add an AI disclosure only if applicable.** No AI-use note appears in the submission. If AI assistance was used, document what it helped with and how you verified or adapted the result, following the group's policy.

## Overall assessment

The solution meets the substantive PY011 requirements. The comprehensions, study-hour conversion, topic collection, generator conditions, and final report are correct. The generator-exhaustion demonstration is already present through a second loop, so no exception-handling technique or later-phase tool is needed.

**Next step:** Clarify the set explanation and add a short comment to the existing exhaustion demonstration. The remaining suggestions are readability improvements rather than functional corrections.
