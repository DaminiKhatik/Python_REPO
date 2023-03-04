#Individual characters of strings are not assignable
foo = "bar"
foo[0] = "c"
print(foo)


#Tuple's individual members aren't assignable
foo1 = ("bar", 1, "Hello!",) 
foo1[1] = 2 
print(foo1)

#Frozenset's are immutable and not assignable
foo2 = frozenset(["bar", 1, "Hello!"])
foo2[2] = 7 # ERROR 
foo2.add(3)
print(foo2)