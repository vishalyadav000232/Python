# OPERAITOR IN PYTHON 

# --> Oprator is mathematical expretion that perform the opratont between two operand ,

# 1. Arithmatic operators . 
num1 = 41
num2 = 4

addition = num1 + num2 
multiplication = num1 * num2 
substraction = num1 - num2 
divide = num1 / num2
remainder = num1 % num2
floor = num1 // num2
square = num1 ** num2
print(addition ,multiplication ,substraction ,divide ,remainder ,floor , square)


# 2. Relational and Comparision operators . 

isLessThen = 23 < 34 # true 
print(isLessThen)
isGreterThen = 23 < 34 # true
print(isGreterThen)

#----------------------------------------------

isLessThen = 23 > 34 # false
print(isLessThen)
isGreterThen = 23 > 34 # false
print(isGreterThen)

print(7==7) # true
print(4!=5) # true

# 3. Assignment  operators .
  
name = "Manas kumar lal" #  = --> Right value store un the left one.
num1 = 40
num1 -= 10 
print(num1)  # -= -->  Right value substract from the left then store in left memoey location . 40-10 = 30
num1 += 25; # + --> Right value add in the    left then store in left memoey location . 30+20 = 50


# similarly as  --> /= and *= . **= 



# 4. logical  operators .


# 1. and --> if both value is true then return true otherwise falsetrue

isTrue = True and True # --> it return true becouse of bothe value has true other wise false
print("isTrue :",isTrue)

# 2. or --> if any value is true then return true otherwise false

isOrOperztors = True or False # -- if any value is true then it will we true other wise false.
print("isOrOperztors :" , isOrOperztors)

# 3. not -- if false then true , and true --> false

notOperaots = not True # --> not logical operators is change the value true-> false and falsr-> true

print("notOperaots:",notOperaots)
# MemberShio Operators 

# 1. in 
# 2 . not in

# Identity OPERATORS

# is
# is not 




# ======== BITWISE OPERATORS =============

#  it is the thre type 

# & , | , ~ it is the same like a logical operators but works in both bit (1 ,0 ) and (true , false)



# ============================ ARITHMATIC OPERATORS  =======================


num1 = 234
num2 = 40

print(num1 + num2);  # Adition
print( num1 - num2); # Substraction
print( num1 * num2); # Multiplication
print( num1 / num2); #Diviosion (Flaot)
print( num1 // num2); # Floor Division
print( num1 % num2);  # Module (Reamiander)
print( num1 ** num2);  # Exponent ( sqaure root )



# ============================ COMPARSION OPERATORS  =======================

print(5 == 5);  # True -- Equal 
print( 5 != 3) # true --> Not Equal
print(5 > 3);  # true ---> Greater then 
print(5 >= 5 ) # true --> grater than equal
print( 5 < 3) # false --> less then 
print( 3<= 3) # true --> less then equal


# ============================ Logical OPERATORS  =======================

print(5 > 3 and 10 > 5)  # True (lodical and )--> true if both condtion is true
print( 5==5 and True != True) # True ( logical or) --> true if any condtion is true
print(not True) # logical not --> reverse the Result


# ============================  Bitwise OPERATORS  =======================

# & AND operators 

bitwiseAnd = 5 & 3 # let's 5 and 3 convert into the binary number - 5-> 0101 and 3 - > 0011
print(bitwiseAnd) # bitwise oprator 1 & 1 -> 1 otherwise return -> 0
                    #                                                  0001 -> 1  

# ` OR operators 
# (^) XOR Operators 
# (~) NOT Opearots
# (<<) Left shift
# (>>) Right Shift



# ============================  Membership OPERATORS  =======================

# Used the chek the wether the value is the part of the sequence or not .

inPresent = "a" in "apple" # retuen true when a in apple present otherwise false
print("inPresent" ,inPresent)

notInPresent = "x" not in "apple" # Return True when "x" is not present

print("notInPresent",notInPresent)



# ============================  Identity OPERATORS  ======================= 

# Used to compare the memory location not just value

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)   # True (same memory)
print(x is z)   # False (different memory)
print(x == z)   # True (same value)



# Operators Precedence (Advance )
result = 10 + 2 * 3 ** 2
# Step 1: 3 ** 2 = 9
# Step 2: 2 * 9 = 18
# Step 3: 10 + 18 = 28
print(result)  # 28



# Walrus Operator (:=) — Assign and use value in one line




#======================= PRACTICE ========================

# Write a Python program to find the area and perimeter of a rectangle using arithmetic operators.

# lenght = int(input("Enter the Lenght of the rectangle :"))
# width = int(input("Enter the Width of the rectangle :"))

# area = lenght * width
# perimeter = 2*(lenght + width)

# print ("Area of Rectangle :", area)
# print ("Perimeter of Rectangle :", perimeter)


# Input a number and print its cube using **.

# num = int(input("Enter the number : "))

# cube = (num ** num) *num
# print( " Cube : ", cube)

# Write a program to swap two numbers without using a third variable.

num1 = 10
num2 = 20
temp = num1
num1 = num2
num2 = temp
print( num1 , num2)



# Check if a number is greater than 100.

number = int(input("enter the number :-"))

isGreater = number > 100

print(isGreater)

# Compare two user-entered numbers and print the larger one.

# Take input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Using comparison operators
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num2} is greater than {num1}")
else:
    print("Both numbers are equal")



# Check if a number lies between 10 and 50.
number = int(input("enter the number :"))

if(number > 10 and number <30):
    print(number);
else:
    print("Number are outside ")


