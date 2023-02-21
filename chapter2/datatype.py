# String Data Type
a_str = 'Hello World' 
print(a_str)    #output will be whole string. Hello World 
print(a_str[0])    #output will be first character. H
print(a_str[0:5]) 
#Set Data Types
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'} 
print(basket) 
#Numbers data type
int_num = 10    #int value
float_num = 10.2    #float value
complex_num = 3.14j    #complex value 
long_num = 1234567    #long value
print(int_num)
print(float_num)
print(complex_num)
print(long_num)
# List Data Type
list = [123,'abcd',10.2,'d']    #can be an array of any data type or single data type.
list1 = ['hello','world']
print(list)    #will output whole list. [123,'abcd',10.2,'d']
print(list[0:2])    #will output first two element of list. [123,'abcd'] 
print(list1 * 2)    #will gave list1 two times. ['hello','world','hello','world']
print(list + list1)    #will gave concatenation of both the lists. [123,'abcd',10.2,'d','hello','world'] 

#Dictionary Data Type
dic={'name':'red','age':10} 
print(dic)    #will output all the key-value pairs. {'name':'red','age':10} 
print(dic['name'])    #will output only value with 'name' key. 'red' 
print(dic.values())    #will output list of values in dic. ['red',10] 
print(dic.keys())
#Tuple Data Type
tuple = (123,'hello') 

tuple1 = ('world') 
print(tuple)    #will output whole tuple. (123,'hello')
print(tuple[0])    #will output first value. (123)
print(tuple + tuple1)    #will output (123,'hello','world')
tuple[1]='update'    #this will give you error.