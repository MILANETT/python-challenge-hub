
def calculate_average(sub1,sub2,sub3):
    total=sub1+sub2+sub3
    avg=total/3
    return avg


nStudents=2
for n in range(nStudents):
    name=input("Enter your name:")
    sub1=int(input("Enter marks for subject 1:"))
    sub2=int(input("Enter marks for subject 2:"))
    sub3=int(input("Enter marks for subject 3:"))
    calculate_average(sub1,sub2,sub3)
    print("Student:",name)
    print("Average:{:.2f}".format(calculate_average(sub1,sub2,sub3)))



def displayName():
    return name

print(displayName())

def calculate():
    add=sub1+sub2
    return add

print(calculate())
#print(add)

#when I added print(add) there was an error
#NameError:name 'add' is not defined
#This shows that a variable inside a function can not be accessed outside the function
num1=98;num2=78
add=num1+num2
print(add)

fruit="apple"
def fruitDisplay():
    fruit="banana"
    return fruit

print("Using the function:",fruitDisplay())
print(fruit)

def product(a,b):
    a*b
def _product(a,b):
    return a*b
def _Product(a=15,b=13):
    return a*b

print(product(10,34))
print(_product(32,12))
print(_Product())
print(_Product(14,12))


#Defining a function is writing what is to be done by the function while calling a function is asking it to do what it was defined to do
#Return gives the value calculated while print displays info so print cannot be used to show the calculated values
#A parameter is the variable written when defining a function while an argument is the value assigned to a function when calling it 
#A local variable is a a variable defined in a function while a global variable is defined outside a function 
#The mistake I encountered is I used name.calculate_average() to call the function thus I encountered an error saying str does not have 'calculate_average' attribute