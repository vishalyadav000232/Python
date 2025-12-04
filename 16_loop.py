# loop in python 

# for loop

#  Iterate over the Subsequence {list , tuple , dictionary ,range}
#  Use Break to exit loop , use Continue to skip the 


fruits = ["apple","banana", "pine-apple","guava","grapes"]

for fruit in fruits:
    print(fruit)


# for loop with rangr keyword range( start , stop  , step)
# Common in indexing or repeated operations

for i in range(5):  # 0 to 4
    print(i)

for i in range(2, 10, 2):  # 2,4,6,8
    print(i)



#  Nested for loop 

for i in range(1,4):
    for j in range(1,4):
        print(i, j)


#  while loop 

i = 1 
while i < 5 :
    print(i)
    i+=1


#  loop control break statement 

for i in range(5):
    if i == 3:
        break  # exit loop
    print(i)

for i in range(5):
    if i == 3:
        continue  # skip iteration
    print(i)


#  else with loop 

# ==> else in. loop  genrally run when the loop is copleted , not if break occurs 


for i in range (3):
    print(i)
else:
    print("loop is ending ")



    # Looping with the Enumurated and zip 


    # Enumerate gives index + value
fruits = ["apple","banana"]
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

# Zip combines two lists
names = ["Alice","Bob"]
scores = [90,85]
gender = ["male" , "female"]
for name, score , gender in zip(names,scores , gender):
    print(name, score ,gender)



# Yield in python 

# -- > yiels is used in the function to crete a generator 

# A generator is special type gives the on value one value t a time at once like return 

# 🔥 1. Difference Between return and yield

# return


#  stop the functiom completly 
# gives only one value 

# yield 

# Pauses the functio and remember where it stoped 
# when next value is needed continue the same point 
# give the multiple value one by one 