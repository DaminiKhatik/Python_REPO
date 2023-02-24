d = {'a': 1, 'b': 2, 'c':3}
for key in d:
    print(key, d[key])
#2nd Way
for key, value in d.items():
    print(key, value)
#3rd way
print([key for key in d])