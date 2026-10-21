#mini student program
#I used AI
#The list of dictionaries is used because we are storing multiple things that relate to one person
students = [
    {
        "name": "Daniel",
        "courses": ["Python", "SQL"],
        "marks": [75, 80]
    },
    {
        "name": "Amina",
        "courses": ["Python", "Java"],
        "marks": [85, 90]
    },
    {
        "name": "Brian",
        "courses": ["SQL", "HTML"],
        "marks": [70, 88]
    }
]

#These are the operations done on the data 

import copy

students = [
    {
        "name": "Daniel",
        "courses": ["Python", "SQL"],
        "marks": [75, 80]
    },
    {
        "name": "Amina",
        "courses": ["Python", "Java"],
        "marks": [85, 90]
    },
    {
        "name": "Brian",
        "courses": ["SQL", "HTML"],
        "marks": [70, 88]
    }
]

#the find_student function is used to search for a student by name. 
# It is placed first because it is used in the rest of the program to prevent duplication
def find_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            print("Student found:", student)
        else:
            print("Student not found.")
    return None

#view all students
def view_all_students():
    if not students:
        print("No student records found.")
        return

    for student in students:
        print(student["name"], "-", student["courses"],
              "-", student["marks"])

#adding new students
def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    if find_student(name):
        print("Student already exists.")
        return

    students.append({
        "name": name,
        "courses": [],
        "marks": []
    })
    print("Student added successfully.")

#This function checks through the names aand courses 
#in order to ensure the student exists and they are doing the course

def update_mark():
    name = input("Enter student name: ").strip()
    student = find_student(name)

    if not student:
        print("Student not found.")
        return

    course = input("Enter course name: ").strip()
    if course not in student["courses"]:
        print("Student is not taking that course.")
        return

    try:
        mark = float(input("Enter new mark (0-100): "))
    except ValueError:
        print("Enter a valid number.")
        return

    if not 0 <= mark <= 100:
        print("Mark must be between 0 and 100.")
        return

    index = student["courses"].index(course)
    student["marks"][index] = mark
    print("Mark updated successfully.")

#This function adds a course to a specific student
#It prevents duplication and validates the marks using try..except
def add_course():
    name = input("Enter student name: ").strip()
    student = find_student(name)

    if not student:
        print("Student not found.")
        return

    course = input("Enter course name: ").strip()

    if not course:
        print("Course name cannot be empty.")
        return

    if course in student["courses"]:
        print("Student already takes this course.")
        return

    try:
        mark = float(input("Enter mark (0-100): "))
    except ValueError:
        print("Enter a valid number.")
        return

    if not 0 <= mark <= 100:
        print("Mark must be between 0 and 100.")
        return

    student["courses"].append(course)
    student["marks"].append(mark)
    print("Course and mark added successfully.")


def remove_course():
    name = input("Enter student name: ").strip()
    student = find_student(name)

    if not student:
        print("Student not found.")
        return

    course = input("Enter course to remove: ").strip()

    if course not in student["courses"]:
        print("Course not found for this student.")
        return

    index = student["courses"].index(course)
    student["courses"].pop(index)
    student["marks"].pop(index)

    print("Course and corresponding mark removed.")

def unique_courses():
    courses = set()
    for student in students:
        courses.update(student["courses"])

    print("Unique courses:", sorted(courses))

def students_by_course():
    course = input("Enter course name: ").strip().lower()
    found = False

    for student in students:
        if any(c.lower() == course for c in student["courses"]):
            print(student["name"])
            found = True

    if not found:
        print("No students found taking that course.")


def selected_student_record():
    name = input("Enter student name: ").strip()
    student = find_student(name)

    if not student:
        print("Student not found.")
        return

    print("\nStudent:", student["name"])
    if not student["courses"]:
        print("No courses registered.")
        return

    print("Courses and marks:")
    for course, mark in zip(student["courses"], student["marks"]):
        print(f"{course}: {mark}")

    backup = copy.deepcopy(students)
    print("Backup created successfully.")
    print("Backup records:", backup)

def main():
    backup = None

    while True:
        print("\n--- STUDENT RECORDS MANAGEMENT ---")
        print("1. View all students")
        print("2. Add a student")
        print("3. Search for a student")
        print("4. Update a student's mark")
        print("5. Add a course")
        print("6. Remove a course")
        print("7. Display unique courses")
        print("8. Display students taking a course")
        print("9. Display a student's record")
        print("10. Create a backup")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_all_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            find_student()
        elif choice == "4":
            update_mark()
        elif choice == "5":
            add_course()
        elif choice == "6":
            remove_course()
        elif choice == "7":
            unique_courses()
        elif choice == "8":
            students_by_course()
        elif choice == "9":
            selected_student_record()
        elif choice == "10":
            print("Backup created successfully:",backup)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
