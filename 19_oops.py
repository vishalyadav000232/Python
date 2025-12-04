# Python Oops --> Object Oriented Programmings

# Classes and Object 

# clas className:
#   def __init__(self , attributr1  attribute2 ):
#       self.attribute1 = attribute1
#       self.attribute2 = attribute2
#   def method(self):
#       retutn f"my attributes are {self.attrinue1} and {self.attributes2}""


# example 

#  pass means empty body 


# What is the self
#  refers the current object 
# always the first parameter in the method 
# helps access the object variable 
# Constructer must be contain one parameter that is denote a Object 



# Instance Varaible 

# each object gets its own copy 


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"
    
    def dictionary(self):
        return {"name": self.name, "age": self.age}
    
p1 = Person("Vishal", 39)
p2 = Person("Rohit", 43)
print(p1.greet())
print(p1.dictionary())
print(p2.greet())
print(p2.dictionary())


# Anothor Exanple 

class Dog:
    def __init__(this , name):
        this.name = name
    
    def bark(this):
    
        print(this.name  + ""  +" " "is barking ....")


d1 = Dog("sheru")
d2 = Dog("toni")
d3 = Dog("monti")

print(type(d1))

print(d1.bark())
print(d2.bark())
print(d3.bark())


# Inheritence 


#  A child class can use and overide properties of a parnent class
#  Used to reuse code and create powerful hierarchies.


# syntax 

# class Parent:
#     pass

# class Child(Parent):
#     pass


# class Animal:
#     def sound(self):
#         return "some sound "
    
# class Dog(Animal):
#     def sound(self):
#         return "bark"
    
# d = Dog()
# print(d.sound())


# Method OVERIDING 
# 
#  

class Parent:
    def show(self):
        print("i am a parent")
    def hide(self):
        print("i am a hide method in the parent ")

class Child(Parent):
    def show(self):
        print("childe ka shoe function hu")


obj = Child()
print(obj.show())
print(obj.hide())
obj1 = Parent()
print(obj1.show())


class Parent:
    def feature1(self):
        print("Feature 1")

class Child(Parent):
    def feature2(self):
        print("Feature 2")

c = Child()
c1 = Parent()
c.feature1()
c.feature2()



# Super()

# Parnt method ko call karne ke liye 

class Parent:
    def show(self):
        print("this is the parent")

class Child(Parent):
    def show(self):
        super().show()
        print("child ka method ")

child = Child()
child.show()


# Constructer inheritence 

class A:
    def __init__(self ):
        print("A construct")

class B(A):
    pass

b = B()
# print(b)



# Childe has constructer want to call parent construer 


class A:
    def __init__(self):
        print("A constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("B constructor")

B()



# Type of the Inheritence 

# Single Inhertence 


class A:
    pass

class B(A):
    pass


# Multilevel

class A:
    def show(self):
        print("this is the pwwarent")

class B(A):
    pass

class C(B):
    pass

c= C()
print(c.show())

# Multple Inheritence 

class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

C().show()   # prints A (Left priority)




# ⭐ Q1. Create a Parent class Animal and Child class Dog. Dog should inherit sound() method.

class Animal:
    def Sound(self):
        print("Animal sound")
    
class Dog(Animal):
    pass

dog = Dog()
dog.Sound()


# ⭐ Q2. Add new feature in Dog class (like bark()).


class Animal:
    def Sound(self):
        print("Animal ssound")
    
class Dog(Animal):
    def bark(self):
        print("bark")

dog = Dog()
dog.Sound()
dog.bark()


# ⭐ Q4. Use super() to call parent method also.


class Animal:
    def Sound(self):
        print("Animal ssoweund")
    
class Dog(Animal):
    def bark(self):
        super().Sound()
        print("bark")

dog = Dog()

dog.bark()


# Private Varibele inherite nahi hote h 

class A:
    _b =20. # Protected Variable
    __a = 10 # Private Variable 

class B(A):
    pass

a = A()
print(a._b) 
# a.__a