#List comprehensions

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


#Conditional List Comprehensions

fruits = [1,2,3,3,4,5,678,89,]
newlist = []

for x in fruits:
   if x % 2 ==0:
    newlist.append(x)

    print(newlist)
    
    #Avoid repetitive and expensive operations using conditional clause
l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
[item for sublist in l for item in sublist]
list(itertools.chain(*l))
print(l)


# Dictionary Comprehensions
myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)


#Generator Expressions

for i in [x**2 for x in range(10)]:  
    print(i)


#Set Comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

output_set = set()
for var in input_list:
	if var % 2 == 0:
		output_set.add(var)

print("Output Set using for loop:", output_set)


#Refactoring ﬁlter and map to list comprehensions
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
squares = [x**2 for x in a] 
print(squares)
filtered = filter(lambda x: x % 2 == 0, range(10)) 
results = map(lambda x: 2*x, filtered)

print(filtered)
print(results)


#Comprehensions involving tuples

my_tuple=(1,3,4,5,6,7,8,9,0,3,3,5,9)
squares = [x**2 for x in my_tuple] 

print(squares)


#Counting Occurrences Using Comprehension
print (sum(    1 for x in range(1000)   
           if x % 2 == 0 and   
           '9' in str(x) 
           
          ))


# Changing Types in a List
items = ["1","2","3","4"] 
[int(item) for item in items]
print(items)
map(float, items) 
print(items)


