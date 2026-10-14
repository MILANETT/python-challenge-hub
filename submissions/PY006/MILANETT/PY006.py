# Student score generator

#defining my function
def calculate_average(python_mark,statistics_mark,calculus_mark):
    total = python_mark + statistics_mark + calculus_mark
    average = total/3
    return average

#program to collect student details
max_students = 2
scores=[]
for student in range(max_students):
    name = input(f"\nStudent {student+1} name: ").capitalize()
    print("Enter your subject marks below")
    python_mark = int(input("Python: "))
    statistics_mark = int(input("Statistics: "))
    calculus_mark = int(input("Calculus: "))
    average_mark=calculate_average(python_mark,statistics_mark,calculus_mark)

#     #storing the score details
    scores.append({
        "name":name,
        "average":average_mark
    })

# print("=== Student Scores Report ===")
for score in scores:
    print(f"Student: {score['name']}")
    print(f"Average: {score['average']:.2f}")


#2. Variable Scope Experiments
# Use separate, small functions to investigate:

# (a) Whether a function can access a variable defined outside it.
#defining a variable outside
num_1 = 10
num_2 = 15
#defining my add function
def add_two_numbers():
    return num_1 + num_2

print(add_two_numbers())
#Output : 25 -> YES a function can access a variable defined outside it


# (b) Whether a variable defined inside a function can be accessed outside it.
def sub_two_numbers():
    num_4 = 54
    num_5 = 55
    return num_5-num_4

#print(num_5-num_4)
#Brought about a NameError: name 'num_5' is not defined. Did you mean: 'num_1'?
#NO , a variable defined inside a function cannot be accessed outside that function

# (c) What happens when a local variable and a global variable share the same name.
#global_variable
num_6 = 12
def product_fun():
    num_6=8 #local variable
    num_7= 9
    return num_6*num_7

print(product_fun())
#Output : 72
print(f"Global variable: {num_6}")
#Output : 12
#Conclusion, the local variable overrides the global variable inside the function but the global variable
# remains unchanged outside the function


# (d) What happens when you attempt to modify a global variable inside a function.
#global variable
x=4
def increment_x():
    x+=1
    return x
#print(increment_x())
#Output : UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
#Conclusion, a local variable cannot be modified inside a function


# (e) The difference between using global variables and passing arguments and returning results.
#Using global variables
x=6
y=3
def add_2_numbers():
    return x+y
print(add_2_numbers())
#Output : 9

#passing arguments
def add_2_numbersv2(x,y):
    return x+y

print(add_2_numbersv2(6,3))
#Output : 9

# 3. Testing and Reflection
#
# (a) Test your calculator with different marks, including at least one mark of "0".
#Student 1 name: Amina
# Enter your subject marks below
# Python: 89
# Statistics: 0
# Calculus: 88
#
# Student 2 name: Brian
# Enter your subject marks below
# Python: 76
# Statistics: 98
# Calculus: 0
# Student: Amina
# Average: 59.00
# Student: Brian
# Average: 58.00

# (b) Explain the difference between:

# - Defining and calling a function.
#Defining a function is where you create a function using the def keyword and ending it with parenthesis
# that either have or lack arguments and then declaring its body in it while calling a function is when you
# write the function's name with its parenthesis at the end with or without arguments depending on its
# nature so that it can accomplish a given task

#GOOGLE ASSISTANCE , I was not quite sure which was the placeholder and which was the actual value , I had
# to confirm since I use them interchangeably and google confirmed my doubts
# - Parameters and arguments.
#Parameters are the variables we list inside the parentheses of a function during definition to act as
# placeholders while Arguments are the actual values we pass into the function when calling it

# - "return" and "print()".
#return is a keyword used inside functions to tell the function what action it should provide back to the
# user that called it while print() is a keyword used inside or outside a function to output the given
# information to a user


# - Local and global variables.
#Local variables are variables that are declared and can only be accessed inside a function while global
# variables are variables declared outside the function and can be accessed inside or outside a function


# (c) Describe one bug you encountered and how you fixed it.
#I indented a function definition without my knowledge ,and it brought about an "Indentation Error"
#I fixed by unindenting the def and everything was back to normal