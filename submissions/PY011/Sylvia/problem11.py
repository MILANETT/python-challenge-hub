members = [
    {"name": "Amina", "challenges_completed": 8, "minutes_studied": 240, "topics": ["Python", "SQL"]},
    {"name": "Brian", "challenges_completed": 5, "minutes_studied": 180, "topics": ["Python", "Statistics"]},
    {"name": "Carol", "challenges_completed": 10, "minutes_studied": 300, "topics": ["Python", "SQL", "Statistics"]},
    {"name": "David", "challenges_completed": 3, "minutes_studied": 90, "topics": ["Python", "Geography"]},
    {"name": "Esther", "challenges_completed": 7, "minutes_studied": 210, "topics": ["SQL", "Geography"]},
]

#list comprehensions
names=[member["name"] for member in members if member["challenges_completed"]>=7 ]
print(names)

names_200=[member["name"] for member in members if member["minutes_studied"]>200 ]
print(names_200)

names_7_=[member["name"] for member in members 
          if member["challenges_completed"]>=7 and member["minutes_studied"]>200]
print(names_7_)

#dictionary comprehensions
nameChallenge={member["name"]:member["challenges_completed"] for member in members}
print(nameChallenge)

nameHours={member["name"]:member["minutes_studied"]/60 for member in members}
print(nameHours)

name7Challenges={member["name"]:member["challenges_completed"] for member in members
                 if member["challenges_completed"] >=7}
print (name7Challenges)

#set comprehensions
topics_={topic 
        for member in members
        for topic in member["topics"] 
        }
print(topics_)

fLetter={member["name"][0] 
       for member in members}
print(fLetter)

#It is appropriate to use a set comprehension because we get unique names of the topic 
#The topics are repeated between the members so a set is suitable becaues it prevents duplicates

#generator comprehensions
names200=(member["name"] for member in members if member["minutes_studied"]>=200)
for name in names200:   
    print(name)
print("\n")
names6=(member["name"] for member in members if member["challenges_completed"]<6)
for name in names6:
    print(name)
print("After the exhausted generator")
for name in names6:
    print(name)
#the values are not displayed after the generator is exhausted

print("======Activity report=======")
print("Members who have completed at least seven challenges")
print(names)
print("Each member's study time in hours")
print(nameHours)
print("All distinct learning topics represented in the community")
print(topics_)
print("The names of members who have studied for at least 200 minutes")
names200=(member["name"] for member in members if member["minutes_studied"]>=200)
for name in names200:
    print(name)
