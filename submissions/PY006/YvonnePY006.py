students=2
for student in range(students):
    student_name=str(input("Enter  Student's name:"))
    student_mark1=int(input("Enter mark for subject 1:"))
    student_mark2=int(input("Enter mark for subject 2:"))
    student_mark3=int(input("Enter mark for subject 3:"))

    def calculate_avg(*marks):#arbitrary arguments(args)...you don't know how 
         sum=0                 #arguments will be passed
         for mark in marks:
          sum+=mark
  
          Average = sum/len(marks)
         return Average


    def display_StudentDetails():
         print("STUDENT:",student_name)
         print(f"Average:{calculate_avg(student_mark1,student_mark2,student_mark3):.2f}")

    

    print("===STUDENT REPORTS===")
    display_StudentDetails()



#all the variables ie student_name,student_marks are global variables and can be accessed by any function
#variables eg sum is a local variable and will only be used by calculate_avg function
#using the same name for global and local variables -the local variable can only be changed within the function it is initialized
#global functions can be changed outside functions
#Defining a function is creating a function and its parameters
#a parameter is passed when a function is created and an argument is passed in parentheses when a function is called
#