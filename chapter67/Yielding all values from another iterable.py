#Yielding all values from another iterable
def fb(x):    
    yield from range(x * 2) 
    yield from range(10)
print(list(fb(11))) 