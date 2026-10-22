print("PERSONAL STUDY TOOLKIT \n")

#FLEXIBLE PARAMETERS
print("!!!FLEXIBLE PARAMETERS!!!")
def summarize_scores(*scores):#arbitrary arguments (*args)..accept any number of arguments passed 
    sum=0                     #thrrough the function when its being called
    for score in scores:
        sum+= score
        average=sum/len(scores)
    return average

def student_Details(**details):#keyword arguments (*kwangs)..take any number of key=value argumrnts
    print("STUDENT NAME:",details["name"])#when the function is called
    print("STUDENT REGISTRATION NUMBER:",details["reg_NO"])
    print("STUDENT AGE:",details["age"])
    print(f"STUDENT AVERAGE MARK:{summarize_scores(100,80,90):.2f}")



student_Details(name="Yvonne",reg_NO="SCT213-C002-0024/2024",age=20)

print("\n")
#DEFAULT AND KEYWORD ARGUMENTS
print("!!!DEFAULT AND KEYWORD ARGUMENTS!!!")
def studySession_Report(name,topic,time=30):#creates a default study time duration time of 30 minutes
    """shows difference btwn default and keyword args"""
    print(f"{name} studied {topic} for {time} minutes")


studySession_Report("Statistics","Yvonne")
#Using the Keyword arguments prevents the incorrect placement of the arguments when the function is called 
#however when mixing both the positional args come before the keyword args
studySession_Report("Yvonne Biegon",topic="Statistics")
#during the function call the function automatically inputs the default time ie 30 minutes
studySession_Report(name="Yvonne Biegon",topic="Statistics",time=60)
#when you alocate another time value the function overrides the previous default value 

print("\n")
#Positional-only and keyword-only parameters
print("!!!POSITIONAL-ONLY AND KEYWORD-ONLY PARAMETER!!!")
def POSITIONALvsKEYWORD(fname,lname,/,reg_NO,School,*,position1,position2):
    """ Parameters before the / symbol must be passed positionally
       Parameters after the * symbol must be passed as keywords.
    fname,lname must be positional
    regn0,school can be either positional or keyword
    position1,position2 must be keyword"""
    print(f"My name is{fname} {lname},registration number {reg_NO} a student at {School}.\n I am also a {position1} and {position2}")

POSITIONALvsKEYWORD("Yvonne","Biegon","SCT213-C002-0024/2024",School="JKUAT",position1="GDG WIT lead",position2="Membership Coordinator Rotarcat Club of JKUAT")
#POSITIONALvsKEYWORD("Yvonne",lname="Biegon","SCT213-C002-0024/2024",School="JKUAT",position1="GDG WIT lead",position2="Membership Coordinator Rotarcat Club of JKUAT")
#the code above raises the error SyntaxError: positional argument follows keyword argument

print("\n")
print("!!!DOCSTRINGS AND USEFUL COMMENTS!!!")
# a string literal placed as the very first statement inside a function, method, class, or module

print("\n")
print("!!!FUNCTION COMPOSITION AND HIGHER-ORDER FUNCTIONS!!!")
#the output()function accepts another function as an argument
def ascend_NOs(list):
     list.sort()
     return list

def descend_NO(list):
    list.sort(reverse=True)
    return list

def output(func):
    outputs=func([21, 52, 38, 49, 57, 16, 7, 98])
    print(outputs)

output(ascend_NOs)
output(descend_NO)

print("\n")
print("!!!LAMBDA EXPRESSIONS!!!")
#Lambda function is an anonymous function
#It can take any number of arguments but can have only one expression
numbers = [21, 52, 38, 49, 57, 16, 7, 98]
even_Numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_Numbers)
#lists out the even numbers from the list

print("\n")
print("!!!RECURSION!!!")
#a function calls itself until the base case is reached
def sum_Recursion(n):
    if n==0 :
      return 0
    else:
        return n%10 + sum_Recursion(n//10)
print(sum_Recursion(1234))
#Sum of Digits: Extract the last digit and add it to the recursive result of the
#remaining digitsie 4+3+2+1

print("\n")
print("!!!MATCH CASES!!!")
choice=int(input("ENTER YOUR CHOICE:"))
match choice:
    case 1:
        student_Details(name="Yvonne",reg_NO="SCT213-C002-0024/2024",age=20)

    case 2:
        studySession_Report("Yvonne Biegon",topic="Statistics")

    case 3:
        POSITIONALvsKEYWORD("Yvonne","Biegon","SCT213-C002-0024/2024",School="JKUAT",position1="GDG WIT lead",position2="Membership Coordinator Rotarcat Club of JKUAT")

    case 4:
        print(sum_Recursion(1234))

    case _:
        print("MAKE A CHOICE BETWEEN 1-3")
    