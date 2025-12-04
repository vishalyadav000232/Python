# mutable and immutable i pyhton 


# ==> int
x = 10
print(id(x))
print(x)

x = 23
print(id(x))
print(x)


# ==> string 

name = "vishal"
print(id(name))
name = name + " yadav"
print(id(name))
print(name)


#  Object jinko bina naya banye change kar skte ho matlb ki same memory location par save  changes karna 

list = [1,2,3]
print(id(list))

newlist = list.append(3) # list return a none value 
print(newlist)
print("list :" ,id(list))
print("newlist" , id(newlist))


fullName = "vishal"
name = fullName
print("1",id(name))
print("2",id(fullName))
fullName = "vikas"
name = fullName
print("3" , id(name))
print("4" ,id(fullName))

x = 20
print(id(x))
x=20.00
print(id(x))










import gc

# Enable automatic garbage collection
gc.enable()

# Create a reference cycle
class Node:
    def __init__(self, name):
        self.name = name
        self.ref = None

a = Node("A")
b = Node("B")

a.ref = b
b.ref = a  # cycle created

# Delete original references
del a
del b

# Collect garbage manually
collected = gc.collect()
print(f"Garbage collector: collected {collected} objects.")
