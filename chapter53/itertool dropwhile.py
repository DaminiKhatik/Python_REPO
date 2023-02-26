#itertools.dropwhile
import itertools
def is_even(x):   
    return x % 2 == 0
lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44,55] 
result = list(itertools.dropwhile(is_even, lst))
print(result)