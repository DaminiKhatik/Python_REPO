#create tuple
t = ('a', 'b', 'c', 'd', 'e')
print(t)

#type
t1= ('a', 'b', 'c', 'd', 'e')
type(t1)   

#To create a singleton tuple it is necessary to have a trailing comma.
t2 = ('a','b')
print(t2)
   
t3= tuple('lupins')
print(t3) 


#Tuples are immutable

t = (1, 2)
q = t 
t += (3, 4)
print(t)

# Packing and Unpacking Tuples
first, *more, last = (1, 2, 3, 4, 5) 
print(first)
print(more)
print(last)

#Built-in Tuple Functions
tuple1 = ('a', 'b', 'c', 'd', 'e') 
tuple2 = ('1','2','3')
tuple3 = ('a', 'b', 'c', 'd', 'e')
#length
b=len(tuple1) 
print(b)

#Max of a tuple
a=max(tuple2) 
print(a)

#Max of a tuple
c=min(tuple3) 
print(c)

#Convert a list into tuple
list = [1,2,3,4,5]
c=tuple(list) 
print(c)


#Tuple concatenation
test_tup1 = (1, 3, 5)
test_tup2 = (4, 6)
res = test_tup1 + test_tup2
print("The tuple after concatenation is : " + str(res))



#Indexing Tuples
x = (1, 2, 3) 
print(x[1])
print(x[2])

#Reversing Elements

tuple1 = ('a', 'b', 'c', 'd', 'e') 
rev = tuple1[::-1]
print(rev)