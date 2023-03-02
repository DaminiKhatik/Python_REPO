# Keyword-only  arguments

def greet(*names, greeting="Hello"):
   for name in names:
        print(greeting, name)
greet("Trey", "Jo")


#  Keyword-required arguments
def print_args(arg1, *args, keyword_required, keyword_only=True):  
    print("first positional arg: {}".format(arg1))    
    for arg in args:    
        print("keyword_required value: {}".format(keyword_required))  
       
print( keyword_required=4) 