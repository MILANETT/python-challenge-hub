# PY005 Submission Review — YVONNE

Your submission covers all the main data structures and includes examples for list changes, tuple access, set operations, dictionary methods, nested data, references, and copying. You also included a final mini student-record system.

## What is working well
- The initial student records, rooms, and course membership sets are represented clearly.
- You demonstrate the expected list, tuple, set, and dictionary operations.
- The nested access expressions are written in a way that makes the list → dictionary → inner list structure visible.
- The final system uses a deep copy for backups and separates the main operations into functions.

## Important improvements

1. **Check f-string syntax.** Several f-strings use double quotes inside a double-quoted f-string, for example f"{student["name"]}". This fails to parse in Python 3.10/3.11. Use single quotes for dictionary keys inside the f-string.
2. **Correct the record indexes in the explanations.** The original list order is Daniel at index 0, Amina at index 1, and Brian at index 2. The line labelled “Amina's third mark” reads students[2], which is Brian; the line labelled “Changed Amina's Marks” reads students[0], which is Daniel. Use the correct index or find the student by ID.
3. **A shallow copy is not a reference.** Shallow_reference = student makes both variables refer to the same dictionary; it does not create a shallow copy. Use copy.copy(student), then mutate an element inside the nested marks list to demonstrate that the nested list is shared.
4. **Correct the tuple explanation.** A tuple can contain duplicate values. Its useful property in this scenario is that the tuple itself is immutable.
5. **Keep the Python and Database sets accurate.** Removing a course from a student does not remove that student from the corresponding set when other students still take the course, so the set can retain stale membership. Update the specific student's membership when their last matching course is removed.
6. **Test the final menu's empty and invalid inputs.** The main system has sensible checks for student IDs, courses, and marks. Verify blank IDs, duplicate IDs, non-numeric marks, and attempts to update or remove a course that does not exist.

## Priority
First correct the f-strings and the mislabeled indexes, then fix the shallow-copy demonstration. These are important because they affect whether the code runs and whether the examples actually demonstrate the concept you describe.

**Overall:** Good breadth and useful reflections. The biggest next step is matching each explanation to the exact object being accessed and ensuring the copying examples demonstrate the intended behaviour.
