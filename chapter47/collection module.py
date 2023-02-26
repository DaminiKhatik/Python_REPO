#collections.Counter

import collections
counts = collections.Counter([1,2,3])
print(counts)
count1= collections.Counter('Happy Birthday') 
print(count1)
count2=collections.Counter('I am Sam Sam I am That Sam-I-am That Sam-I-am! I do not like that Sam-Iam'.split()) 
print(count2)


#collections.OrderedDict
from collections import OrderedDict
d = OrderedDict([('foo', 5), ('bar', 6)])
print(d)
OrderedDict([('foo', 5), ('bar', 6)])
d['baz'] = 7
print(d)
([('foo', 5), ('bar', 6), ('baz', 7)])
d['foobar'] = 8
print(d) 
OrderedDict([('foo', 5), ('bar', 6), ('baz', 7), ('foobar', 8)])
print(d)


#collections.namedtuple
from collections import namedtuple
Person = namedtuple('Person', 'age height name')

jack = Person(age=30, height=178, name='Jack S.')

print(jack.age) 
# 30 
print(jack.name) 


#collections.deque
from collections import deque
d=deque('hello')
print(d)
d.append('j') 
print(d)
d.appendleft('f')
print(d)
d.pop() 
print(d)
d.popleft() 
print(d)


#collections.ChainMap
import collections
from collections import ChainMap
dict1 = {'apple': 1, 'banana': 2} 
dict2 = {'coconut': 1, 'date': 1, 'apple': 3}
combined_dict = collections.ChainMap(dict1, dict2) 
print(combined_dict)
reverse_ordered_dict = collections.ChainMap(dict2, dict1)
print(reverse_ordered_dict)


#collections.defaultdict
import collections
from collections import defaultdict
state_capitals = collections.defaultdict(str) 
print(state_capitals)
