#  Closure :  A closure is a functions that remeber the value from its outer functions has finished its excutions 


def outer(msg):
    def inner():
        print(msg)
    return inner

hello = outer("kaho ka hal ba")
hello()

# where it is used in real project ?
# creating a functions factories 
# Data hiding in python
# Writing decorators 

# Closure with mutable state 

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())
print(c())
print(c())
print(c())
print(c())
print(c())


def outer(a):
    b=2
    def inner():
        print(a+ b)
    return inner

f = outer(10)
print(type(f.__closure__))
f()
print(f.__closure__[0].cell_contents)
print(f.__closure__[1].cell_contents)
# print(f.__closure__[2].cell_contents)


# Closiure for the dats hiding 
def bank_account(balance):
    print(balance)
    def withdraw(amount):
        nonlocal balance
        balance -= amount
        return balance
    return withdraw

acc = bank_account(1000)
print(acc(200))   # 800
