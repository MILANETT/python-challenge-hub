members = [
    {"name": "Amina", "challenges_completed": 8,
        "minutes_studied": 240, "topics": ["Python", "SQL"]},
    {"name": "Brian", "challenges_completed": 5,
        "minutes_studied": 180, "topics": ["Python", "Statistics"]},
    {"name": "Carol", "challenges_completed": 10, "minutes_studied": 300,
        "topics": ["Python", "SQL", "Statistics"]},
    {"name": "David", "challenges_completed": 3,
        "minutes_studied": 90, "topics": ["Python", "Geography"]},
    {"name": "Esther", "challenges_completed": 7,
        "minutes_studied": 210, "topics": ["SQL", "Geography"]},
]

# Question 1:
least_seven = [member["name"]
               for member in members if member["challenges_completed"] >= 7]
print(least_seven)
# Output:
# ['Amina', 'Carol', 'Esther']

min_study = [member["name"]
             for member in members if member["minutes_studied"] > 200]
print(min_study)
# Output:
# ['Amina', 'Carol', 'Esther']

combined = [member["name"] for member in members if member["challenges_completed"]
            >= 7 and member["minutes_studied"] > 200]
print(combined)
# output:
# ['Amina', 'Carol', 'Esther']

# Question 2:
challenge_comp = {member["name"]: member["challenges_completed"]
                  for member in members}
print(challenge_comp)
# Output:
# {'Amina': 8, 'Brian': 5, 'Carol': 10, 'David': 3, 'Esther': 7}

study_hrs = {member["name"]: member["minutes_studied"] /
             60 for member in members}
print(study_hrs)
# Output:
# {'Amina': 4.0, 'Brian': 3.0, 'Carol': 5.0, 'David': 1.5, 'Esther': 3.5}

seven_chall = {member["name"]: member["challenges_completed"]
               for member in members if member["challenges_completed"] >= 7}
print(seven_chall)
# Output:
# {'Amina': 8, 'Carol': 10, 'Esther': 7}

# Question 3:
# Used Ai
units = {x for member in members for x in member["topics"]}
print(units)
# Output:
# {'SQL', 'Statistics', 'Python', 'Geography'}

first_letter = {member["name"][0] for member in members}
print(first_letter)
# Output
# {'D', 'E', 'C', 'B', 'A'}

# Explain why a set is appropriate rather than a list
# A set is more appropriate as it stored unique values only and does not allows duplicated so it will display only unique topics and won't repeat the topics


# Question 4 :
# An example on generator expressions
# gen_exp = (x * x for x in range(5))
# print(gen_exp)        #prints <generator object <genexpr> at 0x000002993CA68E10>
# print(list(gen_exp))     #Prints [0, 1, 4, 9, 16]

atleast_min = (member["name"]
               for member in members if member["minutes_studied"] >= 200)
print(atleast_min)
for x in atleast_min:
    print(x)
# Output:
# <generator object <genexpr> at 0x000002AC28F28E10>
# Amina
# Carol
# Esther


chall_six = (member["name"]
             for member in members if member["challenges_completed"] < 6)
for i in chall_six:
    print(i)

# Output:
# <generator object <genexpr> at 0x0000018A10608E10>
# Amina
# Carol
# Esther
# Brian
# David

# Question 5:
print("-"*45)
print("LEARNING ACTIVITY REPORT")
print("Members who have completed at least seven challenges:")
print(seven_chall)
print("Each member's study time in hours:")
print(study_hrs)
print("All distinct learning topics:")
print(units)
print("Names of members who studied for atleast 200 minutes:")
for name in (member["name"] for member in members if member["minutes_studied"] >= 200):
    print(name)

# Output:
# LEARNING ACTIVITY REPORT
# Members who have completed at least seven challenges:
# {'Amina': 8, 'Carol': 10, 'Esther': 7}
# Each member's study time in hours:
# {'Amina': 4.0, 'Brian': 3.0, 'Carol': 5.0, 'David': 1.5, 'Esther': 3.5}
# All distinct learning topics:
# {'Python', 'SQL', 'Geography', 'Statistics'}
# Names of members who studied for atleast 200 minutes:
# Amina
# Carol
# Esther
