marks = [72, 45, 89, 63, 51, 94, 38]
avg = sum(marks)/len(marks)
print("The average is :", avg)

marks = [72, 45, 89, 63, 51, 94, 38]
highest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark

print("The highest mark is:", highest)

marks = [72, 45, 89, 63, 51, 94, 38]
lowest = marks[0]

for mark in marks:
    if mark < lowest:
        lowest = mark

print("The lowest mark is:", lowest)

marks = [72, 45, 89, 63, 51, 94, 38]
total = 0

for mark in marks:
    total = total + mark

avg = total / len(marks)
print("The average is:", avg)
