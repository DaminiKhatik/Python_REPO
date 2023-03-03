import multiprocessing
def fib(n):  
    if n <= 2:        
        return 1   
    else:        
        return fib(n-1)+fib(n-2) 
    p = multiprocessing.Pool()
    print(p.map(fib,[38,37,36,35,34,33]))
