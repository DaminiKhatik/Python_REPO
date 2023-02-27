#Infinite sequences
import itertools
from itertools import islice
def fibonacci():   
    a, b = 1, 1    
    while True:     
        yield a      
        a, b = b, a + b
fibonumber = list(itertools.islice(fibonacci(), 100)) 
print(fibonumber)


