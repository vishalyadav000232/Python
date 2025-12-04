# single thraded programming -
# it runs only one thrade 
# if any blockeble then eontire programm wiat for that complted 
# it is slow

# import time

# def task1():
#     print("task 1 is starts")
#     time.sleep(2)
#     print("end task 1")
# def task2():
#     print("task 2 is starts")
#     time.sleep(2)
#     print("end task 2")

# task1()
# task2()


# multithraded programming 

# import time 
# import threading

# def task(name):
#     print(f"{name}  start")
#     time.sleep(2)
#     print(f"{name}  end")


# t1 = threading.Thread(target=task , args=("task 1",))
# t2 = threading.Thread(target=task , args=("task2",))

# t1.start()
# t2.start()


# t1.join()

# t2.join()


#  Asyncio programming in pythons 


# asyncio is a pythons library to concurrent code using  asyn /await syntax



# it is not multithreding but single threding programming language

# it allow your programm to handle the programm i/o bound efficiently 


# Network Request 
# File Operaations
# Database call
# Api's





# import asyncio

# async def grret():
        
#     print("start the code")
#     await asyncio.sleep(2)
#     print("end the code")

# asyncio.run(grret())


# import asyncio

# async def greet(name, delay):
#     print(f"Hello, {name}")
#     await asyncio.sleep(delay)
#     print(f"Goodbye, {name}")

# async def main():
#     # Run multiple coroutines concurrently
#     await asyncio.gather(
#         greet("Alice", 2),
#         greet("Bob", 1),
#         greet("Charlie", 3)
#     )

# asyncio.run(main())

#
# I/O bound task  with normal 

import time

# def task():
#     time.sleep(2)
#     print("hello")
#     return "donre"

# for _ in range(5):
#     print(task())

    # it take totle time : 10s

#  Fast using async / await. 

import asyncio

async def task():
    print("hello")
    await asyncio.sleep(2)
    return "done"
async def main():
    tasks = [task() for _ in range(5)]
    result = await asyncio.gather(*tasks)
    print(result)
asyncio.run(main())