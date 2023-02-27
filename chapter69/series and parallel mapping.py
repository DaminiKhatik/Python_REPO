#series map

insects = ['fly', 'ant', 'beetle', 'cankerworm'] 
f = lambda x: x + ' is an insect' 
print(list(map(f, insects))) 

#parallel map

def animals(w, x, y):   
    return '{0}, {1}, {2} ARE ALL ANIMALS'.format(w.title(), x, y)

carnivores = ['lion', 'tiger', 'leopard', 'arctic fox'] 
herbivores = ['african buffalo', 'moose', 'okapi', 'parakeet'] 
omnivores = ['chicken', 'dove', 'mouse', 'pig']

import pprint 
pprint.pprint(list(map(animals,  carnivores, herbivores, omnivores)))