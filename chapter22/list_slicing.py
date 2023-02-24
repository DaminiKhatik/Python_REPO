#Using the third "step" argument
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
lst[::2] 
print(lst)

#Selecting a sublist from a list
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
lst[2:4] 
print(lst)

#Reversing a list with slicing
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
b = lst[::-1]
print(b)


# Shifting a list using slicing
my_array = [1, 2, 3, 4, 5]
shift_list(my_array, 3) 
print(my_array)


