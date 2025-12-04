# What is the OOPs

# Object oriented programming paradigram that organize code into the object 


#  Object Represent real word entities 

# Attributes : (Properties , Data )-> Describe the Object 
#  Methods : ( Functions / Behaviour ) -> actions the object 
# 

# Class and Object 

# class --> Blueprint for creating an object 
# Object --> Instances of Object (object == instances) 


class Person:  # class
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age
    
    def greet(self):  # method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Object creation
p1 = Person("Vishal", 21)
p1.greet()


# Constructor __init__

# Special method that  call automatically when a creating an object 
# Initializes object attributes.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Tesla", "Model S")
print(car1.brand)  # Tesla



# 4. Instance Variables vs Class Variables

class Dog:
    species = "Canine"  # Class variable
    def __init__(self, name):
        self.name = name  # Instance variable

d1 = Dog("Tommy")
d2 = Dog("Jerry")

print(d1.name, d1.species)  # Tommy Canine
print(d2.name, d2.species)  # Jerry Canine


# 5. Methods in Python

# Instance methods → work with object instances (self)

class Person:  # class
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age
    
    def greet(self):  #  instance method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Object creation
p1 = Person("Vishal", 21)
p1.greet() # call with the object


# Class methods → work with class, not instance (@classmethod)

# First argument is cls → refers to the class itself

# Can access class variables

# Can change class state (class-level data)

# Often used for alternate constructors

class Math:
    name = "Rohit"
    @classmethod
    def info(cls ):
        
        print("This is a Math class" , cls.name)

 # 15
Math.info()  # This is a Math class


# Static methods → no access to class or instance (@staticmethod)

class Student :
    name = "vishal"

    @staticmethod
    def greet(name):
        print("Welcomr to the real world !" , " " , name)
Student.greet("Rahul")



# Abstractiona in python 



#  Hideing the Complex code and shoeing the nessesory data 

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def strat(self):
        self.clutch = True
        self.acc = True
        print("car strated ...")
    def stop(self):
        self.acc = False
        self.clutch= False
        self.brk = True
        print("car is stopped ")

car = Car()

car.strat()
car.stop()

# ❗️ importent in python 

# Python me abstraction mainly ABC (Abstract Base Class) and abstract methods ke through achieve hoti hai.

# User ko sirf what to do pata ho

# But how it is done hide hota hai

# Abstraction in python used the abc Moodule


# Abstract Basse class 
