

#  Moduls and packages (Basic to Advance)


# What is Moduls ?

# a modules is simply python file .(.py)  that contains variable function and classes 

# example  main.py , util.py . service.py 

#  why do we use the modules 

#  Code Reusablity 
#  Organization 
#  Testing Become easy 
#  Remove duplicates

import utils
print(utils.add(23,32))
print(utils.greet("vishal"))



#  Type of the imports 

#  Normal Imports 

import math

print(math.sqrt(25))


# Import with the alis 

import math as m

print(m.sin(30))



# import Spacific Function 

from math import sqrt

print(sqrt(36))


#  import multiple spacific 

from math import sqrt  , pow

# import Everything (Not recomended )


from math import *

print(sqrt(3290))



#   What is paclage ? 

#   a package is folder that conatains multiple modules , and spacific file 


# Why __init__.py --> python ko batata hai ki yr folder ek package h 

# it turns a directory into a python package so modules can be imported 

