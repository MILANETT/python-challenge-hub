"""PY012 — The Community Progress Tracker.

Complete the questions in the PY012 challenge README.
Use the supplied collections as your starting data.
"""

members = ["Amina", "Brian", "Carol", "David", "Esther"]

challenges_completed = [8, 5, 10, 3, 7]

minutes_studied = [240, 180, 300, 90, 210,90]


# Question 1: Transforming Data with map()
# TODO: Convert study times from minutes into hours.
hours_studied=map(lambda x:x/60,minutes_studied)
print(hours_studied)
print(list(hours_studied))
#The object returned is a map object which does not display the values 
#Converting the map object to a list displays the values

# Question 2: Filtering Records with filter()
# TODO: Identify members who have completed at least seven challenges.
seven_challenges=filter(lambda x:x>=7,challenges_completed)
print(seven_challenges)
print(list(seven_challenges))
#Filter is used to pick out values that meet a certain condition while map is used
#to apply a function to each element in a structure

# Question 3: Combining Data with zip()
# TODO: Combine each member with their challenge count and study time.
challenge_time=zip(members,challenges_completed,minutes_studied)
print(challenge_time)
print(list(challenge_time))

#when the collections are of different lengths say one has 3 items another has 4
#The extra values after the 3rd item are not displayed

# Question 4: Tracking Records with enumerate()
# TODO: Display the members with numbering that starts at 1.
numbered_members=enumerate(members,start=1)
print(numbered_members)
print(list(numbered_members))
#enumerate is much easier to use while a counter must have variable and condition definition
#enumerate makes less mistakes while counter can make mistakes because it is manually maintained

# Question 5: Integrated Analytics Report
# TODO: Use the appropriate functions to produce the consolidated report.
print("\n===Student report====")
print("\n===Members and study hours====")
hours_studied=map(lambda x:x/60,minutes_studied)
members_hours=zip(members,list(hours_studied))
print(list(members_hours))

print("\n===members with at least seven challenges====")
seven_challenges=filter(lambda x:x>=7,challenges_completed)
members_seven=zip(members,list(seven_challenges))
print(list(members_seven))
print("\n===Member records====")
challenge_time=zip(members,challenges_completed,minutes_studied)
print(list(challenge_time))
print("\n===Numbered list of members====")
numbered_members=enumerate(members,start=1)
print(list(numbered_members))
