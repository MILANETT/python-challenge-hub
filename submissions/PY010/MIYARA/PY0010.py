#Question 1
students = ["Amina", "Brian", "Cynthia", "David"]

index = 0

# while index < len(students):
#     print(students[index])
# The original program didn't terminate because index
# was never incremented inside the loop, making the condition index < len(students) 
# permanently True causing an infinite loop.

while index < len(students):
    print(students[index])
    index += 1  # increments index so the loop eventually terminates
# Output :
# Amina
# Brian
# Cynthia
# David

for i in students:
    print(i)
# Output:
# Amina
# Brian
# Cynthia
# David

#Mistakes that can cause records to be skipped or printed repeatedly
# Skipped records - Incrementing by more than 1:
# If you accidentally write index += 2 instead of index += 1, the loop will jump by twos. 

# Repeated printing / Infinite loop -Decrementing the index-:
# If you accidentally write index -= 1 instead of index += 1, the index moves backwards causing the loop to re-print previous records or get trapped in an infinite loop going in reverse.


#Question 2 
amounts = [120, 0, 75, -5, 210, -999, 90, 150]


def process(amounts):
    count = 0
    for i in amounts:
        if i == -999:
            break #Stop processing at -999
        if i <= 0:
            continue #Handles values that should be skipped 
        count += 1
        print(i)
    return count #Gives back the count of numbers that satisfy all checks.

# Output:
# 120
# 75
# 210
print("Valid amounts processed:", process(amounts))
# Output:Valid amounts processed 3

#break:Terminates the entire for loop. When the code hits -999, break exits the loop entirely,
#  preventing any values that appear after the sentinel (like 90 and 150) from being processed.
#continue:Skips the remainder of the current loop iteration and jumps straight to the next item 
# in the list. When the loop encounters 0 or -5, continue skips printing and counting, moving directly to the next amount.
#return: Exits the entire function block, sending the final valid_count value back to the caller 
# (result) and halting any further code execution inside that function.

#Question 3
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

#Printing out each student's name together with their department and student ID.
for dep, details in departments.items():
    for id, deets in details.items():
        print("Students ID:", id, ", Students Name:",
              deets['name'], ", Students Department:", dep)

 # Output :
# Students ID: ST001 , Students Name: Amina , Students Department: Computing
# Students ID: ST002 , Students Name: Brian , Students Department: Computing
# Students ID: ST003 , Students Name: Cynthia , Students Department: Analytics
# Students ID: ST004 , Students Name: David , Students Department: Analytics

# Looping through the outer dictionary alone only yields 
# department names and their values (which are inner dictionaries containing student IDs), 
# not the individual student details (name, units, active status). You must nest a second 
# loop to access the inner dictionary values.

print("-"*40)
print("All Students who are currently active:")
#Printing names of students who are currently active 
for dep, details in departments.items():
    for deets in details.values():
        if deets["active"]:
            print(deets["name"])

# Output:
# All Students who are currently active:
# Amina
# Cynthia
# David

#Printing names and departments of students taking python
for dep, details in departments.items():
    for deets in details.values():
        for i in deets["units"]:
            if i == "Python":
                print("Name:", deets["name"], ", Department:", dep)

# Output:
# Name: Amina , Department: Computing
# Name: Brian , Department: Computing
# Name: Cynthia , Department: Analytic

#Counting students registered in each department 
for dep, details in departments.items():
    count = 0
    for student_id in details:
        count += 1
    print("Department:", dep, "Count:", count)

#Output:
# Department: Computing Count: 2
# Department: Analytics Count: 2

# Looping through the outer dictionary alone only gives you the department keys 
# e.g, Computing and Analytics and their values, which are entire inner dictionaries containing 
# multiple student IDs. It does not unpack the individual student keys or their attributes (name, units, active). 
# To access student details, you must use a nested loop to go one level deeper into the inner dictionary structure.

#Question 4
def calculate_average(*args):
    if args == ():
        return None
    total = 0
    for i in args:
        total += i
    return total/len(args)


print(calculate_average())
print(calculate_average(50))
print(calculate_average(50, 60, 70))
#Output:
# None
# 50.0
# 60.0

# def build_report(name,**details):
#     print("Student's name:",name)
#     print("Student's details:",details)


def build_report(name, **details):
    report_lines = [f"Student Report: {name}"]

    if details:
        for key, value in details.items():
            formatted_key = key.replace("_", " ").capitalize()
            report_lines.append(f"- {formatted_key}: {value}")
    else:
        report_lines.append("- No additional details provided.")

    return "\n".join(report_lines)


print(build_report(name="Monicah", department="Computing",
      average=94, academic_status="Active"))
# Output:
# Student Report: Monicah
# - Department: Computing
# - Average: 94
# - Academic status: Active

print("-"*40)


def register_session(session_name, duration, *, instructor, room="Lab 1"):
    return f"Session name:{session_name} , Duration:{duration} , Instructor:{instructor} , Room:{room}"


print(register_session("Python Basics", 90, instructor="Dianah"))
# Output : Session name:Python Basics , Duration:90 , Instructor:Dianah , Room:Lab 1

# Invalid because the function only accepts positional arguments for session name and duration and not keyword arguments
# register_session(
#     session_name="Python Practice",
#     duration=60,
#     instructor="Grace"
# )

# Invalid because the function only accepts posiitonal arguments for session name and duration and not for instructor name
# register_session(
#     "Python Practice",
#     60,
#     "Grace"
# )

# *args: Returns any number of extra positional arguments into a tuple.
# **kwargs: Returns any number of extra keyword arguments into a dictionary.
# Positional-only parameters (/): Forces parameters to be passed positionally.
# Keyword-only parameters (*): Forces callers to pass parameters using keywords.


#Question 5 
def clean_name(name):
    return name.strip()


def format_name(name):
    return name.title()


def make_greeting(name):
    return f"Hello, {name}!"

print(clean_name(name = "   aMINA wanjiku   "))
print(format_name(name = "   aMINA wanjiku   "))
print(make_greeting(name = "   aMINA wanjiku   "))
#Output:
# aMINA wanjiku
#    Amina Wanjiku   
# Hello,    aMINA wanjiku   !

print(make_greeting(format_name(clean_name(name = "   aMINA wanjiku   "))))
#Output: Hello, Amina Wanjiku!
def comp(name):#Combining the functions 
    return make_greeting(format_name(clean_name(name)))

print(comp("   miyARa   "))
#Output: Hello, Miyara!

def apply_operation(x,func):#Higher-order function 
    return func(x)

print(apply_operation("   MoNicah ",clean_name))
#output :MoNicah
print(apply_operation("nIveah",format_name))
#Output:Niveah
print(apply_operation("   mWaasss", comp))
#Output:Hello, Mwaasss!


#Question 6
students = [
    {"name": "Amina", "score": 72},
    {"name": "Brian", "score": 91},
    {"name": "Cynthia", "score": 65},
    {"name": "David", "score": 84}
]
sorted_students = sorted(students, key=lambda student: student["score"], reverse=True)
print(sorted_students)
#Output:
# [{'name': 'Brian', 'score': 91},
#  {'name': 'David', 'score': 84},
#  {'name': 'Amina', 'score': 72},
#  {'name': 'Cynthia', 'score': 65}]

sorted_alpha= sorted(students, key=lambda student: student["name"])
print(sorted_alpha)
#Output:
# [{'name': 'Amina', 'score': 72},
#  {'name': 'Brian', 'score': 91},
#  {'name': 'Cynthia', 'score': 65},
#  {'name': 'David', 'score': 84}]

#The lambda expression evaluates each dictionary item 
# and returns a specific value e.g student["score"] or student["name"]. 
# sorted() uses that returned value to compare elements and determine their order.

def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)


print(recursive_sum(5))
print(recursive_sum(10))
print(recursive_sum(1))
#Used AI
# Base case: `if n <= 0: return 0`. It is necessary to stop the recursion from running infinitely.
# Moving towards base case: Each recursive call passes `n - 1`, decreasing `n` until it hits `0`.
# Reflection (Infinite recursion): If a recursive function never reaches its base case, 
# Python will exhaust its call stack limit and raise a RecursionError.

#Question 7
first = [10, 20, 30]
second = [10, 20, 30]
third = first

target = 20
first = [10, 20, 30]
second = [10, 20, 30]
third = first

target = 20


print(target in first)
#True
print(target not in second)
#False
print(first == second)
#True
print(first is second)
#False
print(first is third)
#True


# Membership operators in checks if a value exists inside a collection , returns a value that's not in a collection.
# Identity operators (is, is not) check if two variables point to the exact same object in memory.
# Practical use of identity: Checking `val is None` to verify if an optional variable/argument 
# has been initialized or unassigned, because `None` is a unique singleton object.

def find_first_positive(numbers):
    for number in numbers:
        if number <= 0:
            continue
        return number

    print("No positive number found")

print(find_first_positive([0, -4, 12, 8]))
print(find_first_positive([-3, 0, -9]))
print(find_first_positive([]))

#When a positive number exists, the function skips non-positive values with continue 
# and immediately returns the first positive number.
# When no positive number exists, it prints the message and implicitly returns None because 
# there is no explicit return statement at the end.
# To make it consistent, add return None at the end instead of relying on print.
# return exits the function and passes back a value, continue skips to the next loop iteration,
# print only displays output to the console and does not alter control flow or return data.