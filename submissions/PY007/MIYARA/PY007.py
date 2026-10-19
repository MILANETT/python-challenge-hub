# a)
std_sess = 5


def read_std():
    return std_sess


print(read_std())
# Output  -> 5
# The function can read the global variable

# b)


def local_var():
    age = 21
    return age


print(local_var())
# Output -> 21
# print(age) -  Causes an error
#       print(age)
#           ^^^
# NameError: name 'age' is not defined
# A local variable cannot be accessed outside its function

# c)
name = "Monicah"


def lname():
    name = "Miyara"
    return name


print(f"Value inside:{lname()}")
print(f"Value outside:{name}")
# Output :
# Value inside:Miyara
# Value outside:Monicah

# Explanation: When calling the function, the function uses the local inside
# it(Overrides the global variable) but does not modify/ change the global variable outside so the global variable
# still remains unchanged

# d)
count = 7


def inc_global():
    global count
    count += 1
    return count


print(f"1st count:{inc_global()}")
print(f"2nd Count:{inc_global()}")
# Output:
# 1st count:8
# 2nd Count:9

# After removing the keyword count, I got the following error
# UnboundLocalError: cannot access local variable 'count' where it is not
# associated with a value

# Explanation:
# This means that while a function can read a global variable , it can not
# modify it.

# e)


def receive(count, amount):
    count += amount
    return count


print(f"Updted count:{receive(5, 2)}")
# Output -> Updted count:7
# This approach is better as you can easily modify a variable and get the
# expected output without getting an unboundLocal error 
