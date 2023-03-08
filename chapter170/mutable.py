b = bytearray(b'Stack') 
print(id(b))
b += b'Overflow' 
print(id(b))
"""This category includes: lists, dictionaries, bytearrays and sets.
"""
b += b'stackOverflow' 
print(id(b))
