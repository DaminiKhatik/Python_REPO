s = {1, 2}   # or list or generator or even iterator 
i = iter(s)  # get iterator 
a = next(i)  # a = 1 
b = next(i)  # b = 2 
c = next(i)  # raises StopIteration 
print(a)
print(b)


#Iterating over entire iterable
s = {1, 2, 3}
for a in s:   
 print(a)
# copy into list l1 = list(s) 
l1 = [1, 2, 3]
# use list comprehension 
l2 = [a * 2 for a in s if a > 2]  # l2 = [6] 


