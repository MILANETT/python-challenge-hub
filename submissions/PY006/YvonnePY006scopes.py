x=100#x and y are global variables and cann be accessed outside the functions
y=20
def add_No():
    x=80#x and y are local variables  and can only be used in function add_No
    y=30
    return x+y

print("LOCAL VARIABLES SUMMATION :",add_No())#call the function add_No
print("GLOBAL VARIABLES SUMMATION1:",x+y)#adding the global variables

def subtract_No(x,y):#x and y are parameters inside paranthes when function is defined
    return x-y

print("SUBTRACTION:",subtract_No(100,30))#100 and 30 are arguments passed to a function when its called

x=30
y=10
print("GLOBAL VARIABLES SUMMATION2:",x+y)#changes the global variables only