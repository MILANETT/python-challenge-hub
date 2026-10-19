# 🐍 PY008 — The Function Toolkit: Flexible, Composable, and Clever

**Phase:** Phase 4 — Functions  
**Difficulty:** Intermediate beginner  
**Estimated time:** 90–120 minutes  
**Deadline:** Wednesday, 21 October 2026, at 8:00 PM EAT

## 🎯 Objective

Bring the remaining Phase 4 function topics together in one small command-line program. Practise choosing how a function receives information, documenting its purpose, composing functions, and selecting an operation with `match/case`.

PY008 is the final focused challenge before **PY009 — the Phase 4 Boss Battle**. The boss battle will revisit relevant topics from earlier phases as well as functions.

## 🧩 Scenario: Personal Study Toolkit

Build a menu-driven program that lets a user run small study-related tools. Use functions to keep each operation understandable and reusable.

### Part 1 — Flexible parameters

Create a function named `summarize_scores` that accepts any number of positional score arguments using `*args`.

- Return a useful summary of the scores, including the count and average.
- Do not use the built-in `sum()` function for the average.
- Decide what your function should return when no scores are supplied, and handle that case deliberately.

Create a separate function that accepts student details through `**kwargs` and returns a readable report. Test it with different keyword details.

### Part 2 — Default and keyword arguments

Create a function for formatting a study-session report. It must have:
- At least one **default parameter**.
- At least one call using a **keyword argument**.
- At least two calls that demonstrate how a default value is used or overridden.

Use meaningful parameter names. Your examples should make it clear which values are passed and which defaults are applied.

### Part 3 — Positional-only and keyword-only parameters

Create a small function that demonstrates both:
- A positional-only parameter, using `/`.
- A keyword-only parameter, using `*`.

Call the function correctly, then include a short, clearly labelled experiment (commented out if it would stop your program) showing a call that violates one of those rules. Explain the resulting behaviour or error in a comment.

### Part 4 — Docstrings and useful comments

Add a docstring to each function you write. Each docstring should describe the function's purpose and, where relevant, its parameters and return value.

Also include **at least three useful explanatory comments**:
1. One explaining a non-obvious decision or edge case.
2. One explaining what an experiment demonstrates.
3. One explaining why you chose a particular function design.

Avoid comments that simply restate a line of code. Keep comments accurate and write them in your own words.

### Part 5 — Function composition and higher-order functions

- Write two small functions whose results can be used together to produce a final result (function composition).
- Write a higher-order function that accepts another function as an argument and uses it.
- Demonstrate the higher-order function with at least two different functions.

Keep each function focused. Pass information through parameters and return values rather than relying on unnecessary global variables.

### Part 6 — Lambda expressions

Use a `lambda` expression for one short operation where an anonymous function makes sense. Use it with an appropriate higher-order function or sorting operation.

In a comment, explain why a lambda is reasonable for this small operation. Do not replace every named function with a lambda.

### Part 7 — Recursion

Write a recursive function that solves a small, clearly defined problem (for example, calculating a non-negative integer's factorial).

- Include a **base case**.
- Include a recursive case that moves towards the base case.
- Test at least one base-case input and one ordinary input.
- Explain in a comment why the base case is necessary.

Keep the inputs small and non-negative. You do not need to handle enormous numbers.

### Part 8 — Menu with `match/case`

Create a menu that allows the user to choose which tool to run. Use `match/case` to handle at least four choices, plus a default case for an unrecognised choice.

Your menu should call the functions you created in earlier parts. Do not put all the calculations directly inside the `match/case` branches.

Use Python 3.10 or newer for `match/case`.

## 🧪 Testing requirements

Test and show evidence for:
- `*args` with multiple scores and with no scores.
- `**kwargs` with different details.
- A default parameter both left unchanged and overridden.
- Correct and incorrect usage of positional-only / keyword-only parameters.
- The higher-order function with two different functions.
- The recursive function's base case and an ordinary input.
- A valid menu choice and an invalid choice.

Compare numerical results with a manual calculation where appropriate. Your program should remain runnable; isolate intentionally invalid calls in comments rather than letting them interrupt the main program.

## 📌 Rules

- Use functions for the individual tasks and reuse them from the menu.
- Use `*args`, `**kwargs`, default arguments, keyword arguments, positional-only and keyword-only parameters.
- Include function docstrings, function composition, a higher-order function, a lambda expression, recursion, and `match/case`.
- Do not use `sum()` for the score average.
- Avoid unnecessary global state and duplicated calculations.
- Use meaningful names and readable formatting.
- Follow the challenge's AI-use and independent-attempt workflow.

## 📤 Submission checklist

Submit your Python script or Jupyter Notebook when the group's agreed submission process allows it. Your work should include:

- The complete Study Toolkit program.
- Tests or clear testing evidence.
- Docstrings and explanatory comments meeting Part 4.
- Short comments explaining your experiments and design choices.
- An AI-assistance disclosure if you used AI after the initial 30-minute independent attempt.

A separate README is only needed if you have additional information that the code comments and challenge instructions do not already cover. Do not duplicate the same explanations in multiple places.

## 💬 Commenting skill focus

Good comments help a reader understand **why** something is done, what an experiment reveals, or what assumption matters. They should not narrate obvious syntax.

For example:

```python
# Empty input has no meaningful average, so return None rather than dividing by zero.
```

This explains a design decision. A comment such as `# Add one to count` above `count += 1` usually adds little value.

During reviews, we will assess comment usefulness and accuracy as well as code correctness.

## 🚀 Challenge workflow

- For the first **30 minutes**, work independently. Do not use AI, solution searches, or copied code. Your own notes, previous challenges, official documentation, print debugging, and your debugger are allowed.
- After 30 minutes, AI or online research is allowed if you understand, adapt, and can explain anything you use. Disclose AI assistance as required.
- When finished, send **✅ Solved** in the group before the deadline; do not post your code prematurely.
- After the deadline, we will discuss approaches and review submissions.

**Coming next:** PY009 — Phase 4 Boss Battle. Build understanding, not just a program that runs. 🐍🔥
