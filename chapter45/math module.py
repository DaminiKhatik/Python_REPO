import math
#round
x = 1.55
y = 2.51
# round to the nearest integer 
a=round(x)
print(a)
b=round(y)  
print(b)

c=round(x, 1) 
print(c)

d=round(y, 1)
print(d)


#ﬂoor
a1=math.floor(x)  
print(a1)
a2=math.floor(y) 
print(a2)

#ceil
b1=math.ceil(x)   
print(b1)
b2=math.ceil(y) 
print(b2)

#trunc
c1=math.trunc(x)  #  1, equivalent to math.floor for positive numbers 
print(c1)
c2=math.trunc(y) 
print(c1)


###Trigonometry

import math,cmath
x = 1
print(math.sin(x))

print(math.cos(x))

print(math.tan(x))

print(math.asin(1))

print(math.acos(1))

print(math.atan(1))


# Pow for faster exponentiation
from math import pow
a=pow(5,9) 
print(a)


# Inﬁnity and NaN ("not a number")
import math
x = 2
print(f"x contains {x}")

# checks if variable is equal to NaN
if(math.isnan(x)):
	print("x == nan")
else:
	print("x != nan")


# Logarithms

import math
a=math.log(100)
print(a)

b=math.log(math.e)  
print(b)

c=math.log(1) 
print(c)

#constant
from math import pi, e 
print(pi)
print(e)

# Imaginary Numbers
import math
import cmath

a= 8 + 5j
print(a)

a = 8 + 5j
print(type(a))


#Copying signs

from math import copysign
a=math.copysign(-2, 3)
print(a) 


# Complex numbers and the cmath module
import cmath
z = 1 + 3j
print(z)

b=cmath.sqrt(-16) 
print(b)

c=cmath.rect(math.sqrt(2), math.atan(1)) 
print(c)