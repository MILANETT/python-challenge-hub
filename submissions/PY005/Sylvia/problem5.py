#We use a list of dictionaries here because there are multiple students
#The students' info has keys such as name and courses thus we use a dictionary
#The courses key uses a list to allow addition of more courses
#The marks key uses a list because there can be duplicates
import copy

students=[
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
#classRooms uses a tuple because they should remain unchanged
#pythonStudents and databaseStudents uses sets to avoid duplicates
classRooms=("Room A","Room B","Room C")
pythonStudents={ "Daniel","Amina","Brian"}
databaseStudents={ "Daniel","Amina","Brian"}

print(students[0])
print(students[2],'\n')
print(students[0:2])
print("========================")
students.append({
    "name":"Sylvia",
    "student_id":"DS004",
    "courses":["Python","Statistics","Databases"],
    "marks":[40,35,78]
})
students.pop(1)
students[1]["marks"][2]=87
print(students[1])
print("===========================")
print(students.count(students))
#Three methods
students[0].clear()
#the dictionary at index 0 is empty
print(students[0])

#inserting a new student at index 0
#this makes the previous index 0 to move to index 1
students.insert(0,{
    "name":"Andrew",
    "student_id":"DS005",
    "courses":["Python","Statistics","Databases"],
    "marks":[90,67,45]
    
})
print("Student 1:",students[0])

print("============Tuples================")

#Part 3
print(classRooms[0])
print(classRooms[-1])
print(classRooms[0:2])
#When I tried to assign:
#classRooms[2]="Room D"
#TypeError: 'tuple' object does not support item assignment
#It is appropriate because it is immutable

#Part 4
print("\n========Sets=========")
#intersection shows the common elements in both sets
print(pythonStudents .intersection(databaseStudents))
#difference shows the students that are in pythonStudents but not in databaseStudents
print(pythonStudents .difference(databaseStudents))
#union shows all the students in both sets without duplicates
print(pythonStudents .union(databaseStudents))

#A new student is added to the pythonStudents set
pythonStudents.add("Ethan")
print(pythonStudents)

#A student is removed from the databaseStudents set
databaseStudents.remove("Brian")
print(databaseStudents)
#A set is useful here because of its operations eg union
#A list would not be appropriate because its operations are limited.


#part 5
print("\n========Dictionaries===========")
#A key is like a label
#A value is the stored data accessed using the key
#A dictionary is suitable because it stores multiple pieces of data relating to one student
#A list does not have labels thus it is not suitable
print(students)
print(students[0]['name']) 
print(students[0]['student_id']) 
print(students[0]['courses']) 
print(students[0]['marks']) 
students[0]['marks'].insert(1,54)
print(students[0]['marks']) 
students[0]['student_id']="DS006"
print(students[0]['student_id'])
students[0]['marks'].pop(-1)
print(students[0]['marks']) 
#dictionary methods
print(students[0].keys())
print(students[1].values())
#nothing will be displayed since dict at index 1 is empty
print(students[3].items())

#part 6
print("\n=====Nested structures==========")
#To access the Daniel's 2nd course, I used indices
#Daniel's dictionary is in a list and so are the courses
#daniel 2nd course
print(students[0]["courses"][1])

#To access the Amina's 3rd mark, I used indices
#Amina's dictionary is in a list and so are the marks
#amina 3rd mark
print(students[2]["marks"][2])

#To access the Brian's marks, I used indices
#Brian's dictionary is in a list so I used a index to access it
#I used the marks key to access the complete marks list
print(students[3]["marks"])
#I used an index to access a student's dictionary
#then used the courses key and an index to assign a new course to the courses list
students[2]["courses"][2]="Calculus"
print(students[2]["courses"])
#I used an index to access a student's dictionary
#then used the courses key and an index to assign a new course to the courses list
students[2]["marks"][1]=76
print(students[0]["marks"])

#I used an index to access a student's dictionary
#then used the courses key and append to assign a new course to the courses list
#I did the same for the marks key to assign a new mark for the new course
# another course and corresponding marks
students[-1]['courses'].append("Algebra")
print(students[-1]['courses'])
students[-1]["marks"].append(74)
print(students[-1]["marks"])

#part 7
print("\n=====Mutability v immutability==========")
# Mutability refers to the ability of an object to allow changesafter it has been created.
#list
#It is mutable because we can change the elements in the list after it has been created
artists=["Njerae","Little mix","Mutoriah","Sauti sol","Charisma" ]
#tuple
#It is immutable because we cannot change the elements in the tuple after it has been created
student_id=("DS001","DT003","HG004")
#set
#It is mutable because we can change the elements in the set after it has been created
unitCode={"SCT45","FGH78","SDS23","FGD64"}
#dictionary
#It is mutable because we can add or remove elements in the dictionary after it has been created
athlete={
    "name":"Kipyegon Ann",
    "race":"100m",
    "venue":"London"
}

#part 8
print("\n=====references vs copies======")
marks=[70,80,90]
points=marks
points[2]=85
print(points)
print(marks)
#I expected the marks list to retain its original figures
#The points list was changed and the marks list also changed
#This is because points is a reference to the marks list 
#It shows that since a reference points to the same memory location as marks, any changes made to points will also affect marks.

#part 9
student={
    "name":"Sylvia",
    "marks":[45,60,90]
}
stdnt=student
stdnt["id"] = "Ds02"
print(student)

stdent1=copy.copy(student)
stdent1["name"]="Ethan"
stdent1["marks"][2]=80
print("======Shallow copy========")
print(stdent1)
print(student)

stdent2=copy.deepcopy(student)
stdent2["name"]="Sly"
stdent2["marks"][2]=50
print("======Deep copy========")
print(stdent2)
print(student)
#When I made a shallow copy of the student dictionary, changes made to the stdent1 dictionary affected the original student dictionary.
# When I made a deep copy of the student dictionary, changes made to the stdent2 dictionary did not affect the original student dictionary.
# This is because a shallow copy creates a new object but does not create copies of nested objects, while a deep copy creates a new object and copies all nested objects.

#part 10
#scenario A
#List because order is important here
#Set is not appropriate because it is unordered
_students=["Sylvia","Andrew","Ethan"]

#scenario B
#Dictionary because the data has labels
#List is not appropriate because it does not have labels
Students={
    "name":"Sylvia",
    "age":24,
    "course":"Medicine"
}
#scenario C
#Set is used because it does not allow duplicates 
#List is not appropriate because it allows duplicates
courses={"Medicine","Computer science","Data science"} 

#scenario D
#tuple is used since the data is fixed
#List is not appropriate because it is mutable
coordinates=(45,67)

#scenario E
#Dictionary of dictionaries is used because the data has labels and there are multiple students
#List of dictionaries is not appropriate because it does not have labels
students={
    "DS001":{
        "name":"Sylvia",
        "age":24,
        "course":"Medicine"
    }
}
#scenario F
#List of dictionaries is used because we are storing multiple things that relate to one person
students=[
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
]


#final reflection
#The easiest data structure to use was the list because it is mutable and is ordered.
#The most confusing data structure to use was the set because it is unordered.
#I learnt that when you reference a variable any changes to the reference reflects on the original while for copies the original is not affected.
#Before this challenge i did not know set operations.

#DEBUGGING REQUIREMENTS
#When adding a new course and the corresponding marks,i tried to use slicing and the courses key but i got TypeError
#TypeError:list indices must be integers or slices,not str
#To fix it,I used index -1

#When i was deepcopying , I got AttributeError: dict object has no attribute 'deepcopy'
# I had not imported the copy module, when i imported it the error was fixed