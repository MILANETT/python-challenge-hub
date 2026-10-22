

# Accept any number of scores using *args
def summarize_scores(*scores):
    """Calculate the number of scores and their average."""

    # Handle empty scores to avoid division by zero
    if not scores:
        return 0, None

    total = 0

    # Add all the scores together
    for score in scores:
        total += score

    # Return the count and average
    return len(scores), total / len(scores)


# Accept student details using **kwargs
def student_report(**details):
    """Return student details as a readable report."""

    report = ""

    # Go through each student detail
    for key, value in details.items():
        report += f"{key}: {value}\n"

    # Return the complete report
    return report


# Create a study report with a default status
def study_session(subject, minutes, status="Completed"):
    """Display a study session report."""

    print(subject, minutes, "minutes", status)


# Demonstrate positional-only and keyword-only arguments
def study_plan(subject, /, *, minutes):
    """Display a study plan."""

    print("Study", subject, "for", minutes, "minutes")


# Incorrect usage experiments:
# study_plan(subject="Python", minutes=30)
# TypeError: subject must be passed positionally.

# study_plan("Python", 30)
# TypeError: minutes must be passed as a keyword.


# Convert hours into minutes
def to_minutes(hours):
    """Convert hours to minutes."""

    return hours * 60


# Add a 10-minute break to study time
def add_break(minutes):
    """Add a break to study time."""

    return minutes + 10


# Higher-order function that accepts another function
def apply_function(func, number):
    """Apply a given function to a number."""

    # This design allows different functions to be reused
    return func(number)


# Calculate factorial using recursion
def factorial(n):
    """Calculate the factorial of a non-negative integer."""

    # Base case stops the recursion
    if n == 0:
        return 1

    # Recursive case moves towards zero
    return n * factorial(n - 1)


# Keep displaying the menu until the user exits
while True:

    print("\nSTUDY TOOLKIT")
    print("1. Scores")
    print("2. Student Report")
    print("3. Study Session")
    print("4. Factorial")
    print("5. Tests")
    print("0. Exit")

    # Ask the user to choose an option
    choice = input("Choose: ")

    # Catch invalid numerical inputs without stopping the program
    try:

        match choice:

            case "1":
                scores = []

                # Get scores separated by spaces
                values = input("Enter scores: ").split()

                # Convert the scores into numbers
                for value in values:
                    scores.append(float(value))

                # Display the number of scores and average
                print(summarize_scores(*scores))

            case "2":

                # Get student details
                name = input("Name: ")
                course = input("Course: ")

                # Print the report returned by the function
                print(student_report(name=name, course=course))

            case "3":

                # Get subject and study duration
                subject = input("Subject: ")
                minutes = int(input("Minutes: "))

                # Display study session using default status
                study_session(subject, minutes)

                # Use positional and keyword arguments
                study_plan(subject, minutes=minutes)

            case "4":

                # Get the number for factorial
                n = int(input("Number (0-10): "))

                # Only allow numbers between 0 and 10
                if 0 <= n <= 10:
                    print(factorial(n))
                else:
                    print("Invalid number")

            case "5":

                # Test *args with multiple and empty scores
                print(summarize_scores(70, 80, 90))
                print(summarize_scores())

                # Test **kwargs with different student details
                print(student_report(name="John", age=20))
                print(student_report(name="Mary", course="Python"))

                # Test default and overridden parameters
                study_session("Python", 30)
                study_session("Math", 40, status="Pending")

                # Test positional-only and keyword-only arguments
                study_plan("Python", minutes=30)

                # Function composition: convert hours, then add a break
                print(add_break(to_minutes(2)))

                # Test higher-order function with two functions
                print(apply_function(to_minutes, 2))
                print(apply_function(add_break, 30))

                # Create sample study sessions
                sessions = [("Math", 40), ("Python", 20)]

                # Lambda is suitable for this short sorting operation
                print(sorted(sessions, key=lambda x: x[1]))

                # Test recursion using base and ordinary cases
                print(factorial(0))
                print(factorial(5))

            case "0":

                # Exit the loop and end the program
                print("Goodbye")
                break

            case _:

                # Handle unrecognised menu choices
                print("Invalid choice")

    # Handle letters or invalid values where numbers are expected
    except ValueError:
        print("Invalid input! Please enter a valid number.")

