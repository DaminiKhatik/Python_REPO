from struct import pack
print(pack('I3c', 123, b'a', b'b', b'c')) 


#Unpack a byte object according to a format string
from struct import unpack
print(unpack('I3c', b'{\x00\x00\x00abc')) 