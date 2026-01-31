'''
Docstring for 39_functional programing


why iterator and generators deos exist 


❓ Problem with normal lists


nums = [x for x in range(1_000_000)]

Python creates 1 million numbers in memory at once.

Python creates 1 million numbers in memory at once.

📌 That is fine for small data.
❌ But for big data (logs, payments, users, file lines), it becomes:

slow

memory heavy

sometimes crashes




✅ Solution: Lazy Evaluation (Generate when needed)

Instead of storing all values, Python gives values one by one only when you ask.

That’s the whole concept of:

✅ Iterators
✅ Generators
'''

# nums = [x for x in range(  1_000_000)]
# print(nums)



# how iteration work internaly 

numss = [12, 21,21,3]

it = iter(numss)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


# print(next(it)) error

nums = [10, 20, 30]
it = iter(nums)

print(list(it))  # [10, 20, 30]
print(list(it))  # []



def make_squares(n):
    for i in range(n):
        yield i*i

g = make_squares(3)
print(g)
print(next(g))
print(next(g))
print(next(g))


total = sum(x*x for x in range(1_000_000))
print(total)




# function decorator 

def my_decorator(fn):
    def wrapper():
        print("Before function")
        fn()
        print("after Function")
    return wrapper


@my_decorator
def hello():
    print("Hello Vishal")

hello()


#  hello  = my_decorator(hello)  internally 



def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper


@log_calls
def adda(a, b , name = "vishal" , age= 1):
    return a + b , name , age

print(adda(2, 5))

# add = log_calls(add)







from functools import wraps
import time

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[LOG] {func.__name__} took {(end-start):.4f}s")
        return result
    return wrapper
@logger
def process():
    for _ in range(10_00000):
        pass

process()





def outer():
    count = 0
    # print(count)
    def inner():
        nonlocal count
        count += 1   # error
        return count
    return inner
d = outer()
print(d())
print(d())
print(d())
print(d())



square = [i*i for i in range(10)]
print(square)
filter_even_num = [i for i in range(21) if i%2 == 0]
print(filter_even_num)
names = ["vishal", "yadav", "python"]
uppercase = [val.upper() for val in names]
print(uppercase)

s = "comprehension"
remove = [ch for ch in s if ch not in ['a','e','i','o','u']]
print(remove)

words = ["apple", "banana", "kiwi", "mango", "pear"]


unique_lengths = {len(word) for word in words}
print(unique_lengths)

cube = {x : x*x*x for x in range(5)}
print(cube)


scores = {"A": 55, "B": 70, "C": 90, "D": 40}
filter_dic = {val : scores[val] for val in scores if scores[val] >=60}
print(filter_dic)


tabel = [[i*i for i in range(4)] for i in range(4)]
print(tabel)


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [x for row in mat for x in row]

print(flatten)


'''
gen = (x*x for x in range(1_000_000))  # lazy evaluation
[expr for outer in outer_iterable for inner in outer if condition]
{key_expr: value_expr for item in iterable if condition}
{expression for item in iterable if condition}
[expression for item in iterable if condition]

'''





# lambda function 

# a lambda function is the small function in python usd for the sort tearm function opration 

'''
syntaxt --

name = labda argument : exprestion 

note -

no def nedded 
return the value automatically 
ofen usrd indide the map sorted , reduce

'''


add = lambda a , b : a+b
print(add(23  ,23))










# Map 


'''
map( function , iterable) apply finction to each element in the iterable abd thr return a map objrct 
'''

nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x*x, nums))
print(squared)  # [1, 4, 9, 16, 25]



# filter(function, iterable) keeps only items where function(item) returns True.
# filter is lazy → memory efficient
# Great for stream processing


nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6]



# functools.reduce(function, iterable, initializer=None) reduces a sequence to a single value by applying function cumulatively.

from functools import reduce
nums = [1, 2, 3, 4, 5, 6]
sum_all = reduce(lambda x , y: x+y , nums , 0)

print(sum_all)