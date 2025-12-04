#  Synchronouse Programming
# -->  it is alsp known as the sequencial and blocking programming 
# it execute task in predeterminant order 
#  Each operations wait for previous oprations to complete 

# Synchronous programing not suitable for the i/o (time consuming task )





# Asynchronous Prgramming runs task independent from each others
#  Enable the concurrent executions and improved the performence 

# Sutaible for I/O bound (time consuming task)

# Advantages 
# concurrency - [allow to multiple task]
# Responsiveness - [keep applictions interfsce responsive]
# Scalability - [easy to scale operations as these are asynchrously ]
# Sutaibilty - it is not good for cpu bound task


# terminology '

# Concuurencey - DEaling with many task at once (Managing multiple task)
# parallelism - Doing multiple task at the same time (Execiting the multilple task)



# Threading --> A process can have one or more threads that share the memory and resources . Suitable for i/o bound activities 


# Multi Processing ->many process with there own memory suitable to achives paralleslism for cpu bound task  


# async Modules 

# import asyncio


# async def greet():
#     print("hello")
#     await asyncio.sleep(2)
#     print("....world")


# asyncio.run(greet())
# asyncio.run(greet())

# multiple

import asyncio
import time

async def greet(name):
    print(f"starting greeting for : {name}")
    await asyncio.sleep(2)
    print(f" hello {name}")

async def main():
    start = time.time()
    await asyncio.gather(greet("anil"), greet("sunil"), greet("vijay") , greet("vishal"))
    elaps_time = time.time() - start
    print(f" totle time : {elaps_time}")
asyncio.run(main())