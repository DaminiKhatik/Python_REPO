# MD5 hash of a string

import hashlib
string = "hello buddies!"
sha256 = hashlib.sha256()
sha256.update(string)
string_hash = sha256.digest()

print(f"Hash:{string_hash}")

"""output:

Hash:'T\xe2\xe4\xf2{\x98\xb0\xb2\xec*+~\xbd\xcf\x8c\x8d\x19\xbe\xf5U\xd6n\x8a\x1e\xaa\xda:\xf0O4\xcbw'

"""