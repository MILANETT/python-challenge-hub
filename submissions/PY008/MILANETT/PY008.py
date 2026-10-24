"""
PY008 — The Function Toolkit
Complete the TODOs to build your Personal Study Toolkit.

Use Python 3.10+ for match/case.
Write docstrings for every function and add comments that explain
important decisions, experiments, and design choices.
"""


# Part 1: *args
def summarize_scores(*scores):
    """Return a summary of the supplied scores. TODO: complete."""
    # TODO: Return a useful result for zero or more scores.
    if scores:
        #Calculating the count of the scores
        scores_count=len(scores)
        #Calculating the average of the scores
        total_scores = 0
        for score in scores:
            total_scores += score

        average_score=total_scores/scores_count


        print(f"Number of scores: {scores_count}\nAverage score:{average_score}")
    else:
        print("Please pass some scores!!")

#Testing summarize_scores
#When values have been passed
#summarize_scores(50,51,52,53,54)
#Output:Number of scores: 5 , Average score:52.0
#When no scores are passed
#summarize_scores()
#Output:Please pass some scores!!


# Part 1: **kwargs
def build_student_report(**details):
    """Return a readable report from keyword details. TODO: complete."""
    print("\n____STUDENT REPORT_____")
    print(f"Name: {details['name']}")
    print(f"Student ID: {details['student_id']}")
    print(f"Age: {details['age']}")
    print(f"Average Score: {details['average_score']}")

#Testing build_student_report
#Passing only the keyword arguments in the function
build_student_report(name="Milan", student_id="S001",age=21,average_score=91)
#Output: Name: Milan Student ID: S001 Age: 21 Average Score: 91
#Displays the report normally

#Passing only one keyword argument from the function body and the rest new ones
#build_student_report(name="Stephanie", gender="F" ,stream=21)
#Output: Name: Stephanie, KeyError: 'student_id'
#The keyword details must match the function body requirements

# Part 2: default and keyword arguments
def format_session_report(student, duration=30, subject="Python"):
    """Format a study-session report. TODO: complete.
    every student has a default duration of 30 minutes
    every student has their default subject as python
    """
    print("\n_______STUDENT STUDY SESSION REPORT_______")
    print(f"Student Name: {student}")
    print(f"Duration Studied: {duration}")
    print(f"Subject: {subject}")

#Example
#Passing only the non_default parameter
format_session_report("Milan")
#Output:_______STUDENT STUDY SESSION REPORT_______ ,Student Name: Milan ,Duration Studied: 30 ,Subject: Python
#Passing all parameters
format_session_report("Stephanie", 45, subject = "C++")
#Output:_______STUDENT STUDY SESSION REPORT_______,Student Name: Stephanie,Duration Studied: 45,Subject: C++
format_session_report("Paul", 50)
#Output: _______STUDENT STUDY SESSION REPORT_______,Student Name: Paul,Duration Studied: 50,Subject: Python
#Conclusion: The default parameters only use the default value when none is passed to them but can accept
#arguments which override the default argument

# Part 3: positional-only and keyword-only parameters
def describe_session(student, /, subject, *, duration):
    """Demonstrate positional-only and keyword-only parameters. TODO: complete.
    student = positional
    subject= not specified, can take either form
    duration = keyword
    """
    print("\n___SESSION DESCRIPTION___")
    print(f"{student.capitalize()} studied {subject} for {duration} minutes.")

#Test
#Correct call
describe_session("DAISY","Python",duration=45)
#Output:Daisy studied Python for 45 minutes.
#Incorrect call to see whether the implementations can be mixed
#describe_session(student="DAISY","Python",duration=45)
#Output: SyntaxError: positional argument follows keyword argument
#The function expects the argument to be passed as a value only not with a key since it is strictly declared positional

# Part 5: function composition
def clean_name(name):
    """Return a cleaned version of a name. TODO: complete.
    Takes a name given in any format and Capitalizes it to make it clean
    """
    return name.capitalize()



def make_greeting(name):
    """Return a greeting for a cleaned name. TODO: complete.
    Takes the cleaned name from the clean_name function and prints a GREETING """
    print(f"\nHello, {clean_name(name)}")

#Testing using a lowercase name
make_greeting("francesca")

# Part 5: higher-order function
def apply_operation(value, operation):
    """Apply the supplied function to value. TODO: complete.
    The function allows either of the two operations: squaring it or cubing it
    """
    if operation == "square_value":
        #A lambda function is necessary here to help define a function on the go for an inner function operation
        square_value = lambda : value*value
        print("\n__SQUARE OPERATION__")
        print(f"The square of {value} is {square_value()}")

    elif operation == "cube_value":
        cube_value = lambda : value*value*value
        print("\n__CUBE OPERATION__")
        print(f"The cube of {value} is {cube_value()}")

    else:
        print("Entered a valid operation")

#Tests
#Squaring a value
apply_operation(2,"square_value")
apply_operation(3,"cube_value")





# Part 6: lambda
# TODO: Create and use a short lambda expression where appropriate.


# Part 7: recursion
def factorial(number:int):
    """Return the factorial of a non-negative integer. TODO: complete.
    Takes any non-negative integer and calculates its factorial
    """

    if number == 0 or number == 1:
        #base case
        return 1
    else:
        #recursive case
        return number * factorial(number-1)

#Test
print("\n")
#Base case input
print(factorial(1))
#Ordinary input
print(factorial(6))
#The base case helps the recursion to know when to stop and in this case when it arrives at one it knows that
#it should no longer proceed calling itself


# Part 8: menu with match/case
def main():
    """Display the toolkit menu and call the relevant functions. TODO: complete.
        A menu that allows the user to perform either of the four tasks:
        1. Summarize a list of given scores
        2. Build a student report
        3. Make a greeting
        4. Find the square and/or cube of a number
        5. Calculate factorial of a number
        6. Exit the program
    """
    # TODO: Include at least four choices and a default case.
    print("====== A Student's Handy Toolkit ======")
    print("1. Describe a Student's Study Session")
    print("2. Make a greeting")
    print("3. Find the square and/or cube of a number")
    print("4. Calculate factorial of a number")
    print("5. Exit the program")



    while True:
        choice = input("\nEnter a number from 1 to 5\n")
        match choice:
            case "1":
                print("___Describe a Student's Study Session___")
                student=input("Enter student's name: ")
                subject=input("Enter subject's name: ")
                duration=int(input("Enter the duration: "))
                describe_session(student,subject, duration=duration)
            case "2":
                print("___Make a greeting___")
                name = input("Who do you wish to greet: ")
                make_greeting(name)
            case "3":
                print("___Find the square and/or cube of a number___")
                value=int(input("Enter the number: "))
                operation=input("Enter the operation(square_value or cube_value): ").strip().lower()
                apply_operation(value, operation)
            case "4":
                print("___Calculate factorial of a number___")
                number=int(input("Enter the number : "))
                print(factorial(number))
            case "5":
                break
            case _:
                print("Please enter a valid choice!!!")



if __name__ == "__main__":
    main()
