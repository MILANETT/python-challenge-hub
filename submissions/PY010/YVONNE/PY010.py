students = ["Amina", "Brian", "Cynthia", "David"]

index = 0

while index < len(students):
    print(students[index])
#The loop did not terminate because the index was not incremented 
    index +=1

print("\n")
print("FOR LOOP")
for student in students:
    print(student)

print("\n")
#Suppose the list contains 100 records. Describe two different programming mistakes that 
# could cause records to be skipped or printed repeatedly.
   #i)not incrementing the loop could cause the loop to never terminate

print("\n")
print("!!!TRANSACTION PROCESSING!!!")
amounts = [120, 0, 75, -5, 210, -999, 90, 150]

print("IGNORE NEGATIVE AMOUNTS")
for amount in amounts:
    if amount<=0:
        continue
    print (amount)

print("\n")
print("Stop processing when the amount -999 is encountered.")
for amount in amounts:
    if amount == -999:
        break
    print(amount)

print("\n")
print("For every other positive amount, print it.")
for amount in amounts:
    if amount >= 0:
        print(amount)

print("\n")
print("TRANSACTION FUNCTION")
def department_Transaction(amount):
    for amount in amounts:
        if amount <= 0:
            continue

        elif amount == -999:
            break

        else :
            print(amount)

department_Transaction(amounts)

print("\n")
print("Dictionaries Within Dictionaries")
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
print("\n")
print("Each students name,department and ID")

for x,department in departments.items():
   print(x)

   for z,y in department.items():
      print(z)

      for k,l in y.items():
           if k=="name":
             print (k,":",l)

print("\n")
print("names of all students who are currently active")
for x,department in departments.items():
   
    for z,y in department.items():

         for k,l in y.items():
             if k == "active" and l==True:
               print (y["name"])

print("\n")
print("every student taking Python and print their name and department")
for x,department in departments.items():

   for z,y in department.items():

       if "Python" in y["units"]:
           print(y["name"],":",x)

    

print("\n")
print("Count how many students are registered in each department")
for x, department in departments.items():

    count = 0

    for z in department:
        count += 1

    print(x, ":", count)


print("\n")
print(" THE FUNCTION WORKSHOP")
print("\n")
print("Flexible Average")
def calculate_average(*marks):
        if not marks:
           return None

        sum=0                 
        for mark in marks:
            sum+=mark
            Average = sum/len(marks)
        return Average
    

print(calculate_average(100,100,100))
print(calculate_average(80,80))
print(calculate_average())

print("\n")
print("Configurable report")
def student_details(name,**others):
    print("STUDENT'S NAME:",name)
    print("STUDENT'S DEPARTMENT:",others["dept"])
    print("STIUDENT'S AVERAGE:",others["avg"])
    print("{} from {} department has an average of {}".format (name,others["dept"],others["avg"]))

student_details("Yvonne",dept="Data Science",avg=100)

print("\n")
print("Strict parameter positions")
def register_session(session_name,duration,/,*,instructor,room="Lab 1"):
    print("SESSION NAME:",session_name)
    print(f"DURATION:{duration} MINUTES")
    print("INSTRUCTOR:",instructor)
    print("ROOM:",room)


register_session("session one",30,instructor="Mbao",room="CLB 101")
register_session("session two",60,instructor="James")#will use the default

#register_session(session_name="Python Practice",duration=60,instructor="Grace")
#the above is invalid becoz session name and durtion must be positional and not keyword argument
#register_session("Python Practice",60,"Grace")
#the above is invalid because the instructure name takes a keyword argument not positional

print("\n")
print("FUNCTION COMPOSITION AND HIGHER ORDER FUNCTIONS")
print("Building a Processing Pipeline ")
name = "   aMINA wanjiku   "
def clean_name(name):
    """REMOVE WHITE SPACES"""
    name=name.strip()
    return name
   
def format_name(name):
    """CORRECT FORMAT"""
    name=name.title()
    return name

def make_greeting(name):
    """ADD A GREETING"""
    return "Hello" + "" +name

print(clean_name(name))#removes white spaces
print(format_name(name))#Capitilizes the first letter of each word
print(make_greeting(name))#adds hello greeting before name

print(format_name(clean_name(name)))#Capitilizes the first letter of each word after romoving spaces
print(make_greeting(format_name(clean_name(name))))#adds hello after Capitilizing the first letter of each word after romoving spaces

print("\n")
print("Higher order function")
def apply_operation(value, function):
    return function(value)


# Applying the clean_name  function
cleaned = apply_operation(name, clean_name)
print(cleaned)

# Applying the formatted  function  to cleanned name
formatted = apply_operation(cleaned, format_name)
print(formatted)

# Applying the greeting function to formatted and cleaned name
greeting = apply_operation(formatted, make_greeting)
print(greeting)

print("\n")
print("LAMBDAS AND RECURSION")
students = [
    {"name": "Amina", "score": 72},
    {"name": "Brian", "score": 91},
    {"name": "Cynthia", "score": 65},
    {"name": "David", "score": 84}
]

print("Sort the students by score from highest to lowest using sorted() and a lambda expression")
sorted_students_score=sorted(students,key= lambda x:x["score"])
print(sorted_students_score)

print("\n")
print("Sort the students alphabetically by name using a lambda expression.")
sorted_students_name=sorted(students,key=lambda x: x["name"])
print(sorted_students_name)
#sorted function soarts the lst according to the specified value eg mae/score to be used

print("\n")
print("RECURSION")
def recursive_sum(n):
    if n==0:#base case shows where the recursion stops
        return 0
    else:
        return n+ recursive_sum (n-1)

print(recursive_sum(5))
print(recursive_sum(3))
print(recursive_sum(1))
#the function calls itself until the  base case is reached and in each call it subtracts 1

print("\n")
print("MEMBERSHIP AND IDENTITY") 
print("Similar Does Not Mean Identical")
first = [10, 20, 30]
second = [10, 20, 30]
third = first

target = 20
#Predict the result of each expression before running the code
#target in first-TRUE
#target not in second-FALSE
#first == second-TRUE
#first is second-FALSE
#first is third-TRUE
print(f"TARGET IS IN FIRST:",target in first)
print(f"TARGET IS NOT IN SECON;D:",target not in second)
print(f"FIRST IS EQUAL SECOND:",first == second)
print("FIRST AND SECOND REFER TO SAME OBJECT IN MEMORY:",first is second)
print("FIRST AND SECOND REFER TO SAME OBJECT IN MEMORY:",first is third)
#membership operators(in,not in) check if a certain value is in a list of values
#identity operators(is ,is not) check if two objects are located in the same memory location
#(==) checks if two objects are similar
#identity operators would be appropriate when you want to check if two variables refer to same objects 
#rather than just similar contents

print("\n")
print("DEBUGGING CLINIC")
print("Diagnose Before You Repair")
#def find_first_positive(numbers):
#    for number in numbers:
#        if number <= 0:
#            continue
#        return number

#    print("No positive number found")
#Explain what happens when the list contains a positive number"
#It is returned  but if number is 0 or negative it skips
#"Explain what happens when the list contains no positive numbers."
#
print("Modify the function so it returns a consistent result in both cases. ")
print("Explain why return, continue, and printing a message are not interchangeable.")

def find_first_positive(*numbers):
    for number in numbers:
        if number <= 0:
            continue
        return number

    print("No positive number found")

print(find_first_positive(-3,0,-9))

def find_first_positive(*numbers):
    for number in numbers:
        if number <= 0:
            continue
        return number

    return None
print(find_first_positive(0,-4,5,7,12,-3))