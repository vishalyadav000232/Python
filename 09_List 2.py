# what is the list 

# --> ordered
# --> Mutable
# --> Can hold multiple datatype 
# --> Allows Duplicate 

# syntax -->

 # list_name = [item1 , item2 , item3]


list = [ 1,2,3,"python" , True]
print(list)
print(type(list))


# ACCESSING THE DATA IN THE LIST 


first = list[0]
second = list[1]
third = list[2]
fourth = list[3]
fift = list[3]

print( first , second , third , fourth , fift)

list[4]= False

print(list)

# SLICING IN THE LIST 

# also slicing are possile on the basic of the negative index.

fruits = [ "apple", "banana", "sitafal", "papaya "]

print(fruits[2:]) # print the list from the index 2 to last index.
print(fruits[:5]) # slicing the from starting index to the given index ',
print(fruits[::-1]) # reversing 




#  ADDING ELEMENT IN THE LIST 

# append() --> add the one element at the last 
# insert(index , value)
# etend(itreble) -- add multiple item like tupple , set dictionary string etc



marks = [23.4 ,34.43 , 34.32,324]
marks1 = ["hindi" , " english" , " maths"]
print(marks)
marks.append( 25 ) # 25 append at the last in the marks list.
print(marks)
marks.insert( 3 , 50) # insert the value at the index of the 3 the value is the 50 
print(marks)

newList = marks.extend(marks1)
print(marks )


# REMOVING ELEMENTS 

#--> REMOVE(value) --> remove by the specific item 
#--> pop(index) --> remove by the inxing
#-->clear() --> Empty list []
#--> del --> Delete completly 

temperature = [23, 43, 34, 234]
print(temperature)

temperature.remove(43)  # Removes 43 from the list
print(temperature)

removed_value = temperature.pop(2)  # Removes element at index 2 (234)
print(removed_value)  # pop() returns the removed value
print(temperature)

temperature.clear()  # Clears all elements, list becomes empty
print(temperature)

del temperature  # Deletes the entire list variable
# print(temperature)  # ❌ This will give an error (variable no longer exists)



#LOOPING THROUGH THE LIST 

fruits = [ "apple", "kela", "amrud",]
for val in fruits:
    print(val)