from abc import ABC, abstractmethod
class Account(ABC) :
    bank_name = "Yadavji_Bank"

    def __init__(self , owner , account_no , initial_bal = 0):
        self.owner = owner
        self.account_no = account_no
        self.__balance = initial_bal #private attributee Encapsulation 

       # Abstraction: abstract methods force subclasses to implement these
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    # @property to safely read private attiributes 

    @property
    def balance(self):
        return self.__balance;

    def _change_balance(self , amount):
        self.__balance +=amount
    def __str__(self):
        return f"{self.owner} | {self.account_no} | Balance :{self.__balance}"
    
       # Magic: length as number of digits in account number (just for demo)
    def __len__(self):
        return len(str(self.account_no))
    
    def __add__(self, other):
        if isinstance(other, Account):
            return (self.owner + " & " + other.owner, self.balance + other.balance)
        return NotImplemented
    
    @classmethod
    def bank_info (cls):
        return f"Bank : {cls.bank_name}"
    
    @staticmethod
    def validate_amount(amount):
        if not isinstance(amount , (int , float)):
            raise TypeError("Amount Must be a Number ")
        if amount <= 0 :
            raise TypeError("Amount must be postive !")

class SavingAcounts(Account):
    def __init__(self, owner, account_no, initial_bal=0 , intrest_rate = 0.08):
        super().__init__(owner, account_no, initial_bal)
        self.intrest_rate = intrest_rate

    def deposit(self, amount):
        self.validate_amount(amount)
        self._change_balance(amount)
        return f" Depositr Amount {amount} to Saving "
    
    def withdraw(self, amount):
        self.validate_amount(amount)
        if self.balance < amount:
            raise TypeError("Insuffiecent Balance")
        self._change_balance(-amount)
        return f"Withdrew {amount} from current"
    

    def apply_intrest(self , year):
        self.year = year
        interest = self.intrest_rate * self.balance * year
        self._change_balance(interest)
        return interest
    


class CurrentAccount(Account):
    def __init__(self, owner, account_no, initial_bal=0 ,over_draft_limit = 1000):
        super().__init__(owner, account_no, initial_bal)
        self.over_draft_limite = over_draft_limit

    def deposit(self, amount):
        self.validate_amount(amount)
        self._change_balance(amount)
        return f"Deposited {amount} to current"
    
    def withdraw(self, amount):
      self.validate_amount(amount)
      if amount > (self.balance + self.over_draft_limite):
          raise TypeError( "Exceeded overdraft limit")
      self._change_balance(-amount)
      return f"Withdrew {amount} from current"


# small bank serviec demonstrate the polymorphisme 


class BankServies:
    def __init__(self):
        self.accounts = {}
    def add_accounts(self , account: Account):
        self.accounts[account.account_no] = account

    def transfer(self, from_account , to_account , amount):
        if from_account not in self.accounts or to_account not in self.accounts:
            raise TypeError( "invalide account no .")
        from_acc = self.accounts[from_account]
        to_acc = self.accounts[to_account] 

        from_acc.withdraw(amount)
        to_acc.deposit(amount)


print(Account.bank_info())


vishal = SavingAcounts("Vishal Yadav" , 8808763176 , 100000)
rahul = CurrentAccount("Rahul Yadav" , 8707595797 , 76334)

bank = BankServies()
bank.add_accounts(vishal)
bank.add_accounts(rahul)

print(bank.accounts)


print(vishal)
print(rahul)

print(vishal + rahul)

vishal.deposit(2000000)
print(vishal)
vishal.withdraw(2000000)
print(vishal)
print(vishal.apply_intrest(4))




bank.transfer(8808763176 , 8707595797 , 50000)
print(vishal)
print(rahul)




