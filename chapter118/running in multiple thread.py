import threading
import os
def process():  
    print("Pid is %s, thread id is %s" % (os.getpid(), threading.current_thread().name))
threads = [threading.Thread(target=process) 
for _ in range(10)] 
for t in threads:   
 t.start()
for t in threads:   
 t.join() 