# PY004 — Student Performance Analyzer

**Challenge ID:** PY004  
**Phase:** Phase 2 — Control Flow  
**Topic:** Control Flow  
**Difficulty:** Beginner → Intermediate  
**Estimated time:** 60 minutes  
**Original deadline:** Monday, 8:00 PM

## 🎯 Learning Objectives

By completing this challenge, you should be able to:

- Use `if`, `elif`, and `else` to make decisions.
- Combine conditional statements with loops.
- Use `for` loops and `while` loops appropriately.
- Validate user input.
- Use counters and accumulators.
- Calculate statistics without `max()`, `min()`, or `sum()`.
- Translate a larger problem into smaller programming tasks.
- Test boundary values and invalid input.

## 📝 Problem Statement

You are building a Student Performance Analyzer.

The program should allow a user to enter the marks of several students and then analyze their performance.

First, ask:

**How many students would you like to enter?**

For each student, ask for:

- Student name.
- Student mark.

Determine the student's grade using the following grading scale:

| Mark | Grade |
|---|---|
| 70–100 | A |
| 60–69 | B |
| 50–59 | C |
| 40–49 | D |
| Below 40 | E |

For every student, display a report similar to:

```text
Student: Peter
Mark: 67
Grade: B
```

## 📊 Class Summary

After all students have been processed, display:

- Number of students entered.
- Number who achieved an A.
- Number who achieved a B.
- Number who achieved a C.
- Number who achieved a D.
- Number who achieved an E.
- Highest mark.
- Lowest mark.
- Average mark.

**Restrictions:** You may not use `max()`, `min()`, or `sum()`. Calculate these values yourself.

## 🚨 Input Validation

Your program must not accept a mark outside the valid range of 0–100.

If the user enters an invalid mark, display an appropriate message and ask them to enter the mark again.

For example:

```text
Invalid mark. Please enter a mark between 0 and 100.
```

An invalid mark must not be included in the class statistics.

## 🔁 Control-Flow Requirements

Your solution must demonstrate all of the following:

- `if`
- `elif`
- `else`
- At least one nested conditional.
- A `for` loop.
- A `while` loop.
- `range()`.
- `break`.
- `continue`.
- `pass`.
- At least one nested loop.
- At least one counter.
- At least one accumulator.

Decide where each construct makes sense rather than inserting them randomly just to satisfy the checklist.

## 🧠 Problem-Solving Milestone

Before writing the program, identify the following.

### What needs to branch?

Which parts of the problem require the program to make a decision?

For example: Which grade does a mark belong to?

### What needs to repeat?

Which parts need to happen multiple times?

For example: Process each student.

### What must keep repeating until something happens?

Identify where a condition must remain true or false before the program can continue.

## 🐛 Debugging and Testing

Test your program using at least these scenarios.

**Test 1 — Different grades**

Enter several students with marks covering different grade ranges.

**Test 2 — Invalid input**

Enter at least one invalid mark and confirm that the program requests another mark.

**Test 3 — Boundary values**

Test marks such as:

- 40
- 50
- 60
- 70
- 100

Check that each mark receives the correct grade.

If you encounter an error, explain:

1. What Python is telling you.
2. What caused the error.
3. How you fixed it.

This explanation is required when a bug occurs, so the group can learn from the problems encountered.

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

After 30 minutes, research and AI are allowed, but you must understand and implement the solution yourself.

## 🧠 After Solving

Be prepared to explain:

1. What part of your program branches?
2. What part repeats?
3. Why did you choose a `for` loop there?
4. Why did you choose a `while` loop there?
5. Where did you use a counter?
6. Where did you use an accumulator?
7. Where did you use a nested conditional?
8. Where did you use a nested loop?
9. What purpose did `break`, `continue`, and `pass` serve?
10. Which part of the problem was hardest to translate from English into Python?

## 📤 Submission

When you have genuinely attempted the challenge, send:

**✅ Solved**

Do not post your code yet.

We will discuss the logic and problem-solving approach first, then share and compare implementations.

## 🏁 The Real Goal

Do not think:

*How do I use every control-flow statement?*

Think:

*What does this problem require the computer to do repeatedly, and what decisions does it need to make?*

The Python control-flow tools are there to express your solution.

**The problem comes first. The syntax comes second.** 🐍
