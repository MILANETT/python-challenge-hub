# PY009 Submission Review — YVONNE

Your solution is organised into clear functions for registering, issuing, returning, cancelling, finding, and reporting requests. The separate inventory and request dictionaries are also a good foundation for a small program like this.

There are, however, a few important correctness gaps to fix before the program matches the challenge requirements.

## What is working well

- Request IDs and requester names are checked for blank values, and duplicate IDs are rejected.
- Issuing checks both the request's status and the available quantity before reducing stock.
- Returns restore stock only when a request is currently issued.
- Cancellation is limited to requests that have not been issued.
- The report shows total, available, and issued quantities and includes all request records.
- The functions have clear names and mostly handle invalid request IDs with early returns.

## Important issues

1. **The supplied starting requests are missing.** The challenge requires EQ001, EQ002, and EQ003 to be present at startup. Without them, the program starts with an empty request dictionary and does not represent the given desk state.
2. **Initial availability is inconsistent with the required starting state.** The inventory begins with every item fully available. If the initial issued records are added, Projector availability must start at 2 (4 total minus 2 issued) and Laptop availability at 4 (6 total minus 2 issued). The pending EQ002 request does not reduce available microphones.
3. **Non-numeric quantity input crashes the program.** The code calls int(input(...)) before validating the text. The challenge specifically asks you to validate quantity text before conversion and handle invalid text without relying on try/except. Read the input as text, check isdigit(), and only then convert it.
4. **The extension-cable name is misspelled and does not match the challenge.** The inventory key Extention_Cable should be aligned with the provided Extension cable label. A consistent, human-readable name also makes user input easier.
5. **The quantity rule should explicitly reject non-positive values.** You correctly reject values less than or equal to zero after conversion, but this check is only reached if the conversion succeeds. Keep it after the text validation as well.

## Improvements to make next

- Show available quantities in the equipment list, not just the equipment names, so users can make an informed request.
- Consider putting the menu call inside an import guard so tests can import functions without immediately starting interactive input.
- Add tests for duplicate IDs, non-numeric quantity text, insufficient stock, cancellation, and repeated returns.

## Priority

Fix the missing starting records and quantity-input validation first. Then correct the inventory label and verify the initial report against the values in the challenge statement.

**Overall:** The program's function layout is a good start, but the missing initial records and unsafe quantity conversion are important gaps. Fixing those will make the solution much closer to the required equipment-desk behaviour.
