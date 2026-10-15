#Small Student Performance Checker
name = "Peter"
age ="20"
marks = ["72","45","89","63","51"]
has_submitted = True
bonus = None
#Data Preparation
age = int(age)
intMarks = []
for i in marks:
    intMarks.append(int(i))


#total and average marks
totalMarks = 0
for i in intMarks:
    totalMarks += i
averageMark = totalMarks/len(intMarks)

#Check student's performance: ternary operator
is_an_adult = True if age>=18 else False

atLeast50avg = True if averageMark>=50 else False

atLeast70avg = True if averageMark>=70 else False

alreadySubmitted = True if has_submitted  else False

passed = True if atLeast50avg and alreadySubmitted else  False

#Check the Marks
is89inMarks = "89" in marks
is100inMarks = "100" in marks

#handle the bonus
finalAverage = averageMark
bonus=5 if bonus is None else bonus
finalAverage += bonus

#Report
print("-------------------------------")
print(f"{name}'s Performance Report")
print(f"Student: {name}")
print(f"Age: {age}")
print(f"Total marks: {totalMarks}")
print(f"Average: {averageMark}")
print(f"Adult: {is_an_adult}")
print(f"Passed: {passed}")
print(f"Contains 89: {is89inMarks}")
print(f"Contains 100: {is100inMarks}")
print(f"Bonus: {bonus}")
print(f"Final average: {finalAverage}")