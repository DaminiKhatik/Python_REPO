#Deque Module

#Basic deque using
from collections import deque
d = deque([1, 2, 3])
p = d.popleft()        
d = deque([2, 3])
d.appendleft(5)   
print(d)

# Available methods in deque
#Creating empty deque:
dl = deque() 
print(dl)
#Creating deque with some elements:
dl = deque([1, 2, 3, 4])  # deque([1, 2, 3, 4])
print(dl)

#Adding element to deque:
dl.append(5)  # deque([1, 2, 3, 4, 5])
print(dl)

#Adding element left side of deque:
dl.appendleft(0)  # deque([0, 1, 2, 3, 4, 5])
print(dl)

#Adding list of elements to deque:
dl.extend([6, 7])  # deque([0, 1, 2, 3, 4, 5, 6, 7])
print(dl)

#Adding list of elements to from the left side:
dl.extendleft([-2, -1])  # deque([-1, -2, 0, 1, 2, 3, 4, 5, 6, 7])
print(dl)

#Using .pop() element will naturally remove an item from the right side:
dl.pop()  # 7 => deque([-1, -2, 0, 1, 2, 3, 4, 5, 6])
print(dl)

#Using .popleft() element to remove an item from the left side:
dl.popleft()  # -1 deque([-2, 0, 1, 2, 3, 4, 5, 6])
print(dl)

#Remove element by its value:
dl.remove(1)  # deque([-2, 0, 2, 3, 4, 5, 6])
print(dl)

#Reverse the order of the elements in deque:
dl.reverse()  # deque([6, 5, 4, 3, 2, 0, -2]) 
print(dl)


############limit deque size
from collections import deque
d2 = deque(maxlen=3)  # only holds 3 items 
d2.append(1)  # deque([1]) 
d2.append(2)  # deque([1, 2]) 
d2.append(3)  # deque([1, 2, 3]) 
d2.append(4)  # deque([2, 3, 4]) (1 is removed because its maxlen is 3) 
print(d2)
            