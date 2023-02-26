from itertools import permutations

a = "HELLO"

p = permutations(a)

# Print the obtained permutations
for j in list(p):
    print(j)
