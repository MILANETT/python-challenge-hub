# Part 1
def summarize_scores(*args):  # *args accepts any number of positional arguments
    count = len(args)
    total = 0
    for arg in args:  # arguments stored in a tuple since they are positional arguments
        total = total + arg
    avg = total/count

    if count == 0:  # when no scores are supplied
        print("Count : 0 , Average: None ")

    print("Count:", count)
    print("Average:", avg)


summarize_scores(50, 70, 90)
# Output:
# Count: 3
# Average: 70.0


def stu_details(**kwargs):  # **kwargs accepts any number of keyword arguments
    # Arguments stored in a dictionary since they are keyword arguments
    print("Students name:", kwargs["fname"], " ", kwargs["lname"])


stu_details(fname="Monicah", lname="Miyara")
stu_details(fname="Elizabeth", lname="Rose")
print("======================================")

# Output:
# Students name: Monicah   Miyara
# Students name: Elizabeth   Rose


# Part 2
def time(no_of_hrs, day="Monday"):  # default param day = "Monday"
    print("Hours studied:", no_of_hrs)
    print("Day studied:", day)


time(no_of_hrs=7)  # Call using keyword argument
# Output
# Hours studied: 7
# Day studied: Monday

time(5,)  # Default value is used
# output
# Hours studied: 5
# Day studied: Monday

time(3, day="Friday")  # Default value is overridden
# Output
# Hours studied: 3
# Day studied: Friday


# Part 3
def pet(type, name, /):  # Accepts only positional arguments
    print("My pet is a", type, "and its name is", name)


pet("dog", "Bunny")
# Output :
# My pet is a dog and its name is Bunny


def course(*, name, school):  # Accepts only keyword arguements
    print("I study", name, "in a school called", school)


course(name="Data Science", school="JKUAT")
# Output
# I study Data Science in a school called JKUAT


# def course(*,name,school):
#     print("I study",name ,"in a school called",school)
# course("Data science","JKUAT")
# Tried calling my function by assigning it positional arguments instead of keyword args and got the following error
#     course("Data science","JKUAT")
#     ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: course() takes 0 positional arguments but 2 were given
# This means that when you use keyword only parameters then you should pass keyword arguments
# and not positional arguments

# Part 5
def sub(x):
    return x - 5


def pow(x):
    return x**2


def comp(x):  # A function composition
    return pow(sub(x))


print(" Composition 1:", comp(10))
# Output : Composition 1: 25
print("Composition 2:", comp(25))
# Output : Composition 2: 400

# Higher order funtion


def higher_func(x, func):
    return func(x)


print("Higher func 1:", higher_func(95, sub))
print("Higher func 2:", higher_func(7, pow))
# Output
# Higher func 1: 90
# Higher func 2: 49

# Part 6
# Used Ai
numbers = [60, 70, 40, 20, 50]
sorted_numbers = sorted(numbers, key=lambda x: -x)
print(sorted_numbers)
# Output:[70, 60, 50, 40, 20]
# Lambda is appropriate for this operation because the operation itself is small and
# single use and does not need a lengthy function that causes clutter.


# Part 7
def factorial(n):
    if n == 0:  # Base case so that function can stop calling itselt at n == 0
        return 1
    # Recursive case - reduces n until it reaches 0
    return n * factorial(n - 1)


print("Factorial of 3:", factorial(3))
print("Factorial of 0:", factorial(0))


# Part 8
def display_menu():
    print("\n =================================")
    print("1.Summarise the scores")
    print("2.Display the students details")
    print("3.Demonstrate the function composition")
    print("4.Calculate the factorial")
    print("5.Sort the numbers using lambda instead of function")
    print("0.Exit")


def run_menu():
    while True:
        display_menu()
        choice = input("Enter your choice:")

        match choice:
            case "1":
                summarize_scores(50, 70, 90)

            case "2":
                stu_details(fname="Monicah", lname="Miyara")

            case "3":
                number = int(input("Enter a number:"))
                print("Composition result:", comp(number))

            case "4":
                number = int(input("Enter a non negative number:"))
                if number < 0:
                    print("Please enter a non negative number")
                else:
                    print("Factorial:", factorial(number))

            case "5":
                numbers = [60, 70, 40, 20, 50]
                sorted_numbers = sorted(numbers, key=lambda x: -x)
                print("Sorted Numbers:", sorted_numbers)

            case "0":
                print("Exiting the menu!")
                break

            case _:
                print("Invalid choice!Please select a number between 0 and 5 ")


run_menu()
