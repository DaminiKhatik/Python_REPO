#Zipping two iterators until they are both exhausted
import itertools
from itertools import zip_longest
s1 = {12, 13,11}
s2 = {'l', 'm', 'k'}
s3={"hiii","hello","hey"}

for t in zip_longest(s1, s2,s3):
    print(t)