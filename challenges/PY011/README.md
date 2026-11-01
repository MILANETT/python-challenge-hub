# PYTHON CHALLENGE #011

**Challenge ID:** PY011  
**Phase 5:** Pythonic Data Processing  
**Difficulty:** Intermediate  
**Level:** Intermediate  
**Deadline:** Sunday, 8 November 2026, at 8:00 PM EAT

**Topics Covered:**
- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Generator expressions

## The Learning Analytics Team

A growing programming community wants to understand how its members are progressing. The team has collected information about members, their study activities, and the programming topics they are interested in.

The existing records contain useful information, but preparing reports manually is becoming inconvenient. You've been asked to process these records and produce simplified datasets that can support the team's reporting activities.

Use the following records throughout the challenge:

```python
members = [
    {"name": "Amina", "challenges_completed": 8, "minutes_studied": 240, "topics": ["Python", "SQL"]},
    {"name": "Brian", "challenges_completed": 5, "minutes_studied": 180, "topics": ["Python", "Statistics"]},
    {"name": "Carol", "challenges_completed": 10, "minutes_studied": 300, "topics": ["Python", "SQL", "Statistics"]},
    {"name": "David", "challenges_completed": 3, "minutes_studied": 90, "topics": ["Python", "Geography"]},
    {"name": "Esther", "challenges_completed": 7, "minutes_studied": 210, "topics": ["SQL", "Geography"]},
]
```

### Question 1: Identifying Active Members

The team wants a quick way to identify members who have made significant progress.

1. Create a list containing the names of members who have completed at least seven challenges. Use a list comprehension.
2. Create another list containing the names of members who have studied for more than 200 minutes. Use a list comprehension.
3. Create a list of the names of members who have completed at least seven challenges and studied for more than 200 minutes.

### Question 2: Preparing Member Reports

The team needs simplified records for its reporting system.

1. Create a dictionary mapping each member's name to the number of challenges they have completed. Use a dictionary comprehension.
2. Create another dictionary mapping each member's name to their study time in hours.
3. Create a dictionary containing only members who have completed at least seven challenges, with their names as keys and completed challenges as values.

### Question 3: Exploring Learning Interests

The team wants to establish which programming and learning areas are represented in the community.

1. Create a set containing all distinct topics studied by members. Use a set comprehension.
2. Create a set containing the first letter of every member's name. Use a set comprehension.
3. Explain why a set is appropriate for storing the distinct topics rather than a list.

### Question 4: Processing Large Records

The team expects its membership to grow and wants to avoid creating unnecessary lists when processing large collections.

1. Create a generator expression that produces the names of members who have studied for at least 200 minutes.
2. Retrieve and display the generated names one at a time.
3. Create a second generator expression that produces the names of members who have completed fewer than six challenges.
4. Demonstrate what happens when you attempt to retrieve another value after the generator has been exhausted.

### Question 5: Bringing It Together

The team needs a compact learning activity report.

Create a report that displays:

- Members who have completed at least seven challenges.
- Each member's study time in hours.
- All distinct learning topics represented in the community.
- The names of members who have studied for at least 200 minutes.

Use comprehensions and a generator expression where appropriate. Keep the code readable and avoid repeating calculations unnecessarily.

---

## Preparation for PY012

Next week's challenge will focus on **functional data processing**.

Prepare the following Python concepts:

- `map()`
- `filter()`
- `zip()`
- `enumerate()`

Pay attention to how these functions process collections, how they differ from ordinary loops, and what they return.
