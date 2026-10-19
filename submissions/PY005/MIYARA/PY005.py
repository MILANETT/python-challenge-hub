# 1. What information am I storing?
#   Students name, ID, courses, marks, the class_rooms and which students take Python and Databases.

# 2. Which information is ordered?
#   The students, each student's courses and marks and the rooms .

# 3. Which information needs unique values?
#   The set of courses in the class, and the groups of students per course (a student should not appear twice in a group).

# 4. Which information needs labels/keys?
#   Each student's record (name, student_id, courses, marks) 

# 5. Which information should not change?
#   The class rooms (a tuple)

# 6. Which structures will be nested?
#    Dictionary (student ID -> record) -> record dictionary -> courses list and marks list inside it.

# 7. Where could references cause unexpected changes?
#   If I make a "backup" with `backup = records`, both names point to the same object, so changing one changes the other.

# 8. Where might I need a copy instead of the original object?
#   For the backup. It must be a deep copy because the records contain nested lists (courses and marks).

students = [
    {#Dictionary
    "Name":"Daniel",
    "Student_Id":"DS001",
    "Courses":["Python","Statistics","Databases"],
    "Marks":[78,64,82]
    },
    {
    "Name":"Amina",
    "Student_Id":"DS002",
    "Courses":["Python","Statistics","Databases"],
    "Marks":[91,73,88]
    },
    {
    "Name":"Brian",
    "Student_Id":"DS003",
    "Courses":["Python","Statistics","Databases"],
    "Marks":[56,68,61]
    }
]


print("Students:",students, end="\n\n")

#1."students" -list
#I chose lists because they store the collection of all students in the class.
#They store info in order and order matters because it keeps registration order and allows indexing.
#They allow duplicates because two students could share a name.
#They are also mutable as students can join and leave the class.

#2.Each student's record -DICTIONARY
# I chose dictionary because the labels matter and not the order.
# The dictionary provides keys which are needed to store the values.
# Dictionaries were suitable because they are mutable.

#3."courses" -list
# they store what the students take and I chose lists because order matters as they are ordered in line with the marks gotten.
#They do not need keys so lists are preferred over dictionaries and they are mutable hence prefeerred for this data over tuples 

#4."marks" -list
# I chose lists as they are ordered and linked to the course on takes on.
# A set would be inappropriate as they don't allow duplicated yet one can get the same mark in two different courses 
#They do not need keys and so dictionary was inappropriate and they are mutable hence tuples would have been inappropriate 

#5."class_rooms" -> tuple
#I chose tuples because duplicates are not allowed therefore a room can only be of a unique type 
# They don't need keys and are not mutable 

#.6"python_students" - set
# I chose a set because order does'nt matter , only membership does and duplicates matter
# They are also mutable

print("The 1st student is:",students[0],end="\n")#The first student using indexing

print("The 2nd student is:",students[-1],end="\n")#The last student using indexing 

print("The 1st two students:",students[0:2],end="\n")#The first 2 students using slicing

students.append({"Name":"Monicah","Student_Id,":"DS004","Courses":["Python","Statistics","Databases"],"Marks":[98,84,96]})
print("Students list after adding a new student:",students ,end="\n")#Added a new student using append
print("\n")
students.pop()#Removes the  student at the last index
print("Students list after removing the last student:",students, end = "\n\n")
print("\n")
students[1]["Marks"] = [96,94,86] #Changed Amina's marks 
print("Students list after updating Amina's marks:",students, end ="\n")
print("\n")
# students" is a list because the students are ordered 
# Indexing is useful because I can jump straight to the first, last or any student by position without looping.
# Slicing is useful because it gives me a section of the class as a new list in one step.
# append adds one new student at the end of the list
# pop removes a student from the end of the list
class_rooms = ("Room A","Room B","Room C") #tuple
print("\n\n")
print("The 1st room:",class_rooms[0])#1st room
print("The last room:",class_rooms[-1])#Last room
print("The 1st two rooms:",class_rooms[0:2])#1st 2 rooms
#Tried modifying Index 0 of the tuple class_rooms and got the type error below 
#class_rooms[0] = "Room D"

#TypeError: 'tuple' object does not support item assignment - Because tuples do not support muttability so their contents cant be changed after creation
#The tuple stayed ("Room A", "Room B", "Room C").

# What this tells me: immutability means the object itself cannot be changed after creation. To change it I would have to build a new tuple.
# Why a tuple fits: the room list is fixed information and should not be changed by accident.
python_students = {"Daniel","Amina","Brian"}#Set - Membership testing, Eliminating duplicates
database_students = {"Daniel","Amina","Brian"}

print("Students in both groups:", python_students & database_students) # both python and db

print("Students in Python but not in Database:", python_students - database_students) # python but not db

print("Students in at least one group:", python_students | database_students) # atleast one 

print("Is Brian in Python students?", "Brian" in python_students) #whether Brayo takes python

python_students.add("Monicah")#Add a new student
print("Python students after adding a new student:", python_students)
print("\n")

database_students.remove("Brian")#Remove a student
print("Database students after removing a student:", database_students)
print("\n")

#Intersection & finds who is in both groups, (-) finds who is in one group but not the other, union (|) combines both
# groups with no repeats, `in` checks membership, add inserts, and remove deletes an item.
# A set is useful because the question is "who belongs to which group", not "in what order", and duplicates are removed automatically.
# A list would be less appropriate because I would need loops and if-statements to compare two lists and remove duplicates myself
# and membership checks in a list are slower for large data.

print("Student's name:", students[0]["Name"]) #student's name 

print("Student's ID:", students[0].get("Student_Id"))# student's Id

print("Student's courses:", students[0].get("Courses"))#student's course

print("Student's marks:", students[0].get("Marks")) #student's marks 
print("\n")

students[0].update({"Grade":"A"}) #Added grade to Daniel's info
print("Students list after updating Daniel's info:", students)
print("\n")

students[2].update({"Marks":[78,90,54]})#Modified Brian's marks
print("Students list after updating Brian's marks:", students)
print("\n")

del students[0]["Grade"] #Removed a piece of information
print("Students list after removing Daniel's grade:", students)
print("\n")

# A key-value pair is a label attached to a piece of information, like "name" -> "Daniel".
# Dictionaries suit student records because each record has different kinds of information, and I can retrieve each by a meaningful name.
# A list like ["Daniel", "DS001", ...] would force me to remember that index 0 is the name and index 1 is the ID. A dictionary makes the code
#readable (student["name"]) and less error-prone.
print("Daniel's Keys:", students[0].keys())

print("Amina'sValues:",students[1].values())

print("Brian's items:",students[2].items())

print("Daniel's 2nd course:", students[0]["Courses"][1])

print("Amina's 3rd mark:", students[1]["Marks"][2])

print("Brian's marks:", students[2]["Marks"])

students[2]["Courses"][2]="SQL" #Changed Brian's last course to SQL
print("Students list after updating Brian's course:", students)
print("\n")

students[0]["Marks"][1] = 50 #Changed Daniel's 2nd mark 
print("Students list after updating Daniel's mark:", students)
print("\n")

students[1]["Courses"].append("SQL")
students[1]["Marks"].append(75)
print("Students list after updating Amina's course and marks :", students)
print("\n")
# I started at the outer list students and used an index to pick one student.
# Then I used a key ("courses" and "marks") to reach the inner list.
# Then I used another index to reach the exact mark or course.
#  list -> dictionary -> list -> element.
# When adding a course I had to change two lists, because the courses and marks are linked by position.
list_example=[5,6,7,8] #lists - Mutable
list_example.append(9) 
print("List after updating:",list_example)
tuple_example =(5,6,7,8) #Tuple - Immutable
try:
    tuple_example.append(9)
except AttributeError as error:
    print("Tuples are immmutable")
print("Tuple:",tuple_example)
set_example = {5,6,7,8} #Sets - Mutable
set_example.add(9)
print("Set:",set_example)
dict_example = {
    "name":"Monicah",
    "Age":21
}
dict_example["Course"] = "Data Science and Analytics" #Dictionary - Mutable 
print("Dictionary:",dict_example)
marks = [70,80,90] #Referencing
mod_marks = marks
mod_marks.append(100)
print("Original marks:", marks)
print("Modified marks:", mod_marks)

#I expected only mod_marks to change because I only edited it.
# What happened: Both printed out the same output
# Why the original list changes:It makes a second name that points to the SAME list object in memory.
# What this tells me: in Python, variables are names that refer to objects that don't hold the objects themselves. With mutable objects,
# changing it through one name is visible through every name.
student = {
    "Name":"Daniel",
    "Marks":[70,80,90]
}

student_ref = student
print("Student reference:", student_ref)

student_scopy = student.copy()#shallow copy

student_scopy["Marks"] = [78,90,100]
print("Student shallow copy:", student_scopy)
import copy
student_dcopy = copy.deepcopy(student)#deep copy 
student_dcopy["Name"]=["Monicah"]
print("Student deep copy:", student_dcopy)
# Scenario A: names of students in the order they registered
#   Choice: LIST.
#   Reasoning: a list keeps insertion order and allows indexing.
#   Alternative: a set would lose the registration order. A tuple could not grow as new students register.


# Scenario B: a student's info with labels (name, age, course)
#   Choice: DICTIONARY.
#   Reasoning: each value has a meaningful label, and I can retrieve it by key .
#   Alternative: a list would force me to remember what each position means, making the code harder to read and easier to break.

# Scenario C: unique courses in a university
#   Choice: SET.
#   Reasoning: a set automatically eliminates duplicates, so adding "Python" twice keeps just one.
#   Alternative: a list would store duplicates and I would have to check if course not in list manually each time.

# Scenario D: fixed coordinates (x, y) that should not change
#   Choice: TUPLE.
#   Reasoning: a tuple is immutable, so the coordinates cannot be changed by accident.
#   Alternative: a list could be modified accidentally. A dictionary would be heavier than needed for two plain values.

# Scenario E: quickly associate each student ID with that student's record
#   Choice: DICTIONARY (student ID as key, record as value).
#   Reasoning: dictionary lookup by key is direct and fast, and IDs are unique, which matches the unique-keys property.
#   Alternative: a list of records would require looping through every record to find a matching ID.

# Scenario F: a student's marks with their courses, organised inside the record
#   Choice: a DICTIONARY (the student record) containing LISTS (courses and
#   marks), a nested structure.
#   Reasoning: the record keeps everything for one student together, the lists keep order so courses[i] matches marks[i], and marks can repeat.
#   Alternative: separate top-level lists for courses and marks would spread one student's data around and make it easy to lose alignment.

students = {
    "DS001": {"name": "Daniel", "marks": {"Python": 78, "Statistics": 64, "Databases": 82}},
    "DS002": {"name": "Amina",  "marks": {"Python": 91, "Statistics": 73, "Databases": 88}},
    "DS003": {"name": "Brian",  "marks": {"Python": 56, "Statistics": 68, "Databases": 61}},
}

menu = """
=== Student Records ===
 1. View all students
 2. Add a student
 3. Search for a student
 4. Update a student's mark
 5. Add a course
 6. Remove a course
 7. Display all unique courses
 8. Display students in a course
 9. Display a student's record
10. Create backup
11. Restore from backup
 0. Quit"""
 
while True:
    print(menu)
    choice = input("Choose: ").strip()
 
    to_show = []  # IDs to print in the shared display block at the bottom
 
    if choice == "0":
        print("Goodbye.")
        break
 
    elif choice == "1":
        to_show = list(students)
 
    elif choice == "2":
        name = input("Name: ").strip().title()
        if not name:
            print("Name cannot be empty.")
        else:
            number = len(students) + 1
            while f"DS{number:03d}" in students:
                number += 1
            sid = f"DS{number:03d}"
 
            marks = {}
            print("Enter courses and marks (blank course name to finish).")
            while True:
                course = input("  Course: ").strip().title()
                if not course:
                    break
                while True:  # validate mark
                    try:
                        mark = float(input(f"  Mark for {course}: "))
                        if 0 <= mark <= 100:
                            break
                    except ValueError:
                        pass
                    print("Enter a number between 0 and 100.")
                marks[course] = int(mark) if mark.is_integer() else mark
 
            students[sid] = {"name": name, "marks": marks}
            print(f"Added {name} as {sid}.")
 
    elif choice == "3":
        term = input("Name to search: ").strip().lower()
        to_show = [sid for sid, r in students.items() if term in r["name"].lower()]
        if not to_show:
            print("No matches.")
 
    elif choice in ("4", "5", "6"):
        sid = input("Student ID: ").strip().upper()
        record = students.get(sid)  # a REFERENCE to the record, not a copy
 
        if record is None:
            print(f"No student with ID {sid}.")
        else:
            if choice == "4":
                course = input("Course: ").strip().title()
                if course not in record["marks"]:
                    print(f"{record['name']} is not taking {course}.")
                else:
                    while True:
                        try:
                            mark = float(input("New mark: "))
                            if 0 <= mark <= 100:
                                break
                        except ValueError:
                            pass
                        print("Enter a number between 0 and 100.")
                    record["marks"][course] = int(mark) if mark.is_integer() else mark
                    print("Mark updated.")
 
            elif choice == "5":
                course = input("Course to add: ").strip().title()
                if course in record["marks"]:
                    print("Already taking that course.")
                else:
                    while True:
                        try:
                            mark = float(input(f"Mark for {course}: "))
                            if 0 <= mark <= 100:
                                break
                        except ValueError:
                            pass
                        print("Enter a number between 0 and 100.")
                    record["marks"][course] = int(mark) if mark.is_integer() else mark
                    print("Course added.")
 
            else:  # choice == "6"
                course = input("Course to remove: ").strip().title()
                if record["marks"].pop(course, None) is None:
                    print(f"{record['name']} is not taking {course}.")
                else:
                    print("Course removed.")
 
    elif choice == "7":
        courses = {c for record in students.values() for c in record["marks"]}
        print("Courses taken by the class:", ", ".join(sorted(courses)) or "none")
 
    elif choice == "8":
        course = input("Course: ").strip().title()
        names = [r["name"] for r in students.values() if course in r["marks"]]
        print(f"Taking {course}:", ", ".join(names) if names else "nobody")
 
    elif choice == "9":
        sid = input("Student ID: ").strip().upper()
        if sid in students:
            to_show = [sid]
        else:
            print(f"No student with ID {sid}.")
 
    elif choice == "10":
        backup = copy.deepcopy(students)  # nested dicts -> shallow copy would share records
        print(f"Backup created ({len(backup)} students).")
 
    elif choice == "11":
        if backup is None:
            print("No backup yet.")
        else:
            students = copy.deepcopy(backup)  # copy again so the backup stays untouched
            print("Records restored from backup.")
 
    else:
        print("Invalid choice.")
 
    # ---- shared display block: replaces the show() function ----
    for sid in to_show:
        record = students[sid]
        print(f"\n{sid} | {record['name']}")
        if not record["marks"]:
            print("   (no courses)")
        else:
            for course, mark in record["marks"].items():
                print(f"   {course:<15}{mark}")
            print(f"   {'Average':<15}{sum(record['marks'].values()) / len(record['marks']):.1f}")