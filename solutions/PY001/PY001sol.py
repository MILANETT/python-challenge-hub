# ============================================================
# PY001: FINDING THE HIGHEST, LOWEST AND AVERAGE MARKS
# Topics: Variables, Lists, Loops, Conditions and Accumulators
# ============================================================

# STEP 1: Store the marks.
#
# A list allows us to keep multiple values in one variable.
# Each mark is an integer, and list indexing starts at 0.
marks = [72, 45, 89, 63, 51, 94, 38]


# STEP 2: Initialize the highest and lowest marks.
#
# We use marks[0] to access the first mark in the list.
# Initially, this mark is both the highest and lowest mark
# we have encountered because we have not checked the others.
#
# Starting with an actual mark is safer than assuming that
# marks are always positive or always below some arbitrary limit.
highest = marks[0]
lowest = marks[0]


# STEP 3: Initialize an accumulator.
#
# An accumulator is a variable that collects a result gradually.
# We start total at 0 because no marks have been added yet.
total = 0


# STEP 4: Examine every mark.
#
# The for loop visits each element in the list, one at a time.
# During each iteration, the variable 'mark' holds the current
# element being examined.
for mark in marks:

    # Compare the current mark with the highest mark found so far.
    # If the current mark is larger, update highest.
    if mark > highest:
        highest = mark

    # Compare the current mark with the lowest mark found so far.
    # If the current mark is smaller, update lowest.
    if mark < lowest:
        lowest = mark

    # Add the current mark to the running total.
    #
    # total += mark is shorthand for:
    # total = total + mark
    #
    # The updated total is retained for the next iteration.
    total += mark


# STEP 5: Calculate the average.
#
# The average is the total divided by the number of marks.
# len(marks) returns the number of elements in the list.
#
# We calculate this manually instead of using sum().
average = total / len(marks)


# STEP 6: Display the results.
#
# An f-string lets us insert variable values into text.
# :.2f formats the average to exactly two decimal places.
print(f"Highest mark: {highest}")
print(f"Lowest mark: {lowest}")
print(f"Average mark: {average:.2f}")


# ============================================================
# EXPECTED OUTPUT
# ============================================================
#
# Highest mark: 94
# Lowest mark: 38
# Average mark: 64.57
#
# ============================================================
# IMPORTANT NOTE
# ============================================================
#
# This solution assumes the list contains at least one mark.
# If the list were empty, marks[0] would cause an IndexError,
# and calculating an average would require handling that case.
#
# In this challenge, the list is provided and is non-empty.