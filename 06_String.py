

#===================  STRING =========================

# --> a string is sequence of character enclosed with single , dobule and triple quote

str1 = "this is the duble qoute"
str2 = 'this is the single qoute'
str3 = """ this is the triple qoute"""

str4 =" this is the escape sequnce chat example , \n i want to ptint thid line into the next line"

print(str4)

str5 = "vishal "
print(len(str5)) # length function includes the space also Special char and digit.



# Accessing Character and Indexing 

str = "vishal"
first = str[0] # first letter of the string -> V
last = str[-1] # Last letter of the string -> l

print(first , last)

# String Slicing 

# --> you can extract the part of the string using [:]

part = str[2:4] # sh  [ include : exclude]


print(part)

print(str[3:]) # start given index and go to last (lenght of the string)
print(str[:5]) # start from 0 index and go thre given index .



# string method (Basic to Intermediate)

#  ✅ .upper() -->


str = "vishal"
new = str.upper()
print(str , new)


# .lower() -->

uppercase= "VISHAL"
lower = uppercase.lower()
print(uppercase , lower)


# .title() --> Capitilized each word .

normal = " helli my self vishal yadav"
capitlized = normal.title()
print(normal ,capitlized)


# .strip() --> Remove the white spacees

h1 = "  this is"
h2 = h1.strip() # It remove the leading and trailing whit space 

print(len(h1) , h1 ,len(h2) , h2)


# .replace() --> Replace the substring 

str = "my name is vishal"
changeName = str.replace("vishal",'Vikas')
print(str , changeName)


# split() ---> Split into the list 

listString = "naman"
listStr = list(listString)
# join = listStr.join()
listStrNew = listString.split(" ")
print(listStr , listStrNew)


# String formating [ importent for productin level]


# 1 . f-steing --> fastest and cleanest dyanamic text.

name = "visha yadav"
age = 22
formating = f"hello my name is {name} and i am {age} year old ."
print(formating)


# format() method -->


text = "hello my school name {}. and i am in {} classs"
formate = text.format("vishal",33)
print(text , formate)


# Old style formating ... { % }

name = "Rohit"
age = 33

oldWayToFormate = "name is %s and age id %d  ."
# print(oldWayToFormat % (name , age))
print("name is %s and age id %d ." %(name , age))




# String Operations 

a =  "hello"
b = "world"

conctination = a + " " + b
print(conctination)

repeat = a *4 # Reapeat hello repeat 4 times like hellohellohellohello
print(repeat)

membership = "H" in a

print(membership) 



#String Iteration 


char = " vishal yadav"

for  ch in char:
    print(ch)


    # \n --> new Line
    #\t --> new tab
    #\\ --> backSlash
    #\` --> single quote

# Advance Topic in string 

# 1. string Immutaibility 

# -->. You can't Change a string after creation 

s = "Hello"
# s[0] = 'Y' ❌ → Error
s = "Y" + s[1:]  # ✅ New string

print(s)

# 1. String Searching...

msg = "Hello world"
print(msg.find("world"))   # 6
print(msg.startswith("He")) # True
print(msg.endswith("ld"))   # True

# find()--> Search a Sunstring and return the index where the substring is start . if
# Substrini not found then retuen -1;

# startwith()--> Check the wether the given the string strt with thr given prefix [True . False]

# endwith() --> Check the wether the given the string end with thr given prefix [True . False ]



# Count and index 

text = "banana"
count = text.count("a") # 3
print(count)
index = text.index("n") # 2
print(index)


intro = " my name {} , and i am {} year old ."
intro.format("vishal" , 29)
print(intro)
hello = "{} scored {}".format("Vishal", 90)
print(hello)


#  string immutability .

# string can't be change 
 
str = " hello"
#"##str[2]="v"
#print(str) # ❌ it can't be change 

modify = "vis" + str[3:]
print(modify)

