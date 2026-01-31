'''
Docstring for 41_multiprocessing



Multiprocessing 

what is the multiproecessing 

Python’s multiprocessing module allows you to run multiple processes at the same time.

🔥 Why we need it?

Because Python has GIL (Global Interpreter Lock) which prevents true parallel execution of CPU-heavy threads.

So for:
✅ CPU-bound tasks → use multiprocessing
✅ I/O-bound tasks → use threading / async
'''



from multiprocessing import Process

def square(n):
    print(n * n)

if __name__ == "__main__":
    p = Process(target=square, args=(5,))
    p.start()
    p.join()



from multiprocessing import Process

def worker(i):
    print(f"Worker {i} running")

if __name__ == "__main__":
    processes = []

    for i in range(5):
        p = Process(target=worker, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


from multiprocessing import Process, Queue

def producer(q):
    q.put("Hello")
    q.put("World")

def consumer(q):
    print(q.get())
    print(q.get())

if __name__ == "__main__":
    q = Queue()

    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()



from multiprocessing import Process, Pipe

def sender(conn):
    conn.send("Message from sender")
    conn.close()

def receiver(conn):
    print(conn.recv())

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()

    p1 = Process(target=sender, args=(child_conn,))
    p2 = Process(target=receiver, args=(parent_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
