# 🐍 PY006 — Reusable Functions: From Instructions to Results

**Phase:** Phase 4 — Functions  
**Difficulty:** 🟢 Beginner  
**Estimated time:** 60 minutes  
**Deadline:** Thursday, 15 October 2026, at 8:00 PM EAT

## 🎯 Challenge Objective

As our Python programs become more complex, repeating the same calculations and instructions makes code harder to maintain.

Functions help us organize instructions into reusable blocks. However, to use functions confidently, we must also understand how information enters a function, how results leave it, and where variables can be accessed.

In this challenge, you'll build a small student score calculator using a reusable function. You'll also investigate parameters, arguments, return values, and the foundations of variable scope.

The goal is to understand not just how to write a function, but how to design one that can be reused in different situations.

## 📝 The Problem

Create a program that collects the names and marks of two students, calculates their average marks, and displays a report for each student.

Your program must use a reusable function rather than repeating the same calculation throughout the code.

## Part 1 — Create a Reusable Function

Define a function named `calculate_average` that:

- Accepts three subject marks as parameters.
- Calculates the average of the three marks.
- Returns the calculated average using `return`.
- Does not print the average from inside the function.

Call this function for both students and store the returned values in variables.

### Investigation

Before moving on, answer these questions in comments in your code:

1. What is the difference between defining a function and calling it?
2. What are parameters?
3. What are arguments?
4. When you call your function, what information are you passing into it?
5. Why is reusing the same function better than repeating the calculation?

**Important:** Do not use Python's built-in `sum()` function for the calculation.

## Part 2 — Collect and Display Student Information

For each student:

1. Ask for their name.
2. Collect marks for three subjects.
3. Convert the marks to appropriate numeric values.
4. Call `calculate_average()` to calculate their average.
5. Store the returned average in a variable.
6. Display their name and average, formatted to two decimal places.

Your report should clearly distinguish the two students.

### Example Run

The following is an example of how your program might interact with the user. Your prompts and report layout may differ, provided the required information and calculations are correct.

```text
=== STUDENT SCORE CALCULATOR ===

Enter first student's name: Amina
Enter mark for subject 1: 80
Enter mark for subject 2: 70
Enter mark for subject 3: 90

Enter second student's name: Brian
Enter mark for subject 1: 60
Enter mark for subject 2: 50
Enter mark for subject 3: 70

=== STUDENT REPORTS ===

Student: Amina
Average: 80.00

Student: Brian
Average: 60.00
```

Your output must be based on the information entered by the user. Do not hard-code the example names, marks, or averages.

## Part 3 — Investigate Parameters, Arguments, and Return Values

Now investigate how information moves between your function and the rest of your program.

Using your calculator and small experiments where necessary, explore the following:

1. What happens when you pass different marks into the same function?
2. What is the relationship between an argument and its corresponding parameter?
3. What is the difference between `return` and `print()`?
4. What happens if a function calculates a value but does not explicitly return it?
5. Why can a returned value be stored in a variable and used in another calculation?
6. Why is it useful to keep the calculation separate from the reporting logic?

Record your observations in comments using your own words.

Your experiments should demonstrate the behavior you describe rather than simply repeat definitions.

## Part 4 — Investigate Variable Scope

A function can use variables, but where a variable is created affects where it can be accessed.

You do not need to master every scope rule in this challenge. Your goal is to experiment, observe, and explain what happens.

Keep these experiments separate from your main student score calculator so that they do not interfere with its results.

### A. Accessing a global variable

1. Create a variable outside a function.
2. Access that variable from inside a function without modifying it.
3. Observe what happens.
4. Explain why the function can or cannot access it.

### B. Accessing a local variable

1. Create a variable inside a function.
2. Try to access it outside that function.
3. Observe what happens.
4. Explain the result, including any error you encounter.

### C. Using the same variable name

1. Create a variable outside a function.
2. Inside a function, create a local variable with the same name.
3. Display the variable inside the function.
4. Display the variable outside the function.
5. Explain whether changing the local variable necessarily changes the global variable.

### D. Investigating global modification

1. Create a global variable.
2. Experiment with reassigning that variable inside a function without using the `global` keyword.
3. Observe what happens.
4. Investigate how using `global` changes the behavior.
5. Explain what you discovered.

Use a separate experimental function for this investigation. Do not introduce unnecessary global-variable dependencies into your student score calculator.

### E. Comparing approaches

Consider two ways a function might obtain information:

- Reading or modifying variables outside the function.
- Receiving information through parameters and returning results.

Explain why the second approach is often preferable for calculations that need to be reused.

**Learning note:** These experiments introduce scope. PY007 will explore local and global scope, variable accessibility, and the `global` keyword in greater depth.

## Part 5 — Test Your Calculator

Testing helps you determine whether your program behaves correctly under different conditions.

Test your calculator with at least these cases:

- **Different marks:** Give the two students different sets of marks.
- **Zero marks:** Include at least one subject mark of `0`.
- **Identical marks:** Test a student whose three marks are identical.
- **Fractional average:** Use marks that produce an average with decimal places.
- **Repeated use:** Confirm that the same function correctly calculates averages for both students.

For each test, compare the displayed average with a manual calculation.

Document your testing evidence. Your evidence may include terminal output screenshots and brief explanations in your code comments.

## Part 6 — Debugging Investigation

Encounter or deliberately introduce at least **one bug** while developing or testing your program.

If your program works immediately, deliberately introduce a small mistake, investigate it, and then fix it.

Document the following in comments:

1. What did you expect to happen?
2. What actually happened?
3. What error message or unexpected behavior did you observe?
4. What caused the problem?
5. How did you fix it?
6. Why does your fix work?

The goal is not to avoid every mistake. It is to learn how to investigate and correct mistakes systematically.

## 📌 Challenge Rules

- Use `def` to define your function.
- Use parameters to receive the subject marks.
- Use `return` to send the average back to the calling code.
- Reuse the same calculation function for both students.
- Do not duplicate the average formula outside the function.
- Do not use `sum()`, `max()`, or `min()` in the calculator or scope experiments.
- Use concepts from previous challenges wherever appropriate.
- Keep your scope experiments separate from the main calculator.
- Use meaningful variable and function names.
- Write readable code with useful comments.
- Do not hard-code the example results.

## 📤 Submission Requirements

Submit the following when the challenge reaches the submission stage:

### 1. Python code

Your code must contain:

- The student score calculator.
- The reusable `calculate_average()` function.
- Separate scope experiments.
- Meaningful comments explaining your observations.

### 2. Testing evidence

Demonstrate that your calculator works with different marks, including a mark of `0`.

### 3. Reflection

Answer these questions in your own words:

1. What is the difference between defining and calling a function?
2. What is the difference between a parameter and an argument?
3. Why is `return` useful compared with `print()`?
4. What is the difference between a local variable and a global variable?
5. What happened when you used the same variable name inside and outside a function?
6. What did you observe when you tried to modify a global variable?
7. Why might passing arguments and returning results be preferable to relying on global variables?
8. What mistake did you encounter, and how did you debug it?
9. What was the most challenging part of this exercise?

### AI assistance disclosure

If you use AI after the initial 30 minutes, clearly comment where it assisted you and explain how it helped.

You must understand and be able to explain every part of your submitted code.

## 🧠 Learning Milestone

By completing this challenge, you should be able to:

- Define and call a reusable function.
- Pass arguments into parameters.
- Return a calculated result.
- Explain the difference between printing and returning.
- Reuse a function with different inputs.
- Recognize the difference between local and global variables.
- Describe what happens when variables share the same name in different scopes.
- Explain why well-designed functions should receive the information they need rather than depend unnecessarily on global state.
- Test and debug a small Python program systematically.

## 🚀 Our Challenge Workflow

### During your initial attempt

For the first 30 minutes, do not use AI, Google searches for solutions, or copied code.

You may use:

- Official Python documentation.
- Your own notes.
- Previous challenges.
- `print()` for debugging.
- Your debugger.
- Your own experiments.

### After the first 30 minutes

If you remain stuck, you may consult AI or other research resources. However:

- Understand any suggested code before using it.
- Adapt and implement the solution yourself.
- Do not submit code you cannot explain.
- Clearly disclose where AI assisted you and how it helped.

### When finished

1. Send **✅ Solved** in the group before the deadline.
2. Do not post your code prematurely.
3. Be prepared to explain your logic, testing, debugging, and reflections.

### After the deadline

We will discuss the logic and problem-solving approaches before comparing implementations.

Complete your reflection and be prepared to explain the decisions you made.

Remember: the objective isn't merely to make the program run. It's to understand why it works.

## 🔜 Coming Next: PY007 — Inside and Outside: Understanding Scope

In PY007, we'll build on the functions you've learned and explore how Python manages variables in greater depth.

### Topics coming up

- Local variables and local scope.
- Global variables and global scope.
- Variable accessibility inside and outside functions.
- Local and global variables sharing the same name.
- Modifying global variables and understanding the `global` keyword.
- Passing arguments and returning values instead of unnecessarily relying on global variables.
- Understanding how scope affects the design and behavior of functions.

### Preparation task

As you work on PY006, pay attention to where you create your variables and whether you can access them inside or outside a function.

Bring your observations to PY007. You don't need to master every scope rule now; you need to investigate, observe, and ask good questions.

**Your mission for now:** master the foundations of functions. We'll investigate scope more deeply in the next challenge.

Happy coding! 🐍🔥
