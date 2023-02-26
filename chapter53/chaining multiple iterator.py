from itertools import chain
odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]

# chaining odd and even numbers
numbers = list(chain(odd, even))

print(numbers)
