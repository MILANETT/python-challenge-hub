# PY005 Submission Review — MILANETT

You put substantial effort into the challenge: the file contains explanations for the data-structure choices, examples of nested access and copying, debugging notes, and a mini student-record system. The reflections are a useful part of the submission, not just decoration.

## What is working well
- A list of dictionaries is a sensible structure for the initial collection of student records.
- You demonstrate list operations, tuple indexing/slicing, set operations, dictionary updates, nested access, and the difference between a reference and a copy.
- The mini system is divided into named functions for viewing, adding, searching, updating, and managing courses.
- The backup operation uses copy.deepcopy(), which is appropriate for a nested list of dictionaries containing lists.

## Important improvements

1. **Check Python-version syntax.** Several f-strings use double quotes both outside and inside the expression, for example a form like f"{student["student_id"]}". This fails to parse in Python 3.10/3.11. Use single quotes for dictionary keys inside a double-quoted f-string, or vice versa.
2. **Validate student IDs and names.** In the mini system, reject blank names/IDs and duplicate IDs before appending a new student. Otherwise, the same ID can identify more than one record.
3. **Keep the course sets synchronized.** Adding a student or changing their courses does not consistently update python_students and database_students. Removing one student's course should update that student's membership without leaving stale set entries.
4. **Protect course/mark alignment.** Courses and marks are stored in parallel lists, so every addition/removal must change both lists at the same index. You do this in several places; keep that invariant explicit and test it after every edit.
5. **Handle invalid counts.** A negative number of courses silently results in no iterations. Reject negative course counts and consider how the program should behave if the user enters non-numeric text.
6. **Improve the backup interaction.** The backup is created, but the menu has no restore option. If you intend to support restoring, add a clear option and test that later changes to students do not alter the saved backup.

## Priority
First make the f-strings parse on the Python version used by the group, then test duplicate IDs and course/mark alignment. After that, verify that the set memberships and backup behave as intended.

**Overall:** A comprehensive attempt with strong documentation and evidence of debugging. Focus now on correctness at the program boundaries and on keeping related data structures synchronized.
