# Encoding and Decoding Base64
import base64 
s = "Hello World!"
b = s.encode("UTF-8")
print(b)
e = base64.b64encode(b)
print(e)
f=e.decode("UTF-8")
print(f)

# Encoding and Decoding Base32
import base64
from base64 import b32encode
s1 = b'I love python'
# Using base64.b32encode() method
h = b32encode(s1)
print(h)

#Encoding and Decoding Base16
import base64
from base64 import b16encode
s1 = b'I love python'
# Using base64.b16encode() method
h2= b16encode(s1)
print(h2)


#Encoding and Decoding Base85
import base64
from base64 import b85encode
s1 = b'I love python'
# Using base64.b16encode() method
h21= b85encode(s1)
print(h21)

#Encoding and Decoding ASCII85
import base64
from base64 import a85encode
s1 = b'I love python'
# Using base64.b16encode() method
h3= a85encode(s1)
print(h3)