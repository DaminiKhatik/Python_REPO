#Copy a dictionary
d1 = {1:[]} 
d2 = d1.copy() 
a=d1 is d2 
print(a)
b=d1[1] is d2[1] 
print(b)

#Performing a shallow copy
import copy 
c = [[1,2]]
d = copy.copy(c)
a=c is d 
print(a)
b=c[0] is d[0]
print(b)

#Performing a deep copy
import copy 
c = [[1,2]] 
d = copy.deepcopy(c) 
a=c is d 
print(a)
b=c[0] is d[0]
print(b)

#Performing a shallow copy of a list
l1 = [1,2,3] 
l2 = l1[:]    
print(l2)

#Copy a set
s1 = {()} 
s2 = s1.copy() 
s1 is s2
s2.add(3) 
print(s1) 
print(s2)
