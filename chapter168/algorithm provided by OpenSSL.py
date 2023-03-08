# MD5 hash of a string

import hashlib
string = b"hello buddies!"
sha256 = hashlib.sha256()
sha256.update(string)
string_hash = sha256.hexdigest()

print(f"Hash:{string_hash}")

"""output:

Hash:54e2e4f27b98b0b2ec2a2b7ebdcf8c8d19bef555d66e8a1eaada3af04f34cb77
"""