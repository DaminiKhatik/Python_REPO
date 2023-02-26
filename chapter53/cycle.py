
import itertools as it 
cycle_iterator = it.cycle('abc123')
[next(cycle_iterator) for i in range(0, 10)]
print(cycle_iterator)