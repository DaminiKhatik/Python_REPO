
#Creating an enum (Python 2.4 through 3.3)

from enum import Enum

class Season(Enum):
	SPRING = 1
	SUMMER = 2
	AUTUMN = 3
	WINTER = 4

for fruit in (Season):
	print(fruit.value,"-",fruit)

#Iteration
from enum import Enum
class Shake(Enum):
  vanilla = 7
  chocolate = 4  
  cookies = 9
  mint = 3
for s in Shake:
    print(s,"=",s.value)