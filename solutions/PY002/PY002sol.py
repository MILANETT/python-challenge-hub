# ============================================================
# PY002: STUDENT PERFORMANCE CHECKER
# Topics: Data Types, Type Conversion and Operators
# ============================================================


# STEP 1: Store the original information.
#
# Notice that age and the marks are strings, not integers.
# This is intentional: we will practise converting data types.
name = "Peter"
age = "20"
original_marks = ["72", "45", "89", "63", "51"]

# A Boolean represents a truth value: True or False.
has_submitted = True

# None represents the absence of a value.
# Here, it means that no bonus has been assigned yet.
bonus = None


# STEP 2: Convert the data into appropriate types.
#
# int() converts the string "20" into the integer 20.
# This allows us to perform numerical comparisons with age.
age = int(age)

# Convert each mark from a string to an integer.
#
# This is a list comprehension: it creates a new list by
# applying int() to every mark in original_marks.
#
# We preserve original_marks so we can later demonstrate
# membership checks on strings rather than integers.
marks = [int(mark) for mark in original_marks]


# STEP 3: Calculate the total and average without sum().
#
# total is an accumulator. It collects each mark as we loop
# through the list, starting from zero.
total = 0

for mark in marks:
    total += mark

# len(marks) tells us how many marks are in the list.
# Division with / produces a floating-point result.
average = total / len(marks)


# STEP 4: Evaluate the student's performance.
#
# Comparison operators return Boolean values: True or False.
is_adult = age >= 18
average_at_least_50 = average >= 50
average_at_least_70 = average >= 70

# has_submitted is already a Boolean, so bool() is redundant
# here. We include it to demonstrate explicit type conversion.
submitted = bool(has_submitted)

# The logical operator 'and' requires BOTH conditions
# to be True for the student to pass.
passed = average_at_least_50 and submitted


# STEP 5: Check whether particular marks are present.
#
# The 'in' operator checks membership in a collection.
# Since original_marks contains strings, we search for strings.
#
# For example, "89" is a string, while 89 is an integer.
# They represent the same digits but are different data types.
contains_89 = "89" in original_marks
contains_100 = "100" in original_marks

# 'not in' checks that an item is absent from a collection.
does_not_contain_100 = "100" not in original_marks


# STEP 6: Handle the bonus.
#
# 'is None' checks whether bonus refers to Python's None object.
# It is the conventional way to test for an absent value.
if bonus is None:
    bonus = 5

# Preserve the original average before applying the bonus.
original_average = average

# The augmented assignment operator '+=' adds the bonus
# to the existing value of average.
#
# This is equivalent to:
# average = average + bonus
average += bonus

final_average = average


# STEP 7: Display the report.
#
# :.2f formats floating-point values to two decimal places.
print(f"Student: {name}")
print(f"Age: {age}")
print(f"Total marks: {total}")
print(f"Average: {original_average:.2f}")
print(f"Adult: {is_adult}")
print(f"Passed: {passed}")
print(f"Average at least 70: {average_at_least_70}")
print(f"Contains 89: {contains_89}")
print(f"Contains 100: {contains_100}")
print(f"Does not contain 100: {does_not_contain_100}")
print(f"Bonus: {bonus}")
print(f"Final average: {final_average:.2f}")


# ============================================================
# EXPECTED OUTPUT
# ============================================================
#
# Student: Peter
# Age: 20
# Total marks: 320
# Average: 64.00
# Adult: True
# Passed: True
# Average at least 70: False
# Contains 89: True
# Contains 100: False
# Does not contain 100: True
# Bonus: 5
# Final average: 69.00
#
# ============================================================
# KEY LESSON
# ============================================================
#
# A program must use the right data types for the operations
# it performs. Strings are useful for text, integers for whole
# numbers, floats for decimal calculations, Booleans for
# truth values, and None for the absence of a value.
#
# Also notice that 'passed' is evaluated using the original
# average, before the bonus is applied. The final average
# is a separate result.