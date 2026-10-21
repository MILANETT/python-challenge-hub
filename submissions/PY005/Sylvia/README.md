## Understand the Data
A **list of dictionaries** is used to store the students' information. The students' names and courses are the keys.
The courses' values are written inside a **list** because it is **mutable**.
The marks' values are also in a **list** because it allows **duplicates**
The classrooms are stored in a **tuple** because the classes should remain **unchanged**
The pythonStudents and databaseStudents are stored in **sets** to **avoid duplicates**

## Lists
I used indexing to display the first and last student's records.I used append() to add a new student to the list of dictionaries.
I used pop() to remove one student record.
I used these list methods:
clear(): I used it to clear the record of the first student leaving it empty
insert(): I used it to insert a new student at index 0; this pushes the previous index 0 to 1

## Tuples
For the classroom tuple, I tried changing the values,
but I encountered an error since tuples are immutable.
I also used indexing to display the values at specific positions.

## Sets
I used three set operations on the pythonStudents and databaseStudents sets:
**intersection**
**difference**
**union**
I used add() to add a new student to the pythonStudents set
I used remove() to remove a student to the databaseStudents set


## Dictionaries
I used indexing in the dictionaries to access the students' name, courses, marks and id.
I also changed some student details using indexing.

## Nested structures
I used an index to access a student's dictionary 
then used the courses key and append to assign a new course to the courses list
I did the same for the marks key to assign a new mark for the new course

## Mutability and immutability
I created various data structures to investigate mutability.
I concluded that lists, sets and dictionaries are mutable while tuples are immutable

## References and copies
I used import **copy** to do shallow copying and deep copying
### Mini student program
I created the mini student program in problem5.1.py using AI

## DEBUGGING REQUIREMENTS
When adding a new course and the corresponding marks,i tried to use slicing and the courses key but i got TypeError
TypeError:list indices must be integers or slices,not str
To fix it,I used index -1

When i was deepcopying , I got AttributeError: dict object has no attribute 'deepcopy'
I had not imported the copy module, when i imported it the error was fixed
