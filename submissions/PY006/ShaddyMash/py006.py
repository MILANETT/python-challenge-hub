# PART 1 - CALCULATING THE AVERAGE

# This function takes three marks, calculates their average
# and returns the answer.
def calculate_average(mark1,mark2,mark3):
    average=(mark1+mark2+mark3)/3
    return average


# PART 2 - STUDENT SCORE CALCULATOR

print("===STUDENT SCORE CALCULATOR===\n")
print("First student details:")

# Getting the first student's name.
# The loop repeats if the name is left empty.
error=True
while error:    
    std1Name=input("Enter first student's name:")
    if std1Name=="":
        print("Field cannot be empty.")
        continue
    else:
        error=False
        continue

# Getting the first student's first mark.
# The mark must be between 0 and 100.
error=True
while error:
    try:
        std1mark1=float(input("Enter first mark:"))
        if std1mark1<0 or std1mark1>100:
            print("Invalid entry. Mark can only be from 0 to 100.")
        else:
            error=False
    except:
        print("Invalid entry. Field can only contain numbers and cannot be empty")

# Getting the second mark.
# try and except help prevent errors from wrong inputs.
error=True
while error:
    try:
        std1mark2=float(input("Enter second mark:"))
        if std1mark2<0 or std1mark2>100:
            print("Invalid entry. Mark can only be from 0 to 100.")
        else:
            error=False
    except:
        print("Invalid entry. Field can only contain numbers and cannot be empty")

# Getting the third mark.
error=True
while error:
    try:
        std1mark3=float(input("Enter third mark:"))
        print("\n")
        if std1mark3<0 or std1mark3>100:
            print("Invalid entry. Mark can only be from 0 to 100.")
        else:
            error=False
    except:
        print("Invalid entry. Field can only contain numbers and cannot be empty")

error=True

print("Second student details:")

# Getting the second student's name.
while error:    
    std2Name=input("Enter second student's name:")
    if std2Name=="":
        print("Field cannot be empty.")
        continue
    else:
        error=False
        continue

# Getting the second student's first mark.
error=True
while error:
    try:
        std2mark1=float(input("Enter first mark:"))
        if std2mark1<0 or std2mark1>100:
            print("Invalid entry. Mark can only be from 0 to 100.")
        else:
            error=False
    except:
        print("Invalid entry. Field can only contain numbers and cannot be empty")

# Getting the second mark.
error=True
while error:
    try:
        std2mark2=float(input("Enter second mark:"))
        if std2mark2<0 or std2mark2>100:
            print("Invalid entry. Mark can only be from 0 to 100.")
        else:
            error=False
    except:
        print("Invalid entry. Field can only contain numbers and cannot be empty")

# Getting the third mark.
error=True
while error:
    try:
        std2mark3=float(input("Enter third mark:"))
        if std2mark3<0 or std2mark3>100:
            print("Invalid entry. Mark can only be from 0 to 100.")
        else:
            error=False
    except:
        print("Invalid entry. Field can only contain numbers and cannot be empty")


# Calling the same function for both students.
# This saves us from writing the calculation twice.
std1avg=calculate_average(std1mark1,std1mark2,std1mark3)
std2avg=calculate_average(std2mark1,std2mark2, std2mark3)

# Displaying the results to two decimal places.
print("===STUDENT REPORTS===\n")
print(f"Student: {std1Name}")
print(f"Average: {std1avg:.2f}\n")

print(f"Student: {std2Name}")
print(f"Average: {std2avg:.2f}\n")


# PART 3 - VARIABLE SCOPE

# EXPERIMENT 1 - ACCESSING A GLOBAL VARIABLE

# y is global because it is outside the function.
# x is local because it is created inside the function.
# The function can use the global variable y.
y=30
def vscope():
    x=25
    print(x+y)
vscope()

# EXPERIMENT 2 - ACCESSING A LOCAL VARIABLE OUTSIDE

# This causes an error because x only exists inside vscope.
# The except block catches the error.
try:
    print(x+y)
except:
    print("X is not a global variable therefore not defined outside the function")


# EXPERIMENT 3 - SAME VARIABLE NAME

# x is now created outside the function.
x=40
print(x)

# This y is local and does not change the global y.
def vscope2():
    y=40
    print(y)
vscope2()
print(y)

# The function prints 40 but the global y remains 30.
# This shows that the two variables are separate.


# EXPERIMENT 4 - CHANGING A GLOBAL VARIABLE

# The global keyword allows us to change a global variable
# from inside a function.

number=10

def change_number():
    global number
    number=20
    print(number)

change_number()
print(number)

# Both print 20 because the global number was changed.


# EXPERIMENT 5 - USING PARAMETERS AND RETURN

# Here I pass a number into the function instead
# of changing a global variable.

value=10

def add_number(value):
    value=value+5
    return value

result=add_number(value)

print(value)
print(result)

# The original value remains 10.
# The returned result is 15.
# This shows that we can get results without
# changing the original variable.


# PART 4 - TESTING

# Testing the average function with different marks.
# I also included zero to see if it works.

print("===TEST RESULTS===")

print(f"Test 1: {calculate_average(80,70,90):.2f}")
print(f"Test 2: {calculate_average(60,50,70):.2f}")
print(f"Test 3: {calculate_average(0,60,90):.2f}")
print(f"Test 4: {calculate_average(0,0,0):.2f}")

# Expected results:
# Test 1: 80.00
# Test 2: 60.00
# Test 3: 50.00
# Test 4: 0.00


# PART 5 - REFLECTION QUESTIONS


# 1. What is the difference between defining and calling a function?

# Defining a function is creating instructions for it to follow.
# Calling a function is telling Python to actually run those
# instructions.


# 2. What is the difference between a parameter and an argument?

# A parameter is the variable written when creating a function.
# An argument is the actual value we give that variable
# when calling the function.


# 3. Why is return useful compared to print?

# Return gives back an answer that I can store in a variable
# or use somewhere else in my code.
# Print only displays the answer on the screen.


# 4. What is the difference between local and global variables?

# A local variable is created inside a function and can
# normally only be used there.
# A global variable is created outside functions and can
# normally be accessed from both inside and outside.


# 5. What happened when you used the same variable name
# inside and outside a function?

# I noticed that changing the variable inside the function
# did not affect the one outside.
# Even though they had the same name, they were separate.


# 6. Why is passing arguments and returning results better
# than relying on global variables?

# It makes the function easier to reuse with different values.
# It also helps avoid accidentally changing variables
# that are being used in other parts of the program.


# 7. What mistake did you encounter and how did you debug it?

# I initially forgot to reset error to True before some
# of my while loops.
# This caused the loops to be skipped after entering
# a valid mark.
# I fixed it by resetting error to True before each loop.
# I also forgot to divide the total marks by 3 at first.
# I corrected the formula to calculate the actual average.


# FINAL REFLECTION

# I learned how functions can make calculations easier
# because I can use the same function more than once.
# I also understood the difference between return and print.
# The scope experiments helped me see how variables inside
# functions behave differently from those outside.
