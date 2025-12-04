# Decorators 
""" 
A functions that wrapa another functionn and add extra functionality 
without changing the original functions code 

why we do need decorators?

code reusable 

Dry principle follow 

Logging , authoentications , timing caching, retry logic validations 

esialy add hota h 



"""

# example 

def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("after functuon run ")
    return wrapper


@my_decorator
def say_hello():
    print("hello")

say_hello()


# Functions are first class function

def greet():
    return "hi there"

func_var = greet

print(func_var())

def outer():
    def inner ():
        return " heelo vishal"
    return inner

greet = outer()
print(greet)
print(greet())


# first decorators functions 


def fun():
    print( " finctiom in actions")

def first_decoratots(fucn):
    def deoratoes():
        print("befor function call")
        fucn()
        print("after the fucntion call")
    return deoratoes


# decoratos_fun = first_decoratots(fun)
# decoratos_fun()

@first_decoratots
def new_fun():
    print("this is new fun decorators ")

new_fun()
print(new_fun)


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b , **extra):
    return a + b

print(add(10, 20 , name = " vishal" , age = 23))


import aiohttp
import asyncio

async def fetch(url, session):
    async with session.get(url) as resp:
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as session:
        urls = ["https://google.com" for _ in range(5)]
        tasks = [fetch(url, session) for url in urls]
        results = await asyncio.gather(*tasks)
        print(results)

asyncio.run(main())
