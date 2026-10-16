# ============================================================
# PY005: STUDENT RECORDS MANAGER
# Topics: Lists, Tuples, Sets, Dictionaries, Nested Structures,
#         Mutability, References, Shallow and Deep Copying
# ============================================================

import copy


# ============================================================
# FINAL TASK PLANNING — THINK BEFORE CODING
# ============================================================
#
# 1. What information am I storing?
#    Student names, IDs, courses, marks and classroom names.
#
# 2. Which information is ordered?
#    Student records, courses and marks have meaningful order.
#
# 3. Which information needs unique values?
#    Course collections and student membership sets.
#
# 4. Which information needs labels/keys?
#    Each student's record uses dictionary keys such as
#    "name", "student_id", "courses" and "marks".
#
# 5. Which information should not change?
#    The classroom collection is represented by a tuple
#    because the challenge treats it as a fixed collection.
#
# 6. Which structures will be nested?
#    A list contains student dictionaries; each dictionary
#    contains lists of courses and marks.
#
# 7. Where could references cause unexpected changes?
#    Two variables can refer to the same list or dictionary.
#
# 8. Where might I need a copy?
#    A backup should not accidentally change when the original
#    student records are edited.


# ============================================================
# PART 1 — UNDERSTAND THE DATA
# ============================================================

students = [
    {
        "name": "Daniel",
        "student_id": "DS001",
        "courses": ["Python", "Statistics", "Databases"],
        "marks": [78, 64, 82]
    },
    {
        "name": "Amina",
        "student_id": "DS002",
        "courses": ["Python", "Statistics", "Databases"],
        "marks": [91, 73, 88]
    },
    {
        "name": "Brian",
        "student_id": "DS003",
        "courses": ["Python", "Statistics", "Databases"],
        "marks": [56, 68, 61]
    }
]

# A tuple is suitable for this fixed classroom collection.
class_rooms = ("Room A", "Room B", "Room C")

# Sets store unique values and support efficient membership
# tests and operations such as union and intersection.
python_students = {"Daniel", "Amina", "Brian"}
database_students = {"Daniel", "Amina", "Brian"}

# DATA-STRUCTURE REFLECTION:
#
# students: A list is appropriate because student records
# have an order and we may add or remove records.
#
# Each student record: A dictionary is appropriate because
# fields such as name and student_id have meaningful labels.
#
# courses and marks: Lists are appropriate because order
# matters and values can be updated.
#
# class_rooms: A tuple represents a fixed ordered collection.
#
# python_students and database_students: Sets represent
# membership without needing duplicate student names.


# ============================================================
# PART 2 — LISTS
# ============================================================

print("\n========== PART 2: LISTS ==========")

# Indexing retrieves a single item from a list.
# Index 0 is the first item; index -1 is the last.
print("First student:", students[0])
print("Last student:", students[-1])

# Slicing retrieves a section of the list.
# [:2] means start at the beginning and stop before index 2.
print("First two students:", students[:2])

# append() adds a new record to the end of the list.
new_student = {
    "name": "Grace",
    "student_id": "DS004",
    "courses": ["Python", "Statistics", "Databases"],
    "marks": [80, 75, 85]
}
students.append(new_student)

# insert() adds an item at a specified index.
# Here, Grace is moved to the beginning of the list.
students.insert(0, students.pop())

# pop() removes and returns an item.
# Remove Grace from index 0 to demonstrate the method.
removed_student = students.pop(0)
print("Removed student:", removed_student["name"])

# Change a mark by navigating through the nested structure.
# students[0] is Daniel's dictionary.
# ["marks"] accesses his marks list.
# [0] accesses the first mark in that list.
students[0]["marks"][0] = 79

print("Daniel's updated marks:", students[0]["marks"])

# LIST REFLECTION:
#
# append() adds a new item.
# insert() adds an item at a chosen position.
# pop() removes an item and returns it.
#
# Indexing is useful when a particular position is known.
# Slicing is useful when we need a section of a list.
#
# We can update a nested mark because both the list of
# students and each student's marks list are mutable.


# ============================================================
# PART 3 — TUPLES
# ============================================================

print("\n========== PART 3: TUPLES ==========")

print("First room:", class_rooms[0])
print("Last room:", class_rooms[-1])
print("First two rooms:", class_rooms[:2])

# Tuples are immutable: their individual elements cannot
# be reassigned after the tuple has been created.
#
# We deliberately attempt the modification and catch the
# expected error so the rest of the program can continue.
try:
    class_rooms[0] = "Room Z"
except TypeError as error:
    print("Tuple modification failed:", error)

# TUPLE REFLECTION:
#
# Python raises TypeError because tuple item assignment
# is not supported.
#
# Immutability protects the tuple's element assignments.
# A tuple is useful when the collection should be treated
# as fixed. Note that a tuple containing a mutable object
# does not make that nested object immutable.


# ============================================================
# PART 4 — SETS
# ============================================================

print("\n========== PART 4: SETS ==========")

# Intersection (&) returns members shared by both sets.
print(
    "Taking both courses:",
    python_students & database_students
)

# Difference (-) returns members in the first set
# that are not present in the second set.
print(
    "Python but not Databases:",
    python_students - database_students
)

# Union (|) returns all unique members from both sets.
print(
    "Taking at least one course:",
    python_students | database_students
)

# Membership checks whether an item exists in a collection.
print("Brian takes Python:", "Brian" in python_students)

# add() inserts a member. Adding an existing member would
# not create a duplicate.
python_students.add("Grace")
print("Python students after adding Grace:", python_students)

# discard() removes a member if present and does not raise
# an error if the member is absent.
database_students.discard("Brian")
print("Database students after removing Brian:", database_students)

# SET REFLECTION:
#
# Intersection finds shared membership.
# Difference finds members unique to one set.
# Union combines memberships without duplicates.
# The 'in' operator tests membership.
#
# Sets are useful for membership questions and uniqueness.
# A list can preserve order and duplicates, but checking
# shared or unique membership generally requires more work.


# ============================================================
# PART 5 — DICTIONARIES
# ============================================================

print("\n========== PART 5: DICTIONARIES ==========")

# Dictionary keys let us retrieve labelled information
# without remembering the position of every field.
daniel = students[0]

print("Name:", daniel["name"])
print("Student ID:", daniel["student_id"])
print("Courses:", daniel["courses"])
print("Marks:", daniel["marks"])

# Add a new key-value pair.
daniel["year"] = 2

# Update an existing value by assigning to its key.
daniel["year"] = 3

# get() retrieves a value safely when a key might be absent.
# If "email" does not exist, it returns the supplied default.
print("Email:", daniel.get("email", "Not provided"))

# keys(), values() and items() provide views of the
# dictionary's keys, values and key-value pairs.
print("Fields:", list(daniel.keys()))
print("Values:", list(daniel.values()))
print("Key-value pairs:", list(daniel.items()))

# pop() removes a key and returns its value.
removed_year = daniel.pop("year")
print("Removed year:", removed_year)

# DICTIONARY REFLECTION:
#
# A key-value pair connects a label to its corresponding value.
# For example, "name" is a key and "Daniel" is its value.
#
# Dictionaries are appropriate for records because fields
# are named. A simple list would require remembering indexes
# such as record[0] for a name and record[1] for an ID.


# ============================================================
# PART 6 — NESTED DATA STRUCTURES
# ============================================================

print("\n========== PART 6: NESTED STRUCTURES ==========")

# Access Daniel's second course:
# list -> first student dictionary -> courses list -> index 1
print("Daniel's second course:", students[0]["courses"][1])

# Amina is currently at index 1.
# Her third mark is at index 2 of her marks list.
print("Amina's third mark:", students[1]["marks"][2])

# Brian is at index 2.
print("Brian's marks:", students[2]["marks"])

# Update one course and its corresponding mark.
# The course and mark lists are aligned by position:
# index 0 in each list refers to the same course.
students[0]["courses"][0] = "Advanced Python"
students[0]["marks"][0] = 79

# Add another course and its mark at matching positions.
students[1]["courses"].append("Machine Learning")
students[1]["marks"].append(90)

print("Updated Daniel's record:", students[0])
print("Updated Amina's record:", students[1])

# NESTED STRUCTURE REFLECTION:
#
# To access Daniel's second course, we first select the
# student from the outer list, then the "courses" field
# from the dictionary, then the second course from that list.
#
# When courses and marks are stored in parallel lists,
# their positions must remain aligned. A more complex system
# might instead store each course with its corresponding mark.


# ============================================================
# PART 7 — MUTABILITY VS IMMUTABILITY
# ============================================================

print("\n========== PART 7: MUTABILITY ==========")

example_list = [10, 20, 30]
example_tuple = (10, 20, 30)
example_set = {10, 20, 30}
example_dictionary = {"score": 80}

# Lists, sets and dictionaries are mutable: their contents
# can be changed after creation.
example_list[0] = 99
example_set.add(40)
example_dictionary["score"] = 95

# A tuple's elements cannot be reassigned.
# We demonstrate that behavior safely.
try:
    example_tuple[0] = 99
except TypeError:
    print("Tuple elements cannot be reassigned.")

print("Mutable list:", example_list)
print("Tuple:", example_tuple)
print("Mutable set:", example_set)
print("Mutable dictionary:", example_dictionary)

# MUTABILITY REFLECTION:
#
# Mutable means an object can be changed after it is created.
# Immutable means its value or elements cannot be changed
# through the object's supported mutation operations.
#
# A variable is a reference to an object; changing a mutable
# object does not require creating a new variable.


# ============================================================
# PART 8 — REFERENCES VS COPIES
# ============================================================

print("\n========== PART 8: REFERENCES VS COPIES ==========")

original_marks = [70, 80, 90]

# This assignment does not create a second list.
# Both variables refer to the same list object.
marks_reference = original_marks

marks_reference[0] = 100

print("Original list:", original_marks)
print("Reference variable:", marks_reference)
print(
    "Same object:",
    original_marks is marks_reference
)

# REFERENCES REFLECTION:
#
# Changing marks_reference also changes what we see through
# original_marks because both names refer to the same object.
# Assignment creates another reference, not an automatic copy.


# ============================================================
# PART 9 — SHALLOW VS DEEP COPYING
# ============================================================

print("\n========== PART 9: SHALLOW AND DEEP COPIES ==========")

student = {
    "name": "Daniel",
    "marks": [70, 80, 90]
}

# A normal reference points to the exact same dictionary.
student_reference = student

# A shallow copy creates a new outer dictionary.
# Nested objects, such as the marks list, remain shared.
student_shallow_copy = student.copy()

# A deep copy recursively copies nested objects too.
student_deep_copy = copy.deepcopy(student)

# Modify the nested marks list through the shallow copy.
student_shallow_copy["marks"][0] = 50

print("Original after shallow-copy edit:", student)
print("Shallow copy:", student_shallow_copy)
print("Deep copy before its edit:", student_deep_copy)

# The shallow copy shares the nested marks list with student,
# so changing that list affects both dictionaries.
#
# The deep copy has its own nested marks list.
student_deep_copy["marks"][1] = 40

print("Original after deep-copy edit:", student)
print("Deep copy after its edit:", student_deep_copy)

# COPYING REFLECTION:
#
# Reference: same outer object and same nested objects.
# Shallow copy: new outer object, shared nested objects.
# Deep copy: new outer object and recursively copied contents.
#
# Shallow copying can be dangerous when nested lists or
# dictionaries are modified because changes may appear in
# more than one record.


# ============================================================
# PART 10 — DATA-STRUCTURE DECISION CHALLENGE
# ============================================================

# SCENARIO A: Student names in registration order.
# Choice: list.
# Reason: Lists preserve order and allow additions/removals.
# Alternative: a set does not guarantee the registration
# order as the intended feature and removes duplicates.

# SCENARIO B: Labelled information such as name, age and course.
# Choice: dictionary.
# Reason: Each value is accessed using a meaningful key.
# Alternative: a list relies on positional indexes, which are
# harder to interpret and maintain.

# SCENARIO C: Unique university courses.
# Choice: set.
# Reason: A set stores unique values and removes duplicates.
# Alternative: a list permits duplicate course names unless
# additional checks are written.

# SCENARIO D: Fixed coordinates (x, y).
# Choice: tuple.
# Reason: A tuple represents a fixed ordered pair.
# Alternative: a list allows individual elements to be
# reassigned, which is less suitable when the pair is fixed.

# SCENARIO E: Student IDs associated with records.
# Choice: dictionary keyed by student ID.
# Reason: The ID directly retrieves the corresponding record.
# Alternative: searching a list requires iterating through
# records until the correct ID is found.

# SCENARIO F: Courses and marks organized in a student record.
# Choice: dictionary containing nested collections.
# Reason: A dictionary labels the record's fields, while
# nested structures store multiple courses and marks.
# Alternative: unrelated flat lists make the relationship
# between each student's courses and marks harder to maintain.


# ============================================================
# DEBUGGING REQUIREMENT — TWO EXAMPLES
# ============================================================

# DEBUGGING EXAMPLE 1: Invalid list index.
debug_marks = [70, 80, 90]

# Expected: retrieve the fourth mark.
# Actual: IndexError because valid indexes are 0, 1 and 2.
try:
    print(debug_marks[3])
except IndexError as error:
    print("Debugging example 1:", error)

# Fix: use a valid index or check the list length first.
print("Corrected access:", debug_marks[2])


# DEBUGGING EXAMPLE 2: Modifying a tuple.
debug_rooms = ("Room A", "Room B")

# Expected: change the first room.
# Actual: TypeError because tuple item assignment is unsupported.
try:
    debug_rooms[0] = "Room C"
except TypeError as error:
    print("Debugging example 2:", error)

# Fix: if changing rooms is required, use a mutable list.
editable_rooms = list(debug_rooms)
editable_rooms[0] = "Room C"
print("Corrected rooms:", editable_rooms)


# ============================================================
# PART 11 — MINI STUDENT RECORD SYSTEM
# ============================================================

# Use a fresh copy of the initial records for the interactive
# system. The earlier sections intentionally modified students.
records = [
    {
        "name": "Daniel",
        "student_id": "DS001",
        "courses": ["Python", "Statistics", "Databases"],
        "marks": [78, 64, 82]
    },
    {
        "name": "Amina",
        "student_id": "DS002",
        "courses": ["Python", "Statistics", "Databases"],
        "marks": [91, 73, 88]
    },
    {
        "name": "Brian",
        "student_id": "DS003",
        "courses": ["Python", "Statistics", "Databases"],
        "marks": [56, 68, 61]
    }
]

backup = None


def find_student(student_id):
    """Return the student record matching an ID, or None."""
    for record in records:
        if record["student_id"] == student_id:
            return record
    return None


def display_student(record):
    """Print all fields in a student record."""
    print(f"\nName: {record['name']}")
    print(f"Student ID: {record['student_id']}")
    print(f"Courses: {record['courses']}")
    print(f"Marks: {record['marks']}")


def display_all_students():
    """Display every student record."""
    if not records:
        print("No student records available.")
        return

    for record in records:
        display_student(record)


def add_student():
    """Collect and append a new student record."""
    student_id = input("Enter new student ID: ").strip()

    if find_student(student_id) is not None:
        print("That student ID already exists.")
        return

    name = input("Enter student name: ").strip()

    records.append({
        "name": name,
        "student_id": student_id,
        "courses": [],
        "marks": []
    })

    print("Student added successfully.")


def search_student():
    """Search for a student by ID."""
    student_id = input("Enter student ID to search: ").strip()
    record = find_student(student_id)

    if record is None:
        print("Student not found.")
    else:
        display_student(record)


def update_mark():
    """Update a mark using the student's course position."""
    student_id = input("Enter student ID: ").strip()
    record = find_student(student_id)

    if record is None:
        print("Student not found.")
        return

    if not record["courses"]:
        print("This student has no courses yet.")
        return

    print("Courses:", record["courses"])

    course = input("Enter course to update: ").strip()

    if course not in record["courses"]:
        print("Course not found.")
        return

    # Find the course's index so we update its corresponding mark.
    course_index = record["courses"].index(course)

    try:
        new_mark = float(input("Enter new mark (0-100): "))

        if not 0 <= new_mark <= 100:
            print("Mark must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    record["marks"][course_index] = new_mark
    print("Mark updated successfully.")


def add_course():
    """Add a course and its corresponding mark."""
    student_id = input("Enter student ID: ").strip()
    record = find_student(student_id)

    if record is None:
        print("Student not found.")
        return

    course = input("Enter course name: ").strip()

    if course in record["courses"]:
        print("This student already has that course.")
        return

    try:
        mark = float(input("Enter mark for the course (0-100): "))

        if not 0 <= mark <= 100:
            print("Mark must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    # Add the course and mark at corresponding positions.
    record["courses"].append(course)
    record["marks"].append(mark)

    print("Course and mark added successfully.")


def remove_course():
    """Remove a course and its corresponding mark."""
    student_id = input("Enter student ID: ").strip()
    record = find_student(student_id)

    if record is None:
        print("Student not found.")
        return

    course = input("Enter course to remove: ").strip()

    if course not in record["courses"]:
        print("Course not found.")
        return

    # Both values must be removed at the same index.
    # Otherwise, the remaining courses and marks could become
    # misaligned.
    course_index = record["courses"].index(course)
    record["courses"].pop(course_index)
    record["marks"].pop(course_index)

    print("Course and corresponding mark removed.")


def display_unique_courses():
    """Display every unique course across the class."""
    unique_courses = set()

    for record in records:
        for course in record["courses"]:
            unique_courses.add(course)

    print("Unique courses:", sorted(unique_courses))


def display_students_by_course():
    """Find students taking a selected course."""
    course = input("Enter course to search for: ").strip()
    found_students = []

    for record in records:
        if course in record["courses"]:
            found_students.append(record["name"])

    if found_students:
        print(f"Students taking {course}:", found_students)
    else:
        print("No students found for that course.")


def create_backup():
    """Create an independent backup of nested student records."""
    global backup

    # A deep copy prevents edits to nested lists in the original
    # records from changing the backup.
    backup = copy.deepcopy(records)
    print("Backup created successfully.")


def restore_backup():
    """Restore records from the most recent backup."""
    global records, backup

    if backup is None:
        print("No backup exists yet.")
        return

    # Deep-copy again so the restored records and saved backup
    # do not share mutable nested structures.
    records = copy.deepcopy(backup)
    print("Records restored from backup.")


# MENU LOOP:
#
# The while loop keeps the system running until the user exits.
# Each menu choice calls a separate function, making the program
# easier to read and maintain.
while True:
    print("\n========== STUDENT RECORD MANAGER ==========")
    print("1. View all students")
    print("2. Add a student")
    print("3. Search for a student")
    print("4. Update a student's mark")
    print("5. Add a course")
    print("6. Remove a course")
    print("7. Display unique courses")
    print("8. Display students taking a course")
    print("9. Display a selected student's record")
    print("10. Create a backup")
    print("11. Restore the backup")
    print("0. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        display_all_students()

    elif choice == "2":
        add_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_mark()

    elif choice == "5":
        add_course()

    elif choice == "6":
        remove_course()

    elif choice == "7":
        display_unique_courses()

    elif choice == "8":
        display_students_by_course()

    elif choice == "9":
        student_id = input("Enter student ID: ").strip()
        record = find_student(student_id)

        if record is None:
            print("Student not found.")
        else:
            display_student(record)

    elif choice == "10":
        create_backup()

    elif choice == "11":
        restore_backup()

    elif choice == "0":
        print("Exiting Student Record Manager. Goodbye!")
        break

    else:
        print("Invalid option. Please choose from the menu.")


# ============================================================
# FINAL REFLECTION
# ============================================================
#
# Lists were useful for ordered collections that can change.
# Tuples represented fixed ordered collections.
# Sets handled uniqueness and membership operations.
# Dictionaries organized labelled student information.
#
# Nested structures let us represent realistic records, but
# they require careful navigation and consistent relationships.
#
# References and copies behave differently: a reference points
# to the same object, a shallow copy shares nested objects,
# and a deep copy recursively copies nested structures.
#
# Choosing a data structure depends on the information and
# operations the program needs, not just the syntax available.