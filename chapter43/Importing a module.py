import random 
print(random.randint(1, 10))


#Import modules from an arbitrary ﬁlesystem location
import sys
sys.path.append("/path/to/directory/containing/your/module") 
import mymodule

#Importing all names from a module

import math 

pie = math.pi
print("The value of pi is : ",pie)

sqrt=math.sqrt(4)

print("The value of sqrt is : ",sqrt)

c=math.ceil(2.7) 

print("The value of c is : ",c)

print(math.factorial(6))

x = min(5, 10, 25)
print(x)

y = max(5, 10, 25)
print(y)

x1 = pow(4, 3)

print(x1)


#Programmatic importing
import importlib 
random = importlib.import_module("random")
collections_abc = importlib.import_module("collections.abc")
print(collections_abc)


# PEP8 rules for Imports
from math import sqrt
from math import ceil
sqrt=sqrt(4)

print("The value of sqrt is : ",sqrt)

c=ceil(2.7) 

print("The value of c is : ",c)


#Importing speciﬁc names from a module

from random import randint 
print(randint(1, 10)) 

from math import pi 
print(pi) 

import random 
a=random.randrange(1, 10) 
print(a)

#Importing submodules
from module.submodule import function
from package.subpackage import module
from package.subpackage.module import attribute

#Re-importing a module
import math 
from importlib import reload 
math.pi = 3
print(math.pi)  
reload(math) 
print(math.pi)

# __import__() function
mathematics = __import__('math')
print(mathematics.fabs(-2.5))

mathematics = __import__('math')
print(mathematics.pow(2,4))