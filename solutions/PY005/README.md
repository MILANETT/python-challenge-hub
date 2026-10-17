# PY005 — Student Records Manager: Solution Approach

This guide explains the main design decisions in the reference solution. Read it alongside `solution.py`.

## 1. Choose structures based on the data

The starting records demonstrate how structures can work together:

- A **list** keeps student records in order and allows records to be added or removed.
- A **dictionary** associates labels such as `name`, `student_id`, `courses`, and `marks` with their values.
- Lists inside a record hold the student's courses and marks.
- A **tuple** represents the provided room collection, which the exercise treats as fixed.
- **Sets** represent collections where duplicate names are not useful and set operations can compare membership.

The goal is not to use every structure everywhere. Choose a structure based on the operations the program needs.

## 2. Navigate nested data one level at a time

To retrieve a student's mark, first select the student from the outer list, then select the `"marks"` value from that student's dictionary, and finally index the marks list.

Think of this as following a path through containers. When a nested lookup fails, check each step: the outer index, dictionary key, and inner index.

## 3. Understand mutability

Lists, sets, and dictionaries can be changed after creation. Tuples cannot have their individual elements reassigned.

A failed tuple mutation is an intentional experiment. If you run it directly, Python stops the program at that line. To let the rest of the reference solution continue, the demonstration can be isolated or left as a commented experiment and its expected error described in comments. Do not introduce exception handling unless the group has learned it.

## 4. References and copies are different

Assigning a second variable to an existing list does not make a new list. Both names refer to the same object, so a mutation through one name is visible through the other.

A **shallow copy** creates a new outer container but can still share nested mutable objects. A **deep copy** recursively copies nested contents, making it more suitable for an independent backup of nested student records.

The reference solution uses deep copying when creating and restoring backups so changes to the working records do not unintentionally change the saved backup.

## 5. Organize the interactive record manager

Keep the menu readable by giving each operation a focused function, such as displaying records, searching, adding a student, updating a mark, or managing courses.

A typical menu flow is:

1. Display the available actions.
2. Read the user's choice.
3. Call the function for that action.
4. Repeat until the user chooses to exit.

Search by student ID when possible, because the ID is intended to identify a specific record. When updating a mark, locate the student and then the correct mark index. Keep the course and mark positions aligned when the design associates each mark with a corresponding course.

## 6. Why sets help with course queries

A set can collect course names without retaining duplicates. Set operations can compare the students enrolled in different course groups. For a report of students taking a particular course, inspect each record's course list and display matching students.

## 7. Test operations in small steps

Before testing the full menu, verify the smaller operations independently:

- Display the original records.
- Search for an existing and a missing ID.
- Add a student and display the updated list.
- Update a mark and check the correct record changed.
- Add and remove a course.
- Create a backup, change the records, and restore the backup.

Also inspect the effect of references, shallow copies, and deep copies separately so their behaviour is easy to compare.

## Concepts used

- Lists, tuples, sets, and dictionaries
- Indexing, slicing, and collection methods
- Nested data structures
- Mutability and immutability
- References, shallow copies, and deep copies
- Functions and a menu loop
- Searching and updating records

## Common mistakes to watch for

- Using a list index or dictionary key incorrectly.
- Forgetting that sets do not preserve duplicates.
- Assuming that assigning a variable creates a copy.
- Assuming a shallow copy also copies every nested list.
- Updating the wrong student's record.
- Removing a course without keeping related data consistent.
- Accidentally changing the backup while modifying the original records.

**Key idea:** Good data-structure choices make the required operations natural; understanding references keeps those operations predictable.