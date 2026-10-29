# 🐍 PY010 — Refinement Challenge: From Almost Working to Reliable Python

**Challenge ID:** PY010  
**Phase:** Phase 4 — Functions, Control Flow & Problem-Solving Refinement  
**Level:** Targeted Refinement  
**Estimated Time:** 90–120 minutes  
**Deadline:** Thursday, 29 October 2026, at 8:00 PM EAT

## 🎯 The Purpose

You have already learned how to write loops, work with dictionaries, define functions, pass arguments, and use functional programming techniques.

But knowing a concept and using it reliably are two different things.

A loop can run forever. A program can process the same record repeatedly. A function can return too early. A dictionary can contain the information you need, yet your code can still struggle to retrieve it. A recursive function can work for one input and fail badly for another.

This challenge revisits the areas where we need more practice.

You will diagnose faulty logic, correct code, implement small functions, and explain why your revised solutions work.

**The objective is not merely to make your code run. It is to understand why it runs correctly.**

---

## Section 1: Control Flow Under Control

### Question 1 — The Repeating Records [12 Marks]

A program receives a list of student records that must be processed one at a time.

The following code is supposed to print each student's name once.

    students = ["Amina", "Brian", "Cynthia", "David"]

    index = 0

    while index < len(students):
        print(students[index])

Unfortunately, the program does not finish on its own.

**Tasks**

a. Explain precisely why the program does not terminate. [3 marks]

b. Correct the program using a while loop. [3 marks]

c. Rewrite the solution using a for loop. [2 marks]

d. Suppose the list contains 100 records. Describe two different programming mistakes that could cause records to be skipped or printed repeatedly. [4 marks]

### Question 2 — Stop, Skip, or Finish? [12 Marks]

A department processes a collection of transaction amounts.

The rules are:

- Ignore amounts that are zero or negative.
- Stop processing when the amount -999 is encountered.
- For every other positive amount, print it.
- Once the processing function finishes, the caller should receive the number of valid amounts processed.

**Tasks**

a. Write a function that processes the following list according to the rules:

    amounts = [120, 0, 75, -5, 210, -999, 90, 150]

b. Use continue to handle the values that should be skipped. [3 marks]

c. Use break to stop processing at the sentinel value. [3 marks]

d. Return the number of valid amounts processed. [2 marks]

e. Explain the difference between break, continue, and return in the context of your function. [4 marks]

**Important:** Values appearing after the sentinel must not be processed. Check for the sentinel before applying the rule that skips non-positive values.

---

## Section 2: Dictionaries Within Dictionaries

### Question 3 — The Department Records [14 Marks]

A university department stores information about its students in a nested dictionary.

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

**Tasks**

a. Loop through the structure and print each student's name together with their department and student ID. [4 marks]

b. Print the names of all students who are currently active. [3 marks]

c. Find every student taking Python and print their name and department. [3 marks]

d. Count how many students are registered in each department. [2 marks]

e. Explain why looping through the outer dictionary alone does not directly give you each student's details. [2 marks]

**Requirements**

- Use loops to navigate the nested structure.
- Do not manually print each student's details.
- Your code must continue to work if another department or student is added to the dictionary.

---

## Section 3: Functions That Behave Properly

### Question 4 — The Function Workshop [14 Marks]

A small reporting program needs reusable functions rather than repeated calculations and hardcoded results.

Implement the following functions.

**A. Flexible average**

Write a function called calculate_average that accepts any number of numeric positional arguments and returns their average.

Requirements:

- Use *args.
- Return None when no values are provided.
- Do not print the result inside the function.
- Do not use Python's built-in sum() function.

Test it with zero arguments, one argument, and several arguments.

**B. Configurable report**

Write a function called build_report that accepts a student's name as a required argument and accepts any number of additional named details.

For example, a caller should be able to provide a student's name, department, average, and academic status without the function needing a separate parameter for every possible detail.

Requirements:

- Use **kwargs.
- Return a report as a string.
- Handle the case where no additional details are provided.

**C. Strict parameter positions**

Write a function called register_session with these requirements:

- session_name must be supplied positionally.
- duration must be supplied positionally.
- instructor must be supplied by keyword.
- room must be supplied by keyword and default to "Lab 1".

Use positional-only and keyword-only parameters to enforce these rules.

Demonstrate one valid call and explain why each of the following calls is invalid:

    register_session(
        session_name="Python Practice",
        duration=60,
        instructor="Grace"
    )

    register_session(
        "Python Practice",
        60,
        "Grace"
    )

**D. Explain your design**

Briefly explain the purpose of *args, **kwargs, positional-only parameters, and keyword-only parameters. [2 marks]

**Marking:** Correct behaviour, handling of edge cases, appropriate parameter syntax, and meaningful return values will be assessed across the question.

---

## Section 4: Function Composition and Higher-Order Functions

### Question 5 — Building a Processing Pipeline [12 Marks]

A student-reporting system performs several operations on a name:

1. Remove unnecessary spaces.
2. Convert the name to title case.
3. Add a greeting.

Implement three separate functions:

- clean_name(name)
- format_name(name)
- make_greeting(name)

Each function must return a value rather than print it.

**Tasks**

a. Test each function independently. [3 marks]

b. Combine the functions so that the original name passes through the three operations in the correct order. [3 marks]

c. Write a higher-order function called apply_operation that accepts a value and a function, applies that function to the value, and returns the result. [3 marks]

d. Use apply_operation with at least two different functions. [3 marks]

**Test input:**

    name = "   aMINA wanjiku   "

Your implementation should not depend on the name being correctly capitalised or free of unnecessary spaces.

**Remember:** Passing a function to another function is different from calling that function immediately.

---

## Section 5: Lambdas and Recursion

### Question 6 — Small Functions, Big Ideas [16 Marks]

This section focuses on two areas that require more than memorising syntax.

### A. Lambda expressions [6 marks]

Given the following records:

    students = [
        {"name": "Amina", "score": 72},
        {"name": "Brian", "score": 91},
        {"name": "Cynthia", "score": 65},
        {"name": "David", "score": 84}
    ]

**Tasks**

a. Sort the students by score from highest to lowest using sorted() and a lambda expression. [2 marks]

b. Sort the students alphabetically by name using a lambda expression. [2 marks]

c. Explain what the lambda expression returns for each student and how sorted() uses that value. [2 marks]

### B. Recursion [10 marks]

Write a recursive function called recursive_sum(n) that returns the sum of all integers from 1 through n.

For example, calling recursive_sum(5) should return 15.

**Tasks**

a. Implement the function recursively without using a loop or the built-in sum(). [4 marks]

b. Identify the base case and explain why it is necessary. [2 marks]

c. Explain how the function moves towards its base case. [2 marks]

d. Test the function with at least three inputs, including the smallest input your implementation supports. [2 marks]

**Reflection:** What could happen if a recursive function never reaches its base case?

---

## Section 6: Membership and Identity

### Question 7 — Similar Does Not Mean Identical [8 Marks]

Consider the following code:

    first = [10, 20, 30]
    second = [10, 20, 30]
    third = first

    target = 20

**Tasks**

a. Predict the result of each expression before running the code. [4 marks]

    target in first
    target not in second
    first == second
    first is second
    first is third

b. Explain the difference between the membership operators in and not in, and the identity operators is and is not. [2 marks]

c. Give one practical situation where checking identity is appropriate, and explain why checking equality would not express the same intention. [2 marks]

Do not rely on whether two variables happen to display the same contents. Think about what each operator actually tests.

---

## Section 7: The Final Debugging Clinic

### Question 8 — Diagnose Before You Repair [12 Marks]

A colleague has written a function intended to return the first positive number in a list.

    def find_first_positive(numbers):
        for number in numbers:
            if number <= 0:
                continue
            return number

        print("No positive number found")

They report that the function sometimes returns None, and their program behaves inconsistently when no positive number exists.

**Tasks**

a. Explain what happens when the list contains a positive number. [2 marks]

b. Explain what happens when the list contains no positive numbers. [3 marks]

c. Modify the function so it returns a consistent result in both cases. [3 marks]

d. Explain why return, continue, and printing a message are not interchangeable. [4 marks]

Test your revised function with:

    [0, -4, 12, 8]
    [-3, 0, -9]
    []

---

# 📦 Submission Requirements

Submit your completed work as a Python script or Jupyter Notebook, following the group's established submission process.

Your submission should contain:

1. Your solutions to the questions.
2. Meaningful function and variable names.
3. Comments explaining important decisions and non-obvious logic.
4. Test evidence for normal cases and edge cases.
5. Brief explanations wherever a question asks you to explain your reasoning.
6. An AI-assistance disclosure if required by the group's rules.

You may organise your work into separate functions or sections. You do not need to force every question into one large program.

## 🧪 Testing Expectations

At minimum, test:

- A loop that processes an empty collection and one that processes several items.
- A loop that must skip an item and another that must stop at a sentinel.
- Nested dictionaries with multiple departments and students.
- Functions with no optional arguments and with several arguments.
- Invalid function-call patterns for positional-only and keyword-only parameters.
- Function composition and higher-order function calls.
- Lambda sorting with multiple records.
- Recursion at the base case and with a larger input.
- Membership and identity expressions.
- A debugging function with positive, negative, and empty inputs.

Do not assume that a program is correct just because one test passes.

# 🧭 Challenge Rules

- For the first **30 minutes**, work independently. Do not use AI, solution searches, or copied code.
- Your notes, previous challenges, official Python documentation, print debugging, and your debugger are allowed.
- After the first 30 minutes, you may use AI or online research, but you must understand, adapt, and be able to explain anything you use.
- Do not post your code in the group before the agreed discussion stage.
- When finished, send **✅ Solved** in the group before the deadline.
- Be ready to explain not just what you changed, but why your changes work.

## 🏁 Final Reflection

After completing the challenge, answer these questions in a few sentences:

1. Which concept did you find most difficult, and why?
2. Which mistake are you now better equipped to recognise?
3. What will you check first when a loop runs indefinitely or a recursive function fails?
4. Which topic still needs another round of practice?

**The goal is dependable programming: code that terminates when it should, handles edge cases, and behaves the way you intended.** 🐍
