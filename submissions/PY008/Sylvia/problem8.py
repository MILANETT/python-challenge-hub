"""
PY008 — The Function Toolkit
Complete the TODOs to build your Personal Study Toolkit.

"""

# Part 1: *args
def summarize_scores(*scores):
    total=0
    avg=0

    if not scores:
        print("No score was supplied")

    else:
        for score in scores:
            total+=score
            avg=total/len(scores)
        
    return print(f"The total of the scores is  {total} and the average is {avg} ")

#In this function, I used a for loop so that it iterates through the scores arguments
print(summarize_scores(50,34,23,67,28))
print(summarize_scores())

# Part 1: **kwargs
def build_student_report(**details):
    for key,value in details.items():
        print(f"{key}={value}")

print(build_student_report(name=" Sylvia Mugure ",course=" Data Science ",studentID=" DS001 "))

# Part 2: default and keyword arguments
def format_session_report(student, duration=30, subject="Python"):
    report=print(f"{student} studied {subject} for {duration} minutes")
    return report

format_session_report(student="Sylvia")
format_session_report(student="Andrew",duration=50,subject="Java")
format_session_report(student="Ethan",duration=70,subject="Javascript")

# Part 3: positional-only and keyword-only parameters
def describe_session(student, /, subject, *, duration):
    description=print("Student:",student,"\nSubject:",subject,"\nSession duration:",duration)
    return description

print(describe_session("Sylvia","Python",duration=30))
#Demonstrating what happens when you give positional arguments instead of keyword arguments
#print(describe_session("Sylvia","Python",30))
#TypeError:the function takes 2 positional arguments but 3 were given

# Part 5: function composition
def clean_name(name):
    cleaned_name=name.title().strip()
    return cleaned_name

print(clean_name(" sylvia "))

def make_greeting(name):
    greeting="Hello "+name
    return greeting

print(make_greeting(clean_name(" sylvia ")))

# Part 5: higher-order function
def apply_operation(operation_, operation):
    return operation_(operation)  

print(apply_operation(make_greeting, clean_name(" sylvia ")))

# Part 6: lambda
numbers = [3,5,2]
print(sorted(numbers, key=lambda number: number))
#it is reasonable since it does not require many definitions

# Part 7: recursion
def factorial(number):
    if number==0:
        return 1
    else:
        return number*factorial(number-1)

print(factorial(5))
print(factorial(1))
#The base case is necessary because it helps to stop the recursion

# Part 8: menu with match/case
def main():
    # TODO: Include at least four choices and a default case.
    tool=input("Choose a tool from the toolkit:")
    match tool:
        case "lambda_":
            print(sorted(numbers, key=lambda number: number))
        case "horder":
            print(apply_operation(make_greeting(clean_name(" sylvia "))))
        case "_factorial":
            print(factorial(5))
        case  "report":
            format_session_report(student="Andrew",duration=50,subject="Java")
        case _:
            print("Please choose an appropriate tool(lambda_,horder,_factorial,report)")
 

if __name__ == "__main__":
    main()