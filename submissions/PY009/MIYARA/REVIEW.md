# PY009 Submission Review — MIYARA

Your solution uses a nested dictionary for requests, which makes each request's details easy to keep together. You also calculate availability from the requests currently marked Issued, rather than maintaining a separate available-stock value that can drift out of sync.

## What is working well

- The three starting request records are included with the required statuses.
- register_request() checks for duplicate IDs, rejects blank requester names and unknown equipment, and validates quantity text before converting it to an integer.
- issue_equip() verifies that a request exists, is still requested, and can be fulfilled with available stock.
- Return and cancellation operations check the current status before changing it. This also prevents a second return from being accepted.
- The report calculates total, issued, and available quantities and displays pending/active request details.
- Your use of return for early exits keeps invalid operations from continuing into state-changing code.

## Improvements to make next

1. **Validate request IDs more completely.** Strip surrounding whitespace and reject an empty ID before checking uniqueness. As written, a blank ID can be registered, and an ID with surrounding spaces may be stored inconsistently.
2. **Normalize quantity input.** Call strip() before isdigit() so accidental surrounding whitespace does not cause an otherwise valid whole number to be rejected.
3. **Keep status names consistent with the challenge.** The starter records use Requested, and your program currently uses that status, which is good. Preserve consistent capitalization across all operations and reports.
4. **Make the menu import-safe.** Put the menu loop inside main() and call it under if __name__ == "__main__":. Otherwise, importing the file for a test starts prompting for input immediately.
5. **Improve function return values when you revisit the design.** Most operations print success or failure but return None. Returning a boolean or result from the core operation would make it easier to test without inspecting terminal output.
6. **Add focused tests for the state transitions.** Check that an oversized issue leaves stock unchanged, a cancelled request never reduces availability, a return happens only once, and a second attempt to issue the same request is rejected.

## Priority

The core data model and inventory calculation are sound for this challenge. Start with blank/normalized IDs and quantity input, then add repeatable tests for the issue, return, and cancellation rules.

**Overall:** A solid, readable solution with a sensible nested-dictionary design. Most improvements are around input edges, testability, and keeping the interactive menu separate from reusable logic.
