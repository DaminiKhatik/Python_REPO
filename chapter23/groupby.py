things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "harley"), ("vehicle", "speed boat"), ("vehicle", "school bus")] 

dic = {}
f = lambda x: x[0]
for key, group in groupby(sorted(things, key=f), f):   
    dic[key] = list(group) 
    print(dic)
