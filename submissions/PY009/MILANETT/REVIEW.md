# PY009 Submission Review — MILANETT

Thanks for including the program, testing evidence, debugging notes, and AI-assistance disclosure. Your debugging write-up is especially useful because it documents the symptoms, causes, and fixes rather than only showing the final code.

## What is working well

- The starting records are represented, and the initial available quantities correctly account for the two projectors and two laptops already issued.
- You validate IDs against existing IDs, reject blank requester names, match equipment case-insensitively, and validate quantity text before converting it.
- Issuing checks the request status and available quantity before updating the status.
- Returns and cancellations check the current status, preventing a returned item from being returned twice and preventing issued requests from being cancelled.
- The desk report uses one loop over the parallel inventory lists. Your debugging notes explain how nested loops had previously caused each item to print 125 times.
- The comments and debugging notes show a deliberate effort to understand why bugs happened.

## Improvements to make next

1. **Reject a blank request ID.** The menu normalizes IDs, but an empty string is still considered unique and can be registered. Add an explicit blank-ID check inside register_request().
2. **Normalize quantity input.** The menu passes the quantity without calling strip(), so a valid-looking entry such as " 2 " is rejected by isdigit(). Strip the text before validating it.
3. **Consider a more cohesive request structure.** The inventory and request records use parallel lists. They work when every append stays aligned, but forgetting one append can associate the wrong requester, equipment, quantity, or status. A dictionary of request dictionaries would keep each request's fields together. This is an improvement opportunity, not a requirement to rewrite everything immediately.
4. **Keep reusable logic separate from terminal interaction where practical.** The current functions mostly print their outcomes. Returning a success value or result from core operations would make them easier to test and reuse, while the menu could handle messages.
5. **Add a small regression-test checklist.** Your testing evidence and debugging document are valuable; make sure it explicitly verifies duplicate returns, cancellation after issuing, insufficient stock, invalid quantity text, and the inventory before and after each state change.

## Priority

The main logic is thoughtfully structured and the stock calculation is consistent with the statuses used in this program. Focus next on edge-case validation (especially blank IDs and whitespace around quantities), then consider how the data structure can make inconsistent records harder to create.

**Overall:** A substantial, well-documented attempt with good debugging evidence. The next step is making the input boundaries and data representation as reliable as the central issue/return logic.
