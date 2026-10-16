My approach

I defined a function (calculate_avg) and passed three parameters representing the three marks that were to be performed calculations on. I defined a local variable total and passed the sum of the three marks input by the user and returned the average that was calculated by dividing the total by 3(Number of marks inserted).

I created an empty list that would store the students' info. I then used a for loop to loop through a range of the info prompted to the user of the students' info such as name and the three marks scored. I called the function I defined earlier and stored the output in a variable avg and appended the students' list with the info the user input.
I finally used a for loop to print out the student details.

For part two of the challenge , I was able to prove that a global variable can be accessed by a function but a local variable cannot be accessed outside its function as I tried printing out the local variable num but it caused a Name Error. From the challenge I was also able to gather that when a global and local variable have the same names, the local variable is used as long as the function is called otherwise the global variable is used.I tried modifying the global variable inside a function but I got an UnboundLocalError that suggested that a "Local variable" wasn't defined hence proving that the global variable can't be modified inside the function unless you use the global keyword inside the function.
