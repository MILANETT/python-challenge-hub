#PART 1

G_variable=20
def G_access():
    global G_variable
    print(G_variable)
    
G_access()

#PART 2

def L_access():
    L_variable=20
    print(L_variable)
L_access()
#print(L_variable)

#PART 3

def s_cope():
    G_variable=90
    print(G_variable)
s_cope()
print(G_variable)

#PART 4
count=0
def increase():
    global count
    count+=1
    print(f"The count is:{count}")
increase()
increase()

s_count=0
def s_increase():
    s_count
    s_count+=1
    print(f"Without global declaration:{s_count}")
s_increase()

#PART 5
def design(count,amount):
    U_count=count
    U_amount=amount
    return U_count
design()