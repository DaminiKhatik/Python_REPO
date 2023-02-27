def xrange(n):   
    i = 0  
    while i < n: 
        yield i 
        i += 1

for i in xrange(100):  
    print(i) 