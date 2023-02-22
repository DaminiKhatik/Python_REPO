#and
1 and 2
#or
1 and 2

#Lazy evaluation

def print_me(): 
    print('I am here!')
    0 and print_me() 
    
    #Testing for multiple conditions
    
a = 1
b = 6 
if a and b > 2:
         print('yes') 
else:
    print('no') 