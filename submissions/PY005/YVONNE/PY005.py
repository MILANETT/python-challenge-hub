students = [
    {
        "name": "Daniel",
        "student_id": "DS001",
        "courses": ["Python", "Statistics", "Databases"],
        "marks": [78, 64, 82]
    },
    {
        "name": "Amina",
        "student_id": "DS002",
        "courses": ["Python", "Statistics", "Databases"],
        "marks": [91, 73, 88]
    },
    {
        "name": "Brian",
        "student_id": "DS003",
        "courses": ["Python", "Statistics", "Databases"],
        "marks": [56, 68, 61]
    }
]

class_rooms = ("Room A", "Room B", "Room C")

python_students = {"Daniel", "Amina", "Brian"}
database_students = {"Daniel", "Amina", "Brian"}

#students-Dictitoinary..key value attributes..stored in a list
#courses and marks-list
#python_students and database_students-set
#class_rooms-tuple
#student_records-Dictionary
#courses and marks-lists

          #LISTS
print("!!!!LISTS!!!!")
#accessing the first student
print("FIRST STUDENT:",students[0])

#accessing the last student
print("LAST STUDENT:",students[-1])

# first two students using slicing.
print("FIRST TWO STUDENTS:",students[:2])

#Add a new student to the class.
students.append(#adds "Yvonne " to the list
    {
        "name":"Yvonne",
        "student_id":"SCT213-C002-0024/2024",
        "courses":["Python", "Statistics", "Databases"],
        "marks":[100,100,100]
    }
)
print("NEW STUDENT LIST:",students)

#Remove one student.
students.pop(-1)#removes the last stunde "Yvonne" from the list
print("NEW STUDENT REMOVED:",students)

#Change a student's mark.
students[1]["marks"][2]=100#changes Aminas 3rd mark from 88  to 100
print("NEW STUDENT RECORDS:",students)

#Demonstrate at least three different list methods meaningfully.
     #myList.sort()...sorts list in ascending order by default..mylist.sort(reverse=True)..sorts in descending order
     #myList.clear()..empties the list
     #myList.insert(2,"Chela")...adds chela to index 2

print("\t")     
           #TUPLES
print("!!!!TUPLES!!!!")
#Access the first room.
print("FIRST ROOM:",class_rooms[0])

#Access the last room.
print("LAST ROOM:",class_rooms[-1])

#Slice the tuple to obtain the first two rooms.
print("FIRST TWO ROOM:",class_rooms[:2])

#Attempt to modify one of its elements.
#class_rooms.append("ROOM D")
#print(class_rooms)
#File "c:\Users\Hello\Desktop\PYTHON\challenge5.py", line 74, in <module>
    #class_rooms.append("ROOM D")
    #^^^^^^^^^^^^^^^^^^
#AttributeError: 'tuple' object has no attribute 'append'
#Tuples are immutable hence the error

print("\t")
        #SETS
print("!!!!SETS!!!!")
#students taking both Python and Databases.
print("STUDENTS TAKING BOTH PYTHON AND  DATABASES:",python_students.intersection(database_students))

#Students taking Python but not Databases.
print("STUDENTS TAKING PYTHON BUT NOT DATABASES:",python_students.difference(database_students))

#Students taking at least one of the two courses.
print("STUDENTS TAKING ATLEAST ONE OF THE TWO COURSES:",python_students.union(database_students))

#Whether ""Brian"" is taking Python.
print("BRIAN IS TAKING PYTHON:","Brian" in python_students)

#Add a new student to the Python set.
python_students.add("Yvonne")
print("NEW PYTHON STUDENTS:",python_students)

#Remove a student from the Database set.
database_students.discard("Daniel")
print("NEW DATABASE STUDENTS:",database_students)

print("\t")
       #DICTIONARIES
print("!!!!!Dictionaries!!!!!")
#Find a student's name using their dictionary key.
#print("FIRST STUDENT'S NAME:",students[0]["name"])..used to accesses specific index
for student in students:#this is where i got AI assistance....I tried the syntax above it and
    print("STUDENTS' NAMES:",student["name"])#its only accessing specific indexes but not all

         #OR
#adds the name to a new list
names = []
for student in students:
    names.append(student["name"])

print("STUDENT NAMES:",names)

#Find their student ID.
for student in students:
    print(f"{student["name"]}:{student["student_id"]}")
print("\t")

#Access their courses.
for student in students:
    print(f"{student["name"]}:{student["courses"]}")

print("\t")
#Access their marks.
for student in students:
    print(f"{student["name"]}:{student["marks"]}")

print("\t")
#Add a new piece of information to a student record.
for student in students:
    student["Class"]="Year 3"#adds the class details to each student
print("NEW STUDENT RECORD WITH CLASS A:",students)

print("\t")
#Modify an existing piece of information
students[0]["name"]="Yvonne"#changes name of first student to Yvonne
print("NEW LIST :",students)

print("\t")
#Remove a piece of information.
for student in students:
    student.pop("Class")#deletes the class details from each student
print("STUDENT RECORDS MINUS CLASS:",students)

print("\t")
#Demonstrate at least three dictionary methods meaningfully.
  #method1...outputs the keys only
print("method I")
for student in students:
    Key=student.keys()
print("DICTIONARY KEYS:",Key)

 #method2...outputs the values only
print("method II")
for student in students:
    print("DICTIONARY VALUES:",student.values())

  #method3...outputs the key value pairs
print("method III")
for student in students:
    for x,y in student.items():
        print("DICTIONARY KEYS AND VALUES:",x,y)

print("\t")
      #NESTED DATA STRUCTURE
#Print Yvonne's second course...I had changed the first student's name to Yvoone from Daniel
Yvonnes_second_course=students[0]["courses"][1]
print("YVONNES'S 2nd COURSE:",Yvonnes_second_course)

print("\t")
#Print Amina's third mark.
Aminas_mark=students[2]["marks"][2]
print("AMINA'S 3rd MARK:",Aminas_mark)

print("\t")
#Print Brian's complete list of marks.
Brians_marks=students[2]["marks"]
print("BRIAN'S MARKS:",Brians_marks)

print("\t")
#Change one student's course.
students[2]["courses"][2]="Theory of Estimation"
print("BRIAN'S STUDENT COURSES:", students[2]["courses"])

print("\t")

#Change one student's mark.
students[0]["marks"][0]=100
print("Changed Amina's Marks:",students[0]["marks"])
print("\t")

#Add another course and corresponding mark where appropriate.
new_course = " AI"
new_marks = [100, 85, 70]
index=0
for student in students:
    student["courses"].append(new_course)
    student["marks"].append(new_marks[index])
    index +=1

print("STUDENT RECORDS WITH NEW COURSES:",students)
print("\t")

      #MUTABILITY VS IMMUTABILITY
#mutability means being able to change a data structure ie add, and remove items
print("!!!!!MUTABILITY VS IMMUTABILITY!!!!!")
myList=[100,True,"Chela",'A']
myTuple=("Flower","Pixel","seat")
mySet={"banana","icecream","pot"}
myDict={
    "Firstborn":"Lawi",
    "Wakili":"Sharon",
    "Daktari":"Chebet"
   }
myList.append('B')
print("Mylist:",myList)#adds B to list
print("\t")

#print("MYTUPLE:",myTuple.add("Yvonne"))..... print("MYTUPLE:",myTuple.add("ME"))
    #                 ^^^^^^^^^^^
     #AttributeError: 'tuple' object has no attribute 'add'
#Tuples are immutable hence cannot add or remove data

mySet.add("ME")
print("MYSET:",mySet)
print("\t")

myDict.update({"Me":"Data Scientist"})
print("MYDICT:",myDict)#adss the me ..datascience to dict

print("\t")
print("!!!!! REFERENCES vs COPIES!!!!!")#AI assistance through this part
marks = [70, 80, 90]
second_marks = marks
second_marks[0] = 100

print("marks:", marks)
print("second_marks:", second_marks)
#I expected the second marks to be printed as a new list with the 100 ie [100,80,90]
#I also expected that changing the second_mark won;t affect the first_mark 
#However the change affected both lists ,this is because second_marks=marks does not create a new list
#Both variables refer to the same list
# This shows that variables in Python can refer to objects.
# Assigning one list variable to another creates a reference
# to the same object rather than creating a new copy.

print("\t")
print("NORMAL REF vs SHALLOW COPYING vs DEEP COPYING COPYING")
student = {
    "name": "Daniel",
    "marks": [70, 80, 90]
}
print("NORMAL REFERENCE")
#normal referencing
Norm_reference = student
Norm_reference["marks"][0] = 100#changing values

print("ORIGINAL STUDENT:", student)#both display the same dictionary
print("NORMAL REFERENCE COPY:", Norm_reference)

print("\t")
print("SHALLOW COPY")

Shallow_reference = student
Shallow_reference["marks"][0] = 100

print("ORIGINAL STUDENT:", student)
print("SHALLOW COPY:", Shallow_reference)

print("\t")

print("DEEP COPYING")
import copy

student = {
    "name": "Daniel",
    "marks": [70, 80, 90]
}
deep_copy = copy.deepcopy(student)
deep_copy["marks"][0] = 100

print("ORIGINAL STUDENT:", student)#Original does not change  
print("DEEP COPY:", deep_copy)
#What is a shallow copy?-creates a new outer object but the objects inside it are still the same
#What is a deep copy?-creates a completely independet copy 
#What happened when the nested list was modified?
#Modifying the shallow copy also changes the original but deep copy retains it originals and creates new copy
#Why can shallow copying be dangerous with nested mutable structures?
#because changing the nested list unintetionally changes the origibal object

print("\t")
#Scenario A:You need to store the names of students in the order they registered.
#List-Lists stores students in registration order
#Scenario B:You need to store a student's information where each piece of information has a meaningful label such as ""name"", ""age"" and ""course"".
#Dictionary-stores student's info in labels..(key  value attributes)
#Scenario C:You need to store the unique courses available in a university where duplicates should automatically be eliminated.
#Set-Sets doesn;t allow duplicates
#Scenario D:You need to store the fixed coordinates of a point:x, y:The values should not accidentally be changed.
#use a tuple with dictionaries ...tuple does'nt allow duplicates
#Scenario E:You need to store students and quickly associate each student ID with that student's record.
#Dictionary-associates each student id eith another record
#Scenario F:You need to store a student's marks together with their courses, while keeping everything organized inside their student record.
#Nested dictionary-to organize the student;s marks and courses inside their records

print('\t')
# FINAL REFLECTION
# Which data structure did I find easiest to use?
#Lists
# Which one confused me the most?
#Nested data structures
# Did I ever choose the wrong structure initially?
#Yes
# What made me change my decision?
#The deliverables of the question
# What did I learn about references and copies?
#that normal references and shallow copies change the original object when changes are made to the copy while deep copy retains the original object and changes only made to the new copy
# What is one thing I understand now that I did not understand  before starting this challenge?
#making copies

#DEBUGGING REQUIREMENT
# File "c:\Users\Hello\Desktop\PYTHON\challenge5.py", line 184, in <module>
#    student[2]["courses"][2]="Theory of Estimation"
#    ~~~~~~~^^^
#KeyError: 2
#I expected to modify Brian's 2nd course to theory of estimatiom
#WHY:It happened because  I was tryind to access key 2 in a dict but that key does not exist
#FIX: students[2]["courses"][2]="Theory of Estimation"
print("!!!!!!!FINAL TASK!!!!!!")

# FINAL TASK — MINI STUDENT RECORD SYSTEM
# FINAL PROBLEM-SOLVING REFLECTION

# 1. What information am I storing?
# Student names, student IDs, courses, marks, classrooms,
# and the students taking Python and Databases.

# 2. Which information is ordered?
# The students list is ordered.
# The courses and marks lists are ordered.
# The classroom tuple is ordered.

# 3. Which information needs unique values?
# Student IDs should be unique.
# Sets store the unique students taking Python and Databases.
# A set will also help display unique courses.

# 4. Which information needs labels/keys?
# Each student dictionary uses keys such as name, student_id,
# courses, and marks.

# 5. Which information should not change?
# Classroom names are stored in a tuple because the tuple
# itself cannot be modified.
# Student IDs should remain unchanged after registration.

# 6. Which structures will be nested?
# The students list contains dictionaries.
# Each dictionary contains courses and marks lists.

# 7. Where could references cause unexpected changes?
# Assigning another variable to students would make it refer
# to the same list. Changes through either variable would
# affect the same records.

# 8. Where might I need a copy instead of the original object?
# I need a deep copy to create an independent backup of
# the students list and its nested dictionaries and lists.


import copy

students = [
    {
        "name": "Daniel",
        "student_id": "DS001",
        "courses": ["Python", "Statistics", "Databases"],
        "marks": [78, 64, 82]
    },
    {
        "name": "Amina",
        "student_id": "DS002",
        "courses": ["Python", "Statistics", "Databases"],
        "marks": [91, 73, 88]
    },
    {
        "name": "Brian",
        "student_id": "DS003",
        "courses": ["Python", "Statistics", "Databases"],
        "marks": [56, 68, 61]
    }
]

class_rooms = ("Room A", "Room B", "Room C")

python_students = {"Daniel", "Amina", "Brian"}
database_students = {"Daniel", "Amina", "Brian"}

backup = None


# Helper function: find a student using their ID

def find_student(student_id):
    for student in students:
        if student["student_id"].lower() == student_id.lower():
            return student

    return None


# 1. View all students

def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print("Name:", student["name"])
            print("Student ID:", student["student_id"])
            print("Courses:", student["courses"])
            print("Marks:", student["marks"])

# 2. Add a student

def add_student():
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if find_student(student_id) is not None:
        print("That student ID already exists.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    student = {
        "name": name,
        "student_id": student_id,
        "courses": [],
        "marks": []
    }

    students.append(student)
    print("Student added successfully.")


# 3. Search for a student

def search_student():
    search = input("Enter student ID or name: ").strip().lower()

    for student in students:
        if (
            student["student_id"].lower() == search
            or student["name"].lower() == search
        ):
            print("\nStudent found:")
            print(student)
            return

    print("Student not found.")


# 4. Update a student's mark

def update_mark():
    student_id = input("Enter student ID: ").strip()
    student = find_student(student_id)

    if student is None:
        print("Student not found.")
        return

    course = input("Enter course name: ").strip().lower()

    for index, course_name in enumerate(student["courses"]):
        if course_name.lower() == course:
            try:
                mark = float(input("Enter new mark (0-100): "))

                if not 0 <= mark <= 100:
                    print("Mark must be between 0 and 100.")
                    return

            except ValueError:
                print("Enter a valid number.")
                return

            student["marks"][index] = mark
            print("Mark updated successfully.")
            return

    print("Course not found for this student.")


# 5. Add a course and its mark

def add_course():
    student_id = input("Enter student ID: ").strip()
    student = find_student(student_id)

    if student is None:
        print("Student not found.")
        return

    course = input("Enter course name: ").strip()

    if not course:
        print("Course name cannot be empty.")
        return

    for course_name in student["courses"]:
        if course_name.lower() == course.lower():
            print("This student already has that course.")
            return

    try:
        mark = float(input("Enter mark (0-100): "))

        if not 0 <= mark <= 100:
            print("Mark must be between 0 and 100.")
            return

    except ValueError:
        print("Enter a valid number.")
        return

    student["courses"].append(course)
    student["marks"].append(mark)

    if course.lower() == "python":
        python_students.add(student["name"])

    elif course.lower() == "databases":
        database_students.add(student["name"])

    print("Course and mark added successfully.")


# 6. Remove a course and its corresponding mark

def remove_course():
    student_id = input("Enter student ID: ").strip()
    student = find_student(student_id)

    if student is None:
        print("Student not found.")
        return

    course = input("Enter course name to remove: ").strip().lower()

    for index, course_name in enumerate(student["courses"]):
        if course_name.lower() == course:
            removed_course = student["courses"].pop(index)
            student["marks"].pop(index)

            if removed_course.lower() == "python":
                if not any(
                    "python" in
                    [c.lower() for c in s["courses"]]
                    for s in students
                ):
                    python_students.clear()

            elif removed_course.lower() == "databases":
                if not any(
                    "databases" in
                    [c.lower() for c in s["courses"]]
                    for s in students
                ):
                    database_students.clear()

            print("Course and corresponding mark removed.")
            return

    print("Course not found.")


# 7. Display all unique courses

def display_unique_courses():
    unique_courses = set()

    for student in students:
        for course in student["courses"]:
            unique_courses.add(course)

    if unique_courses:
        print("Unique courses:")
        for course in sorted(unique_courses):
            print(course)
    else:
        print("No courses registered.")


# 8. Display students taking a particular course

def students_taking_course():
    course = input("Enter course name: ").strip().lower()
    found = False

    for student in students:
        for course_name in student["courses"]:
            if course_name.lower() == course:
                print(student["name"], "-", student["student_id"])
                found = True
                break

    if not found:
        print("No students found taking that course.")


# 9. Display a selected student's full record

def display_record():
    student_id = input("Enter student ID: ").strip()
    student = find_student(student_id)

    if student is None:
        print("Student not found.")
        return

    print("\n--- STUDENT RECORD ---")
    print("Name:", student["name"])
    print("Student ID:", student["student_id"])

    if student["courses"]:
        print("Courses and marks:")

        for index, course in enumerate(student["courses"]):
            print(course, ":", student["marks"][index])
    else:
        print("No courses registered.")


# 10. Create a backup copy

def create_backup():
    global backup

    backup = copy.deepcopy(students)
    print("Backup created successfully.")


# Main menu

while True:
    print("\n===== MINI STUDENT RECORD SYSTEM =====")
    print("1. View all students")
    print("2. Add a student")
    print("3. Search for a student")
    print("4. Update a student's mark")
    print("5. Add a course")
    print("6. Remove a course")
    print("7. Display all unique courses")
    print("8. Display students taking a course")
    print("9. Display a student's full record")
    print("10. Create a backup")
    print("0. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        view_students()

    elif choice == "2":
        add_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_mark()

    elif choice == "5":
        add_course()

    elif choice == "6":
        remove_course()

    elif choice == "7":
        display_unique_courses()

    elif choice == "8":
        students_taking_course()

    elif choice == "9":
        display_record()

    elif choice == "10":
        create_backup()

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

