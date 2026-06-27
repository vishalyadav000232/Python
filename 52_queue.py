'''

Stack in python ---> 

stack is a linear data structure that follow the LIFP (last in first out )


Core Operations
 
Operation	Meaning
push()	--> add element
pop()	--> remove top element
peek() / top() --> 	see top element
isEmpty()	 --> check empty



'''


# Stack implementaiion usig rhe list {connon }



stack = []


# push
stack.append(10)
stack.append(20)
stack.append(30)

# pop
stack.pop()

# peek
print(stack[0])



# Methos using the class (interview style )


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)
            
            
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print(s.pop())
print(s.peek())