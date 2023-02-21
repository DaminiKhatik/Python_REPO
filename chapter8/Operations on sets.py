#intersection
a={1, 2, 3, 4, 5}.intersection({3, 4, 5, 6}) # {3, 4, 5}
#use & operator

print(a)

# Union 
b={1, 2, 3, 4, 5}.union({3, 4, 5, 6}) 
print(b)
# {1, 2, 3, 4, 5, 6}
#use | operator

# Difference
c={1, 2, 3, 4}.difference({2, 3, 5})  # {1, 4} #use- operator
print(c)
# Symmetric difference with
g={1, 2, 3, 4}.symmetric_difference({2, 3, 5}) # {1, 4, 5}
#use ^ operator               
print(g)
# Superset check
d={1, 2}.issuperset({1, 2, 3})  # False
 #use >= operator
print(d)
# Subset check
e={1, 2}.issubset({1, 2, 3})  # True
#use  <= operator
print(e)
# Disjoint check
f={1, 2}.isdisjoint({3, 4})  # True 

print(f)