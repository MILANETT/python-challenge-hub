# PY007 — Inside and Outside: Understanding Scope
# Student: write your experiments below.
#
# Use the README for the challenge requirements.
# Record your observations as comments.
#
# Begin with a global session counter:
completed_sessions = 0

# TODO 1: Write a function that reads the global counter without changing it.
def read_globalSession():
    return completed_sessions

print(read_globalSession()) #Output : 0
# TODO 2: Create a local variable inside a function.
def display_my_var():
    my_var="star"
    return my_var

print(display_my_var())
#         Test what happens when you try to access it outside that function.
#print(my_var)
#Output : NameError: name 'my_var' is not defined
#A local variable is only created at the call of a function and dies immediately the function finishes
# executing

#         Keep any deliberately failing line isolated/commented out afterward.


# TODO 3: Use the same variable name inside and outside a function.
rate = "20%"
def display_rate():
    rate="30%"
    return rate

#         Display both values and explain what you observe.
print(display_rate()) # Output= 30%
print(rate) # Output= 20%
#The local variable printed what was in the function while the global variable printed the initial value

# TODO 4: Write a function that increments completed_sessions.
def add_completed_sessions():
    global completed_sessions
    completed_sessions += 1


add_completed_sessions()
print(completed_sessions)
add_completed_sessions()
print(completed_sessions)
#         Investigate where the global keyword is needed.
#global key is needed to make the function know that it is a global variable
#On omitting it:Output=UnboundLocalError: cannot access local variable 'completed_sessions' where it is not
# associated with a value

# TODO 5: Write a separate function that receives a count and an amount,
#         then returns the updated count without changing the global counter.
def mod_completed_sessions(completed_sessions,amount_completed):
    completed_sessions += amount_completed
    return completed_sessions

# TODO 6: Call your functions to test them and add your observations as comments.
print(mod_completed_sessions(0,5))
print(completed_sessions)
#This approach modifies only the variable created inside unlike the global state modification approach that
# utilizes the global variable to increment