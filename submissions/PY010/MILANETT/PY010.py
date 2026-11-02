"""PY010 — Refinement Challenge starter file.

Complete the questions in the challenge README. You may keep your answers
in this file or organise them into separate files if that is clearer.
Use comments to explain reasoning and include tests for edge cases.
"""


# Question 1: The Repeating Records
# TODO: Correct the while-loop and write a for-loop version.
#a. Explain precisely why the program does not terminate. [3 marks]
#This is because the while loop lacks the flow, currently the loop knows that as long as the index is less than
# the length of the list it needs to print the content of that index position in the list but since the index
# remains zero from the start the program will print the first element infinitely.

# b. Correct the program using a while loop. [3 marks]
print("While loop implementation")
students = ["Amina", "Brian", "Cynthia", "David"]

index = 0

while index < len(students):
    print(students[index])
    index += 1

# c. Rewrite the solution using a for loop. [2 marks]
print("\nFor loop implementation")
for i in students:
    print(i)

# d. Suppose the list contains 100 records. Describe two different programming mistakes that could cause
# records to be skipped or printed repeatedly. [4 marks]
#Used AI's Assistance to get these concepts(Google's Gemini)
# 1. Incrementing inside an if block that isn't reached or incrementing by a number greater than 1, like,
# index += 2, which causes records to be skipped.

# 2. Resetting or modifying the index counter inside the loop body, causing previous records to be printed
# repeatedly.

# Question 2: Stop, Skip, or Finish?
# TODO: Write a function that uses continue, break, and return appropriately.
# a. Write a function that processes the following list according to the rules:
amounts = [120, 0, 75, -5, 210, -999, 90, 150]
def amts_processor(amts:list):
    valid_amounts=0
    for amt in amts:
        if amt == -999:
            # c. Use break to stop processing at the sentinel value. [3 marks]
            break
        elif amt <= 0:
            # b. Use continue to handle the values that should be skipped. [3 marks]
            continue
        else:
            print(amt)
            valid_amounts += 1

    # d. Return the number of valid amounts processed. [2 marks]
    return f"Number of Valid Amounts : {valid_amounts}"

print("\n")
print(amts_processor(amounts))

# e. Explain the difference between break, continue, and return in the context of your function. [4 marks]
# Break brings the loop the end of its cycle abruptly upon meeting the specified condition, continue tells the
# loop not to execute at the meeting of the specified condition but instead skip to the next and continue
# there then return exits the entire function immediately, stopping all execution and sending a value back to
# the caller

# Question 3: The Department Records
# TODO: Create the nested dictionary from the challenge and process it with loops.
departments = {
    "Computing": {
        "ST001": {
            "name": "Amina",
            "units": ["Python", "Statistics", "Databases"],
            "active": True
        },
        "ST002": {
            "name": "Brian",
            "units": ["Python", "Mathematics"],
            "active": False
        }
    },
    "Analytics": {
        "ST003": {
            "name": "Cynthia",
            "units": ["Statistics", "Python", "Geography"],
            "active": True
        },
        "ST004": {
            "name": "David",
            "units": ["Databases", "Geography"],
            "active": True
        }
    }
}

# a. Loop through the structure and print each student's name together with their department and student ID. [4 marks]
print("\nStudent's Name | Department | Student ID")
#Conclusion: actually storing the key in k stores the name of the key not the content of the key
for k in departments:
    for k1 in departments[k]:
        print(f"{departments[k][k1]["name"]:<14} | {k:<10} | {k1}")

# b. Print the names of all students who are currently active. [3 marks]
print("\nActive Students")
for k in departments:
    for k1 in departments[k]:
        if departments[k][k1]["active"]:
            print(f"{departments[k][k1]["name"]}")

# c. Find every student taking Python and print their name and department. [3 marks]
print("\nStudents taking Python")
for k in departments:
    for k1 in departments[k]:
        if "Python" in departments[k][k1]["units"]:
            print("\nStudent's Name | Department")
            print(f"{departments[k][k1]["name"]:<14} | {k:<10}")

# d. Count how many students are registered in each department. [2 marks]
print("\nNumber of students registered in each department")
for k in departments:
    print(f"{k}: {len(departments[k])}")


# e. Explain why looping through the outer dictionary alone does not directly give you each student's details. [2 marks]
#This is because it only accesses its immediate content not the content of its content's content

# Question 4: The Function Workshop
# TODO: Implement calculate_average(*args).
def calculate_average(*nums:int):
    if nums:
        total = 0
        for num in nums:
            total += num
        average = total/len(nums)
        return average
    else:
        return None
#Testing
print("\nZero Arguments")
print(calculate_average())
print("\nOne Argument")
print(calculate_average(3))
print("\nSeveral Arguments")
print(calculate_average(2,3,8,5))

# TODO: Implement build_report(name, **kwargs).
#Used AI ASSISTANCE(GEMINI) to understand how to return report as a string

def build_report(name, **details):
    report = f"Name: {name}"
    for key, value in details.items():
        report += f"\n{key}: {value}"
    return report

print("\nReport with additional details")
print(build_report("Jill", department="Computing", average=89 , academic_status="Active"))
print("\nReport without additional details")
print(build_report("Jill"))

# TODO: Implement register_session with positional-only and keyword-only parameters.
def register_session(session_name,duration,/,*,instructor,room="Lab 1"):
    print("Session Registered Successfully!!!")

print("\n Valid call for register_session()")
register_session(
    "Python Practice",
     60,
    instructor="Grace"
)
#Invalid Calls
# register_session(
#     session_name="Python Practice",
#     duration=60,
#     instructor="Grace"
# )
#Reason: session_name and duration have been passed as keyword ,yet they are specified as positional


# register_session(
#     "Python Practice",
#     60,
#     "Grace"
# )
#Reason: instructor is passed as positional, yet it is specified as keyword

#Briefly explain the purpose of *args, **kwargs, positional-only parameters, and keyword-only parameters. [2 marks]
#*args help in the case where the number of positional arguments are not known
#**kwargs help in the case where the number of keyword arguments are not known
#*positional-only arguments help ensure uniformity of passed arguments as positional mostly where the detail
# being passed is commonly known to avoid unnecessary repetition
#**keyword-only arguments help to ensure the detail entered is correctly matched and positioned , mostly where
# the detail passed is not commonly known


# Question 5: Building a Processing Pipeline
# TODO: Implement clean_name(), format_name(), make_greeting(), and apply_operation().
def clean_name(name):
    return name.strip()
def format_name(name):
    return clean_name(name).capitalize()
def make_greeting(name):
    return f"Hello {format_name(name)}!!!"

raw_name = "   aMINA wanjiku   "
composed_result = make_greeting(format_name(clean_name(raw_name)))
#Testing clean_name()
print(clean_name(raw_name))
#Testing format_name()
print(format_name(raw_name))
#Testing make_greeting()
print(make_greeting(raw_name))

#Combine the functions so that the original name passes through the three operations in the correct order
composed_result = make_greeting(format_name(clean_name(raw_name)))



#higher-order function apply_operation()
def apply_operation(value, operation):
    '''

    :param value: a name
    :param operation: clean_name(), format_name(), make_greeting()
    :return: the product of the operation
    '''
    return operation(value)

#Testing apply_operation() with clean_name()
print(apply_operation("billy",clean_name))
#Testing apply_operation() with make_greeting()
print(apply_operation("billy",make_greeting))


# Question 6: Small Functions, Big Ideas
students = [
    {"name": "Amina", "score": 72},
    {"name": "Brian", "score": 91},
    {"name": "Cynthia", "score": 65},
    {"name": "David", "score": 84}
]
# TODO: Sort the student records with lambda expressions.
#Sorting the students by score
sort_by_score = sorted(students, key = lambda x : x['score'],reverse=True)
#lambda returns the value of the score of a student and then sorted arranges them according to their numerical
# descending order using the score as a comparison key

#Sorting the students by score
sort_by_name = sorted(students, key = lambda x : x['name'])
#lambda returns the value of the name of a student and sorted() arranges them alphabetically using the name as
# a comparison key

# TODO: Implement recursive_sum(n), including a base case.
def recursive_sum(n):
    if n<1:
        return None
    #base case, it helps tell the program when to stop and what to do during stopping
    #function moves towards base case by decrementing the initial number by 1 progressively
    if n == 1:
        return 1
    return n + recursive_sum(n-1)
#Testing recursive_sum(n)
#Using the smallest input
print(recursive_sum(1))
#Using a moderate input
print(recursive_sum(9))
#Using an incorrect input
print(recursive_sum(-898))
#Reflection: What could happen if a recursive function never reaches its base case?
#My Comment:It will loop infinitely
#AI ASSISTED comment: Python will repeatedly add frames to the call stack until it exceeds the maximum recursion
# limit, raising a RecursionError

# Question 7: Similar Does Not Mean Identical
# TODO: Predict and then test the membership and identity expressions.
first = [10, 20, 30]
second = [10, 20, 30]
third = first

target = 20

# a. Predict the result of each expression before running the code. [4 marks]

# target in first - True
# target not in second - False
# first == second - True
# first is second - False
# first is third - True

print(target in first)
print(target not in second)
print(first == second)
print(first is second)
print(first is third)

# b. Explain the difference between the membership operators in and not in, and the identity operators is and
# is not. [2 marks]
#in returns True if a value is in the given structure and False otherwise
#not in returns True if a value is not in the given structure and False otherwise
#is returns True if the two given values point to the same memory address and False otherwise
#is not returns True if the two given values point to the different memory addresses and False otherwise

# c. Give one practical situation where checking identity is appropriate, and explain why checking equality
# would not express the same intention. [2 marks]
#My answer : Where you want to check whether a value references another
#AI ASSISTED ANSWER: Checking if a variable is None (if val is None:). Identity is required here because a
# custom class might implement __eq__ to return True for None, whereas is None strictly checks if the object
# is the singleton None in memory.

# Question 8: Diagnose Before You Repair
# TODO: Repair find_first_positive() and test positive, negative, and empty inputs.
#Initial function
def find_first_positive(numbers):
    for number in numbers:
        if number <= 0:
            continue
        return number

    print("No positive number found")

# a. Explain what happens when the list contains a positive number. [2 marks]
#It prints the first positive number it encounters then stops

# b. Explain what happens when the list contains no positive numbers. [3 marks]
# My answer: Returns No positive number found and  None since there is no positive number to print
#AI ASSISTED ANSWER(GEMINI): If no positive number exists, the loop finishes. Then print("No positive number
# found") executes. Because there is no explicit return statement at the bottom, Python implicitly returns None

# c. Modify the function so it returns a consistent result in both cases. [3 marks]
#Modified Function
def find_first_positive(numbers):
    for number in numbers:
        if number <= 0:
            continue

        return number


    return "No positive number found"

# d. Explain why return, continue, and printing a message are not interchangeable. [4 marks]
#return is what the function should produce ready to be used in any way while continue is skipping an
# iteration for a given condition or value while printing just displays the message
if __name__ == "__main__":
    # Add your own tests here. Keep challenge solutions understandable and
    # test them with both ordinary inputs and edge cases.
    pass
