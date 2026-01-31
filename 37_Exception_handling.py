

'''


Exception handling 



try , except , else , finally 

try --> (the risk zone )
it is the write the code that may couse exception 

except  ---> handles the error so the program does not crash.

else ---> Success zone else run when try success no error occure 

finally --> always runs no matter what:
            error occurs ✅
            error doesn’t occur ✅
            return happens ✅
            break happens ✅

Example:


✅ 8) raise keyword (Manual Exception) 

raised is used to throw exceptio yourself 

'''

'''
try:
    x = 0
except ZeroDivisionError:
    print("You entered 0, division not possible.")
    '''

#  Carching the multiple error 


'''try:
    x = int(input("Enter number: "))
    print(10 / x)

except ValueError:
    print("Invalid input! Please enter integer only.")

except ZeroDivisionError:
    print("0 is not allowed.")'''

# catching the multilple error in one line 
'''
try:
    x = int(input("Enter number: "))
    print(10 / x)
except (ZeroDivisionError , ValueError):
    print("Invalid input or division by zero.")
'''
'''try:
    x = int(input("Enter number: "))
    print(10 / x)

except Exception as e:
    print("Something went wrong:", e)'''




try:
    x = int(input("Enter number: "))
    result = 10 / x
    print(result)
except Exception as e:
    print("Error:", e)

else:
    print("Success! Result:", result)




age = int(input("Enter age: "))

if age < 18:
    raise ValueError("Age must be 18 or above!")

print("You can vote")



# Custom Erro 


# some tike  built-in error not enought
#  so we create own exception class 


class InvalidMarksError(Exception):
    pass

marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    raise InvalidMarksError("Marks must be between 0 and 100!")

print("Marks accepted:", marks)










# ✅ 10) Custom Exception with Message + Extra Data (Advanced)

class PaymentError(Exception):
    def __init__(self, message, amount):
        super().__init__(message)
        self.amount = amount

try:
    amount = int(input("Enter payment: "))
    if amount <= 0:
        raise PaymentError("Payment must be positive", amount)

except PaymentError as e:
    print("Payment Error:", e)
    print("Invalid amount was:", e.amount)


#  Raise vs Return 

'''
raise --> stop function with the error 

return -> stop function with normally 


'''
