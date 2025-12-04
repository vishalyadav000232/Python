# Excption in python 

#  exceptiom is an error  that occure during the program executions 
#  descrupting the normal flow instad of the crashiing 
#  Python allow to handle and catcch a error gracefullly 





# Key Points 

# Occur at runtime not a complie time 
# can be handle using try catch block 



#  Syntax 




# try:
#     # Code that might raise an exceptions 
#     # risky_code()

# except:
#     # Code handle the exceptions

# else:
#     # Optional : run if no exceptions ocuurs 

# finally:
#     # Optional : runs always even the  exception occure or not 




#  try --> try erap that code may fail 
#  except --> handle spacific exceptiomns 
#  else --> result if no exceptions :
#  finnally --> always run even error or not 



#  Types of error 

# Pytho Provide many built in exceptin classe 


# ZeroDivisionError -> divided by zero 
# FileNotFoundError -> file not found 
# ValueError -> invalide value and type Convertion 
# TypeError -> wrong data type operations 
# IndexError -> index out of range 
# KeyError --> Dictionary key not found 
# ImportError --> Moduls imports fails 
# AttributeError -- > Object has no such a attributes 
# NameError --> Variable not defined 

 
try:
    num = int("abc")  # raises ValueError
    print(num)
except ValueError as e:
    print("ValueError caught:", e)



#  user cusomr error 

class MyCustomErro(Exception):
    pass

try:
    raise MyCustomErro("Something went wrong")
except MyCustomErro as e:
 
    print(e)


try:
    x = int(input("Enter number: "))
    y = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)


    # You can raise the exception 

age = -5
if age < 0:
    raise ValueError("Age can't be a negative ")

