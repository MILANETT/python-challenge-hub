MY APPROACH FOR THE PYTHON CHALLENGE 007
---
I created two global variables and a function add_NO adding the global variables x and y.  

I then did the local access challenge by creating a function subtract_NO() with two local variables a and b .I then tried accessing the local variables using print(a) which threw the NameError .  

For the same name different scopes I created max_NO and min_NO variables both globally and locally each having different values and multiplied the local and global  variables which displayed different answers.  

My approach for the modifying the global state was:I created a variable count and initialized it to 0,then created a function counter() with global variable count that is to be incremented by 1 everytime it is called .When the function is called it increments by 1 ie 1,2,3...  

The last part was to update the counter by a certain amount.I created the udate_counter() function which took two parameters count and amount.Count was globally initialized to 1 and update_counter() was to return count + amount.When the function is called it receives the arguments count and amount and adds the amount to the count variable and ouputs new count each time.

