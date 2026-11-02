# PY009 Submission Review — Sylvia

**File reviewed:** `bossbattle.py`  
**Review status:** Revision recommended

## What is working well

- The starting inventory and three existing requests are represented using lists and dictionaries.
- The helper functions separate equipment lookup, request lookup, issuing, returning, cancellation, and reporting.
- The issue operation checks the request status and available quantity before changing inventory.
- Return and cancellation operations check the current status, preventing a returned request from being returned again and preventing an issued request from being cancelled.
- The report displays total, issued, and available quantities, as well as pending requests.
- Comments explain the purpose of several operations and validation checks.

## Corrections and improvements

1. **Stay within the PY009 concepts boundary.** Lines 14–17, 70, and 84–87 use `any()` with generator expressions. These belong to the next phase and are not listed in `challenges/PY009/CONCEPTS.md` (PY001–PY008). Replace them with loops or other approaches already covered. The use of `.casefold()` at lines 15, 85, and 116 should also be checked against what has actually been taught; it is not listed in the PY009 concepts reference.
2. **Fix quantity validation for requests.** Lines 93–98 convert the input directly with `int()`, so non-numeric text will stop the program. Also, when the quantity is zero or negative, line 98 updates `inventoryQuantity` instead of `quantity`. The while condition therefore keeps checking the original invalid value and can loop forever. Read the text first, validate it before conversion, and update the same quantity variable when asking again.
3. **Validate the extra inventory inputs too.** Lines 1, 23, and 40 convert user input directly to integers. Non-numeric input will cause the program to stop. The additional inventory feature also accepts a blank equipment name at line 12. These are extra features beyond the core requirements, but their inputs still need to be checked if you keep them.
4. **Reject blank request IDs.** Line 67 checks whether an ID already exists, but does not reject an empty ID. Add a blank check before adding the request.
5. **Correct the menu's exit option.** The menu displays option 5 as Exit (line 227), but selecting it calls `find_request(requestID)` at line 239 before leaving. If no new requests were entered, `requestID` has never been assigned and this causes a `NameError`; otherwise, the program unexpectedly looks up the last ID entered. The option 6 branch is not shown in the menu and does not exit the loop. Make option 5 print the goodbye message and break.
6. **Normalize equipment names consistently.** The first equipment prompts at lines 12 and 83 call `.title()` without first removing surrounding whitespace. A name with leading or trailing spaces can be stored or rejected inconsistently. Strip the input before comparing or storing it.
7. **Keep interactive execution separate from the functions.** The input prompts and loops run at module level, and `inventoryMenu()` is called directly at line 246. Importing the file therefore starts the interactive program. If you intend to test or reuse the functions by importing the file, move the setup and menu into `main()` and use the main guard, provided that convention has been covered.

## Overall assessment

The issuing, returning, and cancellation functions show a good understanding of request-status transitions. However, the current version has important input-validation and menu-flow defects, and it uses Phase 5 iteration tools before the group has covered them. These issues should be corrected before treating the solution as complete.

**Next step:** First remove the out-of-scope `any()`/generator-expression usage, fix the quantity-validation loop and exit option, then test blank IDs, invalid quantities, repeated returns, and stock-limit cases. This is feedback on the submitted version, not a grade.
