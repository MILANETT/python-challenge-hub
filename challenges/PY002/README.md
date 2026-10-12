# PY002 — Student Performance Checker

**Challenge ID:** PY002  
**Phase:** Foundations  
**Topic:** Data Types + Type Conversion + Operators  
**Difficulty:** Beginner → Intermediate  
**Estimated time:** 45 minutes  
**Original deadline:** Thursday, 12:00 PM

## 🎯 Learning Objectives

By completing this challenge, you should be able to:

- Work with different Python data types.
- Convert strings into appropriate numeric types.
- Perform arithmetic operations without using `sum()`.
- Use comparison and logical operators.
- Use assignment operators to update values.
- Test membership using `in`.
- Test object identity using `is`.
- Distinguish between `None` and ordinary values.
- Generate a report from calculated results rather than hard-coded output.

## 📝 Problem Statement

You are building a small student performance checker.

Start with the following data:

```python
name = "Peter"
age = "20"
marks = ["72", "45", "89", "63", "51"]
has_submitted = True
bonus = None
```

Write a Python program that processes this information and produces a performance report.

## Part 1 — Prepare the Data

The `age` and all values in `marks` are currently strings.

Convert them into appropriate numeric types.

Then calculate:

- Total marks.
- Average mark.

**Restriction:** Do not use `sum()`.

## Part 2 — Check the Student's Performance

Create variables that determine whether:

- The student is an adult (`age >= 18`).
- The average mark is at least 50.
- The average mark is at least 70.
- The student has submitted their work.

Create a variable called `passed`.

A student passes if:

**Their average is at least 50 AND they have submitted their work.**

## Part 3 — Check the Marks

Using a membership operator, determine:

- Whether `"89"` exists in the original `marks` list.
- Whether `"100"` exists in the original `marks` list.

## Part 4 — Handle the Bonus

The student's bonus is initially:

```python
bonus = None
```

Using an identity operator, check whether `bonus` is `None`.

If it is `None`, assign a bonus of `5`.

Then use an assignment operator such as `+=` to add the bonus to the average.

Calculate:

**Final average = average + bonus**

## Part 5 — Produce the Report

Print a report containing at least the following information:

```text
Student: Peter
Age: 20
Total marks: 320
Average: 64.00
Adult: True
Passed: True
Contains 89: True
Contains 100: False
Bonus: 5
Final average: 69.00
```

These values illustrate the expected result. Your program must calculate them; do not hard-code them.

## 📋 Required Concepts

Your solution must demonstrate all of the following:

- `int`
- `float`
- `str`
- `bool`
- `None`
- Type conversion
- Arithmetic operators
- Comparison operators
- Logical operators
- Assignment operators (`=`, `+=`, etc.)
- Membership operators (`in`, `not in`)
- Identity operators (`is`, `is not`)

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

After 30 minutes, you may research or use AI, but you must understand the solution and implement it yourself.

## 🧠 Reflection and Discussion

After solving, be prepared to explain:

1. Where did you use type conversion?
2. Give an example of an arithmetic operator you used.
3. Give an example of a comparison operator.
4. Where did you use a logical operator?
5. Where did you use a membership operator?
6. Why did you use `is None` instead of `== None`?
7. Where did you use an assignment operator other than `=`?
8. Which variables in your program are `int`, `float`, `str`, `bool`, and `None`?

## 📤 Submission

Once you have genuinely attempted the problem, send:

**✅ Solved**

Do not post your code yet.

We will discuss the logic and approaches first, then share and compare implementations.

## 🏁 The Goal

Learn to recognize Python's data types, convert values correctly, and use operators to build a program whose results are calculated rather than hard-coded.

**Understand the values. Choose the right operations. Explain your reasoning.** 🐍
