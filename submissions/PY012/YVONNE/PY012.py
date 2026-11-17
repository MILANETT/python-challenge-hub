print("!!!THE COMMUNITY PROGRESS TRACKER!!!")
members = ["Amina", "Brian", "Carol", "David", "Esther"]

challenges_completed = [8, 5, 10, 3, 7]

minutes_studied = [240, 180, 300, 90, 210]

print("TRANSFORMING DATA WITH MAP")
#The map() function executes a specified function for each item in an iterable
#The item is sent to the function as a parameter.
print("\n")
#Use map() to convert minutes_studied into hours.
print("Converting minutes to hrs using map()")
def minutesToHours(minutes):
    return minutes/60

x=map(minutesToHours,(minutes_studied))
print(x)# Display the resulting values.
minutes_to_hours=list(x)# Convert the result into a list and display it.
print(minutes_to_hours)
# Explain the type of object returned by map() and why converting it into a list may be useful.
#it returns a map object (an iterator) rather than a list 
#convert it to a list to view or store all items immediately.
print("\n")
print("FILTERING RECORDS WITH FILTER()")
#The filter() function returns an iterator where the items are filtered through
#  a function to test if the item is accepted or not.

#Use filter() to identify members who have completed at least seven challenges
def completed_enough(challenge):
    return challenges_completed[challenge] >= 7

# Filter the indices where challenges_completed >= 7
valid_indices = list(filter(completed_enough, range(len(members))))
print(valid_indices)
# Get the member names using the filtered indices
qualified_members = [members[member] for member in valid_indices]
# Display the resulting member names.
print(qualified_members)

# Explain the purpose of filter() and how it differs from map()
#filter() function extracts elements from an iterable that satisfy a specific condition while
#map() transforms every element in an iterable


print("\n")
print("COMBINING DATA WITH ZIP()")
#zip() function returns a zip object, which is an iterator of tuples where the first item in each passed 
# iterator is paired together, and then the second item in each passed iterator are paired together etc.

#Use zip() to combine the three collections.
Zipped=zip(members,challenges_completed,minutes_studied)
# Display each member alongside their corresponding values.
# Convert the zipped result into a list and display it.
print(list(Zipped))

for member, challenge,minute in zip(members, challenges_completed,minutes_studied):
    print(f"{member} completed {challenge} challenges in {minute/60} hours.")

# What happens if the collections being combined have different lengths?
#the zip() stops as soon as the shortest iterable runs out of items ignoring the extra elements in longer lists

print("\n")
print("TRACKING RECORDS WITH ENUMERATE()")
#enumerate() function adds a counter as the key of the enumerate object.

#Use enumerate() to display each member alongside their position in the original collection.
enumerated=enumerate(members,1)# Start the numbering at 1 instead of 0.
print(list(enumerated))# Convert the result into a list and display it.

# Explain the difference between using enumerate() and manually maintaining a counter in a loop.
#enumerate() automatically tracks both the index and the item in a single step, 
# whereas manually maintaining a counter requires creating, updating, and managing a separate index variable yourself.
print("\n")
print("INTERGRATED ANALYSIS REPORT")
#All members and their study hours.
member_minutes=zip(members,minutes_to_hours)
print(list(member_minutes))

# Members who have completed at least seven challenges.
print(qualified_members)

# Each member's name, challenge count, and study time, combined into a single record.
Zipped=zip(members,challenges_completed,minutes_studied)
print(list(Zipped))

# A numbered list of members, starting from 1.
enumerated=enumerate(members,1)
print(list(enumerated))











