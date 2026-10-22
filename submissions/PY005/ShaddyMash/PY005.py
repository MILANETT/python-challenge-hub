students=[{"name":"Daniel",
           "student_id":"DS001",
           "course":["Python","Statistics","Databases"],
           "marks":[78,64,82]
           },
          {"name":"Amina",
           "student_id":"DS002",
           "course":["Python","Statistics","Databases"],
           "marks":[91,73,88]
           },
          {"name":"Brian",
           "student_id":"DS003",
           "course":["Python","Statistics","Databases"],
           "marks":[56,68,61]
           }
          ]

# The program runs in a loop until the user chooses to exit.
access=True
while access:
    # Display the menu for available actions.
    print("\nWELCOME TO THE STUDENT RECORD SYSTEM.")
    print("SELECT WHAT YOU WANT TO DO BY NUMBER:")
    print("1. View all students.")
    print("2. Add a student.")
    print("3. Search for a student.")
    print("4. Update a student's mark.")
    print("5. Display all unique courses taken by the class.")
    print("6. Display students taking a particular course.")
    print("7. Create a backup copy of the student records.")
    print("8. Exit.")

    # Keep asking until the user enters a valid menu option.
    error=True
    while error:
        try:
            entry=int(input("Enter your choice: "))
            if entry>=1 and entry<=8:
                error=False
            else:
                print("Invalid entry. Your choice can only be from 1 to 8.")
        except ValueError:
            print("Invalid entry. Enter a number from 1 to 8.")

    # Option 1: Display every student record currently stored in the program.
    if entry==1:
        print(students)

    # Option 2: Add a new student to the students list.
    elif entry==2:
        # Create a blank dictionary for the student being added.
        student={}

        # Ask for and validate the student's name.
        n_error=True
        while n_error:
            name=input("Enter your name: ").strip()
            if name=="":
                print("Name cannot be empty.")
            else:
                student.update({"name":name})
                n_error=False

        # Ask for and validate a unique student ID.
        id_error=True
        while id_error:
            student_id=input("Enter your student ID: ").strip()
            exists=False
            for record in students:
                if record["student_id"]==student_id:
                    exists=True
            if student_id=="":
                print("Student ID cannot be empty.")
            elif exists==True:
                print("That student ID already exists.")
            else:
                student.update({"student_id":student_id})
                id_error=False

        # Ask how many courses the student wants to enter.
        c_error=True
        while c_error:
            try:
                c_count=int(input("How many courses do you want to enter? "))
                if c_count<0:
                    print("Invalid entry. Enter 0 or a positive number.")
                else:
                    c_error=False
            except ValueError:
                print("Invalid entry. Enter a number.")

        # Store the course names and marks in separate lists.
        courses=[]
        marks=[]
        for i in range(c_count):
            # Get a valid course name and prevent duplicates inside the same student record.
            course_error=True
            while course_error:
                course=input("Enter your course: ").strip()
                if course=="":
                    print("Course cannot be empty.")
                elif course in courses:
                    print("Course already entered.")
                else:
                    courses.append(course)
                    course_error=False

            # Get a valid mark for that course.
            mark_error=True
            while mark_error:
                try:
                    mark=int(input("Enter the marks for the course: "))
                    if mark<0 or mark>100:
                        print("Invalid mark. Enter a number from 0 to 100.")
                    else:
                        marks.append(mark)
                        mark_error=False
                except ValueError:
                    print("Invalid entry. Enter a number.")

        # Add the course list and marks list to the student dictionary.
        Courses={"course":courses}
        Marks={"marks":marks}
        student.update(Courses)
        student.update(Marks)
        students.append(student)
        print("Student added successfully.")

    # Option 3: Search for a student using their ID.
    elif entry==3:
        id_search=input("Enter the student ID of the student you want to search: ").strip()
        found=False
        for student in students:
            if student["student_id"]==id_search:
                print("Student found.")
                print(student)
                found=True
                break
        if found==False:
            print("Student record not found.")

    # Option 4: Update a student's course marks or course list.
    elif entry==4:
        # Find the student record by ID before making updates.
        UC_id_search=input("Enter the student ID of the student whose marks or courses you want to update: ").strip()
        found=False
        for student in students:
            if student["student_id"]==UC_id_search:
                found=True
                break

        if found==False:
            print("Student record not found.")
        else:
            # Ask the user what type of update they want to perform.
            print("What do you want to do?")
            print("1. Change course marks.")
            print("2. Add a course.")
            print("3. Remove a course.")
            UC_error=True
            while UC_error:
                try:
                    UC_entry=int(input("Enter your choice: "))
                    if UC_entry>=1 and UC_entry<=3:
                        UC_error=False
                    else:
                        print("Invalid entry. Your choice can only be from 1 to 3.")
                except ValueError:
                    print("Invalid entry. Enter a number.")

            # Update an existing mark for a specific course.
            if UC_entry==1:
                course_search=input("Enter the name of the course: ").strip()
                if course_search in student["course"]:
                    course_index=student["course"].index(course_search)
                    new_mark_error=True
                    while new_mark_error:
                        try:
                            new_mark=int(input("Enter the new mark: "))
                            if new_mark<0 or new_mark>100:
                                print("Invalid mark. Enter a number from 0 to 100.")
                            else:
                                student["marks"][course_index]=new_mark
                                new_mark_error=False
                                print("Mark updated successfully.")
                        except ValueError:
                            print("Invalid entry. Enter a number.")
                else:
                    print("Course not found.")

            # Add one or more new courses and marks to a student's record.
            elif UC_entry==2:
                c_error=True
                while c_error:
                    try:
                        c_count=int(input("How many courses do you want to add? "))
                        if c_count<0:
                            print("Invalid entry. Enter 0 or a positive number.")
                        else:
                            c_error=False
                    except ValueError:
                        print("Invalid entry. Enter a number.")

                for i in range(c_count):
                    course_error=True
                    while course_error:
                        course=input("Enter your course: ").strip()
                        if course=="":
                            print("Course cannot be empty.")
                        elif course in student["course"]:
                            print("Student already takes this course.")
                        else:
                            course_error=False

                    mark_error=True
                    while mark_error:
                        try:
                            mark=int(input("Enter the marks for the course: "))
                            if mark<0 or mark>100:
                                print("Invalid mark. Enter a number from 0 to 100.")
                            else:
                                mark_error=False
                        except ValueError:
                            print("Invalid entry. Enter a number.")

                    # Append instead of replacing the existing course and mark lists.
                    student["course"].append(course)
                    student["marks"].append(mark)
                print("Course(s) added successfully.")

            # Remove a course and its corresponding mark from the student's lists.
            elif UC_entry==3:
                course=input("Enter the name of the course you want to remove: ").strip()
                if course in student["course"]:
                    course_index=student["course"].index(course)
                    # Remove the matching mark at the same position.
                    student["course"].pop(course_index)
                    student["marks"].pop(course_index)
                    print("Course removed successfully.")
                else:
                    print("Course not found.")

    # Option 5: Show all distinct courses in the class.
    elif entry==5:
        # Sets keep one copy of each course automatically.
        unique_courses=set()
        for student in students:
            for course in student["course"]:
                unique_courses.add(course)
        print("The unique courses are:", unique_courses)

    # Option 6: Show all students enrolled in a specific course.
    elif entry==6:
        course_search=input("Which course? ").strip()
        names=[]
        for student in students:
            if course_search in student["course"]:
                names.append(student["name"])
        print("The students taking", course_search, "are:", names)
        if names==[]:
            print("There are no students taking", course_search)

    # Option 7: Create a backup copy of the records for the current session.
    elif entry==7:
        # Copy the inner lists as well so the backup does not change with the original.
        backup=[]
        for student in students:
            copy=student.copy()
            copy["course"]=student["course"].copy()
            copy["marks"]=student["marks"].copy()
            backup.append(copy)
        print("This is the backup record:", backup)
        print("This backup only lasts while the program is running.")

    # Option 8: Exit the program.
    elif entry==8:
        print("Goodbye.")
        access=False
