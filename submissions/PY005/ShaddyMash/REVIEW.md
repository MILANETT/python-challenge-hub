# PY005 Submission Review — ShaddyMash

Your program goes beyond the individual data-structure exercises and builds a menu-driven student manager. The nested student records are kept together, and the code includes validation loops for menu choices, IDs, marks, and course names.

## What is working well
- The list of dictionaries keeps each student's fields together.
- You reject blank names and IDs, check for duplicate IDs, and validate marks within the 0–100 range.
- Updating and removing a course also updates the mark at the same index, preserving the course/mark relationship.
- The unique-course operation uses a set, and the backup creates a new outer dictionary and copies the two nested lists, which is sufficient for the current record structure.
- The comments explain the purpose of the main menu actions and important validation choices.

## Improvements

1. **Use consistent names and formatting.** The keys use singular "course" while the variable is called courses, and the code has many compressed expressions. Consistent names and spacing will make the larger program easier to maintain.
2. **Normalize comparisons.** Course and ID comparisons are case-sensitive. Consider normalizing the user input and stored values consistently so "python" and "Python" do not behave like unrelated courses.
3. **Test empty course lists.** Updating or removing a course should report that no matching course exists when a student has no courses. Your checks mostly handle this, but include an explicit test.
4. **Consider a clearer backup copy.** Your manual copy correctly copies the outer student dictionary and the course/marks lists for the current structure. If new nested mutable fields are added later, remember that this approach must be updated or replaced with a deep copy.
5. **Improve the display of all students.** Printing the entire list at once works, but a loop that displays one student's name, ID, courses, and marks on separate lines is easier to scan.

## Priority
The core operations and validation are in good shape. Focus next on consistent case handling and readable output, then test the update/remove actions with missing courses and students who have no courses.

**Overall:** A strong, practical submission with useful validation and a working menu structure. The main opportunities are consistency, presentation, and broader edge-case testing.
