"""The __name__ special variable is used to check whether a ﬁle has been imported as a module or not, and to identify a function, class, module object by their __name__ attribute. """

# __name__ == '__main__'

if __name__ == '__main__':   
    print('hello')



#function_class_or_module.__name__
import os

class hello:  
    pass
def hi(x):  
    x += 2 
    return x
print(hi) 
print(hi.__name__) #hi
print(hello)
print(hello.__name__) 
print(os.__name__) # os
