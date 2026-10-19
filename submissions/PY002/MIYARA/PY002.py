name = "Peter"
age = "20"
marks = ["72", "45", "89", "63", "51"]
has_submitted = True
bonus = None

print(type(name))
print(type(age))
print(type(marks))
print(type(has_submitted))
print(type(bonus))

new_age = int(age)
print(type(new_age))
print("Student:", name)
print("Age:", new_age)

new_marks = []
for j in marks:
    new_marks.append(int(j))
print("Student Marks:", new_marks)

total = 0
for i in new_marks:
    total += i
print("Total :", total)

avg = total/len(new_marks)
print("Average:", avg)

if new_age >= 18:
    print("Adult:", True)
else:
    print("Adult:", False)

if avg >= 50:
    print("Average is greater than 50")
else:
    print("Average is less than 50")

if avg >= 70:
    print("Average is greater than 70")
else:
    print("Average is less than 70")

if has_submitted:
    print("Student has submitted their work!")


# if avg >= 50 and has_submitted:
#     print("Passed")
passed = avg >= 50 and has_submitted
print("Passed:", passed)

if "89" in marks:
    print("89:", True)
else:
    print("89:", False)


if "100" not in marks:
    print("100:", False)
else:
    print("100:", True)


if bonus is None:
    bonus = 0
bonus += 5
print("Bonus:", bonus)

f_avg = avg + bonus
print(f"Final AAverage: {f_avg}")
