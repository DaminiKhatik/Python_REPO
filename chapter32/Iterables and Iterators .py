#Section 32.1: Iterator vs Iterable vs Generator

#Here mytuple is iterable and myit is iterator.
mytuple=(“red” , “blue”, “green”)
myit = iter(mytuple)
print(next(myit))

#This will return red.

print(next(myit))

#This will return blue.

print(next(myit))

#This will return green.