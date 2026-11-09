#list containing dictionaries
members = [
    { "name": "Amina",
      "challenges_completed": 8, 
      "minutes_studied": 240, "topics": ["Python", "SQL"]},
    { 
        "name": "Brian", 
        "challenges_completed": 5, 
        "minutes_studied": 180, 
        "topics": ["Python", "Statistics"]},
    {
        "name": "Carol", 
        "challenges_completed": 10,
        "minutes_studied": 300, 
        "topics": ["Python", "SQL", "Statistics"]},
    {
        "name": "David", 
        "challenges_completed": 3, 
        "minutes_studied": 90, 
        "topics": ["Python", "Geography"]},
    {
        "name": "Esther", 
        "challenges_completed": 7, 
        "minutes_studied": 210, 
        "topics": ["SQL", "Geography"]},
]

print("!!!IDENTIFYING THE ACTIVE MEMBERS!!!")
print("Names of members who completed at least 7 challenges")
#use for loop to access each dictionary then access the keys of the dictionaries given the condition
for member in members:
    for x,y in member.items():
          if x=="challenges_completed" and y>=7:
             print(member["name"])

print("\n")
print("names of members who have studied for more than 200 minutes")
for member in members:
    for x,y in member.items():
        if x=="minutes_studied" and y > 200:
            print(member["name"])

print("\n")
print("names of members who have completed at least seven challenges and studied for more than 200 minutes.")
for member in members:
    if member["challenges_completed"] >= 7 and member["minutes_studied"] > 200:
        print(member["name"])

print("\n")
print("!!!PREPARING MEMBER REPORTS!!!")
print("dictionary mapping each member's name to the number of challenges they have completed")
#inititialize an empty dictionaryu then update the values into the dictionary
dict1={}
for member in members:
        for x,y in member.items():
           if x=="challenges_completed":
            dict1.update({member["name"]:member["challenges_completed"]})
print(dict1)

print("\n")
print("another dictionary mapping each member's name to their study time in hours.")
studyTime_dict={}
for member in members:
    for x,y in member.items():
        if x=="minutes_studied":
            studyTime_dict.update({member["name"]:member["minutes_studied"]})
print(studyTime_dict)

print("\n")
print("dictionary containing only members who have completed at least seven challenges, with their names as keys and completed challenges as values.")
challenges_dict={}
for member in members:
    for x,y in member.items():
          if x=="challenges_completed" and y>=7:
             challenges_dict.update({member["name"]:member["challenges_completed"]})
print(challenges_dict)

print("\n")
print("EXPLORING AND LEARNING INTERESTS")
print("set containing all distinct topics studied by members")
#intialize an empty set and loop through the list updating the topic to the set 
#a set does not contain duplicates so it will only take unique values
topics_=set()
for member in members:
    for x,y in member.items():
        if x=="topics":
          topics_.update(member[x])
print(topics_)

print("\n")
print("set containing the first letter of every member's name")
#initialize an empty set
#loop through the list in the outer loop,loop through the keys in the send loop to extract the keys
#extract the key that is "name" and update the first letters of names to the set ie update(member[x][0]
fName=set()
for member in members:
    for x,y in member.items():
        if x=="name":
           fName.update(member[x][0])
print(fName)
#Explain why a set is appropriate for storing the distinct topics rather than a list.
#Because a set does not allow duplicates unlike a list

print("\n")
print("!!!PROCESSING LARGE RECORDS!!!")#GENERATOR EXPRESSIONS
#learnt generator expressions with AI assistance
print("expression that produces the names of members who have studied for at least 200 minutes")
studied_names=(member["name"] for member in members if member["minutes_studied"] >= 200)

for name in studied_names:
       print(name)

print("\n")
print("Retrieve and display the generated names one at a time")
#use next()
names=(member["name"]
       for member in members)

print(next(names))
print(next(names))
print(next(names))
print(next(names))
print(next(names))


print("\n")
print("generator expression that produces the names of members who have completed fewer than six challenges.")
six_challenges=(member["name"] for member in members if member["challenges_completed"] < 6)

for name in six_challenges:
    print(name)

print("\n")
print("Demonstrate what happens when you attempt to retrieve another value after the generator has been exhausted.")
#print(next(six_challenges))
    #print(next(six_challenges))
   #       ~~~~^^^^^^^^^^^^^^^^
#StopIteration
#it throws a stop iteration error because the generator expression has been exhausted by the for loop

#print(next(names))
#    print(next(names))
#          ~~~~^^^^^^^
#StopIteration
##it throws a stop iteration error because the generator expression has been exhausted

print("\n")
print("!!!REPORT!!!")
# 1. Members who completed at least 7 challenges
active_members = [
    member["name"]
    for member in members
    if member["challenges_completed"] >= 7
]


# 2. Each member's study time converted from minutes to hours
study_hours = {
    member["name"]: member["minutes_studied"] / 60
    for member in members
}


# 3. All distinct learning topics in the community
all_topics = {
    topic
    for member in members
    for topic in member["topics"]
}


# 4. Names of members who studied for at least 200 minutes
# Using a generator expression
studied_members = (
    member["name"]
    for member in members
    if member["minutes_studied"] >= 200
)


# 5. Display the learning activity report
print("* Members who completed at least 7 challenges:")
for name in active_members:
    print(name)

print("\n")
print("* Study time in hours:")
for name, hours in study_hours.items():
    print(f"{name}: {hours:.1f} hours")

print("\n")
print("* Distinct learning topics:")
print(all_topics)

print("\n")
print("* Members who studied for at least 200 minutes:")
for name in studied_members:
    print(name)

print("\n!!!END!!!")