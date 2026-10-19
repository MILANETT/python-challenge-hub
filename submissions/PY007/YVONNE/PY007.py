#GLOABL ACCESS
print("!!!GLOBAL ACCESS!!!")
x=100
y=100
def add_NOs():
    print(x+y) 

add_NOs()
#the function add_NOs can access the global variables x and y

#LOCAL ACCESS
print("!!!LOCAL ACCESS!!!")
def subtract_NOs():
    a=80
    b=60
    return a - b

print(subtract_NOs())
#print(a)
#File "c:\Users\Hello\Desktop\PYTHON\PY007.py", line 19, in <module>
#    print(a)
#          ^
#NameError: name 'a' is not defined
#the variables a and b can only be accessed by the function subtract_NOs

#SAME NAME DIFFERENT SCOPES
print("!!!SAME NAME DIFFERENT SCOPES!!!")
max_NO=9
min_NO=3
def multiply_NOs():
    max_NO=4
    min_NO=2
    return max_NO * min_NO

print("GLOBAL VARIABLES MULTIPLICATION:",max_NO*min_NO)
print("LOCAL  VARIABLES MULTIPLICATION:",multiply_NOs())
#the global varible multiplication outputs 27 
#local variable multiplication  will be 8

#MODIFYING THE GLOBAL STATE
print("!!!COUNTER EXECUTION !!!")
count=0
def counter ():
    global count
    count+=1

    print(count) 
    
counter()
counter()
counter()

#File "c:\Users\Hello\Desktop\PYTHON\PY007.py", line 39, in counter
#    count+=1
#    ^^^^^
#UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
#when the global keyword is removed it brings the error above

#COMPARE DESIGNS
print("!!!COMPARE DESIGNS!!!")
count=1
def update_counter(count,amount):
    return count+amount

count=update_counter(count,1)
print(count)

count=update_counter(count,2)
print(count)

count=update_counter(count,2)
print(count)
#update_counter() does not change a global variable. It calculates and returns a new value, and you decide where to store that value.
#however counter() modifies the count variable by 1 everytime its clled