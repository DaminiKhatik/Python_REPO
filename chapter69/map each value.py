from functools import partial
from operator import mul

rate = 0.9 
dollars = {'under_my_bed': 1000, 
           'jeans': 45,
           'bank': 5000}
a=sum(map(partial(mul, rate), dollars.values()))
print(a)


b=list(map(abs, (1, -1, 2, -2, 3, -3))) 
print(b)

