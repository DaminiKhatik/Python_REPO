#Working around the Global Interpreter Lock (GIL) 
import multiprocessing 
import time 
from multiprocessing import Pool
def countdown(n): 
    while n > 0:     
        n -= 1
COUNT = 10000000
start = time.time() 
with multiprocessing.Pool as pool:  
    pool.map(countdown, [COUNT/2, COUNT/2])
    pool.close()   
    pool.join()
end = time.time()
print(end-start)
