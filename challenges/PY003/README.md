# PY003 — Student Introduction Generator

**Challenge ID:** PY003  
**Phase:** Foundations  
**Topic:** Input & Output + String Basics  
**Difficulty:** Beginner → Intermediate  
**Estimated time:** 45 minutes  
**Original deadline:** Saturday, 8:00 PM

## 🎯 Learning Objectives

By completing this challenge, you should be able to:

- Collect user input using `input()`.
- Display formatted output using `print()`.
- Store user input in variables.
- Format output using f-strings.
- Access characters using string indexing and slicing.
- Apply string methods to user input.
- Handle unnecessary spaces around a name.
- Read error messages and explain how errors occur.
- Translate English requirements into Python instructions.

## 📝 Problem Statement

You are building a small Student Introduction Generator.

A user should be able to enter some basic information about themselves, and your program should generate a short personalized profile.

Ask the user for:

- Their full name.
- Their course.
- Their university.
- Their favourite programming language.

The program should then produce a report similar to:

```text
================================
       STUDENT PROFILE
================================

Name: Peter Mwangi
Course: Data Science
University: JKUAT
Favourite Language: Python

Name length: 12
First character of name: P
Last character of name: i

Thank you, Peter Mwangi!
================================
```

The exact information and output must come from the user's input. Do not hard-code the user's answers.

## 📋 Requirements

### Part 1 — Get Information from the User

Use `input()` to collect all four pieces of information.

Store each response in an appropriately named variable.

### Part 2 — Produce Formatted Output

Use `print()` to display the student's information in a clear, readable format.

Use at least one f-string in your output.

### Part 3 — Work with the Student's Name

Using the name entered by the user:

- Display the number of characters in the name.
- Display the first character.
- Display the last character.

You must use string indexing and/or slicing for the character operations.

### Part 4 — Use String Methods

Apply at least two string methods to the user's input.

At least one method should affect how the text is displayed.

Choose the methods yourself.

### Part 5 — Handle Unnecessary Spaces

Your program should still work if the user enters their name with unnecessary spaces at the beginning or end.

For example, a user might enter their name with spaces around `Peter Mwangi`.

The resulting profile should not display those unnecessary spaces around the name.

## 🐛 Debugging Requirement

Before submitting, deliberately test your program with different inputs.

Perform at least two different tests.

### A. Identify an Error

Give one actual error encountered while writing or testing your program.

Record the error message, or at least its important part.

If your program runs without producing an error, deliberately introduce a small mistake, run the program, and investigate the resulting error.

### B. Interpret the Error

Explain in your own words what Python is telling you went wrong.

Do not simply provide the name of the error. Explain what operation caused the problem and what Python expected instead.

### C. Explain Your Fix

Document:

1. What caused the error.
2. How you fixed it.
3. Why your fix solves the problem.

**These debugging observations and explanations must appear as clear comments in your submitted Python code.**

## 🧠 Discussion Milestone — English to Python

During the challenge, attempt to translate the English requirements into Python instructions yourself.

The main discussion after the deadline will focus on this process.

Be prepared to explain:

**How did you turn the English description into Python instructions?**

Use this breakdown:

1. What information do I need?
2. What variables do I need?
3. What operations do I need?
4. What Python tools or concepts can perform those operations?
5. What should the program output?

Develop the habit of asking what a problem requires and how to express each step in Python, rather than immediately asking which code to type.

## 🚨 Challenge Rules

### First 30 minutes

**Not allowed:**
- ChatGPT, Gemini, or other AI tools.
- Searching for solutions.
- Copying code.

**Allowed:**
- Official Python documentation.
- Your own notes.
- `print()` debugging.
- Experimenting in Python or Jupyter.

After 30 minutes, research and AI are allowed, but you must understand the solution and implement it yourself.

## 📤 Submission

When you have genuinely attempted the challenge, send:

**✅ Solved**

Do not post your code yet.

We will discuss the approach, debugging experience, and English-to-Python translation first, then share and compare implementations.

## 🎯 Concepts Being Tested

- `input()`
- `print()`
- Variables
- `str`
- f-strings
- String indexing
- String slicing
- Basic string methods
- Reading error messages
- Basic debugging
- Translating an English problem into Python

## 🏁 The Goal

Build the habit of turning a problem statement into a sequence of clear instructions, then using Python to express those instructions.

**Understand the requirement. Break it down. Write the code. Test your reasoning.** 🐍
