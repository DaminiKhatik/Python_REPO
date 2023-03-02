def test_func(arg1, arg2, arg3): # Usual function with three arguments  
    print("arg1: %s" % arg1)  
    print("arg2: %s" % arg2) 
    print("arg3: %s" % arg3)
kwargs = {"arg3": 3, "arg2": "two"}
test_func(1, **kwargs )


#kwargs and default values
def fun(**kwargs):   
    print (kwargs.get('value', 0))
    fun() 
    fun(value=1) 
    
    