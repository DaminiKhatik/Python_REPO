#Counting all occurrence of all items in an iterable: collections.Counter

from collections import Counter
c = Counter(["a", "b", "c", "d", "a", "b", "a", "c", "d"])
print(c)

#Getting the most common value(-s): collections.Counter.most_common()
from collections import Counter 
adict = {'a': 5, 'b': 3, 'c': 5, 'd': 2, 'e':2, 'q': 5} 
a=Counter(adict.values())
print(a)


#Counting the occurrences of one item in a sequence: list.count() and tuple.count()
atuple = ('bear', 'weasel', 'bear', 'frog') 
b=atuple.count('bear') 
print(b)