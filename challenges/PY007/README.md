# 🐍 PY007 — Inside and Outside: Understanding Scope

**Phase:** Phase 4 — Functions  
**Difficulty:** Beginner  
**Estimated time:** 45–60 minutes
**Deadline:** Monday, 19 October 2026, 8:00PM EAT

## 🎯 Objective

Investigate where variables can be accessed, what happens when local and global names match, and how a function can modify a global variable.

## 🧪 Challenge: Study Session Tracker

Start with a global variable that records how many study sessions have been completed. Build small functions and experiments to understand scope.

### Part 1 — Global access

- Create a function that reads the global session count without changing it.
- Call the function and observe the result.

### Part 2 — Local access

- Create a variable inside a function and display it there.
- In a separate experiment, try accessing that local variable outside the function. Observe the error, then remove or comment out the failing line so the rest of your program can run.
- Explain your observation in a code comment.

### Part 3 — Same name, different scope

- Create a global variable.
- Inside a function, create a local variable with the same name but a different value.
- Display the value inside and outside the function. Explain whether the global value changed.

### Part 4 — Modifying global state

- Write a function that increases the global session count by one.
- Use the `global` keyword where needed.
- Call the function at least twice and show the updated count after each call.
- Explain what changes when you remove the `global` declaration.

Keep this experiment separate from the next part.

### Part 5 — Compare designs

Write a second function that receives a count and an amount as arguments and **returns** the updated count instead of changing a global variable.

Test it and add a short comment comparing this approach with modifying global state.

## ✅ Check your work

Your experiments should demonstrate:

- A function reading a global variable.
- A local variable being unavailable outside its function.
- Local and global variables sharing a name without being the same variable.
- A global value being updated through a function.
- A parameter-and-return approach that does not rely on changing the global count.

Record your observations as comments beside the relevant experiments. Keep the main program runnable; isolate any line you deliberately use to observe an error.

## 🔜 Coming Next: PY008 — Default and Keyword Arguments

Next, we'll make functions more flexible by exploring:

- **Default arguments:** giving parameters default values.
- **Keyword arguments:** passing arguments by naming the parameters.
- Calling the same function in different ways and understanding how defaults are used.

Happy coding! 🐍
