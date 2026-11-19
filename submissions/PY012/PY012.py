# #Question 1
members = ["Amina","Brian","Carol","David","Esther"]
challenges_completed = [8,5,10,3,7]
minutes_studied = [240,180,300,90,210]

hours_studied = map(lambda x:x/60 , minutes_studied)
print(hours_studied)

#Output:
# <map object at 0x00000225BDFC9300>

hours_studied_list = list(hours_studied)#Converted the result into a list
print(hours_studied_list)
#Output:
# [4.0, 3.0, 5.0, 1.5, 3.5]

#Type of object map() returns and why converting to a list may be useful
#map() returns an ject which is an iterator.It applies the given func to each item as you iterate over it
#rather than building all results immediately.Converting to a list may be usefyl when you want to display 
# or isnpect all results at once or access them using their indexes.

# #Question 2 
least_seven = filter(lambda m:m[1] >= 7 ,zip(members, challenges_completed))
for i,j in least_seven:
    print(i)

#Output:
# Amina
# Carol
# Esther

least_seven_list = list(filter(lambda m:m[1] >= 7 ,zip(members, challenges_completed)))
print(least_seven_list)

#Output
# [('Amina', 8), ('Carol', 10), ('Esther', 7)]

# Purpose of filter() and how it differs from map()
#filter() selects items from an iterable that satisfy a certain condition while map() transforms every item by applying a func 
#hence it returns an iterator of the transfored results.

# #Question 3
details = zip(members,challenges_completed,minutes_studied)
for i in details:
    print(i)

#Output:
# ('Amina', 8, 240)
# ('Brian', 5, 180)
# ('Carol', 10, 300)
# ('David', 3, 90)
# ('Esther', 7, 210)

zipped_details = list(details)
print(zipped_details)

#What happens when collections being combined have different lenghts?
#Zip stops as soon as the shortest list runs out of items.Any extra items in other lists are left out.

#Question 4
enumerate_info = enumerate(members ,start = 1)
for idx,member in enumerate_info:
    print(f"{idx}.{member}")
    
#Output:
# 1.Amina
# 2.Brian
# 3.Carol
# 4.David
# 5.Esther

enumerated_list = list(enumerate(members,start =1))
print(enumerated_list)
#Output:
#[(1, 'Amina'), (2, 'Brian'), (3, 'Carol'), (4, 'David'), (5, 'Esther')]

#Difference between using enumerate() and manuallly maintaining a counter loop
#enumerate() gives you each item and its index automatically while in using a counter loop you have to initialize 
#the counter first and increment it yourself which one might occassionally forget.

#Question 5
students = list(map(lambda x:x/60 , minutes_studied))
seven_7 = list(filter(lambda x:x[1] >= 7 , zip(members,challenges_completed)))
all_together = list(zip(members,challenges_completed,minutes_studied))
positions = list(enumerate(members,start = 1))

print("-"*45)
print("INTEGRATED ANALYSIS REPORT")
print("-"*45)

print(students)

print("Members and their study hours:")
for i,j in zip(members,students):
    print("Members:", i , ",Study Hours:", j )

print("Members with atleast 7 challenges:")
for name, chal in seven_7:
    print("Name:", name , ",Challenges:", chal)

print("Combined report:")
for detail in all_together:
    print("Name:",detail[0],",Challenges completed:",detail[1],"Hours studied:",detail[2])

print("Numbered list of members:")
for idx,name in positions:
    print(idx,name)