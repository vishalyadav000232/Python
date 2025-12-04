print("hello world");
age = 29
print(age)
print(39+1)
print(293)
# import sys

# a = []
# b =[]
# print(sys.getrefcount(a))

# import sys

# a = []
# print("RC of empty list:", sys.getrefcount(a))

# b = a
# c = a
# print("RC after two assignments:", sys.getrefcount(a))



# import sys
# import gc

# class Node:
#     def __init__(self, name):
#         self.name = name
#         self.ref = None

#     def __del__(self):
#         print(f"{self.name} destroyed")

# # Disable GC to see reference counting failure
# gc.disable()

# a = Node("A")
# b = Node("B")

# # Create cycle
# a.ref = b
# b.ref = a

# print("Refcount A:", sys.getrefcount(a))
# print("Refcount B:", sys.getrefcount(b))

# # Remove original references
# a = None
# b = None

# print("After setting variables to None (GC disabled):")
# print("Objects NOT destroyed due to cycle")



# Larger number and dynamic string create a new  memory location .

# num = 400
# num2 = 400
# print("number 1",id(num))
# print('number 2',id(num2))
# print (num is num2)


# a = 400
# b = 400
# print(a is b)


l1 = [1,2,3]
l2 = l1
print("l1",l1 , "l2 :" , l2)
print("l1 refrence :" , id(l1))
print("l2 refrence :" , id(l2))

l1 = "vihsla "
l1 = [1 , 2, 3]
print(" nwq l1 : " , l1 , "l2 : " , l2)

print("l1 updated refrence :" , id(l1))
l1[1 ]= 22
print(l1)
print(l2)

print("l1 refrence :" , id(l1))
print("l2 refrence :" , id(l2))




myList = [4,5,6]
yourList = myList
print( myList , yourList )
print(id(myList),id(yourList))
myList[0]=223
print(myList , yourList)
print(id(myList),id(yourList))



h1 = [ 1 ,2 ,3]
h2 = h1[:]
print(id(h1))
print(id(h2 ))


# 
s = "hello\nworld"
print(s)
str(s) # same like a print 
repr(s) # print the internal part that is like \n and \t  escape sequence char 



