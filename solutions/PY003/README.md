# PY003 — Student Introduction Generator: Solution Approach

This guide explains the reasoning behind the reference solution. Read it alongside `solution.py`.

## 1. Collect the information first

Use `input()` to ask for the student's name, course, university, and favourite programming language. Store each answer in a clearly named variable.

Remember: `input()` returns a string. These fields are text, so they can remain strings.

## 2. Clean the name before using it

A person may accidentally enter spaces before or after their name. Apply the string method `.strip()` to remove surrounding whitespace, then use the cleaned name for the rest of the profile.

Cleaning the value once near the beginning keeps later output consistent. It is better than trying to correct the same problem separately in every print statement.

## 3. Inspect the name

Use:

- `len(name)` to find the number of characters.
- `name[0]` to access the first character.
- `name[-1]` to access the last character.

These operations assume the cleaned name is not empty. This beginner challenge focuses on ordinary non-empty input; handling an empty name safely can be added once the group has studied the necessary conditional logic.

## 4. Format the profile

Use `print()` to create a readable report and f-strings to insert the variables into the output. String methods can also standardize how some text is displayed—for example, `.title()` or `.upper()`. Choose methods intentionally; they do not all perform the same kind of change.

## 5. Debug by isolating the cause

If the output is wrong, test one small part at a time. For example, print the cleaned name, its length, and the first and last characters before formatting the complete profile.

For the required debugging reflection, record an actual error or a deliberately introduced small mistake, explain what caused it, and document the fix in comments. Do not merely write the error name.

## Concepts used

- `input()` and `print()`
- Variables and strings
- `str.strip()` and other string methods
- `len()`
- String indexing
- f-strings
- Testing and reading error messages

## Common mistakes to watch for

- Forgetting that `input()` returns a string.
- Cleaning the name after some of its properties have already been calculated.
- Using index `0` for the last character instead of `-1`.
- Forgetting that indexing an empty string causes an error.
- Typing sample profile details directly instead of using the user's input.

**Key idea:** Break a written requirement into small steps: collect the data, clean it, inspect it, and present it clearly.