# PY005 — Student Records Manager

**Challenge ID:** PY005  
**Phase:** Data Structures  
**Difficulty:** Intermediate  
**Estimated time:** 75 minutes  
**Original deadline:** Thursday, 8:00 PM

## 🎯 Topics

- Lists
- List indexing and slicing
- List methods
- Tuples
- Sets
- Set operations
- Dictionaries
- Dictionary methods
- Nested data structures
- Mutability vs. immutability
- References vs. copies
- Shallow vs. deep copying

## 🧠 Problem-Solving Milestone

**Given a problem, can you choose the appropriate data structure?**

This challenge is not mainly about memorizing methods.

Learn to examine information and ask:

*What kind of data is this, what operations do I need, and which structure makes those operations natural?*

## 🏫 The Problem

You have been asked to build a small Student Records Manager for a class.

Start with the following data:

```python
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
```

Build a program that works with this information.

## ⚠️ Important — Reflections Must Be Written in Your Code

Whenever you are asked to explain, reflect, justify, observe, or reason, write your response as Python comments in your submitted code.

For example:

```python
# I chose a set because duplicate values should automatically be removed.
# A list would be less appropriate because I do not need duplicate students.
```

Do not leave your reasoning only in your head or wait until the discussion session to explain it.

Your submitted code must contain your reasoning as comments.

## Part 1 — Understand the Data

Identify the data structure being used for each of the following and explain why it makes sense:

1. `students`
2. Each individual student's record
3. `courses`
4. `marks`
5. `class_rooms`
6. `python_students`
7. `database_students`

Write your answers as comments in your code.

Consider:

- What kind of information is stored?
- Does order matter?
- Do duplicates matter?
- Are labels or keys needed?
- Should the data be mutable?

## Part 2 — Lists

Using `students`:

1. Print the first student's complete record using indexing.
2. Print the last student's complete record using indexing.
3. Print the first two students using slicing.
4. Add a new student to the class.
5. Remove one student.
6. Change a student's mark.
7. Demonstrate at least three different list methods meaningfully.

Write comments explaining:

- Why `students` is stored as a list.
- Why indexing and slicing are useful.
- What each list method does and why you chose it.

## Part 3 — Tuples

Use `class_rooms`:

1. Access the first room.
2. Access the last room.
3. Slice the tuple to obtain the first two rooms.
4. Attempt to modify one of its elements.

Observe what happens.

Write comments explaining:

- What happened when you tried to modify the tuple.
- Why Python prevents the modification.
- What this tells you about immutability.
- Why a tuple could be appropriate for this data.

## Part 4 — Sets

Use the supplied `python_students` and `database_students` sets to determine:

1. Students taking both Python and Databases.
2. Students taking Python but not Databases.
3. Students taking at least one of the two courses.
4. Whether `"Brian"` is taking Python.
5. Add a new student to the Python set.
6. Remove a student from the Database set.

Write comments explaining:

- What each set operation does.
- Why a set is useful here.
- Why a list would be less suitable for some of these operations.

## Part 5 — Dictionaries

Using the student records:

1. Find a student's name using a dictionary key.
2. Find their student ID.
3. Access their courses.
4. Access their marks.
5. Add a new piece of information to a student record.
6. Modify an existing piece of information.
7. Remove a piece of information.
8. Demonstrate at least three dictionary methods meaningfully.

Write comments explaining:

- What a key-value pair represents.
- Why dictionaries are useful for student records.
- Why a dictionary is more appropriate than a simple list for labelled information.

## Part 6 — Nested Data Structures

The `students` structure contains multiple layers:

```text
students
   ↓
list
   ↓
student dictionary
   ↓
courses → list
marks   → list
```

Using the existing data:

1. Print Daniel's second course.
2. Print Amina's third mark.
3. Print Brian's complete list of marks.
4. Change one student's course.
5. Change one student's mark.
6. Add another course and corresponding mark where appropriate.

Write comments explaining how you navigated through the nested structure.

Explain the sequence of structures you moved through rather than simply stating the final result.

## Part 7 — Mutability vs. Immutability

Create examples using:

- A list
- A tuple
- A set
- A dictionary

For each one, determine whether it is mutable or immutable.

Write comments answering:

*What does mutability actually mean in Python?*

Do not simply write `# List = mutable`.

Explain what it means to change an object after it has been created.

## Part 8 — References vs. Copies

Create:

```python
marks = [70, 80, 90]
```

Then create another variable referring to that list.

Modify the list through the second variable and observe what happens to the original.

Write comments explaining:

- What you expected.
- What actually happened.
- Why the original list changed.
- What this tells you about variables and references in Python.

## Part 9 — Shallow vs. Deep Copying

Create a nested structure such as:

```python
student = {
    "name": "Daniel",
    "marks": [70, 80, 90]
}
```

Create:

1. A normal reference.
2. A shallow copy.
3. A deep copy.

Modify the nested `marks` list through the appropriate variables and observe which objects are affected.

Write comments answering:

- What is a shallow copy?
- What is a deep copy?
- What happened when the nested list was modified?
- Why can shallow copying be dangerous with nested mutable structures?

## Part 10 — Data-Structure Decision Challenge 🧠

For each situation, choose the most appropriate data structure.

For every answer, provide your choice, your reasoning, and why another reasonable alternative would be less suitable.

**Scenario A:** Store the names of students in the order they registered.

**Scenario B:** Store a student's information with meaningful labels such as `name`, `age`, and `course`.

**Scenario C:** Store the unique courses available in a university, automatically eliminating duplicates.

**Scenario D:** Store the fixed coordinates of a point: `x, y`. The values should not accidentally be changed.

**Scenario E:** Store students and quickly associate each student ID with that student's record.

**Scenario F:** Store a student's marks together with their courses, keeping everything organized inside their student record.

Write every answer and justification as comments in your Python file.

Do not submit only the structure names. We are testing your decision-making, not your ability to recognize vocabulary.

## 🏆 Final Task — Mini Student Record System

Build a small interactive program that allows the user to:

1. View all students.
2. Add a student.
3. Search for a student.
4. Update a student's mark.
5. Add a course.
6. Remove a course.
7. Display all unique courses taken by the class.
8. Display students taking a particular course.
9. Display a selected student's record.
10. Create a backup copy of the student records.

### Restrictions

- Do not use classes yet.
- Do not use external libraries.
- Do not use pandas.
- Use Python's built-in data structures.
- Choose the structure that best fits each piece of information.
- Do not create unnecessary duplicate structures simply to satisfy the challenge.

## 🧠 Final Problem-Solving Reflection

Before coding the final task, write your answers as comments at the top of your program.

```python
# 1. What information am I storing?
#
# 2. Which information is ordered?
#
# 3. Which information needs unique values?
#
# 4. Which information needs labels/keys?
#
# 5. Which information should not change?
#
# 6. Which structures will be nested?
#
# 7. Where could references cause unexpected changes?
#
# 8. Where might I need a copy instead of the original object?
```

Then implement your solution.

After implementation, add another comment section:

```python
# FINAL REFLECTION
#
# Which data structure did I find easiest to use?
#
# Which one confused me the most?
#
# Did I ever choose the wrong structure initially?
#
# What made me change my decision?
#
# What did I learn about references and copies?
#
# What is one thing I understand now that I did not understand
# before starting this challenge?
```

These reflections must be visible in your submitted `.py` file.

## 🐛 Debugging Requirement

Encounter or deliberately create at least two different errors or unexpected behaviours involving data structures.

For each one, write a comment documenting:

1. What you expected.
2. What actually happened.
3. The error or behaviour you observed.
4. Why it happened.
5. How you fixed it.

Use this structure:

```python
# DEBUGGING REFLECTION 1
# Expected:
#
# Actual:
#
# Why it happened:
#
# Fix:
```

Repeat the structure for the second debugging reflection.

## ⏱️ Challenge Rules

### First 30 minutes

**Not allowed:**
- ChatGPT.
- Gemini.
- Google searches for solutions.
- Copying code.

**Allowed:**
- Python documentation.
- Your notes.
- Previous challenges.
- `print()`.
- A debugger.
- Experimenting in Python.

### After 30 minutes

AI and searching are allowed, but you must understand and rewrite anything you use.

## 📤 Submission

When you have genuinely attempted the challenge, send:

**✅ Solved**

Then wait for the discussion session.

During discussion, be prepared to explain:

1. Why you chose each data structure.
2. What surprised you about references.
3. What happened with shallow versus deep copies.
4. Why sets were useful.
5. Why dictionaries were useful.
6. The hardest nested structure you worked with.
7. One data structure you initially chose incorrectly.
8. What made you change your decision.
9. The hardest English-to-Python translation.

## 🎯 The Real Goal

By the end of PY005, stop thinking:

*Which Python syntax do I use?*

Start thinking:

*What is the nature of this data, what operations do I need, and which data structure makes those operations natural?*

### The progression so far

- **PY001:** Manipulate values.
- **PY002:** Work with data types and operators.
- **PY003:** Interact with users and strings.
- **PY004:** Control program flow.
- **PY005:** Choose and structure data.

The syntax is becoming the tool. Your decisions are becoming the programming. 🐍
