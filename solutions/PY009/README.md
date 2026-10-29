# PY009 — Reference Solution

This folder contains a complete, runnable implementation of **The Equipment Desk**.

## Run it

From the repository root, use Python 3.10 or newer:

    python solutions/PY009/solution.py

The program uses only built-in Python features and does not use classes, file storage, external packages, or exception handling.

## Design choices

- **Inventory:** INVENTORY stores each equipment type and its total quantity.
- **Requests:** requests stores each request under its unique ID, with the requester, equipment, quantity, and status.
- **Available stock:** available_quantity_for() calculates availability as total quantity minus the quantity in requests currently marked Issued. This avoids separately changing stock in multiple operations and keeps the report consistent with request statuses.
- **Starting records:** EQ001 and EQ003 begin as issued; EQ002 begins as requested. Their quantities are reflected in availability automatically.
- **Validation:** Request IDs and names are checked for blank values; duplicate IDs and unknown equipment are rejected. Quantity text is checked with isdigit() before conversion, then checked to ensure it is positive.
- **State transitions:** Only Requested requests can be issued or cancelled. Only Issued requests can be returned, so a returned request cannot restore availability a second time.
- **Menu:** match/case routes repeated operations until the user exits.

## Manual verification checklist

Try each of the following before treating the solution as verified:

- [ ] The initial report shows 2 projectors and 2 laptops currently issued, with 2 projectors and 4 laptops available.
- [ ] EQ002 appears as a pending request.
- [ ] A blank ID, duplicate ID, blank requester, unknown equipment, and non-numeric/zero/negative quantity are rejected.
- [ ] A valid request can be registered and issued.
- [ ] An issue exceeding available stock is rejected without changing the report.
- [ ] A request can be cancelled before issuing, but an issued request cannot be cancelled.
- [ ] An issued request can be returned once; a second return is rejected.
- [ ] A returned or cancelled request does not count as currently issued.
- [ ] The report lists total, available, issued, pending requests, and individual request details.
- [ ] Invalid menu choices are rejected and the menu continues.

This is one valid implementation, not the only possible design. The important properties are valid state transitions, consistent inventory calculations, input validation, and readable code.
