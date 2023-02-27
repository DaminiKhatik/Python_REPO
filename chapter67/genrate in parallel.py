 #Iterating over generators in parallel
import itertools
from itertools import zip_longest
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
for x, y in zip_longest(a,b): 
    print(x,y)
