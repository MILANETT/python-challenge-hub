"""PY011 — The Learning Analytics Team.

Complete the questions in the PY011 challenge README.
Use the supplied member records as your starting data.
"""

members = [
    {"name": "Amina", "challenges_completed": 8, "minutes_studied": 240, "topics": ["Python", "SQL"]},
    {"name": "Brian", "challenges_completed": 5, "minutes_studied": 180, "topics": ["Python", "Statistics"]},
    {"name": "Carol", "challenges_completed": 10, "minutes_studied": 300, "topics": ["Python", "SQL", "Statistics"]},
    {"name": "David", "challenges_completed": 3, "minutes_studied": 90, "topics": ["Python", "Geography"]},
    {"name": "Esther", "challenges_completed": 7, "minutes_studied": 210, "topics": ["SQL", "Geography"]},
]


# Question 1: Identifying Active Members
# TODO: Use list comprehensions to create the requested lists.
#A list of members that have completed at least seven challenges
seven_chals=[member["name"] for member in members if member["challenges_completed"]>=7]
#A list of members who have studied for more than 200 minutes
more_than_200mins=[member["name"] for member in members if member["minutes_studied"]>200]
#A list of the names of members who have completed at least seven challenges and studied for more than 200 minutes
seven_chals_and_more_than_200mins =[member["name"] for member in members if member["challenges_completed"]>=7 and member["minutes_studied"]>200]


# Question 2: Preparing Member Reports
# TODO: Use dictionary comprehensions to create the requested dictionaries.
#a dictionary mapping each member's name to the number of challenges they have completed
name_plus_chals = {member["name"]: member["challenges_completed"] for member in members}
#dictionary mapping each member's name to their study time in hours
name_plus_hours = {member["name"]:member["minutes_studied"]/60 for member in members}
#a dictionary containing only members who have completed at least seven challenges
name_plus_7_or_more_chals = {member["name"]: member["challenges_completed"] for member in members if member["challenges_completed"]>=7}

# Question 3: Exploring Learning Interests
# TODO: Use a set comprehension to collect distinct topics and name initials.
#a set containing all distinct topics studied by members
#AI ASSISTANCE(GEMINI)-Initially I passed on alist to the set but got unhashable list error then after
# researching on how to retrieve information in a hashable way , Gemini introduced me to a nested set comprehension
distinct_topics = {topic for member in members for topic in member["topics"]}
#a set containing the first letter of every member's name
first_letter= {member["name"][0] for member in members}
#why a set is appropriate for storing the distinct topics rather than a list
#This is because a set will not store the same topic more than once since sets automatically eliminate
# duplicates while lists would store the same topic as many times as possible since it allows duplicates
# which would not bring out the distinctness


# Question 4: Processing Large Records
# TODO: Create and consume the requested generator expressions.
#a generator expression that produces the names of members who have studied for at least 200 minutes
more_than_200mins_gen=(member["name"] for member in members if member["minutes_studied"]>200)

#Retrieve and display the generated names one at a time
#Used AI ASSISTANCE(GEMINI NOTEBOOK) to find ways of retrieving and displaying information from a generator
# object,I only thought of for loop but found out about the next() function for one at a time
print(next(more_than_200mins_gen))
print(next(more_than_200mins_gen))
print(next(more_than_200mins_gen))
#Demonstrate what happens when you attempt to retrieve another value after the generator has been exhausted
#  print(next(more_than_200mins_gen))
#Output: StopIteration
#It brings about the stop iteration error because it has reached the end and cannot produce any more values

#a second generator expression that produces the names of members who have completed fewer than six challenges
less_six_chals=(member["name"] for member in members if member["challenges_completed"]<6)


# Question 5: Bringing It Together
# TODO: Produce the final learning activity report.
print("\nLEARNING ACTIVITY REPORT\n")
print(f"Members who have completed at least seven challenges: {name_plus_7_or_more_chals}")
print(f"Each member's study time in hours: {name_plus_hours}")
print(f"All distinct learning topics represented in the community: {distinct_topics}")
# AI ASSISTANCE (GEMINI) Creating a fresh generator expression for the report since the other was consumed
at_least_200mins_report_gen = (member["name"] for member in members if member["minutes_studied"] >= 200)

print("Members who have studied for at least 200 minutes:")
for name in at_least_200mins_report_gen:
    print(f"  • {name}")