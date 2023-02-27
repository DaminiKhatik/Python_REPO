# Basic use of map, itertools.imap and future_builtins.map

#map function
def addition(n):
	return n + n
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

#imap
names = ['Fred', 'Wilma', 'Barney'] 
from itertools import imap 
b=imap(len, names) 
print(b)

#future_builtins
names = ['Fred', 'Wilma', 'Barney'] 
from future_builtins import map  
a= map(len, names) 
print(a)