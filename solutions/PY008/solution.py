"""PY008 — The Function Toolkit: reference implementation.

Run this file with Python 3.10 or newer.
"""


def summarize_scores(*scores):
    """Return the count and average for zero or more scores.

    The average is None when no scores are supplied because an empty
    collection has no meaningful average.
    """
    count = len(scores)

    if count == 0:
        return {"count": 0, "average": None}

    total = 0
    for score in scores:
        total += score

    return {"count": count, "average": total / count}


def build_student_report(**details):
    """Return a readable report containing the supplied keyword details."""
    if not details:
        return "No student details were supplied."

    lines = ["Student Report"]
    for key, value in details.items():
        # Keep this function flexible: the caller chooses which fields exist.
        readable_key = key.replace("_", " ").title()
        lines.append(f"{readable_key}: {value}")

    return "\n".join(lines)


def format_session_report(student, duration=30, subject="Python"):
    """Return a study-session report, using defaults when omitted."""
    return f"{student} studied {subject} for {duration} minutes."


def describe_session(student, /, subject, *, duration):
    """Return a session description with positional-only and keyword-only inputs."""
    return f"{student} studied {subject} for {duration} minutes."


def clean_name(name):
    """Remove surrounding whitespace and normalize a name's capitalization."""
    return name.strip().title()


def make_greeting(name):
    """Return a greeting, composing clean_name() with the greeting format."""
    return f"Hello, {clean_name(name)}!"


def square(number):
    """Return the square of a number."""
    return number * number


def cube(number):
    """Return the cube of a number."""
    return number * number * number


def apply_operation(value, operation):
    """Apply the supplied function to value and return its result."""
    # Accepting a function object makes this a higher-order function.
    return operation(value)


def factorial(number):
    """Return the factorial of a non-negative integer using recursion."""
    if number < 0:
        raise ValueError("Factorial is defined here only for non-negative integers.")

    if number == 0:
        # The base case stops recursion; 0! is 1.
        return 1

    # Each call uses a smaller number and moves towards the base case.
    return number * factorial(number - 1)


def show_score_summary():
    """Collect scores and display their count and average."""
    raw_scores = input("Enter scores separated by spaces (or press Enter for none): ").split()

    try:
        scores = [float(raw_score) for raw_score in raw_scores]
    except ValueError:
        print("Please enter numbers separated by spaces.")
        return

    summary = summarize_scores(*scores)
    print(f"Count: {summary['count']}")
    if summary["average"] is None:
        print("Average: not available (no scores supplied)")
    else:
        print(f"Average: {summary['average']:.2f}")


def main():
    """Run the Personal Study Toolkit menu until the user chooses to exit."""
    while True:
        print("\n===== Personal Study Toolkit =====")
        print("1. Summarize scores")
        print("2. Build a student report")
        print("3. Format a study-session report")
        print("4. Describe a study session")
        print("5. Make a greeting")
        print("6. Apply a higher-order operation (square or cube)")
        print("7. Sort study sessions using a lambda")
        print("8. Calculate a factorial")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                show_score_summary()

            case "2":
                name = input("Student name: ").strip()
                course = input("Course: ").strip()
                report = build_student_report(name=name, course=course)
                print(report)

            case "3":
                student = input("Student name: ").strip()
                subject = input("Subject [Python]: ").strip() or "Python"
                raw_duration = input("Duration in minutes [30]: ").strip()

                if raw_duration:
                    try:
                        duration = int(raw_duration)
                    except ValueError:
                        print("Duration must be a whole number.")
                        continue
                else:
                    duration = 30

                print(format_session_report(student, duration, subject))

            case "4":
                student = input("Student name: ").strip()
                subject = input("Subject: ").strip()
                raw_duration = input("Duration in minutes: ").strip()

                try:
                    duration = int(raw_duration)
                except ValueError:
                    print("Duration must be a whole number.")
                    continue

                print(describe_session(student, subject, duration=duration))

            case "5":
                name = input("Who would you like to greet? ")
                print(make_greeting(name))

            case "6":
                raw_number = input("Enter a number: ").strip()
                try:
                    number = float(raw_number)
                except ValueError:
                    print("Please enter a number.")
                    continue

                operation_choice = input("Choose square or cube: ").strip().lower()
                match operation_choice:
                    case "square":
                        operation = square
                    case "cube":
                        operation = cube
                    case _:
                        print("Choose either square or cube.")
                        continue

                print(apply_operation(number, operation))

            case "7":
                sessions = [
                    ("Mathematics", 45),
                    ("Python", 30),
                    ("Statistics", 60),
                    ("Geography", 25),
                ]
                # The lambda is short and useful as a one-off sorting key.
                sorted_sessions = sorted(sessions, key=lambda session: session[1])
                print("Sessions from shortest to longest:")
                for subject, duration in sorted_sessions:
                    print(f"{subject}: {duration} minutes")

            case "8":
                raw_number = input("Enter a non-negative whole number: ").strip()
                if not raw_number.isdigit():
                    print("Please enter a non-negative whole number.")
                    continue

                print(f"{raw_number}! = {factorial(int(raw_number))}")

            case "0":
                print("Goodbye!")
                break

            case _:
                print("Unrecognised choice. Please choose one of the listed options.")


if __name__ == "__main__":
    main()
