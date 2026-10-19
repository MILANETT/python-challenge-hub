
no_of_students = int(input("How many students would you like to enter?"))

#These three are instances of accumulators as they accumulate the data as the loop runs 
names = [] #an empty list created so that it stores the names inputted 
marks = []
grades = []

counta = 0
countb = 0
countc = 0
countd = 0
counte = 0
for i in range(no_of_students):
    name = input("Enter the name of the student:")
    
    while True:#nested loop----a while within a for loop 
        mark = int(input("Enter the marks obtained:"))
        if mark>=0 and mark<= 100:
            break
        print("Enter a mark between 1 and 100")# thrown when user inputs a value not within the range 
    

    if 70<= mark <=100:
        grade = "A"
        counta = counta + 1 #adds the number of 'A's calculated into the counter variable "counta"
    elif 60<= mark <70:
        grade = "B"
        countb = countb + 1
    elif 50<= mark <60:
        grade = "C"
        countc = countc + 1
    elif 40<= mark <50:
        grade = "D"
        countd+= 1
    else:
        grade = "E"
        counte+= 1

    names.append(name) #adding the names inputted into the list created 
    marks.append(mark) #adding the marks inputed into the list created
    grades.append(grade) #adding the grades calculated into the list created 



highest = marks[0]
for k in marks:
    if k > highest:
        highest = k

lowest = marks[0]
for n in marks:
    if n < lowest:
        lowest = n

total = 0
for x in marks:
    total += x #Also an accumulator
avg = total/len(marks)
print("============================================")
print("Students Report")
for j in range(no_of_students):
    print("Student:", names[j])
    print("Mark:", marks[j])
    print("Grade:", grades[j])

print("============================================")
print(f"Number of students entered:{no_of_students}")
print(f"Number of students with an A:{counta}")
print(f"Number of students with a B:{countb}")
print(f"Number of students with a C:{countc}")
print(f"Number of students with a D:{countd}")
print(f"Number of students with an E:{counte}")

print("============================================")

print("Highest mark:", highest)
print(f"Lowest mark:{lowest}")
print(f"Average mark:{avg}")