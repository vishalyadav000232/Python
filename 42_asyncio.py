'''
Asyncio. 

asynio is the python built in library 
it is used run programm con-currently 
event loop 
task 
coroutin
i/o asyn

📌 Best for:
✅ I/O-bound work (network calls, API, DB, file, sleep, web scraping)
❌ Not best for CPU-heavy tasks (use multiprocessing)



'''


# Core Concept of the asyncio


# 👉(A) Coroutin (async def)
import asyncio

# async def hello():
#     print("this is the corotuin fn")

# fn = hello()
# print(fn) #<coroutine object hello at 0x102e12740> 

# calling corotin does not run immediately 
# you must run it using event loop 


# 👉 await 

''' 
pauses here the corotuin , let other task run , resume when ready 

asyncio.sleep() is non-blocking sleep.
'''

# async def task(n):
#     print(f"start task {n}")
#     await asyncio.sleep(2)
#     print(f"end task {n}")


# 👉 Running an asyncio program 


# async def main(n):
#     print(f"start task {n}")
#     await asyncio.sleep(2)
#     print(f"end task {n}")


# asyncio.run(main(1))


# 👉  Concurrency with asyncio.gather()


#  without concurrency 



# async def task(name):
#     print("start", name)
#     await asyncio.sleep(2)
#     print("end", name)

# async def main():
#     await task("A")
#     await task("B")

# asyncio.run(main())


#  with concurrency 



# async def task(name):
#     print("start", name)
#     await asyncio.sleep(2)
#     print("end", name)

# async def main():
#     await asyncio.gather(
#         task("A"),
#         task("B")
#     )

# asyncio.run(main())



# 👉  Task (asyncio.create_task())




async def task(name):
    print("start", name)
    await asyncio.sleep(2)
    print("end", name)

async def main():
    t1 = asyncio.create_task(task("A"))
    t2 = asyncio.create_task(task("B"))

    print("tasks created")

    await t1
    await t2

asyncio.run(main())


#  👉 Event loop --> asyncio works because of the event loop.

'''
“One thread + one loop + many tasks”

runs tasks
pauses tasks on await
resumes them when ready

'''
