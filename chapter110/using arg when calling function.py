def print_args(arg1, arg2):    
    print(str(arg1) + str(arg2))
a = [1,2] 
b = tuple([3,4])
print_args(*a) 
print_args(*b) 