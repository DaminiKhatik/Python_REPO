from itertools import cycle, islice

sequence = cycle(["G", "D", "e", "C"])

schords = [a for a in islice(sequence, 25)]

print(schords)

