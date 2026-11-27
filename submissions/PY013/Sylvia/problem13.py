"""PY013 — The Community Performance Report.

Complete the questions in the PY013 challenge README.
Use the supplied member records as your starting data.
"""

members = [
    {"name": "Amina", "challenges_completed": 8, "minutes_studied": 240},
    {"name": "Brian", "challenges_completed": 5, "minutes_studied": 180},
    {"name": "Carol", "challenges_completed": 10, "minutes_studied": 300},
    {"name": "David", "challenges_completed": 3, "minutes_studied": 90},
    {"name": "Esther", "challenges_completed": 7, "minutes_studied": 210},
]


# Question 1: Ranking Members with sorted()
# TODO: Sort members by challenges completed and study time.
memberSort=sorted(members,key=lambda members:members["challenges_completed"],reverse=True)
print(memberSort)

memberStudy=sorted(members,key=lambda members:members["minutes_studied"],reverse=False)
print(memberStudy)
#reverse is used to determine the order of arrangement of values
#key is used to determine the criteria used to arrange the values
# Question 2: Checking Conditions with any() and all()
# TODO: Check the requested conditions across the membership.
minutes300 = any(member["minutes_studied"] >= 300 for member in members)
print(minutes300)
challenges3=all(member["challenges_completed"]>=3 for member in members)
print(challenges3)
challenges10=any(member["challenges_completed"]>=10 for member in members)
print(challenges10)
minutes90=all(member["minutes_studied"]>=90 for member in members)
print(minutes90)
#any is used to check if at least one element meets the conditions given
#all is used to check if all elements meet the conditions

# Question 3: Finding Extremes with min() and max()
# TODO: Define key functions and identify the required members.
fewChallenges=min(member["challenges_completed"] for member in members)
print("Fewest challenges:",fewChallenges)
mostMinutes=max(member["minutes_studied"] for member in members)
print("Longest study time:",mostMinutes)
#Key argument is useful since it helps in specifying the value to be used

# Question 4: Calculating Totals with sum()
# TODO: Calculate the total challenges, total study time, and average study time.
Challenges=sum(member["challenges_completed"] for member in members)
minutes=sum(member["minutes_studied"] for member in members)
print(Challenges)
print("Total study time:",minutes)
avg=minutes/len(members)
print("Average study time:",avg)
# Question 5: Integrated Community Report
# TODO: Produce the consolidated report using the functions from this challenge.
print("=========Community Report========")
print(minutes300)
print(challenges3)
print("Lowest challenge count:",fewChallenges)
print("Highest study time:",mostMinutes)
print("Total challenges:",Challenges)
print("Total study time:",minutes)