a = {1, 2, 2, 3, 4} 
b = {3, 3, 4, 4, 5}
a1=a.intersection(b) 
print(a1)

a2=a.union(b) 
print(a2)

a3= a.difference(b) 
print(a3)

a4=b.difference(a)
print(a4)

a5=a.symmetric_difference(b) 
print(a5)

a6=b.symmetric_difference(a) 
print(a6)
c = {1, 2} 
a7=c.issubset(a) 
print(a7)

a8=a.issubset(c) 
print(a8)
