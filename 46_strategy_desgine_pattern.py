''' 
Strategy desgin pattern is a behavioral design pattern that enables selecting an algorithm's
behavior at runime instead of the compile time. It defines a family of th alogorithms,
encapsulates each one. and  makes them interchangeable. this pattern lets the algorithm vary independently from cleints that use it.

in the  strategy design pattern, we have three main components:
1. Strategy : this is an interface that defines a common method for all the algorithms. it declares a method that the concete strategies must implement.

2. Concrete Strategies: these are the classes that implement the strategy interface and 
provide spacific implementations of  the algorithm. each concrete strategy encapsulates a
spaccific algorithm or behavior.

3. Context: this is the class that uses a strategy. it maintains refernce to a starategy
object and can call its method to execute the algorithm. the context is configured with a  concrete strategy object and can change it at runtime to alter itd behavior.

'''

from abc import ABC, abstractmethod

# Interface

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# concurrent strategy 1

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, card_holder, cvv):
        self.card_number = card_number
        self.card_holder = card_holder
        self.cvv = cvv

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card ({self.card_holder})")


# Concrete Strategy 2

class UpiPayment(PaymentStrategy):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"Paid {amount} using UPI ({self.upi_id})")


# ---------------------------
# Context
# ---------------------------
class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)


# ---------------------------
# Client Code (Usage)
# ---------------------------
payment = PaymentContext(
    CreditCardPayment("1234-5678", "Vishal Yadav", "123")
)
payment.pay(1000)

print("Switching payment method...")

payment.set_strategy(UpiPayment("vishal@ybl"))
payment.pay(500)

        
    