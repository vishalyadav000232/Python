import time
import asyncio


# 🟢 LEVEL 1 — Core Async/await Basics (10 Questions)

# Goal: Understand coroutines, event loop, await rules.

# 1️⃣ Write an async function that waits 1 second and returns "Task Done".


async def task():
    await asyncio.sleep(1)
    return "task Done"

print(asyncio.run(task()))

# 2️⃣ Create three async functions and run them using asyncio.gather().

async def task(i):
    await asyncio.sleep(1)
    return f"task Done {i}"

async def main():
    result = await asyncio.gather(
        task(1),
        task(2),
        task(3)
        )
    return result

print(asyncio.run(main()))



# 3️⃣ Create the same three functions and run them using asyncio.create_task() and await them manually.


async def task(i):
    await asyncio.sleep(1)
    return f"task Done {i}"

async def main():
    t1 = await asyncio.create_task(task(1))
    t2 = await asyncio.create_task(task(2))
    t3 = await asyncio.create_task(task(3))

    return [t1,t2,t3]
   
    

print(asyncio.run(main()))



# 4️⃣ Create a synchronous function + async function.
# Try calling async function without await. Observe the error.

def syn_fun():
    print(" i am a synchronouse function ..")

async def async_fun():
    print(" I am async functions ")
    await asyncio.sleep(2)
    return "async is done "

def main():
    syn_fun()

    result =  async_fun() # calling async function  withous await 

    print( result) # peint coroutin object instead of the result 


main()
# 5️⃣ Write an async program that prints numbers 1–5 with a delay of 1 second, but total time should be 1 second using gather.

async def print_num(i):
    print(f"currnt task ")
    await asyncio.sleep(1)
    print(i)

async def main():
    task = [print_num(i) for i in range(1,6)]

    await asyncio.gather(*task)


asyncio.run(main())

# 6️⃣ Write two tasks:

# One prints time every second

# One prints “work done” after 3 sec
# Run them simultaneously.


#  Task one 

async def print_time():
    for _ in range(5):
        print(f"Current Time : {time.strftime("%H:%M:%S")}")
        await asyncio.sleep(1)

async def work_done():
    for _ in range(6):
         
        await asyncio.sleep(2)
        print("Work Done ")
   


async def main():
    await asyncio.gather(
        print_time(),
        work_done()
    )

asyncio.run(main())
print("End Question no . 6")
# 7️⃣ Write a function to measure time taken by synchronous vs async code.
def hello ():
    for _ in range (7):
        print("this is synchronus fn")

async def greet(name):
    print(f"starting greeting for : {name}")
    await asyncio.sleep(2)
    print(f" hello {name}")

async def main():
    starts = time.time()
    hello()
    els_time = time.time()- starts
    print(f" totle time : {els_time}")

    start = time.time()
    await asyncio.gather(greet("anil"), greet("sunil"), greet("vijay") , greet("vishal"))
    elaps_time = time.time() - start
    print(f" totle time : {elaps_time}")
asyncio.run(main())

# 8️⃣ Write a simple coroutine chain:
# main() → taskA() → taskB() → result.



# 9️⃣ Write a program that starts a task and continues doing other work without blocking.

# 🔟 Write an async timer that counts down from 10 to 1.

# 🟡 LEVEL 2 — Intermediate (Tasks, gather, wait) (10 Questions)

# Goal: Learn scheduling, cancelling, waiting, switching.

# 1️⃣ Create 5 async tasks that sleep for different times (like 1,2,3,4,5).
# Print them in order they finish using asyncio.wait(return_when=FIRST_COMPLETED).

# 2️⃣ Create a task and cancel it after 1 second. Catch asyncio.CancelledError.

# 3️⃣ Run 20 tasks with .create_task() and return results using gather.

# 4️⃣ Write an async version of this synchronous code:

# for i in range(10):
#     time.sleep(1)
#     print(i)


# It should run in 1 second.

# 5️⃣ Write two tasks:

# One CPU-like task (fake using loop)

# One I/O task (async sleep)
# Observe event loop scheduling.

# 6️⃣ Create a progress bar using async tasks.

# 7️⃣ Use asyncio.shield() to protect a task from cancelation.

# 8️⃣ Implement timeout using asyncio.wait_for().

# 9️⃣ Create a producer/consumer scenario using asyncio.Queue.

# 🔟 Implement rate-limiting using async sleep (e.g., max 5 tasks/sec).

# 🔵 LEVEL 3 — Networking & aiohttp (15 Questions)

# Goal: Real web scraping, API batching, concurrency control.

# 1️⃣ Use aiohttp to fetch HTML from 1 URL.

# 2️⃣ Fetch 5 URLs concurrently.

# 3️⃣ Read URLs from a list file and fetch them async.

# 4️⃣ Write an async web scraper to extract <title> from 10 websites.

# 5️⃣ Send 50 API requests and return the fastest 5 results using wait(FIRST_COMPLETED).

# 6️⃣ Handle HTTP errors with try/except in aiohttp.

# 7️⃣ Implement retries (3 times) for failed requests.

# 8️⃣ Limit concurrency to max 5 requests at a time (use asyncio.Semaphore).

# 9️⃣ Download 10 images using aiohttp and save them locally (aiofiles).

# 🔟 Measure time difference:
# requests (sync) vs aiohttp (async) for 20 URLs.

# 1️⃣1️⃣ Make a JSON API call (GET) to a public API and parse response.

# 1️⃣2️⃣ Write a async function to post JSON data to a dummy API.

# 1️⃣3️⃣ Create a batch scraper: 500+ URLs loaded from file.

# 1️⃣4️⃣ Use aiohttp.ClientSession() efficiently with context manager.

# 1️⃣5️⃣ Build a function that checks the status of 100 websites (ping style).

# 🟣 LEVEL 4 — Async File Handling (10 Questions)

# Goal: Use aiofiles, async iterators.

# 1️⃣ Write to a file asynchronously using aiofiles.

# 2️⃣ Read a file asynchronously.

# 3️⃣ Append lines asynchronously.

# 4️⃣ Read a large file using async iterator:

# async for line in f:


# 5️⃣ Compare performance of sync vs async file writes.

# 6️⃣ Copy file contents asynchronously.

# 7️⃣ Download 5 URLs concurrently and save content using aiofiles.

# 8️⃣ Read JSON file asynchronously and parse it.

# 9️⃣ Watch a log file (simulate tail -f) using async sleeps.

# 🔟 Async read 100 files using gather.

# 🔴 LEVEL 5 — Real-World Mini Projects (10 Projects)

# Goal: Build real applications.

# PROJECT 1 — Async Web Scraper

# Scrape titles of 100 pages using aiohttp + gather + semaphore.

# PROJECT 2 — Website Status Checker

# Check availability of 200 domains using aiohttp.

# PROJECT 3 — Async Bulk File Downloader

# Download 50 files concurrently.

# PROJECT 4 — Async Weather Collector

# Fetch weather from 20 cities concurrently (OpenWeather API).

# PROJECT 5 — Async Database Reader

# Use async SQLite operations (via aiosqlite).

# PROJECT 6 — Realtime Crypto Price Tracker

# Fetch BTC/ETH price every 1 sec using async tasks.

# PROJECT 7 — Async Chat Server

# Using:

# asyncio streams

# background tasks

# broadcast events

# PROJECT 8 — Async Rate-Limited Scraper

# Only 10 requests per second.

# PROJECT 9 — Async Logging System

# Multiple tasks writing logs simultaneously (aiofiles).

# PROJECT 10 — Mini FastAPI App

# Create async endpoints:

# GET /users

# POST /users

# GET /weather

# Compare:

# sync endpoint speed
# vs

# async endpoint speed