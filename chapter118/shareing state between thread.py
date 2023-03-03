import threading
obj = {} 
obj_lock = threading.Lock()
def objify(key, val):   
    print("Obj has %d values" % len(obj))    
    with obj_lock:      
        obj[key] = val   
        print("Obj now has %d values" % len(obj))
ts = [threading.Thread(target=objify, args=(str(n), n)) for n in range(4)] 
for t in ts:   
    t.start() 
    for t in ts:
    t.join()
    print("Obj final result:")
    import pprint;pprint.pprint(obj)
