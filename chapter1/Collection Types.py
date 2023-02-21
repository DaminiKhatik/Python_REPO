# Python program to demonstrate Creation of List  
# Creating a Empty List 
empty_list = [] 
print("Initial blank List: ") 
print(empty_list) 
print("---------------------------------------------")
# Creating a List with the use of a String 
List = ['Apurva'] 
print("\nList with the use of String: ") 
print(List) 
print("----------------------------------------------")    
# Creating a List with the use of multiple values 
List = ["My", "Name", "Is" ,"Apurva"] 
print("\nList containing multiple values: ") 
print(List[0])  
print(List[2])
print("----------------------------------------------")
# Creating a List with Integer Value:
int_list = [1, 2, 3]
print(int_list)
print("----------------------------------------------")
#Mixed Datatype list:
mixed_list = [1, 'abc', True, 2.34, None]
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List) 
nested_list = [['a', 'b', 'c'], [1, 2, 3]]
print("\nMulti-Dimensional List: ") 
print(nested_list)
print("-----------------------------TUPLE---------------------------------------")

# Python program to demonstrate Creating an empty tuple 
Tuple1 = () 
print("Initial empty Tuple: ") 
print (Tuple1) 
    
# Creating a Tuple with the use of Strings 
Tuple1 = ('HELLO', 'WORLD') 
print("\nTuple with the use of String: ") 
print(Tuple1) 
    
# Creating a Tuple with the use of list 
list1 = [1, 2, 4, 5, 6] 
print("\nTuple using List: ") 
print(tuple(list1)) 
  
# Creating a Tuple with the use of built-in function 
Tuple1 = tuple('Apurva') 
print("\nTuple with the use of function: ") 
print(Tuple1) 
  
# Creating a Tuplewith nested tuples 
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('python', 'Java') 
Tuple3 = (Tuple1, Tuple2) 
print("\nTuple with nested tuples: ") 
print(Tuple3)

print("-----------------------------SETS--------------------------------")

# Python program to demonstrate Creation of Set in Python 
   
set1 = set() 
print("Initial blank Set: ") 
print(set1) 
    
# Creating a Set with the use of a String 
set1 = set("IlikePython") 
print("\nSet with the use of String: ") 
print(set1) 
  
# Creating a Set with the use of a List 
set1 = set(["hey", "hello", "hii"]) 
print("\nSet with the use of List: ") 
print(set1) 
  
# Creating a Set witha mixed type of values (Having numbers and strings) 
set1 = set([1, 2, 'Lotus', 4, 'Lily', 6, 'ROse']) 
print("\nSet with the use of Mixed Values") 
print(set1)

print("-----------------------------Dictionaries--------------------------------")
# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
    
# Creating a Dictionary  with Integer Keys 
Dict = {1: 'lily', 2: 'rose', 3: 'marigold'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 
    
# Creating a Dictionary with Mixed keys 
Dict = {'Name': 'flowers', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 
    
# Creating a Dictionary with dict() method 
Dict = dict({1: 'lily', 2: 'rose', 3: 'marigold'} ) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 
    
# Creating a Dictionary with each item as a Pair 
Dict = dict([(1, 'APURVA'), (2, 'NIMKAR')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 