'''
Queue --> it is linear datastructue that follows the FIFO (firrst in first out )


Operation	--> Meaning
enqueue()	--> add element (rear)
dequeue()	---> remove element (front)
peek()	    --> front element
isEmpty()	---> check empty



'''


# pyhon implemetation using list (common method )

queue = []

queue.append(10)   # enqueue
queue.append(20)

queue.pop(0)       # dequeue ❌ O(n)

print(queue)


#  using collection.queue 


from collections import deque


q = deque()
print(q)
q.append(10)
q.append(20)
q.append(30)
q.append(40)

q.popleft()
print(q[0])
print(  q)


# ===============================================================
# methos 3 using class 
# ===============================================================


class Queue:
    
    def __init__(self):
        self.queue = []
        
        
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return "Empty"
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0
    
    
qu = Queue()
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
qu.enqueue(50)
qu.dequeue()
print(qu.queue)



#  Using the linked list 



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):

        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):

        if self.front is None:
            return "Empty"

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return temp.data