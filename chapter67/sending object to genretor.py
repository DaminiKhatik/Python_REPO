def accumulator():   
    total = 0  
    value = None  
    while True:              
        value = yield total       
        if value is None: break         
        total += value
generator = accumulator()
next(generator) 
a=generator.send(1)    # 1
a1=generator.send(10)   # 11 
a2=generator.send(100) #111
print(a)
print(a1)
print(a2)