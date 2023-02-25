#Basic use of ﬁlter

def is_multiple_of_2(num):
    return num % 2 == 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
result = list(filter(lambda x: is_multiple_of_2(x), numbers))
print(result) 


#Filter without function
a=list(filter(None, [1, 0, 2, [], '', 'a'])) 
print(a)
