
# PY006 — Reusable Functions: From Instructions to Results
# Phase 4: Functions

# ============================================================
# PART 1: BUILD A REUSABLE FUNCTION
# ============================================================

def calculate_average(mark1, mark2, mark3):
    # Parameters receive the values passed when the function is called.
    average = (mark1 + mark2 + mark3) / 3

    # return sends the calculated value back to the caller.
    return average


# Calling the same function with different arguments.
average_one = calculate_average(80, 75, 85)
average_two = calculate_average(60, 55, 65)

print("PART 1: TESTING THE FUNCTION")
print(f"First average: {average_one:.2f}")
print(f"Second average: {average_two:.2f}")


# ============================================================
# PART 2: STUDENT PERFORMANCE
# ============================================================

print("\nPART 2: STUDENT PERFORMANCE")

# Collect information for the first student.
name_one = input("Enter the first student's name: ")

mark_one_a = float(input("Enter the first mark: "))
mark_one_b = float(input("Enter the second mark: "))
mark_one_c = float(input("Enter the third mark: "))

# Reuse the function instead of repeating the calculation.
student_one_average = calculate_average(
    mark_one_a, mark_one_b, mark_one_c
)

# Collect information for the second student.
name_two = input("\nEnter the second student's name: ")

mark_two_a = float(input("Enter the first mark: "))
mark_two_b = float(input("Enter the second mark: "))
mark_two_c = float(input("Enter the third mark: "))

student_two_average = calculate_average(
    mark_two_a, mark_two_b, mark_two_c
)

# Display the results.
print("\nSTUDENT RESULTS")
print(f"{name_one}'s average: {student_one_average:.2f}")
print(f"{name_two}'s average: {student_two_average:.2f}")


# ============================================================
# PART 3: UNDERSTANDING VARIABLE SCOPE
# ============================================================

# Experiment 1: Accessing a global variable inside a function.

class_name = "Data Science"

def display_class():
    print(f"Class name inside function: {class_name}")

display_class()

# Observation:
# class_name was created outside the function.
# The function can read it because it is a global variable.


# Experiment 2: A local variable.

def create_message():
    local_message = "Hello from inside the function!"
    print(local_message)

create_message()

# Observation:
# local_message was created inside create_message().
# It can be accessed inside that function.
# It cannot be accessed directly outside the function.
#
# To observe this, remove the comment symbol from the line below
# and run the program again:
#
# print(local_message)
#
# Python will report a NameError because local_message
# does not exist in the outside scope.


# Experiment 3: Global and local variables with the same name.

score = 90  # Global variable.

def display_score():
    score = 50  # Local variable with the same name.
    print(f"Score inside function: {score}")

display_score()

print(f"Score outside function: {score}")

# Observation:
# Inside the function, score refers to the local variable.
# Outside the function, score refers to the global variable.
# The local assignment does not change the global score.


# Experiment 4: Passing information through arguments and return.

def increase_count(count):
    # count receives the argument passed to the function.
    count = count + 1

    # Return the updated value.
    return count


attendance_count = 10

new_attendance_count = increase_count(attendance_count)

print("\nPARAMETERS AND RETURN VALUES")
print(f"Original attendance count: {attendance_count}")
print(f"Returned attendance count: {new_attendance_count}")

# Observation:
# The function calculates and returns a new value.
# attendance_count remains 10 because we did not assign
# the returned value back to attendance_count.
#
# If we wanted to update the original variable, we could write:
#
# attendance_count = increase_count(attendance_count)
#
# This uses a return value and assignment rather than modifying
# a global variable inside the function.


# ============================================================
# REFLECTION
# ============================================================

# 1. Defining a function creates it; calling a function executes it.
#
# 2. A parameter is a variable in the function definition.
#    An argument is the value supplied when calling the function.
#
# 3. print() displays information; return sends a value back
#    to the part of the program that called the function.
#
# 4. A local variable belongs to a function's local scope.
#    A global variable is defined outside functions.
#
# 5. Parameters and return values make functions easier to reuse
#    and reduce dependence on shared global variables.
