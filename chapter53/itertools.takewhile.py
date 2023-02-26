import itertools
def is_even(x):  
  return x % 2 == 0
lst = [0,90, 2, 4, 12, 18, 13, 14,98, 22, 23, 44] 
result = list(itertools.takewhile(is_even, lst))
print(result)
 