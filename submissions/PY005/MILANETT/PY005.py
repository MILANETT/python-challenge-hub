#Small Student Records Manager

#Importing copy module for shallow and deep copying
import copy


students = [
    {
        "name":"Daniel",
        "student_id":"DS001",
        "courses":["Python","Statistics","Databases"],
        "marks":[78,64,82]
    },
    {
        "name":"Amina",
        "student_id":"DS002",
        "courses":["Python","Statistics","Databases"],
        "marks":[91,73,88]
    },
    {
        "name":"Brian",
        "student_id":"DS003",
        "courses":["Python","Statistics","Databases"],
        "marks":[56,68,61]
    }
]

class_rooms=("Room A","Room B","Room C")

python_students={"Daniel","Amina","Brian"}
database_students={"Daniel","Amina","Brian"}

#PART 1 - UNDERSTAND THE DATA
#Students
#It is a "List" which contains a multiple dictionaries inside it, it stores information that can be
#changed by adding or removing students, and the order in which the students are registered matters for
#easy record keeping the structure for entering students can be duplicated and since it is storing another
#collection there is no need for keys , The data should be mutable since we need to be able to add or
#students in the future and so lists are perfect for this since they are ordered, mutable, and allow duplicates

#Each individual student's record
#Each of them is a "Dictionary" which contains unique information for each student, it makes sense to be a
#dictionary so that each detail can be entered in the right space uniformly for neat records . Order matters
# to understand what detail to input first and which follows . We should not input the same student information more than
# once thus we should not have duplicates . The keys are needed to understand what information to store where.
# Data should be mutable in case wee want to update information like students results maybe where they are wrong.
#In addition, a dictionary makes sense for having key value pairs and ordered, mutable, does not allow duplicates

#courses
#It is stored in a "List" , this makes sense since we need a structure that can allow mutability since a
# student can drop do an extra course which we will be required to add to the system , we also need order
# because the position where the course is, should match the same position as its mark in the marks list,
# we need no keys since it is one nature of information, we should not have duplicates though yet lists
# allow duplicates.

#marks
#It is stored in a "List" which makes sense because it allows mutability and has order which allows for
# future changes and easy retrieval

#class_rooms
#Stored in a "Tuple", this makes sense due to a tuple's immutability, this prevents accidentally adding
# classes that do not exist

#python_students and database_students
#Both are stored in a "set", this makes sense in that it allows to track which student does both or one ,
# given the set operations ,and also it is mutable so we can easily add or remove items from the set and
# since it does not allow duplicates , we can not accidentally store the same course twice



#PART 2 - LISTS
#first student's record
print("\tFirst Student's Record")
print(students[0])
#last student's record
print("\tLast Student's Record")
print(students[-1])
#first two students
print("\tFirst Two Student's Record")
print(students[:2])
#adding a new student
students.append({
    "name":"Stacy",
    "student_id":"DS004",
    "courses":["Python","Statistics","Databases"],
    "marks":[82,65,52]
})
print(students)
#removing a student
students.pop()
print(students)
#changing Brian's Statistics Mark
students[2]["marks"][1]=72
print("\nBrians new Statistics Mark")
print(students[2])
#Encountered Errors
#Traceback (most recent call last):
#   File "C:\Users\admin\PycharmProjects\PythonAteTheDataChallenges\PY005.py", line 70, in <module>
#     students[2,"marks"[1]]=72
#     ~~~~~~~~^^^^^^^^^^^^^^
# TypeError: list indices must be integers or slices, not tuple

#LIST METHODS DEMONSTRATION
#Finding number of students using len()
print(f"Number of Students: {len(students)}")
#I have used both append and remove to add and remove a student respectively

#Reflection
#1.Why "students" is stored in a list
#students is stored in a list to allow for easy retrieval of a student's information, given that a list is
# ordered and for easy updating of students given that a list is mutable.

#2.Why indexing is useful here
#For easy retrieval of students information and maintaining order of registration and also updating

#3.Why slicing is useful
#For easy retrieval too and updating of information

#4.What each list method does and why I chose it
# i) append() - it adds an item at the end of a list, I chose it to add the new student at the end so that I
# maintain order of registration.
#ii) pop() - it removes the last element from the list, I chose because I wanted to remove the last student from
# the list



#PART 3 - TUPLES
#accessing the first classroom
print(f"First classroom: {class_rooms[0]}")
#accessing the last classroom
print(f"Last classroom: {class_rooms[-1]}")
#accessing the first two classrooms
print(f"First two classroom: {class_rooms[:2]}")
#An attempt to modify "Room B"
#class_rooms[0]="Room Blue"

#Reflection
#1.When I attempted to modify the tuple the following error was produced:
#Produces a type error:
# Traceback (most recent call last):
#   File "C:\Users\admin\PycharmProjects\PythonAteTheDataChallenges\PY005.py", line 94, in <module>
#     class_rooms[0]="Room Blue"
#     ~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

#2. Why Python prevents modification
#This is because Python expects that no changes whatsoever should be done on a tuple

#3. What this tells you about immutability
#When an object is immutable you cannot modify its data or structure in any manner and doing so results in
# an error.

#4. Why a tuple could be appropriate for this type of data
#Because we do not want to accidentally add any class that does not exist or remove one that exists,
# therefore being in a tuple, they have protection.

#PART 4 - SETS
#Students taking both Python and Databases
print(f"Students taking both Python and Databases: {python_students.intersection(database_students)}")
#Students taking Python but not Databases
print(f"Students taking Python but not Databases: {python_students.difference(database_students)}")
#Students taking at least one of the two courses
print(f"Students taking at least one of the two courses: {python_students.union(database_students)}")
#Whether ""Brian"" is taking python
print(f"Is Brian taking Python: {"Brian" in python_students}")
#Adding new student to Python set
python_students.add("Stacy")
print(f"New Python Set: {python_students}")
#Removing a student from the database set
database_students.remove("Daniel")
print(f"New Database Set: {database_students}")

#Reflection
#1. What each set operation does
#intersection()
#It returns the elements that appear in both given sets in a new set
#difference()
#it returns the elements that are in the first set that aren't present in the other set in a new set
#union()
#returns a new set with all elements in both sets
#in
# checks if an element is a member of the given set
#add()
#It adds an item to the set
#remove()
#removes the named item from the given set

#2.Why is a set useful here
#Because with its operation , it easier to group students into their various categories, and given that it
# does not allow duplicates , you'll not enter the same course twice which helps maintain consistency

#3.Why a list would not be as appropriate for some of these operations
#Because it allows duplicates that would lead to faulty results

#PART 5 - DICTIONARIES
#Finding the information of the second student
print(f"Second Student's Name: {students[1]["name"]}")
print(f"Second Student's ID: {students[1]["student_id"]}")
print(f"Second Student's courses: {students[1]["courses"]}")
print(f"Second Student's marks: {students[1]["marks"]}")
#Adding Amina's age
students[1].update({"age":21})
print(f"New Amina info: {students[1]}")
#Modifying Amina's name to Aminah
students[1].update({"name":"Aminah"})
print(f"New Amina info: {students[1]}")
#Removing the added Amina's Age
del(students[1]["age"])
print(f"New Amina info: {students[1]}")
#Dictionary METHODS
#Finding how many items it stores
print(f"Number of stored Student information: {len(students[0])}")

#Reflections
#1.What a key-value pair represents
#A key is a label while the value is the data stored under a label

#2.Why dictionaries are useful for student records.
#They specify what information it is using the key

#3.Why a dictionary is more appropriate than a simple list for labeled information.
#Because Lists use indices that are automatically assigned integers not customizable keys that can label as
# dictionaries

#PART 6 - NESTED DATA STRUCTURES
#Daniel's Second course(list-dict-list)
print(f"Daniel's Second course: {students[0]["courses"][1]}")
#Amina's Third Mark(list-dict-list)
print(f"Amina's Third Mark: {students[1]["marks"][2]}")
#Brian's complete list of Marks(list-dict)
print(f"All Brian's Marks: {students[2]["marks"]}")
#Changing Daniel's First Course(list-dict-list)
students[0]["courses"][0]="Julia"
print(f"New Daniel's Information: {students[0]}")
#Changing Amina's second Mark(list-dict-list)
students[1]["marks"][1]=83
print(f"New Amina's Information: {students[1]}")
#Adding DSA course and mark to Daniel(list-dict-list)
students[0]["courses"].append("DSA")
students[0]["marks"].append(89)
print(f"New Daniel's Information: {students[0]}")

#PART 7 - MUTABILITY VS IMMUTABILITY
#a list
my_list=[89,67,88]
#tuple
my_tuple=(89,67,88)
#set
my_set={89,67,88}
#dictionary
my_dictionary={
    "Math":89,
    "Science":67,
    "English":88
}

#Reflection
#What does mutability actually mean in Python?
#It means an object can have its items added , removed or replaced without altering its memory location
#The list, set and dictionary are mutable.
#A list is mutable in that you can add, remove or replace an item in a list without altering its memory
# location using different methods like pop() or accessing via indexing and slicing
#A dictionary, just like a list is mutable and we can still add, remove or replace an item in a list without
# altering its memory location using different methods like update() or accessing the values via the keys.
#A set too is mutable but unlike lists and dictionaries we cannot really replace values, but the former can
# be done using methods like add()
#A tuple on the other hand is immutable, this means we can alter its elements after creation , hence we
# cannot add, remove or replace elements of a tuple

#PART 8 - REFERENCES VS COPIES
#creating the given list
marks = [70, 80, 90]
#creating a variable, scores, referring to marks memory space
scores = marks
#modifying scores first value
scores[0]= 72
#observing the original marks
print(marks)

#Reflection
#I expected that marks would not be affected since I initially thought that the variable , scores, would make
# its own copy of the marks list but marks was also modified on modification of scores, this is because in
# python variables do not store the raw value of a variable rather a reference to the memory of the value
# stored, thus the by making scores refer to marks it means they are referring to the same memory space
# hence on modification of either the other should also be affected.

#PART 9 - SHALLOW VS DEEP COPYING
#creating the given nested structure
student={
    "name":"Daniel",
    "marks":[70,80,90]
}
#creating a normal reference
daniel_info=student
#creating a shallow copy
student_shallow_copy=copy.copy(student)
#creating a deep copy
student_deep_copy=copy.deepcopy(student)
#modifying the nested marks
student["marks"][:2]=[75,84]
student_shallow_copy["marks"][:2]=[76,88]
#Observing changes on the various objects
print(f"Original student dictionary: {student}")
print(f"Normal Referenced student dictionary: {daniel_info}")
print(f"Shallow copied student dictionary: {student_shallow_copy}")
print(f"Shallow copied student dictionary: {student_deep_copy}")

#Reflection
#1.What is a shallow copy?
#It is a copy of a variable's information duplicates only the outer structure but references the inner
# nested structure instead of copying it

#2.What is a deep copy?
#It is a copy of a variables information that completely duplicates the whole structure inclusive of the
# outer and inner nested structures

#3.What happened when the nested list was modified?
#When it was modified, the changes were reflected on the original dictionary, the normal referenced and the
# shallow copied but the deep copied remained unchanged

#4.Why can shallow copying be dangerous with nested mutable structures?
#This is because any accidental changes made on the copy will still affect the original.

#PART 10 -DATA STRUCTURE DECISION CHALLENGE
#Scenario A
#List
#This is because while storing, we need to be keen on the order of registration of students and many students
# can share the same name, we can decide to register more students in the future. A list is ordered due to
# indexing and mutable hence it is the most suitable. Maybe a Tuple would have been suitable but ,it is
# immutable hence registering more students in the future would have been an issue, a dictionary on the
# other hand would have been an overkill since it's just names

#Scenario B
#Dictionary
#This is because it stores information in a key value pair format and hence keys would have served as the
# labels.

#Scenario C
#Set
#A set does not allow duplicates, hence it is the most suitable, a dictionary too does not allow duplicates
# but the nature of course names might not require a label.

#Scenario D
#Tuple with nested tuples
#This is because a tuple is immutable hence it would protect the data from accidental changes

#Scenario E
#A Dictionary with nested dictionaries
#Such that each student ID  can be a label of another labelled record, this ensures the data is clearly
# labelled

#Scenario F
#List with a nested dictionary
#A list indicating well that these are courses and marks and dictionary clearly showing a course as a label
# with marks as its value , this helps keep everything neat, given the labeling and with mutability,
# corrections can be easily done, and with the indexing of a List, retrieval is easy



#Program
#FINAL PROBLEM-SOLVING REFLECTION
# 1. What information am I storing?
#I need to store a new student, new student's mark, a new course and a backup of the records

# 2. Which information is ordered?
#students records, courses and marks

# 3. Which information needs unique values?
#the new course set I need to create

# 4. Which information needs labels/keys?
#the new student's record

# 5. Which information should not change?
#the backup

# 6. Which structures will be nested?
#dictionaries of student records in the students list and lists of courses and marks in a student's dictionary

# 7. Where could references cause unexpected changes?
#If I refer to the students records in creating a backup instead of copying, if the records are altered
# accidentally , so will the backup

# 8. Where might I need a copy instead of the original object?
#When creating the backup I need a deepcopy


#FINAL TASK - MINI STUDENT RECORD SYSTEM

###THIS IS A CORRECTED CODE WITH AI Assistance, my initial code is present in the Python codes group

#How did AI(Gemini) assist me:
#I had initially thought of my own system without using functions but felt like it was so scattered and had
# some logical errors, so I presented AI with my already made program where it helped me point out errors and
# suggested how to fix them and have a defined structure, I went through it as I learnt new this but keeping
# them within only what we have covered so far and after understanding where I was wrong, I came back to
# write this code:
print("="*25)
print("A MINI STUDENT RECORD SYSTEM")
print("="*25)

#Encountered error
# Traceback (most recent call last):
#   File "C:\Users\admin\PycharmProjects\PythonAteTheDataChallenges\PY005.py", line 365, in <module>
#     print("=")*25
#     ~~~~~~~~~~^~~
# TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
#Viewing all students

print("----------System Menu----------")
print("1. View all students.")
print("2. Add a student.")
print("3. Search for a student.")
print("4. Update a student's mark.")
print("5. Add a course.")
print("6. Remove a course.")
print("7. Display all unique courses taken by the class.")
print("8. Display students taking a particular course.")
print("9. Display a selected student's record.")
print("10. Create a backup copy of the student records.")
print("11. Exit")



while True:
    # Creating a choice for the user to choose their operation
    choice = input("Choose an operation (1-11): ").strip()

    #View all students
    if choice=='1':
        print("\n___ ALL STUDENTS ___")
        for s in students:
            print(f"ID: {s["student_id"]} | Name: {s["name"]}")


    #Add a student
    elif choice == "2":
        print("\n___ ADD A STUDENT ___")
        new_student_name = input("Student Name: ").capitalize()
        new_student_id = input("Student ID: ").upper()

        new_student_courses = []
        new_student_marks = []
        no_of_courses=int(input(f"How many courses does {new_student_name} take: "))
        for i in range(no_of_courses):
            new_student_course_name=input(f"Course {i+1} name: ").capitalize()
            new_student_courses.append(new_student_course_name)
            new_student_marks.append(int(input(f"Course {i + 1} marks: ")))
            print(f"{new_student_course_name} added successfully!!!")

        students.append({
            "name":new_student_name,
            "student_id":new_student_id,
            "courses":new_student_courses,
            "marks":new_student_marks
        })


    #Search for a student
    elif choice == "3":
        print("\n___ SEARCH FOR A STUDENT ___")
        search_student=input("Enter student's name or id: ").lower()
        found=False
        for s in students:
            if search_student==s["name"].lower() or search_student==s["student_id"].lower():
                found= True
                print(f"Student found!!!")
                print(f"Student ID: {s["student_id"]}")
                print(f"Student Name: {s["name"]}")
                break
        if not found:
            print("Student not found!!!")

    #Update a student's mark
    elif choice == "4":
        print("\n___ UPDATE A STUDENT'S MARK ___")
        search_student=input("Enter student's name or id: ").lower()
        found=False
        for s in students:
            if search_student==s["name"].lower() or search_student==s["student_id"].lower():
                found = True
                search_course=input("Enter course name: ").lower()
                course_found = False
                for course in s["courses"]:
                    if search_course==course.lower():
                        course_found= True
                        course_index=s["courses"].index(course)
                        update_mark = int(input("Enter new mark: "))
                        s["marks"][course_index]=update_mark
                        break
                if not course_found:
                    print("Course not found!!!")
                    break

        if not found:
            print("Student not found!!!")



    #Add a course
    elif choice == "5":
        print("\n___ ADD A COURSE ___")
        search_student=input("Enter student's name or id: ").lower()
        found=False
        for s in students:
            if search_student==s["name"].lower() or search_student==s["student_id"].lower():
                found = True
                new_course=input("Enter course name: ").lower()
                already_exists = False
                for course in s["courses"]:
                    if new_course==course.lower():
                        already_exists = True
                        break
                if already_exists:
                    print("Course already exists for this student!!!")
                else:
                    course_mark = int(input("Enter course mark: "))
                    s["courses"].append(new_course)
                    s["marks"].append(course_mark)
                    print(f"{new_course} added successfully!!!")
                break


        if not found:
            print("Student not found!!!")

    #Remove a course
    elif choice == "6":
        print("\n___ REMOVE A COURSE ___")
        search_student=input("Enter student's name or id: ").lower()
        found=False
        for s in students:
            if search_student==s["name"].lower() or search_student==s["student_id"].lower():
                found = True
                search_course=input("Enter course name: ").lower()
                course_found = False
                for course in s["courses"]:
                    if search_course==course.lower():
                        course_found=True
                        course_index=s["courses"].index(course)
                        s["courses"].pop(course_index)
                        s["marks"].pop(course_index)
                        print("Course removed successfully!!!")
                        break

                if not course_found:
                    print("Course not found!!!")
                break

        if not found:
            print("Student not found!!!")


    #Display all unique courses taken by this class
    elif choice == "7":
        print("\n___ DISPLAY UNIQUE COURSES TAKEN BY THIS CLASS ___")
        unique_courses=set()
        for s in students:
            unique_courses.update(s["courses"])
        print(f"Unique courses: {unique_courses}")


    #Display students taking a particular course
    elif choice == "8":
        print("\n___ DISPLAY STUDENTS TAKING A PARTICULAR COURSE ___")
        search_course = input("Enter the course's name: ").lower()
        found = False
        for s in students:
            for course in s["courses"]:
                if search_course == course.lower():
                    found=True

                    print(s["name"])
                    break
        if not found:
                print("Course not found!!!")


    #Display a selected student's record
    elif choice == "9":
        print("\n___ DISPLAY A SELECTED STUDENT'S RECORD ___")
        search_student=input("Enter student's name or id: ").lower()
        found=False
        for s in students:
            if search_student==s["name"].lower() or search_student==s['student_id'].lower():
                found=True
                print(f"Student ID: {s['student_id']}")
                print(f"Student Name: {s['name']}")
                for course in s["courses"]:
                    crs_idx=s["courses"].index(course)
                    print(f"Course Name: {course}, Course Mark: {s['marks'][crs_idx]}")
                break

        if not found:
            print("Student not found!!!!!!")


    #Create a backup copy of the student records
    elif choice == "10":
        print("\n___ CREATE A BACKUP OF THE STUDENT RECORDS ___")
        students_backup = copy.deepcopy(students)
        print("Created a backup named 'students_backup' successfully for student records.")


    #Exit the program
    elif choice == "11":
        print("Exited the program successfully")
        break

    #Invalid choice
    else:
        print("Enter a valid choice between 1 and 11")
        continue


# FINAL REFLECTION
#
# Which data structure did I find easiest to use?
#list

# Which one confused me the most?
#a dictionary when nested in a list

# Did I ever choose the wrong structure initially?
#no

# What made me change my decision?
#n/a

# What did I learn about references and copies?
#That changes made to references affect the original variable while those made to copies don't

# What is one thing I understand now that I did not understand before starting this challenge?
#How to loop through nested structures

#DEBUGGING REQUIREMENT
# DEBUGGING REFLECTION 1
##Traceback (most recent call last):
#   File "C:\Users\admin\PycharmProjects\PythonAteTheDataChallenges\PY005.py", line 70, in <module>
#     students[2,"marks"[1]]=72
#     ~~~~~~~~^^^^^^^^^^^^^^
# TypeError: list indices must be integers or slices, not tuple

# Expected:
#I expected that my code would help me access the inner dictionary by using the key directly inside the index
# arguments position.

# Actual:
#It  brought up a type error and did not access the inner dictionary
# Why it happened:
#It happened because Python expects an integer as an argument but I passed a string as an argument
# Fix:
#I separated the arguments by passing "marks" later as its own argument to the already accessed list position


# DEBUGGING REFLECTION 2
# Traceback (most recent call last):
#   File "C:\Users\admin\PycharmProjects\PythonAteTheDataChallenges\PY005.py", line 365, in <module>
#     print("=")*25
#     ~~~~~~~~~~^~~
# TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'

# Expected:
#I expected my statement to print 25 "="

# Actual:
#It didn't print the = signs and instead brought up a TypeError

# Why it happened:
#This is because Python expected * inside the print function because it is part of the operation of the
# information to be printed

# Fix:
#I introduced the = sign inside the print() function to make unite it with the information