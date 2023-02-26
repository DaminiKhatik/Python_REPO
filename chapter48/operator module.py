#Itemgetter
import operator
from operator import itemgetter
a = []
a.append(["Nick", 30, "Doctor"])
a.append(["John",  8, "Student"])
a.append(["Paul", 22, "Car Dealer"])
a.append(["Mark", 66, "Retired"])    
a.sort(key=operator.itemgetter(1))    
print(a)

#Operators as alternative to an inﬁx operator
import operator
from operator import add,mul
a=add(1, 6) 
print(a)
b=mul('a', 10) 
print(b)

#Methodcaller
import operator
from operator import methodcaller
alist = ['wolf', 'sheep', 'duck']
a=list(filter(methodcaller('startswith','s'), alist))
print(a)
a=list(filter(methodcaller('startswith','o'), alist))
print(a)
     