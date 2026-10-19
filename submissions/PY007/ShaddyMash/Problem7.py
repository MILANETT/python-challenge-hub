
# PY007 - UNDERSTANDING VARIABLE SCOPE

# PART 1

# A global variable can be accessed inside a function.
G_variable=20
def G_access():
    global G_variable
    print(G_variable)
    
G_access()


# PART 2

# A local variable can only be accessed inside its function.
# Trying to access it outside causes a NameError.

def L_access():
    L_variable=20
    print(L_variable)
L_access()
#print(L_variable)


# PART 3

# Using the same variable name inside a function
# does not change the global variable.

def s_cope():
    G_variable=90
    print(G_variable)
s_cope()
print(G_variable)

# The function prints 90, but the global value remains 20.


# PART 4

# count represents the number of completed study sessions.
# The global keyword allows the function to update it.

count=0
def increase():
    global count
    count+=1
    print(f"The count is:{count}")
increase()
increase()

# The count increases from 0 to 1, then to 2.


# Trying to change a global variable without global
# causes an error because Python treats it as local.

s_count=0
def s_increase():
    s_count
    s_count+=1
    print(f"Without global declaration:{s_count}")

# I used try/except so the error does not stop the program.
try:
    s_increase()
except UnboundLocalError:
    print("Cannot change s_count without global.")


# PART 5

# This function receives the current session count
# and the number of sessions to add.
# It returns the updated count without changing the global one.

def design(count,amount):
    U_count=count+amount
    U_amount=amount
    return U_count

result=design(count,3)

print(f"Updated count:{result}")
print(f"Original count:{count}")

# The updated count is 5, while the global count stays 2.
# Passing arguments and returning results lets me
# calculate new values without changing global variables.
