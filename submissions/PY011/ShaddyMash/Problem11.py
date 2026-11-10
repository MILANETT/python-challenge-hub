
# Member information
members = [
    {"name": "Amina", "challenges_completed": 8, "minutes_studied": 240, "topics": ["Python", "SQL"]},
    {"name": "Brian", "challenges_completed": 5, "minutes_studied": 180, "topics": ["Python", "Statistics"]},
    {"name": "Carol", "challenges_completed": 10, "minutes_studied": 300, "topics": ["Python", "SQL", "Statistics"]},
    {"name": "David", "challenges_completed": 3, "minutes_studied": 90, "topics": ["Python", "Geography"]},
    {"name": "Esther", "challenges_completed": 7, "minutes_studied": 210, "topics": ["SQL", "Geography"]}
]


# Question 1: List comprehensions

# Get names of members with 7 or more challenges
completed = [m["name"] for m in members if m["challenges_completed"] >= 7]

# Get names of members who studied over 200 minutes
studied = [m["name"] for m in members if m["minutes_studied"] > 200]

# Get names of members who meet both conditions
both = [m["name"] for m in members if m["challenges_completed"] >= 7 and m["minutes_studied"] > 200]

print(completed)
print(studied)
print(both)


# Question 2: Dictionary comprehensions

# Match each name with their completed challenges
challenges = {m["name"]: m["challenges_completed"] for m in members}

# Convert study minutes into hours for each member
hours = {m["name"]: m["minutes_studied"] / 60 for m in members}

# Store only members with at least 7 challenges
active = {m["name"]: m["challenges_completed"] for m in members if m["challenges_completed"] >= 7}

print(challenges)
print(hours)
print(active)


# Question 3: Set comprehensions

# Get all topics without repeating any
topics = {t for m in members for t in m["topics"]}

# Get the first letter of each member's name
letters = {m["name"][0] for m in members}

print(topics)
print(letters)

# Sets automatically remove duplicates


# Question 4: Generator expressions

# Generate names of members who studied at least 200 minutes
names = (m["name"] for m in members if m["minutes_studied"] >= 200)

# Print the generated names one at a time
for name in names:
    print(name)

# Check what happens after all values have been used
try:
    print(next(names))
except StopIteration:
    print("No more names")

# Generate names of members with fewer than 6 challenges
few = (m["name"] for m in members if m["challenges_completed"] < 6)

# Display the names one at a time
for name in few:
    print(name)


# Question 5: Learning activity report

print("\nLEARNING ACTIVITY REPORT")

# Display members who completed at least 7 challenges
print("Completed 7 or more challenges:", completed)

# Display study hours for each member
print("Study hours:")
for name, time in hours.items():
    print(name, time)

# Display all unique topics
print("Topics:", topics)

# Display members who studied at least 200 minutes
print("Studied at least 200 minutes:")

# Create another generator because the first was exhausted
names = (m["name"] for m in members if m["minutes_studied"] >= 200)

for name in names:
    print(name)
