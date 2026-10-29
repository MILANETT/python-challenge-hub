# PY005 Submission Review — MIYARA

Your submission includes the required data-structure explanations, nested access examples, and a final interactive student-record program. The final version uses a dictionary keyed by student ID and a nested marks dictionary, which is a reasonable alternative design for the management task.

## What is working well
- The explanations show that you are thinking about order, labels, mutability, uniqueness, and the relationship between courses and marks.
- You demonstrate set intersection, difference, union, membership, and dictionary methods.
- The nested list/dictionary examples correctly show how to move from the students collection to one record and then to its course or mark.
- In the final system, the student ID acts as a direct dictionary key, and the menu covers viewing, adding, searching, updating, and removing courses.

## Improvements

1. **Correct the tuple explanation.** Tuples can contain duplicate values. Their relevant property here is immutability, not uniqueness. Sets are the built-in collection type that automatically removes duplicates.
2. **Demonstrate shallow copying with a nested mutation.** Your shallow-copy example replaces the entire Marks list. That does not demonstrate shared nested state because the copied dictionary receives a new list. Change an element inside the existing nested list to observe that a shallow copy shares that inner list.
3. **Keep the deep-copy value type consistent.** Assigning a list such as ["Monicah"] to the Name field changes the expected name string into a list. Use a string so the record's field type stays consistent.
4. **Initialize backup before the menu.** In the final menu, choosing restore before creating a backup refers to backup before it has been assigned, which raises NameError. Initialize backup to None before the loop and check it before restoring.
5. **Normalize the student ID.** Strip whitespace and use a consistent case for IDs on both creation and lookup, so a record cannot be duplicated merely through different casing or surrounding spaces.
6. **Keep the final record schema clear.** The final task changes from a list of records with separate course/mark lists to a dictionary keyed by ID with marks keyed by course. That is a valid design change; add a short comment explaining the new schema and why it simplifies lookups.

## Priority
Fix the tuple explanation and shallow-copy demonstration first because they are important concepts in this challenge. Then handle the backup-before-restore case and normalize IDs.

**Overall:** Good coverage of the required structures and a sensible final data model. The next step is making the demonstrations accurately show the concept being discussed and guarding the menu's edge cases.
