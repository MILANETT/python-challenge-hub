"""PY010 — Refinement Challenge: reference implementation.

Run with Python 3.10 or newer.
This solution uses built-in Python features and concepts covered in the
group's Phase 0–4 progression. It does not use try/except or raise.
"""


# Question 1: The Repeating Records

def print_student_names(students):
    """Print every student name once using a while loop."""
    index = 0

    while index < len(students):
        print(students[index])
        index += 1


def print_student_names_with_for(students):
    """Print every student name once using a for loop."""
    for student in students:
        print(student)


# Question 2: Stop, Skip, or Finish?

def process_amounts(amounts):
    """Print valid amounts before the sentinel and return their count."""
    valid_count = 0

    for amount in amounts:
        # Check the sentinel first: it ends processing, even though it is negative.
        if amount == -999:
            break

        if amount <= 0:
            continue

        print(amount)
        valid_count += 1

    return valid_count


# Question 3: The Department Records

departments = {
    "Computing": {
        "ST001": {
            "name": "Amina",
            "units": ["Python", "Statistics", "Databases"],
            "active": True,
        },
        "ST002": {
            "name": "Brian",
            "units": ["Python", "Mathematics"],
            "active": False,
        },
    },
    "Analytics": {
        "ST003": {
            "name": "Cynthia",
            "units": ["Statistics", "Python", "Geography"],
            "active": True,
        },
        "ST004": {
            "name": "David",
            "units": ["Databases", "Geography"],
            "active": True,
        },
    },
}


def print_department_students(department_records):
    """Print each student's name, department, and student ID."""
    for department_name, students in department_records.items():
        for student_id, student_details in students.items():
            print(
                f"{student_details['name']} | "
                f"{department_name} | {student_id}"
            )


def print_active_students(department_records):
    """Print the names of students whose active value is True."""
    for students in department_records.values():
        for student_details in students.values():
            if student_details["active"]:
                print(student_details["name"])


def print_python_students(department_records):
    """Print the name and department of every student taking Python."""
    for department_name, students in department_records.items():
        for student_details in students.values():
            if "Python" in student_details["units"]:
                print(f"{student_details['name']} | {department_name}")


def count_students_per_department(department_records):
    """Return a dictionary containing each department's student count."""
    counts = {}

    for department_name, students in department_records.items():
        counts[department_name] = len(students)

    return counts


# Question 4: The Function Workshop

def calculate_average(*args):
    """Return the average of the supplied numbers, or None if empty."""
    if len(args) == 0:
        return None

    total = 0
    for number in args:
        total += number

    return total / len(args)


def build_report(name, **kwargs):
    """Return a student report containing any supplied named details."""
    lines = [f"Student: {name}"]

    if not kwargs:
        lines.append("No additional details supplied.")
    else:
        for detail_name, detail_value in kwargs.items():
            readable_name = detail_name.replace("_", " ").title()
            lines.append(f"{readable_name}: {detail_value}")

    return "\n".join(lines)


def register_session(session_name, duration, /, *, instructor, room="Lab 1"):
    """Return a session summary with enforced positional and keyword inputs."""
    return (
        f"{session_name} | {duration} minutes | "
        f"Instructor: {instructor} | Room: {room}"
    )


# Question 5: Building a Processing Pipeline

def clean_name(name):
    """Remove spaces from the beginning and end of a name."""
    return name.strip()


def format_name(name):
    """Convert a name to title case."""
    return name.title()


def make_greeting(name):
    """Return a greeting containing the supplied name."""
    return f"Hello, {name}!"


def make_clean_greeting(name):
    """Pass a name through cleaning, formatting, and greeting operations."""
    cleaned_name = clean_name(name)
    formatted_name = format_name(cleaned_name)
    return make_greeting(formatted_name)


def apply_operation(value, operation):
    """Apply a supplied function to a value and return its result."""
    return operation(value)


# Question 6: Small Functions, Big Ideas

students = [
    {"name": "Amina", "score": 72},
    {"name": "Brian", "score": 91},
    {"name": "Cynthia", "score": 65},
    {"name": "David", "score": 84},
]


def sort_students_by_score(student_records):
    """Return student records ordered from highest score to lowest."""
    return sorted(
        student_records,
        key=lambda student: student["score"],
        reverse=True,
    )


def sort_students_by_name(student_records):
    """Return student records ordered alphabetically by name."""
    return sorted(
        student_records,
        key=lambda student: student["name"],
    )


def recursive_sum(n):
    """Return 1 + 2 + ... + n for a non-negative integer n."""
    if n == 0:
        return 0

    return n + recursive_sum(n - 1)


# Question 7: Similar Does Not Mean Identical

def demonstrate_membership_and_identity():
    """Display the results of the supplied membership and identity checks."""
    first = [10, 20, 30]
    second = [10, 20, 30]
    third = first
    target = 20

    print("target in first:", target in first)
    print("target not in second:", target not in second)
    print("first == second:", first == second)
    print("first is second:", first is second)
    print("first is third:", first is third)


# Question 8: Diagnose Before You Repair

def find_first_positive(numbers):
    """Return the first positive number, or None when there is no match."""
    for number in numbers:
        if number <= 0:
            continue

        return number

    return None


def main():
    """Run representative examples for the PY010 reference solution."""
    print("QUESTION 1")
    names = ["Amina", "Brian", "Cynthia", "David"]
    print_student_names(names)
    print_student_names_with_for(names)

    print("\nQUESTION 2")
    amounts = [120, 0, 75, -5, 210, -999, 90, 150]
    print("Valid amounts processed:", process_amounts(amounts))

    print("\nQUESTION 3")
    print_department_students(departments)
    print("Active students:")
    print_active_students(departments)
    print("Students taking Python:")
    print_python_students(departments)
    print("Department counts:", count_students_per_department(departments))

    print("\nQUESTION 4")
    print("No values:", calculate_average())
    print("One value:", calculate_average(8))
    print("Several values:", calculate_average(8, 10, 12))
    print(build_report("Amina"))
    print(build_report("Brian", department="Computing", average=84, academic_status="Active"))
    print(register_session("Python Practice", 60, instructor="Grace"))
    print(register_session("Statistics Lab", 90, instructor="Daniel", room="Lab 3"))

    print("\nQUESTION 5")
    name = "   aMINA wanjiku   "
    print("Cleaned greeting:", make_clean_greeting(name))
    print("Uppercase through higher-order function:", apply_operation(name, str.upper))
    print("Greeting through higher-order function:", apply_operation("Amina", make_greeting))

    print("\nQUESTION 6")
    print("By score:", sort_students_by_score(students))
    print("By name:", sort_students_by_name(students))
    print("recursive_sum(0):", recursive_sum(0))
    print("recursive_sum(5):", recursive_sum(5))
    print("recursive_sum(10):", recursive_sum(10))

    print("\nQUESTION 7")
    demonstrate_membership_and_identity()

    print("\nQUESTION 8")
    print(find_first_positive([0, -4, 12, 8]))
    print(find_first_positive([-3, 0, -9]))
    print(find_first_positive([]))


if __name__ == "__main__":
    main()
