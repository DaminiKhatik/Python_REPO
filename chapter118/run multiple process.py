import multiprocessing 
import os
def process():  
    print("Pid is %s" % (os.getpid(),))
processes = [multiprocessing.Process(target=process) for _ in range(4)] 
for p in processes:   
    p.start() 
for p in processes:  
    p.join() 