# '''
# Docstring for 41_multiprocessing



# Multiprocessing 

# what is the multiproecessing 

# Python’s multiprocessing module allows you to run multiple processes at the same time.

# 🔥 Why we need it?

# Because Python has GIL (Global Interpreter Lock) which prevents true parallel execution of CPU-heavy threads.

# So for:
# ✅ CPU-bound tasks → use multiprocessing
# ✅ I/O-bound tasks → use threading / async
# '''



# from multiprocessing import Process

# # def square(n):
# #     print(n * n)

# # if __name__ == "__main__":
# #     p = Process(target=square, args=(5,))
# #     p.start()
# #     p.join()



# # from multiprocessing import Process

# # def worker(i):
# #     print(f"Worker {i} running")

# # if __name__ == "__main__":
# #     processes = []

# #     for i in range(5):
# #         p = Process(target=worker, args=(i,))
# #         p.start()
# #         processes.append(p)

# #     for p in processes:
# #         p.join()


# # from multiprocessing import Process, Queue

# # def producer(q):
# #     q.put("Hello")
# #     q.put("World")

# # def consumer(q):
# #     print(q.get())
# #     print(q.get())

# # if __name__ == "__main__":
# #     q = Queue()

# #     p1 = Process(target=producer, args=(q,))
# #     p2 = Process(target=consumer, args=(q,))

# #     p1.start()
# #     p2.start()

# #     p1.join()
# #     p2.join()



# # from multiprocessing import Process, Pipe

# # def sender(conn):
# #     conn.send("Message from sender")
# #     conn.close()

# # def receiver(conn):
# #     print(conn.recv())

# # if __name__ == "__main__":
# #     parent_conn, child_conn = Pipe()

# #     p1 = Process(target=sender, args=(child_conn,))
# #     p2 = Process(target=receiver, args=(parent_conn,))

# #     p1.start()
# #     p2.start()

# #     p1.join()
# #     p2.join()




# # def task():
# #     print("this is new procewsss")
    
# # if __name__ =="__main__":
# #     ps = Process(target=task)
# #     ps.start()
# #     ps.join()

# # def taskq(n):
# #     print("this is new procewsss" , n)
    
# # if __name__ =="__main__":
# #     processs = []
# #     for i  in range(5):
# #         ps = Process(target=taskq , args=(i,))
# #         processs.append(ps)
# #         ps.start()
# #     for ps in processs:
# #         ps.join()
        
        
# # import multiprocessing

# # def square(n):
# #     print(n*n)

# # if __name__ == "__main__":
# #     processes = []

# #     for i in range(5):
# #         p = multiprocessing.Process(target=square, args=(i,))
# #         processes.append(p)
# #         p.start()

# #     for p in processes:
# #         p.join()
        
        
        
# #  Instea
# # d of the manually create a process we use the poo

# import multiprocessing


# def square(n):
#     print(f"this is the process number {n} and there squre {n*n}")


# if __name__ == "__main__":
#     list = [1,2,3,4,5]
#     with multiprocessing.Pool(4) as p:
#         p.map(square , list )
    
    
    
#     from multiprocessing import Process, Queue

# def worker(q):
#     q.put("Hello")

# if __name__ == "__main__":
#     q = Queue()
#     p = Process(target=worker, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()
    
    
# from multiprocessing import Process, Queue

# def producer(q):
#     for i in range(5):
#         q.put(i)

# def consumer(q):
#     while not q.empty():
#         print(q.get())

# if __name__ == "__main__":
#     q = Queue()
#     p1 = Process(target=producer, args=(q,))
#     p2 = Process(target=consumer, args=(q,))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()
    
# from multiprocessing import Process, Value

# def increment(num):
#     for _ in range(1000):
#         num.value += 1

# if __name__ == "__main__":
#     num = Value('i', 0)

#     p1 = Process(target=increment, args=(num,))
#     p2 = Process(target=increment, args=(num,))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print(num.value)  # wrong result
    
    
#     from multiprocessing import Lock
# from multiprocessing import Lock
# lock = Lock()

# def increment(num):
#     for _ in range(1000):
#         with lock:
#             num.value += 1


# from multiprocessing import Process, Semaphore
# import time

# def task(sem, name):
#     print(f"{name} waiting")
    
#     with sem:
#         print(f"{name} entered")
#         time.sleep(2)
#         print(f"{name} leaving")

# if __name__ == "__main__":
#     sem = Semaphore(2)

#     processes = []

#     for i in range(5):
#         p = Process(target=task, args=(sem, f"P{i}",))
#         p.start()
#         processes.append(p)

  
#     for p in processes:
#         p.join()
        
        
# from multiprocessing import Process
# import os

# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())

# def f(name):
#     info('function f')
#     print('hello', name)

# if __name__ == '__main__':
#     info('main line')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()
    
    
# from multiprocessing import Process, Lock

# def f(l, i):
#     l.acquire()
#     try:
#         print('hello world', i)
#     finally:
#         l.release()

# if __name__ == '__main__':
#     lock = Lock()
    
#     ps = []

#     for num in range(10):
#         p = Process(target=f, args=(lock, num))  # ✅ create process
#         p.start()                                # ✅ start it
#         ps.append(p)                             # ✅ store object
        
#     for p in ps:
#         p.join()                                 # ✅ wait properly




# from multiprocessing import Process , Lock , Value , Queue
# import time



# # def task():
# #     print("child process start")
# #     time.sleep(2)
# #     print("child doone")
    
# # if __name__ == "__main__":
# #     ps = Process(target=task)
    
# #     ps.start()
# #     print(ps.is_alive())
# #     ps.join()
# #     print(ps.is_alive())
    
# #     print("main process done")
    
    
# #  WITH LOCK

# def increment(lock , counter ):
    
#     for _ in range(100000):
#         lock.acquire()
#         counter.value += 1
#         lock.release()

# if __name__ == "__main__":
#     lock = Lock()
#     counter = Value("i", 0)
    
    
#     p1 = Process(target=increment ,args=(lock, counter))
#     p2 = Process(target=increment, args=(lock, counter))
    
#     p1.start()
#     p2.start()
    
#     p1.join()
#     p2.join()
    
    
#     print(counter.value)
    
#     #  Without lock 

# def increments(counter):
#     for _ in range(100000):
#         counter.value += 1   # ❌ race condition

# if __name__ == "__main__":
#     counter = Value('i', 0)
    
#     p1 = Process(target=increments, args=(counter,))
#     p2 = Process(target=increments, args=(counter,))
    
#     p1.start()
#     p2.start()
    
#     p1.join()
#     p2.join()
    
#     print(counter.value)
    
    
# # Use inerna Lock of the value (Best without manual lock)



# def incre(counter):
#     for _ in range(10000):
        
#         with counter.get_lock():
#             counter.value += 1


# if __name__ == "__main__":
#     counter = Value("i", 0)
    
#     p1 = Process(target=incre , args=(counter ,))
#     p2 = Process(target=incre , args=(counter ,))
    
#     p1.start()
#     p2.start()
    
    
#     p1.join()
#     p2.join()
    
#     print(counter.value)
    

# def incres(q):
#     local_counter = 0
#     for _ in range(100000):
#         local_counter += 1
#     q.put(local_counter)
    


# if __name__ == "__main+__":
#     q = Queue()
    
    
#     p1 = Process(target=incres , args=(q ,))
#     p2 = Process(target=incres , args=(q ,))
    
#     p1.start()
#     p2.start()
    
    
#     p1.join()
#     p2.join()
    
    
#     total = q.get() + q.get()
#     print(total)
    
    
# # Manager ---> when need to share dict and list acrosss the proccess 



# from multiprocessing import Manager


# def worker(d , key , value):
#     d[key] = value
    
# if __name__ == "__main__":
#     with Manager() as manager:
#         shared_dict = manager.dict()
#         p1 = Process(target=worker, args=(shared_dict, "a", 1))
#         p2 = Process(target=worker, args=(shared_dict, "b", 2))

#         p1.start()
#         p2.start()

#         p1.join()
#         p2.join()

#         print(shared_dict)
        
    
# # Pipe 

# from multiprocessing import Pipe

# def worker2(conn):
#     conn.send("hello this is the messge through the pipe1")
#     conn.send("hello this is the messge through the pipe2")
#     conn.close()
    
    
# if __name__ == "__main__":
#     parent, child = Pipe()

#     p = Process(target=worker2, args=(child,))
#     p.start()

#     print(parent.recv())
#     print(parent.recv())
#     p.join()

# from multiprocessing import Process, RLock

# def outer(lock):
#     lock.acquire()
#     print("Outer acquired lock")
    
#     inner(lock)
    
#     print("Outer releasing lock")
#     lock.release()

# def inner(lock):
#     lock.acquire()
#     print("Inner acquired lock")
    
#     print("Inner releasing lock")
#     lock.release()

# if __name__ == "__main__":
#     r = RLock()
    
#     p1 = Process(target=outer, args=(r,))
#     p2 = Process(target=inner, args=(r,))
    
#     p1.start()
#     p2.start()
    
#     p1.join()
#     p2.join()
    


# from multiprocessing import Semaphore, Process
# import time

#   # Only 2 processes allowed

# def task(sem , i):
#     sem.acquire()
#     print(f"Process {i} entered")
#     time.sleep(2)
#     print(f"Process {i} leaving")
#     sem.release()

# if __name__ == "__main__":
#     sem = Semaphore(2)
#     pro = []
#     for i in range(5):
#         p = Process(target=task, args=(sem,i,))
#         p.start()
#         pro.append(p)
    
    
    
#     for p in pro:
#         p.join()
        
        
        
        
        
        
# import random      
# # Best Booking system 

# def book_ticket(sem , user_id):
    
#     print(f"User with {user_id} trying to booking....")
    
#     aquire = sem.acquire(timeout=3)
    
    
#     if aquire:
#         print(f"✅ User {user_id} booked a seat")
#         time.sleep(random.randint(1, 3)) 
        
#         print(f"🎫 User {user_id} completed booking")
                
#     else:
#         print(f"❌ User {user_id} failed (No seats available)")
    

# if __name__ == "__main__":
#     seats = 3
#     sem = Semaphore(seats)

#     processes = []

#     for i in range(6):  # 6 users, only 3 seats
#         p = Process(target=book_ticket, args=(sem, i))
#         p.start()
#         processes.append(p)

#     for p in processes:
#         p.join()


# from multiprocessing import Process , Lock , Value


# def debited(balance , lock):
    
#     lock.acquire()
#     balance.value -= 100
#     lock.release()


# if __name__ == "__main__":
    
#     balance = Value("i" , 1000)
#     lock = Lock()
    
#     p1 = Process(target=debited , args=(balance , lock))
#     p2 = Process(target=debited , args=(balance , lock))
#     p3 = Process(target=debited , args=(balance , lock))
#     p4 = Process(target=debited , args=(balance , lock))
    
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
    
#     p1.join()
#     p2.join()
    
    
    
#     print(balance.value)
    
# from multiprocessing import Event  
# import time
    

# def payment(event):
#     print(f"💳 Payment processing started...")
#     time.sleep(3)
#     print(" ✅ paymenr successfully")
#     event.set()


# def prepare_order(event):
#     print("👨‍🍳 Waiting for payment...")
#     event.wait()   # WAIT until payment is done
#     print("🍔 Order preparation started!")
#     time.sleep(2)
#     print("✅ Order ready!")
# if __name__ == "__main__":
    
#     event = Event()
    
#     p1 = Process(target=payment, args=(event,))
#     p2 = Process(target=prepare_order, args=(event,))
    
#     p1.start()
#     p2.start()
    
#     p1.join()
#     p2.join()



# from multiprocessing import Process, Event
# import time

# def build(build_done):
#     print("🔨 Build started...")
#     time.sleep(3)
    
#     print("✅ Build completed")
#     build_done.set()   # signal next stage


# def test(build_done, test_done):
#     print("🧪 Waiting for build...")
    
#     build_done.wait()   # wait for build
    
#     print("🧪 Testing started...")
#     time.sleep(2)
    
#     print("✅ Testing completed")
#     test_done.set()


# def deploy(test_done):
#     print("🚀 Waiting for tests...")
    
#     test_done.wait()
    
#     print("🚀 Deployment started...")
#     time.sleep(2)
    
#     print("✅ Deployment successful!")


# if __name__ == "__main__":
    
#     build_done = Event()
#     test_done = Event()
    
#     p1 = Process(target=build, args=(build_done,))
#     p2 = Process(target=test, args=(build_done, test_done))
#     p3 = Process(target=deploy, args=(test_done,))
    
#     p1.start()
#     p2.start()
#     p3.start()
    
#     p1.join()
#     p2.join()
#     p3.join()



# from multiprocessing import Process, Condition
# import time
# import random

# def chef(cond, orders):
#     for i in range(5):
#         time.sleep(random.randint(1, 3))
        
#         with cond:
#             orders.append(f"Order {i}")
#             print(f"👨‍🍳 Prepared {i}")
            
#             cond.notify()


# def delivery(cond, orders):
#     for _ in range(5):
#         with cond:
#             while not orders:
#                 print("🛵 Waiting for order...")
#                 cond.wait()
            
#             order = orders.pop(0)
#             print(f"🛵 Delivered {order}")


# if __name__ == "__main__":
#     cond = Condition()
#     orders = []

#     p1 = Process(target=chef, args=(cond, orders))
#     p2 = Process(target=delivery, args=(cond, orders))

#     p1.start()
#     p2.start()

# #     p1.join()
# #     p2.join()



# from multiprocessing import Process, Condition
# import time
# import random

# MAX_SIZE = 3

# def producer(cond, buffer):
#     for i in range(10):
#         time.sleep(random.randint(1, 2))
        
#         with cond:
#             while len(buffer) == MAX_SIZE:
#                 print("⛔ Buffer full, producer waiting...")
#                 cond.wait()
            
#             buffer.append(i)
#             print(f"📦 Produced {i}")
            
#             cond.notify_all()


# def consumer(cond, buffer):
#     for _ in range(10):
#         with cond:
#             while not buffer:
#                 print("❌ Buffer empty, consumer waiting...")
#                 cond.wait()
            
#             item = buffer.pop(0)
#             print(f"📤 Consumed {item}")
            
#             cond.notify_all()


# if __name__ == "__main__":
#     cond = Condition()
#     buffer = []

#     p1 = Process(target=producer, args=(cond, buffer))
#     p2 = Process(target=consumer, args=(cond, buffer))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()




from multiprocessing import Process, Condition , Queue
import time

# buffer = []
# MAX_SIZE = 2

# condition = Condition()

# # 🔹 Producer
# def producer():
#     for i in range(5):
#         condition.acquire()

#         while len(buffer) == MAX_SIZE:
#             print("Buffer full, producer waiting...")
#             condition.wait()

#         buffer.append(i)
#         print(f"Produced: {i}")

#         condition.notify()
#         condition.release()

#         time.sleep(1)


# # 🔹 Consumer
# def consumer():
#     for i in range(5):
#         condition.acquire()

#         while len(buffer) == 0:
#             print("Buffer empty, consumer waiting...")
#             condition.wait()

#         item = buffer.pop(0)
#         print(f"Consumed: {item}")

#         condition.notify()
#         condition.release()

#         time.sleep(2)


# if __name__ == "__main__":
#     p1 = Process(target=producer)
#     p2 = Process(target=consumer)

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()
    
    
    
    
def dukandar(store):
    for i in range(5):
        value =  f' value {i}'
        store.put(value)

def coustmer(store):
    for i in range(5):
        item = store.get()
        print("Consumed:", item)


if __name__ == "__main__":
    
    store = Queue()
    p1 = Process(target=dukandar , args=(store,))
    p2 = Process(target=coustmer , args=(store,))
    
    p1.start()
    p2.start()
    
    
    p1.join()
    p2.join()