#Destructuring as values 

a, b = (1, 2) 
print(a) # Prints: 1
print(b) # Prints: 2


#Destructuring as a list
head, *tail = [1, 2, 3, 4, 5]
print(head) # Prints: 1 
print(tail) # Prints: [2, 3, 4, 5]

""" or second option"""

l = [1, 2, 3, 4, 5]
print(l)
a=head = l[0] 
print(a)
b=tail = l[1:]
print(b)

#Ignoring lists in destructuring assignments
a, *_ = [1, 2, 3, 4, 5]
print(a) 

a, *_, b = [1, 2, 3, 4, 5] 
print(a, b)

a, _, b, _, c, *_ = [1, 2, 3, 4, 5, 6]
print(a, b, c) 