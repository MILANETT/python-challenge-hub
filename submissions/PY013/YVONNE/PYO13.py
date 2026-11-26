members = [
    {"name": "Amina", "challenges_completed": 8, "minutes_studied": 240},
    {"name": "Brian", "challenges_completed": 5, "minutes_studied": 180},
    {"name": "Carol", "challenges_completed": 10, "minutes_studied": 300},
    {"name": "David", "challenges_completed": 3, "minutes_studied": 90},
    {"name": "Esther", "challenges_completed": 7, "minutes_studied": 210},
]

print(" RANKING MEMBERS WITH SORTED()")
#Use sorted() to display members in descending order of challenges completed.
print("display members in descending order of challenges completed.")
sorted_members=sorted(members,key=lambda member :member["challenges_completed"],reverse=True)
print(sorted_members)

print("\n")
# Display the members in ascending order of minutes studied.
print(" Display the members in ascending order of minutes studied.")
sorted_membersMins=sorted(members,key=lambda member :member["minutes_studied"])
for member in sorted_membersMins:
    print(member["name"])

# Explain the purpose of the reverse argument and how the key argument affects sorting.
#Reverse argument sorts the list in descending orderr
#key argument is a function to execute to decide the order


print("\n")
print("CHECKING CONDITIONS WITH ANY() AND ALL()")
#Use any() to determine whether at least one member has studied for 300 minutes or more.
print("determine whether at least one member has studied for 300 minutes or more.")
x=any(member["minutes_studied"]>= 300 for member in members)
print(x)

print("\n")
# Use all() to determine whether every member has completed at least three challenges.
print(" determine whether every member has completed at least three challenges.")
y=all(member["challenges_completed"]>= 3 for member in members)
print(y)

# Use both functions to check whether any member has completed at least 10 challenges and whether all members have studied for at least 90 minutes.
if any(member["challenges_completed"]>= 10 for member in members) and all(member["minutes_studied"]>= 90 for member in members):
    print("All members have studied for at least 90 minutes and atleast one has completed at least 10 challenges ")
else: 
    print("The conditions have not been met.")

# Explain the difference between any() and all().
#in any() atleast one item meets the condition in all() every items must meet the condition
print("\n")
print("FINDING EXTREMES WITH MIN() AND MAX()")
#Use min() with the key argument to find the member who completed the fewest challenges.
print("member who completed the fewest challenges")
min_challenges=min(members,key=lambda member :member["challenges_completed"])
print(min_challenges["name"])

print("\n")
# Use max() with the key argument to find the member who studied for the most minutes.
print("member who studied for the most minutes.")
max_challenges=max(members,key=lambda member :member["minutes_studied"])
print(max_challenges["name"])

# Explain why the key argument is useful when comparing dictionaries.
#key argumment tells python what value to compare when deciding the max/min item

print("\n")
print("CALCULATING TOOLS WITH SUM()")
#Use sum() to calculate the total number of challenges completed by all members.
print("calculate the total number of challenges completed by all members.")
total_challenges=sum( member["challenges_completed"] for member in members)
print(total_challenges)

print("\n")
# Calculate the total study time in minutes.
print("Calculate the total study time in minutes.")
total_minutes=sum( member["minutes_studied"] for member in members)
print(total_minutes)

print("\n")
# Calculate the average study time per member using the total study time and the number of members.
print("Calculate the average study time per member using the total study time and the number of members.")
total_members=[member["name"] for member in members]
print(f"TOTAL NUMBER OF MEMBER:", len(total_members))

avg_studyTime=total_minutes/len(total_members)
print(f"AVERAGE STUDY TIME:",avg_studyTime)

print("\n")
print("INTERGRATED COMMUNITY REPORT")
#Members ranked from the highest to the lowest number of completed challenges.
print("Members ranked from the highest to the lowest number of completed challenges")
for member in sorted_members:
    print(member["name"])

# Whether any member has studied for at least 300 minutes.
print(f"member has studied for at least 300 minutes:",x)

# Whether all members have completed at least three challenges.
print(f"all members have completed at least three challenges",y)

# The members with the lowest challenge count and highest study time.
print(f" MEMBERS LOWEST CHALLENGE: ",max_challenges)
print(f" MEMBERS HIGHEST STUDY TIME : ",min_challenges)

# The total challenges completed and total study time across the community.
print(f"TOTAL CHALLENGES COMPLETED:",total_challenges)
print(f"TOTAL STUDY TIME :",total_minutes)
























