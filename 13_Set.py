# Set --> this is the one of  underrated and most powerfull type speacially in the 
# removing duplicate 
# fast membership check 
# feture engineering in ml
# Vocabulary bulding in NLP
# graph algorithm 


# --> it is the unordered and unique collection 
# no index ❌
#  Mutable ✅
# fast O(1) time and space complexity 


# Set Operation 

# Union ( items either in set ) a | b
# Intersection (common list) a & b
# Difference.   a - b
# Symetric difference  a ^ b


#  A set is written using the CuryBraces { };

my_set = { 1, 3, 5,3 ,5,3,3 ,3}    # Set remove the Duplicate value 

print(my_set) # {1 ,3,5}
print(type(my_set)) # class set
print(len(my_set)) # 3


# Creating Set 

set1 = {1,2,3}
set2 = set([1,2,3,4])
set3 = set("hello")
set4 = set()
print(set1 , set2 ,set3 ,set4)

# Accessing the element in set 

# --> Does't access the using the index 

# using loop


for i in set1:
    print(i)


# Adding and Removing Element 


s = set()
s.add(12) # add() add only one value in the set
s.update([23,43,'vishal'])
s.remove(23)    # gives ERROR if 5 not found
s.discard(5)   # NO error if not found
s.pop()        # Remove the random element 
s.clear()       # Clear all set 

print(s)



# 🛑 Set Operation 




a = { 1, 2, 3, 4,9}
b = {4 , 3  ,5, 7}

print("Union : " , a | b)   # Union  a | b
print(a.union(b))


print("Interdection  : " , a & b)   # Intersection a & b
print(a.intersection(b))


print("Difference : " , a - b)      # Difference  a - b
print(a.difference(b))


# Membership in check O(1)
s = { 2 ,3 ,5,3 ,2, 10}
if 10 in s:
    print("present")


s = {x*x for x in range(1, 6)}
print(s)



# Feozen Set 

fs = frozenset([1,2,3])
print(fs)




# 🟦 LEVEL 1: Basic Set Questions


# Q1. Create a set with values s = { 2 ,3 ,5,3 ,2, 10} and print it.

basicSet = set( [2 ,3 ,5,3 ,2, 10])
print(basicSet)


# Q2. Add the number 50 to a set.
basicSet.add(50)

print(basicSet)


# Q3. Add multiple elements (60, 70, 80) to a set.
basicSet.update([60,70,80])
print(basicSet)


# Q4. Remove the element 50 using remove().
basicSet.remove(50)
print(basicSet)



# Q5. Remove the element 999 using discard() and show that no error comes.

basicSet.discard(999)
print( basicSet)


# Q6. Try to access the first element of a set.

# print(basicSet[1]) it is not allowed in set 

# --> they are not store in the fixes position 
# --> Every time you run the code the order can be cahnge 




# Why does it fail?

# Q7. Convert a list with duplicates into a set:\


list1 = [1, 2, 2, 3, 3, 3, 4]
uniqeList  = set(list1)
print(uniqeList)

# Q8. Check if 15 is present inside a set.

s = { 2 ,3 ,5,3 ,2, 10}
if 10 in s:
    print("yes Present ");
else:
    print(" not present ")






#     🟩 LEVEL 2: Intermediate Questions
# Q9. Find union, intersection, difference, symmetric difference between:
A = {1,2,3,4}
B = {3,4,5,6}

print ( A | B) 
print ( A & B) 
print ( A - B) 
print ( A ^ B) 

# Q10. From a set, remove 2 random elements using pop().


s = { 2 ,3 ,5,3 ,2, 10}
s.pop()
remaing = s.pop()  # it return the removed element 
print(s)
print(remaing)



# Q11. Create a set comprehension to store squares of numbers from 1 to 10.

sqaure ={i*i for i in range(1,10)}
print(sqaure)


# Q12. Check if set A is a subset of set B.

A = {1, 4 ,33}
B = {1, 2, 3, 4}

print(A.issubset(B))   # True



# Q13. Check if two sets are disjoint.

A = {1, 2, 4}
B = {4, 5, 6}

print(A.isdisjoint(B))   # True



# Q14. Convert this tuple to a set:
tipl =  (10, 20, 30, 40)
settuple = set(list(tipl))
print(settuple)

# 🟧 LEVEL 3: Advanced Questions


# Q15. Create a frozenset and try adding an element.



# Explain the error.

# Q16. Two sets contain student roll numbers.

# Find students who attended both classes.

# Q17. Two sets contain registered emails and submitted emails.

registered = {"a@mail.com","b@mail.com","c@mail.com"}
submitted = {"a@mail.com"}

never_submitted = registered - submitted
print(never_submitted)


# Find emails that never submitted the form.

# Q18. Given 2 sets of features:
# ML_features = {"age", "salary", "experience"}
# DS_features = {"salary", "degree", "experience"}


# Find common features used in both models.
model1 = {"age","salary","gender","city"}
model2 = {"salary","city","experience"}

only1 = model1 - model2
only2 = model2 - model1
common = model1 & model2
print(common)

# Q19. Remove duplicate words from a sentence using a set.
# Q20. Check if all characters in a password are unique.
# 🟥 LEVEL 4: AI/ML Real-World Set Problems
# Q21. Remove duplicate labels from this ML dataset label list:
# labels = ["cat","dog","cat","horse","dog","lion"]

# Q22. You have a list of stopwords.

# Remove stopwords from a text using sets.

# Q23. Find unique tokens in a dataset sentence list:
# sentences = ["i love ai", "ai loves python", "python loves me"]

# Q24. Features of two ML models: