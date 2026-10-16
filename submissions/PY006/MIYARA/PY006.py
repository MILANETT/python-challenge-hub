def calculate_avg(mark1,mark2,mark3):
    total = mark1 + mark2 +mark3
    return total/3

students = []

for i in range(2):
    name = input(f"Enter the name of student{i}:")
    m1 = int(input(f"Enter mark1 of student{i}:"))
    m2 = int(input(f"Enter mark2 of student{i}:"))
    m3 = int(input(f"Enter mark3 of student{i}:"))

    avg = calculate_avg(m1,m2,m3)
    students.append((name,avg))

for name , avg in students:
    print(f"Name:{name} : Average:{avg:.2f}")


print("=============================")
age  = 18 # Variable defined outside (Global Variable)
def voter(age_of_voter):
    if age_of_voter >= age:
        return "Eligible"
    return "Not eligible"
print(voter(21)) 
# Prints eligible so the function can access a global variable 

def checks ():
    num = 2
    if num % 2 == 0 :
        return "Even"
    return"Odd"
print(checks())
#print(num)
#ERROR - num is not defined hence a variable defined in a func cannot be accessed outside 
#     print(num)
#           ^^^
# NameError: name 'num' is not defined. Did you mean: 'sum'?

num1 = 3
def sum ():
    num1 = 5
    return num1 + 4
print("Sum of 2 numbers",sum())#Uses the local variable 
print(f"Sum of 2 nums:{num1 + 5}")#Uses the global variable 


students = 3
def modify():
     # students = students + 1 
    global students 
    students = students + 1
    return students
print("Students:",modify())
#ERROR -  Tried modifying a gloval variable inside a func 
#     students = students + 1
#                ^^^^^^^^
# UnboundLocalError: cannot access local variable 'students' where it is not associated with a value

total_global = 0
def add_using_global(a, b):
    global total_global
    total_global = a + b 
    return total_global 
print(add_using_global(5,7))            # hidden side effect

def add_using_return(a, b):
    return a + b  

print(add_using_return(7,8))

#BUGGGG 1
#     m2 = int(input("Enter mark2 of student:",i))
#              ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: input expected at most 1 argument, got 2
# What went wrong: input() accepts only one argument,
#  the prompt string. You passed two: the string and i. 
# Unlike print(), which accepts any number of arguments separated by commas,
#  input() cannot take extra values to display.


#BUGGGG 2
#     students.append(name,avg)
#     ~~~~~~~~~~~~~~~^^^^^^^^^^
# TypeError: list.append() takes exactly one argument (2 given)
# What went wrong: append() adds exactly one item to a list.
#  Writing append(name, avg) hands it two separate items, so Python refuses.
# Fix: wrap the two values into one item, such as a tuple, 
# so they are added together as a single entry.


# DIfference between Defining and callng a function
# Defining means writing the function with def - It stores the instructions and runs nothing. 
# Calling means using the function’s name with brackets therefore executing the code.

#Difference between parameters and Arguments
# Parameters are the variable names listed in the function definition. They are placeholders. 
# Arguments are the actual values you pass  when calling the function.

#Difference between return and print()
# return sends a value back to the code that called the function, so it can be stored or used in further calculations.
# print() only displays text on the screen. The value is not available to the program afterwards.

# A local variable is created inside a function and exists only while that function runs.
#  A global variable is created outside all functions and is visible throughout the program.
#  A function can read a global directly, but to modify one it must declare it with the global keyword.
#  Local variables are safer because they can’t be changed accidentally by other parts of the program.



