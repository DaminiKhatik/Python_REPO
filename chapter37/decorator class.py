class NewDocorator:  
    def __init__(self, function):  
        self.function = function  
      
    def __call__(self):  
        self.function()  
@NewDocorator  
def function():  
    print("WelCome to JavaTpoint")  
function()  