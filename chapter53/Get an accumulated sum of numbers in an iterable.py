#Get an accumulated sum of numbers in an iterable
import itertools as it 
import operator
a=list(it.accumulate([1,2,3,4,5])) 
print(a)