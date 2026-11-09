# PYTHON CHALLENGE #012

**Challenge ID:** PY012  
**Phase 5:** Pythonic Data Processing  
**Difficulty:** Intermediate  
**Deadline:** Sunday, 15 November 2026, at 8:00 PM EAT

**Topics Covered:**
- `map()`
- `filter()`
- `zip()`
- `enumerate()`

## The Community Progress Tracker

The Learning Analytics Team has continued improving its reporting system. The team now wants to process member records more efficiently.

Instead of relying entirely on traditional loops, the team has decided to explore Python's built-in functional tools for transforming, filtering, and combining collections.

You have been given the following records:

```python
members = ["Amina", "Brian", "Carol", "David", "Esther"]

challenges_completed = [8, 5, 10, 3, 7]

minutes_studied = [240, 180, 300, 90, 210]
```

### Question 1: Transforming Data with `map()`

The team wants to convert each member's study time from minutes into hours.

1. Use `map()` to convert `minutes_studied` into hours.
2. Display the resulting values.
3. Convert the result into a list and display it.
4. Explain the type of object returned by `map()` and why converting it into a list may be useful.

### Question 2: Filtering Records with `filter()`

The team wants to identify members who have completed at least seven challenges.

1. Use `filter()` to identify members who meet this condition.
2. Display the resulting member names.
3. Convert the result into a list.
4. Explain the purpose of `filter()` and how it differs from `map()`.

### Question 3: Combining Data with `zip()`

The team needs to associate each member with their corresponding challenge completion count and study time.

1. Use `zip()` to combine the three collections.
2. Display each member alongside their corresponding values.
3. Convert the zipped result into a list and display it.
4. What happens if the collections being combined have different lengths?

### Question 4: Tracking Records with `enumerate()`

The team wants to generate numbered member records for its report.

1. Use `enumerate()` to display each member alongside their position in the original collection.
2. Start the numbering at 1 instead of 0.
3. Convert the result into a list and display it.
4. Explain the difference between using `enumerate()` and manually maintaining a counter in a loop.

### Question 5: Integrated Analytics Report

The team now needs a consolidated report containing the following information:

1. All members and their study hours.
2. Members who have completed at least seven challenges.
3. Each member's name, challenge count, and study time, combined into a single record.
4. A numbered list of members, starting from 1.

Use the appropriate tools (`map()`, `filter()`, `zip()`, and `enumerate()`) to produce the report.

Avoid unnecessarily repeating operations when a previously processed result can be reused.

---

## Preparation for PY013

The next challenge will introduce additional tools for working with collections:

- `sorted()`
- `any()`
- `all()`
- `min()` and `max()` with `key`
- `sum()`

You should understand how these functions help with sorting, checking conditions, and performing aggregate operations.
