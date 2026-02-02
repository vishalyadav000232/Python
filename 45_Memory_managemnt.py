'''
Python Memory Managment 


python automatically handle the memory allocation and delocation for object .

Memory managment Basic 

python manage memory automatically through the internal system called python memery managemrnt 


memory in python in devide into three part :

1. Private heap (all object and datastructure )
2. stack and memory (function call frames, local variables)
3. Global memory (global variables, constants)



Program does not manually allocate and deallocate  memory 
Python usr reference count and garbage collection to manage it 


'''

# Reference count 

'''
Every Object in python has a reference count: how many variable and object to point to it 


when refernce count drop to zero python automatically delete the object and free the memory 


'''


import sys

a = [1, 2, 3]
print(sys.getsizeof(a))
b = a # 3
c = a # 4 Reference count increases
print(sys.getrefcount(a))  # Shows reference count (including temporary reference)
del b  # 3 Reference count decreases
print(sys.getrefcount(a))



# Garbage Collection 

'''

Python use a cyclic garbage collector to handle the circular refernce

concept 


gc module module manage the garbage collecter 

pytho use the generational appproch 

Generation 0: New objects
Generation 1: Survived one GC cycle
Generation 2: Long-lived objects (rarely collected)


'''

import gc

# Check if GC is enabled
print(gc.isenabled())

# Disable GC
gc.disable()

# Enable GC
gc.enable()

# Force garbage collection
collected = gc.collect()
print(f"Unreachable objects collected: {collected}")


class Node:
    def __init__(self):
        self.next = None

a = Node()
b = Node()
a.next = b
b.next = a  # Circular reference

del a
del b

# Without gc, memory may not be freed immediately
gc.collect()  # Forces cleanup
