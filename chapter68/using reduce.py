#using reduce
from functools import reduce
import operator 
from operator import mul 
asequence = [1, 2, 3,4]
cumprod = reduce(mul, asequence, 5)
print(cumprod) #120 result


#Cumulative product

import operator 
a=reduce(operator.mul, [10, 5, -3,2]) 
print(a)

# Non short-circuit variant of any/all

import operator  
# non short-circuit "all" 
a1=reduce(operator.and_, [False, True, True, True])
print(a1)
a2=reduce(operator.and_, [True, True, True, True])
print(a2)
a3=reduce(operator.and_, [False, True, False, True])
print(a3)
a4=reduce(operator.and_, [False, True, False, False])
print(a4)

# non short-circuit "any" 
b1=reduce(operator.or_, [False, True, True, True])
print(b1)
b2=reduce(operator.or_, [True, True, True, True])
print(b2)
b3=reduce(operator.or_, [False, True, False, True])
print(b3)
b4=reduce(operator.or_, [False, True, False, False])
print(b4)


