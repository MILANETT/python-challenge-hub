# ============================================================
# PY003: STUDENT INTRODUCTION GENERATOR
# Topics: Input, Output and String Basics
# ============================================================


# STEP 1: Collect information from the user.
#
# input() displays a prompt and waits for the user to type
# a response. The response is returned as a string.
#
# strip() removes whitespace from the beginning and end
# of the response, helping us avoid unwanted extra spaces.
full_name = input("Enter your full name: ").strip()
course = input("Enter your course: ").strip()
university = input("Enter your university: ").strip()
favourite_language = input(
    "Enter your favourite programming language: "
).strip()


# STEP 2: Prepare the course name for display.
#
# title() capitalizes the first letter of each word.
# It creates a new string; it does not modify the original.
display_course = course.title()


# STEP 3: Check that the name is not empty.
#
# If the name is empty, accessing its first or last character
# would cause an IndexError. We therefore handle that case.
if full_name:

    # STEP 4: Display the student profile.
    #
    # An f-string inserts variable values directly into text.
    # Multiplying a string by 32 repeats it 32 times.
    print("=" * 32)
    print("       STUDENT PROFILE")
    print("=" * 32)

    print(f"Name: {full_name}")
    print(f"Course: {display_course}")
    print(f"University: {university}")
    print(f"Favourite Language: {favourite_language}")

    # STEP 5: Perform string operations on the name.
    #
    # len() returns the number of characters, including spaces
    # between words.
    print(f"\nName length: {len(full_name)}")

    # Python string indexing starts at 0.
    # Index 0 gives the first character.
    print(f"First character of name: {full_name[0]}")

    # Negative indexing counts backwards from the end.
    # Index -1 gives the last character.
    print(f"Last character of name: {full_name[-1]}")

    # Display a personalized closing message.
    print(f"\nThank you, {full_name}!")
    print("=" * 32)

else:
    # This branch runs when the user submits an empty name.
    # It prevents the program from trying to index an empty string.
    print("Name cannot be empty. Please enter a name.")


# ============================================================
# DEBUGGING INVESTIGATION
# ============================================================
#
# Suppose we tried to run this statement:
#
# print(full_name[100])
#
# If the name were shorter than 101 characters, Python would
# raise an IndexError because index 100 would be out of range.
#
# The problem is not that indexing is incorrect. The problem
# is that the requested position does not exist in the string.
#
# We use full_name[0] for the first character and
# full_name[-1] for the last character instead.
#
# The invalid statement is deliberately left as a comment,
# so it does not interrupt the working program.


# ============================================================
# TESTING NOTES
# ============================================================
#
# Test 1:
# Name entered: Peter Mwangi
# Expected length: 12
# Expected first character: P
# Expected last character: i
#
# Test 2:
# Name entered: "   Peter Mwangi   "
# After strip(): "Peter Mwangi"
# Expected length: 12
#
# Test 3:
# Submit an empty name.
# Expected behavior: display an error message rather than
# attempting to access the first or last character.
#
# Test 4:
# Enter different profile information and check that the
# output reflects the values you supplied.