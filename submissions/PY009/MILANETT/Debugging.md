# PY009 — Debugging Documentation

## 1. Inventory Stock Initialization Sync

- **Location:** Initial Data Structures (`equip_inventory`)
- **Issue / Behavior:** Initial available quantities for `Projector` and `Laptop` were set to `4` and `6`, respectively, matching their total quantities. However, `EQ001` (2 Projectors) and `EQ003` (2 Laptops) were already registered with the status `"Issued"`.
- **Root Cause:** Initial stock levels did not account for active equipment issues recorded before the program started.
- **Fix Applied:** Adjusted the initial `available_qty` values to account for existing active borrowings:
  - **Projector:** `4 - 2 = 2` available.
  - **Laptop:** `6 - 2 = 4` available.

## 2. Invalid Index Type Exception (`TypeError`)

- **Location:** `issue_equipment()`, `return_equipment()`
- **Issue / Behavior:** The program crashed with `TypeError: list indices must be integers or slices, not str`.
- **Root Cause:** A string variable, `eqt` (e.g., `"Projector"`), was used directly as a list index in `equip_inventory["available_qty"][eqt]`. Python lists require integer indices or slices, not strings.
- **Fix Applied:** Retrieved the integer index corresponding to the requested equipment using `.index()` and used it to access the appropriate list element.

  ```python
  eqt_idx = equip_inventory["equipment"].index(requested_eqt)
  available_qty = equip_inventory["available_qty"][eqt_idx]
  ```

## 3. Comparison Operator Used Instead of Assignment Operator

- **Location:** `issue_equipment()`, `return_equipment()`, `cancel_request()`
- **Issue / Behavior:** Request statuses were not updated in memory, leaving requests with the status `"Requested"` indefinitely.
- **Root Cause:** The equality comparison operator (`==`) was used instead of the assignment operator (`=`). For example:

  ```python
  req_record["Status"][req_idx] == "Issued"
  ```

  This expression compares the existing value with `"Issued"` but does not modify it.
- **Fix Applied:** Replaced comparison operators with assignment operators where status updates were required.

  ```python
  req_record["Status"][req_idx] = "Issued"
  req_record["Status"][req_idx] = "Returned"
  req_record["Status"][req_idx] = "Cancelled"
  ```

## 4. Duplicate Append Loop and Multiple-Trigger Errors

- **Location:** `register_request()`
- **Issue / Behavior:** New requests were appended multiple times during a single operation, or rejection error messages were printed repeatedly.
- **Root Cause:** `.append()` statements were nested inside unnecessary loops, including `for d in req_record:` and `for x in req_record["RequestID"]:`. This caused the same operation to execute repeatedly while iterating over dictionary keys or existing request IDs.
- **Fix Applied:** Removed the unnecessary loops and performed validation checks before appending the new request exactly once.

  ```python
  if valid_id and valid_name and valid_equipment and valid_quantity:
      req_record["RequestID"].append(req_id)
      # Append the remaining parallel-list values once.
  ```

  **Key lesson:** Validate first, then update the data structures once. Avoid placing data insertion operations inside loops unless repeated insertion is intentional.

## 5. Unsafe Integer Parsing (`ValueError`)

- **Location:** `register_request()`
- **Issue / Behavior:** The program crashed when non-numeric input, such as `"abc"`, or an invalid quantity, such as `"-5"`, was supplied.
- **Root Cause:** The program attempted to convert the quantity to an integer using `int(qty)` before validating the input.
- **Fix Applied:** Validated the input before conversion, ensuring it contained positive whole-number digits.

  ```python
  if qty.isdigit() and int(qty) > 0:
      quantity = int(qty)
  ```

  **Key lesson:** Validate external input before converting it to another data type. Note that `.isdigit()` accepts digit characters only; it rejects negative signs, decimal points, and surrounding whitespace. Normalize input first if those formats need to be supported.

## 6. 125× Combinatorial Report Printing Bug

- **Location:** `desk_report()`
- **Issue / Behavior:** Every equipment item appeared 125 times in the desk report.
- **Root Cause:** Three nested loops iterated over `equipment`, `total_qty`, and `available_qty`. Since each list contained five elements, the loops produced `5 × 5 × 5 = 125` iterations.
- **Fix Applied:** Replaced the nested loops with a single index-based loop, keeping the corresponding elements of the parallel lists aligned.

  ```python
  for i in range(len(equip_inventory["equipment"])):
      eqp = equip_inventory["equipment"][i]
      qty = equip_inventory["total_qty"][i]
      av_qty = equip_inventory["available_qty"][i]
      issued_qty = qty - av_qty
  ```

  **Key lesson:** When multiple parallel lists represent attributes of the same records, use a shared index or consider combining the attributes into a more suitable data structure. Nested loops should only be used when every combination of elements is actually required.

## 7. F-String Quote Nesting and Syntax Errors

- **Location:** `view_request()`, `desk_report()`
- **Issue / Behavior:** Python raised syntax errors or parsing warnings when evaluating f-strings containing nested dictionary key references.
- **Root Cause:** Double quotes were nested inside a double-quoted f-string, making the string boundaries ambiguous in the affected Python syntax. For example:

  ```python
  f"{req_record["Requester"][req_idx]}"
  ```

- **Fix Applied:** Used single quotes for the dictionary key inside the double-quoted f-string.

  ```python
  f"{req_record['Requester'][req_idx]}"
  ```

  **Key lesson:** Choose quotation marks carefully when nesting strings inside f-strings. Using different quote styles for the outer string and inner dictionary keys often improves readability and avoids syntax errors.

## 8. Misplaced Code Execution Blocks (Scope and Control Flow)

- **Location:** `return_equipment()`, `cancel_request()`
- **Issue / Behavior:** Stock levels or request statuses were modified even when a request did not exist or did not meet the required status conditions.
- **Root Cause:** State-modification statements were placed outside the validation `if` blocks. Consequently, they could execute even when the relevant conditions were not satisfied.
- **Fix Applied:** Moved stock adjustments and status updates inside their corresponding validation blocks.

  ```python
  if req_record["Status"][req_idx] == "Issued":
      # Restore the appropriate stock quantity.
      # Update the request status to "Returned".
  ```

  ```python
  if req_record["Status"][req_idx] == "Requested":
      # Update the request status to "Cancelled".
  ```

  **Key lesson:** Indentation determines control flow in Python. Keep state-changing operations inside the conditions that authorize them, and validate the current state before performing an operation.

---

## Debugging Lessons Learned

The debugging process reinforced the following programming principles:

1. **Maintain data consistency:** Initial inventory quantities must reflect all existing active issues.
2. **Understand data structures:** Lists use integer indices, while dictionaries use keys.
3. **Distinguish operators:** Use `=` to assign values and `==` to compare values.
4. **Control repetition:** Unnecessary loops can cause duplicate insertions, repeated messages, and incorrect output.
5. **Validate input:** Check user input before converting it to another data type.
6. **Align parallel lists:** Use a shared index when corresponding elements represent the same record.
7. **Write valid f-strings:** Use appropriate quotation marks when accessing dictionary keys inside formatted strings.
8. **Respect control flow:** Place state changes inside the conditions that authorize them.
9. **Protect program state:** Inventory quantities and request statuses must remain consistent after issuing, returning, or cancelling equipment.
10. **Test edge cases:** Check invalid inputs, missing requests, incorrect statuses, insufficient stock, duplicate IDs, and repeated operations.
