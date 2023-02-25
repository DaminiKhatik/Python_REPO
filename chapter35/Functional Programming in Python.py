#Lambda Function
x = lambda a: a + 10
print(x(5))


# Map Function
def myfunc(a):
  return len(a)
x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
print(list(x))


#Reduce Function

import functools
import operator
lis = [1, 3, 5, 6, 2]
 
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lis))
 
print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, lis))
 
 
 
 # Filter Function
seq = [0, 1, 2, 3, 5, 8, 13]
# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

