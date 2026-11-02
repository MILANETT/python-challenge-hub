# PY009 Submission Review — ShaddyMash

**File reviewed:** `Problem9.py`  
**Review status:** Minor improvements recommended

## What is working well

- The inventory dictionary stores total stock, while each request keeps its requester, item, quantity, and status together.
- `available()` calculates stock from requests currently marked `Issued`. This avoids maintaining a second available-stock value that could become inconsistent.
- `register_request()` rejects blank or duplicate IDs, blank requester names, unknown equipment, and non-positive or non-numeric quantities before storing a request.
- Issue, return, and cancellation operations check the current request status before changing it. This prevents issuing the same request twice, returning it twice, or cancelling an issued request.
- The issue operation checks available stock before changing the request to `Issued`.
- The report displays total, available, and issued quantities, pending requests, and all recorded requests with their statuses.
- The menu supports repeated operations and includes a fallback for invalid choices.

## Corrections and improvements

1. **Include the requested testing evidence.** The submission README currently contains only the heading “My approach.” PY009 asks for evidence of normal operations and rejected actions. Add a concise record of tests for registering a request, issuing within available stock, rejecting an oversized issue, returning once, rejecting a second return, cancelling a pending request, and rejecting invalid input.
2. **Check the quantity-validation method against the concepts reference.** Line 62 uses `.isdecimal()`. The PY009 concepts reference specifically gives `.isdigit()` as the taught example. If `.isdecimal()` has not been covered, use the documented method so the solution stays within the agreed learning boundary.
3. **Keep the interactive menu separate from reusable functions.** Lines 179–220 start prompting as soon as the file is imported. If you intend to test or reuse the functions by importing this file, place the menu in a `main()` function and call it under the usual main guard, provided that convention has been covered.

## Overall assessment

The core equipment-desk behaviour is implemented coherently. In particular, deriving availability from the current request statuses gives the program a sound and easy-to-check inventory model. No major state-transition defect is apparent from the submitted code.

**Next step:** Add the missing testing evidence and confirm that the quantity-validation method is within the concepts covered so far. This is feedback on the submitted version, not a grade.
