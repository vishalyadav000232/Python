
# Public attributes


class Student():
    def __init__(self , name):
        self.name = name # Public 


s1 = Student("vishal")
print(s1.name) # allowed to access 
s1.name = "rahul" # allow to modify
print(s1.name)

''' 
Easy access no controlled validation 
issu : any one cannaccess the change the dara wrongly

'''



#  Protected attributes

class Marks():
    def __init__(self , name:str , marks:int):
        self.name = name
        self._marks = marks

m1 = Marks("vishal", 90)
print(m1.name)
print(m1._marks) # possible but not reccomended

m1._marks = 34

print(m1._marks)


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private

    def chek_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount < 0:
            print("❌ Balance cannot be negative!")
        else:
            self.__balance = amount

acc = BankAccount("Vishal", 1000)
print(acc.chek_balance())
print(acc.set_balance(-299))
# print(acc.__balance) #❌ ERROR





# @property is the corator that convete the methos as like attributes 
class Seat:
    def __init__(self, seat_name: str, id: int, is_active: bool):
        self.id = id
        self.seat_name = seat_name
        self.__is_active = is_active

    @property
    def is_active(self):
        return self.__is_active

    @is_active.setter
    def is_active(self, value: bool):
        if not isinstance(value, bool):
            print("❌ is_active must be True or False only")
        else:
            self.__is_active = value


s1 = Seat("A2", 1, False)

print(s1.seat_name)
print(s1.id)
print(s1.is_active)

s1.is_active = True  

print(s1.seat_name)
print(s1.id)
print(s1.is_active)




#  Inheritance 

class Person():
    def __init__(self , name :str , age:int):
        self.name = name
        self.age = age
    def info(self):
        return f"{self.name}, {self.age} years old"


class Student(Person):
    def __init__(self, name , age , roll_no:int , marks:float):
        super().__init__(name, age) 
        self.roll_no = roll_no
        self.marks = marks

    def student_info(self):
        return f"{self.info()}, Roll: {self.roll_no}"

class Teachers(Person):
    def __init__(self, name, age , salary:float , subject :str):
        super().__init__(name, age)
        self.__salary = salary
        self.subject = subject

s1 = Student("Vishal", 22, 101 , 21.2)
print(s1.student_info())


class Writer:
    def write(self):
        return "Writing..."

class Coder:
    def code(self):
        return "Coding..."

class Dev(Writer, Coder):
    pass

d = Dev()
print(d.write())
print(d.code())



def print_all_no(num):
    if num == 0:
        return
    print(id(num) , num)
    print_all_no(num-1)
    
    print("END")

print_all_no(10)




def fact(n):
    if n ==1:
        return 1
    return n * fact(n-1)

resut = fact(4)
print(resut)

# fact(4)
# fact(3)
# fact(2)
# fact(1)



# Ploymorphism 

'''
One name many forms 

same methods and function name nut different beahviour  depending in the objecct


example 

pay() methods exist in the all pyment 

like 
UPI pay
Card pay
Cash pay

Type of the Polymorphisme
 

methods overiding
Ducks Typing 
Operator overiding 

'''

# ✅ 1) Method Overriding (Runtime Polymorphism)

class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

a1 = Dog()
a2 = Cat()

print(a1.sound())
print(a2.sound())



from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self , amount):
        pass


class UPIPayment(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} via UPI"

class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} via Card"

def checkout(payment_obj, amount):
    print(payment_obj.pay(amount))

checkout(UPIPayment(), 500)
checkout(CardPayment(), 1000)
