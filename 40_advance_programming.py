'''

what is the Concurrency 
ans -> dooing the multiple job (tasl) at the same time 
-- Downloading files + showing progress bar
-- Handling many API requests
-- Chat app: message receive + send + notifications



type of the Concurrency 

1-> Concurrency --> task overlap (not aleays the parellel)
2-> Parallelism --> task rin truly at the same time (multicore cpu)
'''


# threading = (best input /output bound)

'''When to use:

✔ Network calls (API requests)
✔ File reading/writing
✔ Web scraping
✔ DB queries

⚠️ In Python, threads don’t speed up CPU-heavy work due to GIL.'''

import threading
import time

'''def task(name):
    print(f"Start {name}")
    time.sleep(2)
    print(f"End {name}")

t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All done")'''


'''
def worker(msg):
    print("start", msg)
    time.sleep(3)
    print("end", msg)

t = threading.Thread(target=worker, args=("hello",), name="vishal")
t.start()

t.join(timeout=2.3)   # main waits only 2.3 seconds

print("Main Finished")

print("current thread")
print(threading.current_thread().name)

print("enumerated thread")
print(threading.enumerate())

print("main thread")
print(threading.main_thread().name)

print("active thread")
print(threading.active_count())
'''
'''
Create and run thread 

threading.Thread(
    group=None,
    target=None,
    name=None,
    args=(),
    kwargs={},
    daemon=None
)

target = function to run in the thread 
arg = tupple of the positional argument 
name = thrad name for the debugging 
daemon = backgroundthrad (true / false)



2) threading.current_thread()
 -- Returns current running thread object.



 3) threading.main_thread()

Returns the main thread object.


4) threading.active_count()

Returns number of alive threads.


5) threading.enumerate()

Returns list of all alive thread objects.

'''
'''

import threading
import time
import random

def download_file(file_name):
    print(f"📥 Download started: {file_name}")
    time.sleep(random.randint(1, 3))  # simulate network delay
    print(f"✅ Download finished: {file_name}")

files = ["a.png", "b.mp4", "c.pdf", "d.zip", "e.jpg"]

threads = []

start_time = time.time()

for f in files:
    t = threading.Thread(target=download_file, args=(f,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end_time = time.time()
print(f"\n🎉 All downloads done in {end_time - start_time:.2f} seconds")

'''
'''

def task(name):

    print(f"[{threading.current_thread().name}] this is the task 1")

    time.sleep(2)
    print(f"[{threading.current_thread().name}] end {name}")


t1 = threading.Thread(target=task, args=("A",), name="Thread-A")
t2 = threading.Thread(target=task, args=("B",), name="Thread-B")

t1.start()
t2.start()

print(f"[{threading.current_thread().name}] join se pahle wala Done")

t1.join()
print(f"[{threading.current_thread().name}] t1 complete ho gaya (A finished)")

t2.join()
print(f"[{threading.current_thread().name}] Done (both finished)")


'''

'''
def worker():
    for i in range(1, 6):
        print(f"[{threading.current_thread().name}] Working... {i} [ is_alive : {t1.is_alive()}]")
        time.sleep(1)


print(f"[{threading.current_thread().name}] Main program started")

t1 = threading.Thread(target=worker, name="Worker-Thread")
t1.start()

# Main thread apna kaam karega parallel me
for j in range(1, 4):
    print(f"[{threading.current_thread().name}] Main doing other work... {j}")
    time.sleep(1)

t1.join()
print(f"[{threading.current_thread().name}] Main program finished [is_LIVE : {t1.is_alive()}]")

'''

'''


Note of the thradin module in python 

Module Purpose : 
threading module Python me multiple tasks ko same program (same process) ke andar run karne ke liye use hota hai.


✅ Best for
I/O-bound tasks (waiting tasks)
network requests
file download/upload
database calls
reading/writing files


❌ Not best for
CPU-bound tasks (heavy calculations)
Because CPython has GIL.


key cpncept -

thrad shared same memory 
thread run concurrently 



Mianthrread --> main thread is the default thread where you program starts 


✅ Concurrency vs Parallelism (Simple)

Concurrency: tasks overlap (looks like running together)
Parallelism: tasks run truly at same time (multi-core)
Threading = mostly concurrency.


thrat LifeCycle 
create -->

t1 = threading.Thread(target = function name , name = thread name , arg , kwrgs)

start -->

t1.start()

wait (OPTIONAL)
t1.join()

main thread wait until the t1  finished 


👉 4) .start() vs .run() (Very Important) 


start() --> create a new thread and run internlly .ryn()

.run()

❌ do not call directly (normally)
Calling .run() runs the function in the same thread, not new thread.

👉  Join (timeOut= flaot)

timeout=None → wait forever
timeout=2 → wait max 2 seconds then run the main tread 


👉 Check thread status 

is_alive()

t1.is_alive() --> retuen true if thread is running 



👉  Thrad naming {for debugging }

t = threading.Thread(target=job, name="Worker-1")
t.start()
print(t.name)


👉  (8) Daemon Threads (Background Threads)
Meaning

Daemon thread runs in background.
If the main program exits, daemon threads are stopped automatically.

👉  Shared data Problem : race condition 


if multiple thrad modify thr same result at the same time --> resut could be the wrong 


Solution : Threadin.Lock

A Lock ensures only one thread at a time enters a critical section.


'''
# import threading
# import time

# def background():
#     while True:
#         print("Running...")
#         time.sleep(.5)

# t = threading.Thread(target=background, daemon=True)
# t.start()

# time.sleep(3)
# print("Main exits now")


# import threading

# count = 0
# lock = threading.Lock()
# def inc():
#     global count
#     for _ in range(100000):
#         with lock:
#             count += 1

# t1 = threading.Thread(target=inc)
# t2 = threading.Thread(target=inc)

# t1.start(); t2.start()
# t1.join(); t2.join()

# print(count)  # may be wrong



# import threading
# import time

# sem = threading.Semaphore(4)

# def task(i):
#     with sem:
#         print("Working:", i)
#         time.sleep(2)

# for i in range(9):
#     threading.Thread(target=task, args=(i,)).start()


from concurrent.futures import ThreadPoolExecutor
import time

def work(x):
    time.sleep(1)
    return x * 2

with ThreadPoolExecutor(max_workers=3) as ex:
    results = list(ex.map(work, [1, 2, 3, 4, 5]))

print(results)
