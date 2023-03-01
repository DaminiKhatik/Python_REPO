# factorial function

def two_sum(a, b):  
   return a + b
   print("addition of two number")



# NamedTuple
import typing 
from typing import NamedTuple
class mydet(NamedTuple):
    name: str
    age: int
    genter: str
# creating a NamedTuple
my_details = mydet('damini_khatik',23,'female')
print(my_details)





# Generic Types
from typing import List, TypeVar

T = TypeVar("T")

def first(container: List[T]) -> T:
    return container[0:2]

  
if __name__ == "__main__":
    list_one: List[str] = ["a", "b", "c"]
    print(first(list_one))
    
    list_two: List[int] = [1, 2, 3]
    print(first(list_two))