# VARIABLE --> Variable is a name given a memory location in a program .

# 1--> Variable can be combinaition of the upperCase and lowerCase and underscore .
# 2--> Variable can't start by the digit that way the valid variable otherwise invalid.
# 3--> We can't use Special Symbol like !@$%^&*( etc. 
# 4--> Variable can be any lenght .

age = 23;
print(age)
age =38;
print(age)
print(age + age)


name = 'vishal yaadav'
print("My name is :" ,name)
age = 50
print("My age is :",age)
price = 99.99
print(price)


# ASSIGNMENT RULE 
b1= "hello"
a1 = b1 # Right side value are store in left side variable .


# TYPE METHOD     
#--> type define the which Datatype of varible is store in the varible 
# : -- there are five type of the datatype in thr python 

# 1--> Integer
# 2--> String
# 3--> Float
# 4--> Boolean
# 5--> None

isAvailble = True;
byDefault = None;

print(type(age))
print(type(name))
print(type(price))
print(type(isAvailble))
print(type(byDefault))


# KEYWORD IN PYTHON 

# => and , as , assert , break , class , continue , def , del , elif , else , except , finally , 
# => False ,for , from , global , if  , import , in , is ,lambda , nonlocal , None , not , or , 
# => pass , raise , return , True , try , with , while , yield ,float , int 

# PYTHON ARE THE CASE SENSITIVE 
# --> in python small a and A is the not same both are have different memory location . 

a= 10
A =20
print( "a : ", a , "A:", A)


# PROBLEM-1 print sum of two number 

num1 = 9320
num2 =3893
sum = (num2 + num2 )
print("Sum of", num1 ," +" , num2 ,"=", sum)




#       EXPRETION EXECUTION 

A,B = 3,4
txt = "$"
print(3*txt*4)
str = A*txt*B
print(str)


num1 = "2"
num2 = 3
symbole = "@"
#sum = (num1 + num2)*2
print(sum) # Python does not add string + number 

print((num1 + symbole)*4) # concatination {string + string} => "vish" + "al" --> vishal


# 🔹 Arithmatic expretion with  integer and float will result in float .

num1 , num2 = 10, 5.50

sum = num1 + num2
mul = num1 * num2
div = num1 / num2
diff = num1 - num2

print( "sum", sum , " mul", mul , " div :", div , " difr :", diff)

#✅ all arithmatic operation will result in the float 


#  🔹 result of the division with two integer will be flaot 

a,b = 4,2
c= a/B
print("two integer division : " , c)


#  🔹 Integer division with flaot and and int eill give int displayed as float 

a, b = 1.5 , 3
c= a//b 
print(c , a/b)


# ⚠️ Result of the (A//B) is Equal to floor(A/B) 
# floor gives the closet , integer , which is lesser than equal to the float value.

A ,B = -12 , 5
C = A//B
print (C)

A ,B = 12 , -4
C = A//B
print (C)


#  🔹 Remainder is  negative when denominator is negative {MODULO (%)}


A ,B = -12 , 5
C = A%B
print (C)

A ,B = 12 , 5
C = A%B
print (C)

A ,B = 12 , -5
C = A%B
print (C)

# + % + = +
# + % - = -
# - % - = +
# - % + = +


# 🔹  COMMENT --> Commment that  ignore by the python interpreter 
# --> it two type 

# sinfle line like as
#Multiline Comment  it will written as



# ✅. INPUT IN PYTHON 

# input() Statement is used to accept vlue (using Kryboaed) from the user 

# 🔹 string input 

# taking input from the user & printig it 

# name = input("Enter Your Name :")
# print(name)

# 🔹 Integer input 

# age = int(input("Enetr your age :"))

# print(age)


# 🔹 Flaot input 

# price = float(input("Enter the price :"))
# print( price)



#⚠️ Practice Time

# 1. /* is a symbole used in python for a single line commet ❌

# 2. 2ndName is an invalid identifier in python ❌

 # 2ndName = vishal --> it is invalid becouse of the varivable name must br start with digit .

 # 3. ** is valid arithmatic Operaitor in python ✅

sqaure = 2**2
print( " here is the squre is : ",sqaure)


# 4. in is a logical operator in python ❌

# 5. Variable declaratin is implicite in python ✅

isAnswer  = not True and False or True
print(isAnswer)




x = 0.3 + 0.1
print(x == 0.3) # false becouse of the float precision 


