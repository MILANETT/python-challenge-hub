# PYTHON CHALLENGE #013

**Challenge ID:** PY013  
**Phase 5:** Pythonic Data Processing  
**Difficulty:** Intermediate  
**Deadline:** Sunday, 22 November 2026, at 8:00 PM EAT

**Topics Covered:**
- `sorted()`
- `any()`
- `all()`
- `min()` and `max()` with `key`
- `sum()`

## The Community Performance Report

The Learning Analytics Team has collected updated records about its members. The team wants to identify performance patterns, rank members, and calculate summary statistics for its weekly report.

You have been given the following records:

```python
members = [
    {"name": "Amina", "challenges_completed": 8, "minutes_studied": 240},
    {"name": "Brian", "challenges_completed": 5, "minutes_studied": 180},
    {"name": "Carol", "challenges_completed": 10, "minutes_studied": 300},
    {"name": "David", "challenges_completed": 3, "minutes_studied": 90},
    {"name": "Esther", "challenges_completed": 7, "minutes_studied": 210},
]
```

### Question 1: Ranking Members with `sorted()`

The team wants to rank members based on their activity.

1. Use `sorted()` to display members in descending order of challenges completed.
2. Display the members in ascending order of minutes studied.
3. Explain the purpose of the `reverse` argument and how the `key` argument affects sorting.

### Question 2: Checking Conditions with `any()` and `all()`

The team wants to check whether certain conditions apply across the membership.

1. Use `any()` to determine whether at least one member has studied for 300 minutes or more.
2. Use `all()` to determine whether every member has completed at least three challenges.
3. Use both functions to check whether any member has completed at least 10 challenges and whether all members have studied for at least 90 minutes.
4. Explain the difference between `any()` and `all()`.

### Question 3: Finding Extremes with `min()` and `max()`

The team wants to identify members with the lowest and highest activity.

1. Use `min()` with the `key` argument to find the member who completed the fewest challenges.
2. Use `max()` with the `key` argument to find the member who studied for the most minutes.
3. Display the names and relevant values of the identified members.
4. Explain why the `key` argument is useful when comparing dictionaries.

You may define small named functions to determine the values used for comparison.

### Question 4: Calculating Totals with `sum()`

The team needs summary figures for its report.

1. Use `sum()` to calculate the total number of challenges completed by all members.
2. Calculate the total study time in minutes.
3. Calculate the average study time per member using the total study time and the number of members.

### Question 5: Integrated Community Report

Prepare a report that displays:

1. Members ranked from the highest to the lowest number of completed challenges.
2. Whether any member has studied for at least 300 minutes.
3. Whether all members have completed at least three challenges.
4. The members with the lowest challenge count and highest study time.
5. The total challenges completed and total study time across the community.

Use the appropriate functions from this challenge. Keep the report readable and avoid repeating calculations unnecessarily.

---

## Preparation for PY014

The next challenge will focus on working with iterators:

- `reversed()`
- `iter()`
- `next()`

Prepare to explore how iterators provide values one at a time and how iteration can be controlled.
