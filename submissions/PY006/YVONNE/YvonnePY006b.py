def collect_StudentDetails():
    global student_name#making the variables global so it can be accessed by any function
    student_name=str(input("Enter  Student's name:"))

    global student_mark1
    student_mark1=int(input("Enter mark for subject 1:"))

    global student_mark2
    student_mark2=int(input("Enter mark for subject 2:"))

    global student_mark3
    student_mark3=int(input("Enter mark for subject 3:"))

def calculate_avg(*marks):#arbitrary arguments(args)...you don't know how 
         sum=0                 #arguments will be passed
         for mark in marks:
          sum+=mark
  
          Average = sum/len(marks)
         return Average

def display_StudentDetails():
         print("STUDENT:",student_name)
         print("Average:",calculate_avg(student_mark1,student_mark2,student_mark3))

students=2
for student in range(students):
    collect_StudentDetails()
    calculate_avg(student_mark1,student_mark2,student_mark3)
    display_StudentDetails()
