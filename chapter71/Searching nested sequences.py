#Searching nested sequences

def outer_index(nested_sequence, value):  
    return next(index for index, inner in enumerate(nested_sequence)
                for item in inner                   
                if item == value)
alist_of_tuples = [(4, 5, 6), (3, 1, 'a'), (7, 0, 4.3)] 
a=outer_index(alist_of_tuples, 'a')  # 1 
b=outer_index(alist_of_tuples, 4.3)
print(a)
print(b)