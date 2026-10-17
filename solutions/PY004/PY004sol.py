# ============================================================
# PY004: STUDENT PERFORMANCE ANALYZER
# Topics: Conditional Statements, Loops, Validation,
#         Counters, Accumulators and Nested Loops
# ============================================================


# STEP 1: Ask how many students will be entered.
#
# input() returns a string, so int() converts the response
# into an integer that we can use with range().
number_of_students = int(
    input("How many students would you like to enter? ")
)


# STEP 2: Initialize the grade counters.
#
# A counter keeps track of how many times something occurs.
# Each counter starts at zero because no students have
# been processed yet.
grade_A = 0
grade_B = 0
grade_C = 0
grade_D = 0
grade_E = 0


# STEP 3: Initialize the running total and extreme values.
#
# total_marks is an accumulator: it collects marks as
# students are processed.
#
# We use None for the highest and lowest marks because
# no valid mark has been entered yet.
total_marks = 0
highest_mark = None
lowest_mark = None

# Store all valid marks in a list.
# We will use this list later to examine repeated marks.
marks = []


# STEP 4: Process each student.
#
# range(number_of_students) produces the required number
# of iterations. student_number starts at zero, so we add
# one when displaying the student number to the user.
for student_number in range(number_of_students):

    print(f"\nStudent {student_number + 1}")

    student_name = input("Enter student name: ").strip()


    # STEP 5: Validate the mark using a while loop.
    #
    # We do not know how many attempts the user might need.
    # Therefore, the while loop keeps asking until a valid
    # mark is entered.
    while True:

        mark_input = input("Enter student mark: ").strip()

        # isdigit() checks whether the string contains digits.
        # It rejects inputs such as "abc" and "-5".
        if mark_input.isdigit():

            # Convert the validated digit string to an integer.
            mark = int(mark_input)

            # Nested conditional:
            # first check that the input is numeric, then
            # check whether the mark is within the valid range.
            if 0 <= mark <= 100:

                # break immediately exits the validation loop.
                # Execution continues after the while loop.
                break

            else:
                print(
                    "Invalid mark. Enter a mark between 0 and 100."
                )

                # continue skips the rest of this iteration
                # and returns to the beginning of the while loop.
                continue

        else:
            print("Invalid input. Enter a whole number.")

            # Ask again because the input was not numeric.
            continue


    # STEP 6: Determine the student's grade.
    #
    # The conditions must be checked from the highest grade
    # threshold to the lowest.
    #
    # For example, a mark of 85 also satisfies mark >= 40.
    # Checking the highest threshold first ensures that 85
    # receives an A instead of a lower grade.
    if mark >= 70:
        grade = "A"
        grade_A += 1

    elif mark >= 60:
        grade = "B"
        grade_B += 1

    elif mark >= 50:
        grade = "C"
        grade_C += 1

    elif mark >= 40:
        grade = "D"
        grade_D += 1

    else:
        grade = "E"
        grade_E += 1


    # STEP 7: Display the individual student's result.
    print(f"\nStudent: {student_name}")
    print(f"Mark: {mark}")
    print(f"Grade: {grade}")


    # STEP 8: Update the accumulator and save the mark.
    #
    # Each valid mark contributes to the class total.
    # append() adds the current mark to the end of the list.
    total_marks += mark
    marks.append(mark)


    # STEP 9: Find the highest and lowest marks.
    #
    # For the first student, initialize both values using
    # their mark. This avoids starting with an arbitrary number.
    if highest_mark is None:
        highest_mark = mark
        lowest_mark = mark

    else:
        # Update the highest mark only when a larger mark
        # is found.
        if mark > highest_mark:
            highest_mark = mark

        # Update the lowest mark only when a smaller mark
        # is found.
        if mark < lowest_mark:
            lowest_mark = mark


    # STEP 10: Demonstrate a nested loop.
    #
    # The inner loop examines the marks collected so far.
    # It counts how many times the current mark appears.
    #
    # Since the current mark has already been appended,
    # occurrences will be at least one.
    occurrences = 0

    for previous_mark in marks:

        if previous_mark == mark:
            occurrences += 1

    # If occurrences is greater than one, the same mark
    # has appeared more than once in the collected list.
    if occurrences > 1:
        print("This mark has occurred more than once in the class.")


# STEP 11: Calculate and display the class summary.
#
# If zero students were entered, we must not divide by zero.
# The condition prevents an invalid average calculation.
if number_of_students > 0:

    average_mark = total_marks / number_of_students

    print("\n========== CLASS SUMMARY ==========")
    print(f"Number of students entered: {number_of_students}")
    print(f"Number who achieved an A: {grade_A}")
    print(f"Number who achieved a B: {grade_B}")
    print(f"Number who achieved a C: {grade_C}")
    print(f"Number who achieved a D: {grade_D}")
    print(f"Number who achieved an E: {grade_E}")
    print(f"Highest mark: {highest_mark}")
    print(f"Lowest mark: {lowest_mark}")
    print(f"Average mark: {average_mark:.2f}")

else:
    print("No students were entered.")


# ============================================================
# UNDERSTANDING pass
# ============================================================
#
# pass is a placeholder statement that does nothing.
# It can be useful when Python requires a statement but
# you have not implemented the behavior yet.
#
# Example:
#
# if mark == 100:
#     pass
#
# This is valid Python, but it does not change the result.
# We have not included this unnecessary condition in the
# main program because it serves no useful purpose there.
#
# ============================================================
# IMPORTANT LIMITATION
# ============================================================
#
# str.isdigit() accepts digit characters, but rejects
# negative numbers and decimal-formatted input such as "75.0".
# For whole-number marks from 0 to 100, that is acceptable.
# A more general input validator could use try/except.