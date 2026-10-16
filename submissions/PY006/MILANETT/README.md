# My approach for PY006(I used the optimized question)
* I started by defining my function using the def keyword, named it calculate_average and assigned to it the three marks of the three subjects as the the three parameters, I then created a variable total which would store the sum of the three marks , and another average
which I assigned the average of the three marks and closed its definition with return average. This would be the average score calculator.
* For the detail collection part, I created a variable max_students to store the number of students whose scores I want and assigned 2 to it.Then I created an empty list named 'scores' where  I would store the collected student name and calculated average to help in easy display, then I looped in the range of the max_students and prompted the user for the student's name and mark for each subject which I stored in variables 'name' and those corresponding to each subject. From there I called the calculate_average function and stored its value in a variable named 'average_mark' then I appendedthe name and average_mark to a dictionary inside the scores list.I followed with a for loop to display each name and average using the print().
* For the second part , here are the conclusion from my experiments;
  A function can access a variable defined outside it
  A variable defined inside a function cannot be accesed outside that function.
  When a local variable and a global variable share the same name, the local variable overrides the global variable inside the function but   the global variable remains unchanged outside the function.
  A local variable cannot be modified inside a function.
  
