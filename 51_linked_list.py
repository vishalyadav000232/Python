'''

Linked List --> a linked list is a linear data structure where element are store in the node are connnected using pointer refrence 

[Data | Next] → [Data | Next] → [Data | Next] → None


'''


# Linked List Implementation 


class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beagin(self , data):
        
        new_node = Node(data)
        
        new_node.next = self.head
        
        self.head = new_node
        
    def insert_at_end(self , data):
        
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head 
        
        while temp.next:
            temp = temp.next
           
        temp.next =new_node
        
        
    def delete(self , key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        
        
    @property
    def lenght(self):
        count = 0
        temp = self.head
        
        while temp:
            count += 1
            temp = temp.next
        
        return  print(count)
    
        
        
        
        
        
    def display(self):
        temp = self.head
        
        while temp:
            print(temp.data , end="  ->  ")
            temp = temp.next
        print(None)
    

ll = LinkedList()
# ll.insert_at_beagin(10)
# ll.insert_at_beagin(20)
# ll.insert_at_beagin(30)

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.delete(20)
ll.display()
ll.lenght
        
        
        
        
# Doubly linked list 


'''
A Doubly linked list is linked list where each node contains two pointers

prev --> pointer to the previouse  node 
next --> pointer to the next node 


[Prev | Data | Next]

Why Doubly linked list -- >

singly linked list only move forword 
dubly linked list move the both directions 


'''



class Node:
    def __init__(self , data):
        self.prev = None
        self.data =data
        self.next = None
    


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beagin(self , data):
        
        new_node = Node(data)
        
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self , data):
        new_node= Node(data)
        
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head 
        
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        
    def delete(self , key):
        
        temp = self.head 
        
        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next 
                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next
            
    def reverse(self):
        temp = None
        current = self.head
        
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp :
            self.head =temp.prev
            
    
    def display(self):

        temp = self.head

        while temp:
            print(temp.data, end=" ⇄ ")
            temp = temp.next

        print("None")
            
            
dl = DoublyLinkedList()

# dl.insert_at_beagin(10)
# dl.insert_at_beagin(30)



dl.insert_at_end(10)
dl.insert_at_end(20)
dl.insert_at_end(30)
dl.insert_at_end(40)
dl.insert_at_end(50)
dl.insert_at_end(60)
dl.display()
dl.delete(20)
dl.display()
dl.reverse()
dl.display()
        

        
        
        
        