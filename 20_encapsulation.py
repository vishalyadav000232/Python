# 


#  Encapsulation means hideing internal Details f a class and Protecting the data from eing changes accesdently 

# you are creates the variable inside the class and do not allow to direct access to them instead , you use the method (getter / setter ) to control how data is access and changes 

# ✅ 1. What is Encapsulation? (Basic)

# A class keeps variables + methods together

# Some variables are private, so they can’t be accessed directly

# You control everything using getter/setter methods


# Simple example 

class Students:
    def __init__(this , name , age):
        this.name = name  # Public variable 
        this.__age = age  # Private variable 
    
    def get_age(this):
        return this.__age
    
    def set_age(this , new_age):
        if new_age > 0:
            this.__age = new_age
        else:
            return "Invalide age"
        
s1 = Students("vishal" , 30)
# print(s1.__age) # private varibel can't access directly 
age = s1.get_age()
print(age)
s1.set_age(83)
new_age = s1.get_age()
print(new_age)




# Q1. Create a class Student with private variable __marks. Add getter and setter.

class Student:
    def __init__(self, name , marks):
        self.name = name 
        self.__marks = marks
    def ger_marks(self):
        return self.__marks
    
    def set_marks(self , new_marks):
        if 0 <= new_marks <100:
            self.__marks = new_marks
        else:
            return " Invaid"
student1 = Student("vishal" , 32)
print(student1.name  ) # name ✅ but marks ❌

print(student1.ger_marks()) # get the marks
student1.set_marks(93)

print(student1.ger_marks())
 # get the marks
student1.set_marks(123) 

print(student1.ger_marks()) # get the marks


# Q2. Make a Bank class with private __balance. Add deposit and withdraw methods.

class Bank :
    def __init__(self , balance = 0):
        self.__balcance = balance
    def deposite(self , amount):
        if amount > 0 :
            self.__balcance += amount
        else:
            print("invalid amount")
    def withdrew(self , amount):
        if amount <=self.__balcance:
            self.__balcance -= amount
        else:
            print("insufficient Balance")
    def get_balance(self):
        return self.__balcance
    
acc = Bank()
bal1 = acc.get_balance()
print(bal1)
acc.deposite(5000)
bal1 = acc.get_balance()
print(bal1)
acc.withdrew(4000)
bal1 = acc.get_balance()
print(bal1)
acc.withdrew(34234)



# Q3. Create a class Employee with protected _salary. Child class Manager should increase salary.

class Employ:
    def __init__(self , name , salary=0):
        self.name = name
        self._salary = salary
    
class Manager(Employ):
    def incres_salary(self , amount):
        if amount > 0:
            self._salary += amount
        else:
            print("invalid")
    def show_salary(self):
        print(f"name : {self.name} Salary : {self._salary}")


e1 = Manager("Babu rao " , 2398)
e1.incres_salary(2983)
e1.show_salary()


class ATM :
    def __init__(self , pin , balance):
        self.__pin = pin
        self.__balance = balance
    def chek_pin(self , enterd_pin):
        return self.__pin == enterd_pin
    
    def withdraw(self , amount , entered_pin ):
        if self.chek_pin(entered_pin):
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("insufficient balcace")
        else:
            print("wrong pin")
    
# Test
atm = ATM(1234, 5000)
print(atm.withdraw(1000, 1234))  # Withdrawn 1000
print(atm.withdraw(500, 1111))   # Wrong PIN

        