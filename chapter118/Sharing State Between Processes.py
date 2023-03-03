import multiprocessing
plain_num = 0 
shared_num = multiprocessing.Value('d', 0) 
lock = multiprocessing.Lock()
def increment():    global plain_num  
with lock:        # ordinary variable modifications are not visible across processes  
    plain_num += 1        # multiprocessing.Value modifications are       
    shared_num.value += 1
ps = [multiprocessing.Process(target=increment) for n in range(4)]
for p in ps: 
    p.start() 
    for p in ps: 
        p.join()
print("plain_num is %d, shared_num is %d" % (plain_num, shared_num.value))
