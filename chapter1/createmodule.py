#Modules can be imported by other modules.
def say_hello(): 
    print("Hello!")
    
import hello
hello.say_hello()

import hello as ai
ai.say_hello()

#Speciﬁc functions of a module can be imported.

from hello import say_hello
say_hello()
