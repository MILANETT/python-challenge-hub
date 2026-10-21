## Global access
I created a function to display the session count which is a **global variable**.

## Local access
I created a function in order to create a **local variable**.
The local variable could not be accessed outside the function.
I tried accessing it using print() but I encountered a NameError

## Same name, different scope
I created 2 variables with the same name; one local and global
I tried changing the value of the global variable using the function but it did not work.

## Modifying global state
I created a function that would increase the value of the session count.
I also created another function that was parameterised to increase the session count.
In comparison,the second function was easier to use since there is no need for creating a global variable.

