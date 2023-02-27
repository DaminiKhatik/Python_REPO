from itertools import imap 
from future_builtins import map as fmap 
image = [[1, 2, 3],        
         [4, 5, 6],        
         [7, 8, 9]]
a=list(map(None, *image)) 
print(a)