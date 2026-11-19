
# Lists containing each member's information
members = ["Amina", "Brian", "Carol", "David", "Esther"]
challenges_completed = [8, 5, 10, 3, 7]
minutes_studied = [240, 180, 300, 90, 210]


# QUESTION 1: map() - Change minutes into hours

# lambda divides each study time by 60
result = map(lambda minutes: minutes / 60, minutes_studied)

print("Map result:", result)  # Shows the map object

# Convert the map result into a list
hours = list(result)
print("Study hours:", hours)


# QUESTION 2: filter() - Find members with at least 7 challenges

# Pair each member with their completed challenges
pairs = zip(members, challenges_completed)

# item[1] represents the number of challenges
result = filter(lambda item: item[1] >= 7, pairs)

print("Filter result:", result)

# Convert the filtered results into a list
selected = list(result)

# Get only the names from the selected records
names = [name for name, count in selected]

print("Selected records:", selected)
print("Member names:", names)


# QUESTION 3: zip() - Combine related information

# Combine names, challenges and study minutes
combined = zip(members, challenges_completed, minutes_studied)

# Convert the combined results into a list
records = list(combined)

# Display each member's information
for name, challenges, minutes in records:
    print(name, challenges, minutes)

print("Combined list:", records)

# zip() stops at the shortest list if lengths are different


# QUESTION 4: enumerate() - Number the members

# Display positions starting from 0
print("Positions starting at 0:")

for number, name in enumerate(members):
    print(number, name)

# Start numbering from 1 instead
numbered = list(enumerate(members, start=1))

print("Positions starting at 1:")

for number, name in numbered:
    print(number, name)

print("Numbered list:", numbered)

# enumerate() counts automatically without a manual counter


# QUESTION 5: Final report

print("\nCOMMUNITY PROGRESS REPORT")

# Display each member's study hours
print("Study hours:")

for name, time in zip(members, hours):
    print(name, time, "hours")

# Display members who completed at least 7 challenges
print("Completed at least 7 challenges:", names)

# Display the combined member records
print("Combined member records:")

for record in records:
    print(record)

# Display the numbered members
print("Numbered members:")

for number, name in numbered:
    print(number, name)
