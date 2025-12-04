# TUPLE --> 

# it cant be change  it is the written with the parethesis ( )
#it is the faster  , memoryEfficient than list 
# it is store the fixd data 
# it has less method becouse of the it is immutalbe


# tuple1 = ( 1, "visjal" , True , 34.4)
# print(tuple)
# print ( type(tuple))


# it cant be modify if you want to modify then it convert into the list 

t = (1, 2, 3)
lst = list(t)
lst.append(4)
t = tuple(lst)
print(t)



# tupple packing and unpacking 

t = 10 , 20 , 30   # it is like destrucur java script 

a  , b ,c = t
print(  a , b , c)

print(t)


#  Tuple Operations

# --> accessing tuple 

t = (1 , 3, 4 , 5  ,44, 5 )

print(t[4])   # return 44 at the index of the 4 
print(t[3:])  # Ite retuen the at the index of the 3 to last index 
print(len(t)) # lenght of the tuple 
print(t.count(44)) # it return  the how many times the given value in the tuple 


tup1 = 1.2 , 3. ,3 ,4
print(tup1)
print(type(tup1))

a, b , c ,d = tup1
print(type(d))


#  with * Operators 

a , c , *b = (3,4 ,4,3,5,33 ,4 ,3.323,) # a and c assign the firsth and second value ans left of the in the tuple b

print( a , b , type(a) , type(b)) # int  , list 


#  memory optimization in the tupel and list 

import sys
print(sys.getsizeof([1,2,3]))  # bigger
print(sys.getsizeof((1,2,3)))  # smaller



# 🟢 LEVEL 1 — BASIC (Beginner Questions)

# 1. Create a tuple with 5 numbers and print the third element.

tuple1 = (1 , 2 , 4, 5, 6,)
print(tuple1[3])


# 2. Create a tuple of strings and print its length.

stringTuple = ("vishal" , "yadav" , "raju ", "ghor")
print(len(stringTuple))

# 3. Slice a tuple (10,20,30,40,50) to get (20,30,40).

slices = (10,20,30,40,50)
print(slices[1:len(slices)-1])

# 4. Count how many times 5 occurs in (5,1,5,2,5,3).


coont = (5,1,5,2,5,3)
print(coont.count(t))


# 5. Find index of 30 in (10,20,30,40)

index = (10,20,30,40)
print(index.index(30))

# 🔵 LEVEL 2 — INTERMEDIATE Questions

# 6. Write a Python program to check if an element exists in a tuple.

tup2 = (10,20,30,40)
print(3 in tup2)


# 7. Convert list [1,2,3,4] to tuple.

list1 = [1,2,3,4] 
listToTuple = tuple(list1)
print(listToTuple)

# 8. Convert tuple (1,2,3,4) to list.

t = (1, 2, 3)
lst = list(t)  # [1, 2, 3]
print(lst)

# 9. Reverse a tuple without using reversed().

t = (1, 2, 3, 4)
rev = t[::-1]  # (4, 3, 2, 1)
print(rev)




# 10. Find the min and max from a tuple of numbers.
numbers = (10, 4, 56, 2, 89, 3)

minimum_value = min(numbers)
maximum_value = max(numbers)

print("Min:", minimum_value)
print("Max:", maximum_value)







# 11. Write a program to join two tuples.

numbers = ( 1, 2 , 2)
numbers2 = 90, 3
result = numbers + numbers2
print(result , type(result))


# 12. Remove duplicates from a tuple (1,2,2,3,3,4).


tuple5 = (1,2,2,3,3,4)
unq = tuple(set(tuple5))

print(unq)

# (Hint: convert to set → tuple)

# 🟣 LEVEL 3 — ADVANCED Python Tuple Problems


# 13. Tuple packing & unpacking:

data = ("Vishal", 23, "Developer")

name , age , ocupations =  data

print( "name : " , name , " age : " , age , "Profations : " , ocupations)

# 14. Unpack tuple using * operator:


t = (1,2,3,4,5)
first , *rest = t
print(first , rest)


# 15. Create a nested tuple and access the value 30:

t = (10, 20, (25, 30, 35))

print(t[2][1]) # Nested tuple value accessing 


# . Write a program to check if all elements in tuple are integers.

t = (1, 2, 3, 4)

is_all_int = all(isinstance(i, int) for i in t) 

# all( ) = > all return true if evry element pass the condtions
# isinstance( object , class) 

print("All elements are integers:", is_all_int)




# 17. Sort a tuple of numbers without using tuple.sort().

value1 = (83,493,49,293,3,39)
temp = list(value1)
temp.sort()      # >sort() it return None value 
result = tuple(temp)
print(result)


# Merge multiple tuples using a loop.

tuples = [(1, 2), (3, 4), (5, 6)]

result = ()

for t in tuples:
    result = result + t

print(result)

# 🔥 LEVEL 4 — REAL-WORLD / AI & ML Tuple Questions

# 19. Store a dataset sample using tuples:

# Each student record: (ID, Name, Age, Grade)
students = (
    (101, "Alice", 20, "A"),
    (102, "Bob", 21, "B"),
    (103, "Charlie", 19, "A"),
    (104, "David", 22, "C")
)

# Print the dataset
for student in students:
    print(student[1])
    print(student[1])

print(students[2][3])



# 20. Given an image shape tuple (224,224,3) extract height, width, and channels.

imageShape =  (224,224,3)
height , width , channel = imageShape
print( "height : ", height , "widht : ",width , "channel : " , channel)


# LEVEL 5 — HARD + LOGIC BUILDING Questions


# 26. Write a program to flatten this tuple:

t = (1, (2,3), (4,5,6))
t5 = (1, (2, (3, (4, (5, (6, 7))))))



def flatten (t):
    result = []
    for i in t:
        if (isinstance(i , tuple)):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
flattenResult = flatten(t5)
print(flattenResult)


# make a nested flatten tupple n number 

def make_nested_tuple (n):
    t = n
    for i in range(n-1 ,0,-1):
        t = (i , t)
    return t
print(make_nested_tuple(10))




# Final Summury 

# Immutable --> that con't change 
# Faster and Memory Effiecient 
# Used in Ai / Ml extensvely 
# Can be key of dictionary (list can't)
# Great for fixed Structure 


