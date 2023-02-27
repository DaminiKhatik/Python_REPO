
#Introduction to context managers and the with statement

with open('hello.txt', 'w') as fileobj:
    fileobj.write("\n hello,world")
    
    
# creating your own context manager
class ContextManager():
    def __init__(self):
        print('init method ') # init method is called as soon as we create instance of a class and then other operations are performed
         
    def __enter__(self):
        print('enter method ')
        return self
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method ')
 
with ContextManager() as manager:
    print('with statement')
    
    #Manage Resources
class File(): 
    def __enter__(self):    
        self.open_file = open(self.hello.txt, self.mode) 
        return self.open_file
    def __exit__(self, *args): 
        self.open_file.close()
