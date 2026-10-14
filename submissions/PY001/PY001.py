marks=[72,45,89,63,51,94,38]
#highest mark
max = marks[0]
for i in marks:
    if i>max:
        max = i
print(max)
#lowest mark
min = marks[0]
for j in marks:
    if j<min:
        min = j
print(min)
#average mark
total = 0
for a in marks:
    total +=a
average = total/len(marks)
print(f"{average:.2f}")