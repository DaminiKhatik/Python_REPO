#Variables and Attributes
import typing

class Foo:  
    x: int = 5
    y: str = 'abc'
print(typing.get_type_hints(Foo)) 

"""Alternatively, we can be accessed by using the __annotations__ special variable or attribute"""


x: int
print(__annotations__)

#Class Members and Methods
class Node(object):
        
 def __init__(self, name, age):
        self.name = name
        self.age = age

@classmethod
def data(cls, name, age):
        node = cls(name,age)
        node.name = name
        node.age = age
        return name ,age
    
    
    # Type hints for keyword arguments
def hello_world(greeting: str = 'Hello'):  
    print(greeting + ' world!')