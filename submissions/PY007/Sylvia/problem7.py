#Global access
sessionCount=1
def displaySessionCount():
    return sessionCount

print(displaySessionCount())

#Local access
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

def addNo():
    add=num1+num2
    return add

#print(add)
#This led to a NameError:name 'add' is not defined
#This shows that you can not access a local variable outside the function

print(f"{num1}+{num2}={addNo()}")

#Same name,different scope
car="Lexus LX700"

def displayCarDetails():
    car="Range Rover Sport"
    return car

print("Using the global variable:",car)
print("Using the function:",displayCarDetails())

#Modifying global state
def increaseCount():
    global sessionCount
    sessionCount+=1
    return sessionCount
#

#When I removed the global keyword I encounter an error
#The local variable 'sessionCount' cannot be accessed because it has no value

print("New session count:",increaseCount())
print("New session count:",increaseCount())
#when I called the function twice,the second result was an increase of the first result


#Compare designs
def increaseSession(sessionCount,amount):
    sessionCount=sessionCount+amount
    return sessionCount

print("New session count:",increaseSession(2,6))

#For the second function,it allows checking of many users' session count easily
#The first function however requires one to assign a number to the variable each time making it tiresome
#I would recommend using the second function