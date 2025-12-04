# FUNCTION IN PYTHON 

# function is reusable code of block that perform a spacific task 

# def function_name (parameter):
#     # code
#     return value 

# why is the function :

# Avoide the repeted code 
# Oraganize code better
#  Reude Logic 
#  Esier Drbuging 




#  Order of paramter in function 

#  def fun_name (normal , *arg , default , **arg)
# 1. Normal parameter
# 2. Variable positional (*arg)
# 3. Default parameter
# 4. Variable Keyword (**arg)






# BASIC FUNCTION WITH NO PARAMETER 

def greet():
    print("Namaste bhai log");
greet()


#  FUNCTION WITH PARAMETEER 

def sum (a, b):
    sum = a + b
    print( sum );
sum(3 , 4) # 7
sum(2389 , 40304) # 42693

# DEFAULT PARAMETER 

def order ( order = "pani leke avo"):
    print("vishal ji" + " " + order)
order()
order("jahar leke avo")


# KEYWORD ARGUMENT (ONLY IN PYTHON )

def info( name , age):
    print( name , age);
info(name = "vishal" , age = 94)


# VARIABLE LENGHT ARGUMENT 

# def total(*numbers):
#     print(sum(numbers))

# total(1, 2, 3, 4, 5, 5)


def total(*numbers):  # *numbers collect the all argument and convert into the tuple
    return numbers

print(total(1, 2, 3, 4))


# KEYWORD VARIBLE ARGUMENT 

def details(**info): # ** in parameter return the dictionary 
    print(type(info))
    print(info);
details(name = "mangaru" , age = -34 , sex = "male ")


# FUNCTION RETURN MULTIPLE VALUE( ONLY PYTHON)

def state():
    return 203,3934,323;

val  = state() # it return into the tuple
print(val)


# ANONYMOUS FUNCTION (LAMDA FUN)

add = lambda a , b: a+b
print(add(30.,34))


# FINDTION INSIDE FUNCTION (NESTED FN)

def outer (name ):
    def inner():
        print("inner function " + " " + name) 
    inner();

outer("vishal")


# HIGHER ORDER FUNCTION (PASS FUNCTION AS ARGUMENT )


def sqaure (x):
    return x*x;
def aply( fun ,value):
    return fun(value)

print( aply(sqaure , 3))


# RECUIRSION IN PYTHON

def fact(n):
    if n == 1:
        return 1
    return n* fact(n-1)

print(fact(5))


# 🔥  Decorators (ONLY PYTHON — Very powerful in AI/ML)

def log(func):
    def wrapper():
        print("Function is running...")
        func()
    return wrapper

@log # @log is the synthatic sugar 
def hello():
    print("Hello!")

hello()








# ✅ 🔥 40 Practice Questions on Python Functions
# 🔹 Part 1: Basic Functions (1–10)

# Write a function to print “Hello Python”.

def greet():
    print("Hello Python")
greet()

# Write a function that takes a number and returns its square.

def sqaure(num):
    print(num*num);
sqaure(25)

# Write a function that adds two numbers.

add  = lambda a, b: a+b;
print(add(293 , 93))

# Write a function to check if a number is even or odd.

def isEven(num):
    if(num % 2 == 0):
        print("number is even ");
isEven(378)

# Write a function to return the maximum of two numbers (without using max()).

def max(a , b):
    if(a > b):
        return a
    else:
        return b
print(max(93 ,340))

# Write a function to calculate simple interest.

def si( ammount , rate  , year):
    simple_intrest = (ammount * rate *year)/100
    print(simple_intrest)

si(7823,32,238)

# Write a function that takes a list and prints all elements.

def shoealist (list):
    for el in list:
        print(el)
   
fruits = [ "apple ","banana", "grapes"]
shoealist(fruits)



# Write a function to find the sum of a list.
def sumOfList(list):
    sum = 0
    for i in list:
        sum += i

    print(sum)

# sumOfList(fruits)
sumOfList([3.3,234,234,54,2,2,34,])

# Write a function that counts the number of vowels in a string.

def countVovels(str):
    count = 0
    for ch in str:
        ch = ch.lower()
        if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
            count += 1
    print( count)
countVovels("vishal")


#  other way ()

def otherWayToCountVowels(s):
    vowels = "aeiou"
    count = 0
    for c in s.lower():
        if c in vowels:
            count += 1;
    print(count)
otherWayToCountVowels("aecou")


# Write a function that converts Celsius to Fahrenheit.

def celciusToFarenite(celc):
    far = ((celc * 9)/5) + 32

    print( far)
celciusToFarenite(36)


# 🔹 Part 2: Default Arguments (11–15)

# Create a function greet(name="Guest").

def greet (name ="guest"):
    print("Welvcome to my world" , name ," dost ")

greet()
greet("jhatu")

# Create a function power(num, exp=2) → returns number raised to exponent.

def poewr( num , exp = 2):
    print( num ** exp)
poewr(2)
poewr(3,3)

# Create a function to calculate area of a rectangle with default width = 10.

def areaOfRectangle( height , width = 10):
    area = height * width
    print( area)
areaOfRectangle(23)

# Create a function to return the full name with middle name default empty.

def full_name(first, last, middle=""):
    if middle:                      # middle name given?
        return f"{first} {middle} {last}"
    return f"{first} {last}"

result = full_name("vishal", "yadav")
result2 = full_name("vishal","yadav", "kumar")
print(result)
print(result2)



# Create a function with default discount = 10% and return final price.

def getDiscount( ammount  , diss = 10):
    dis_value = ammount * diss / 100
    print(dis_value)
getDiscount(1002 , 50)

# 🔹 Part 3: *args (16–20)

# Write a function using *args to return the sum of all numbers.

def sumOfAllNumber(*numbers):
    sum = 0
    for val in numbers:
        sum += val
    print(sum)

sumOfAllNumber(1,3,4,5,6,5,557)

# Write a function using *args to return the maximum value.
def maxValue(*n):
    max = 0
    for i in n:
        if max < i:
            max = i
    print(max)        

maxValue(2,23,23,14,24,453)

# Write a function that accepts multiple strings and prints their length.

def lenghtOfString(*str):
    for s in str:
        print(f"{s} : {len(s)}")


lenghtOfString("india" ,"china" , "Norht America")

# Write a function that multiplies all given numbers using *args.

def multiplyAllNumber(*m):
    mul = 1
    for i in m:
        mul *= i
    print( mul)


multiplyAllNumber(3 ,3,4)

# Write a function to count how many arguments were passed using *args.

def num_of_arg(*arg):
    print(len(arg))

num_of_arg(1,3,4,5,67,)


# 🔹 Part 4: **kwargs (21–25)

# Write a function that prints all key–value pairs using **kwargs.

def all_kay_value(**val):
    print(val)
nam = "mangaru"
umar = 34
isAdmi = True
all_kay_value(name = "vishal" , age = 33 ,isTrue = False)

# all_kay_value(nam , umar , isAdmi) # ❌ we can't pass the as only  varible in kwyWords argumnet 




# Write a function that takes student details using kwargs and returns them as a dictionary.

# Write a function that prints salary details: basic, hra, ta using kwargs.

# Write a function to check if a specific key exists inside kwargs.

# 🔹 Part 5: Return & Nested Functions (26–30)

# Write a function that returns multiple values: sum & product.
def sum_product(a, b):
    s = a + b
    p = a * b
    return s, p



# Write a nested function: outer() → inner() → print “Inner called”.

def outer ():
    def inner():
        print( "this is the inner fuc")
    inner()

outer()
# Write a nested function that calculates square using inner function.

def outer_square(n):
    def inner(x):
        return x * x
    return inner(n)

sqaures = outer_square(3)
print(sqaures)


# Write a function that returns another function.

def greet():
    def hello():
        return "Hello!"
    return hello

msg = greet()
print(msg())

# Create a function calculator() that returns 4 functions: add, sub, mul, div.
def calculator():
    def add(a, b):
        return a + b
    
    def sub(a, b):
        return a - b
    
    def mul(a, b):
        return a * b
    
    def div(a, b):
        return a / b
    
    return add, sub, mul, div

add , sub , mul , div = calculator()

print(add(34,45))
print(sub(34,45))
print(mul(34,45))
print(div(34,45))


# 🔹 Part 6: Lambda Functions (31–35)

# Lambda to add two numbers.

sum = lambda a , b : a + b;
print(sum(2323,23))

# Lambda to find max of two numbers.

max = lambda a , b : a if a > b else b
print(max(23,234))

# Lambda to check even/odd.

isEvens = lambda  n : "even" if n%2==0 else 'odd'
print(isEvens(35))

# Lambda to reverse a string.

revers = lambda str : str[::-1]
print(revers("hello"))

# Lambda to get last digit of a number.

last_digit = lambda n: n % 10
print(last_digit(83720))

# 🔹 Part 7: Higher Order Functions (36–38)

# Write a function that takes another function and a value, then applies it.

def apply_func(func, value):
    return func(value)
def square(x):
    return x * x

result = apply_func(square, 5)
print(result)


# Write a function that filters even numbers using a function parameter.

def filter_number(numbers , base):
    return [n for n in numbers if base(n)]

def evnen(n):
    return n%2==0
def odd(n):
    return n % 2 != 0


numbers = (2.3,3,35,35,4,3,5,8)
print( filter_number(numbers , evnen))
print( filter_number(numbers , odd))


# Write a function that maps square on a list using a function argument.

def map_numbers(numbers, func):
    return [func(n) for n in numbers]
def square(n):
    return n * n
nums = [1, 2, 3, 4]
squares = map_numbers(nums, square)
print(squares)

#  using the lambda function 

squares = map_numbers(nums, lambda x: x*x)
print(squares)



# 🔹 Part 8: Recursion (39–40)

# Write a recursive function to find factorial.

def fact (n):
    if n == 1 :
        return 1
    return n * fact( n-1)

print(fact(5))

# Write a recursive function to find sum of digits of a number.
def sum_of_all_dig(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_all_dig(n//10)
print(sum_of_all_dig(2623198214))



