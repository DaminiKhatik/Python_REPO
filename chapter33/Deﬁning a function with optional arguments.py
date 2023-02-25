def make(action='nothing'):  
 return action

make("fun") # Out: fun
make(action="sleep") # Out: sleep
# The argument is optional so the function will use the default value if the argument is # not passed in. 
make()  # Out: nothing