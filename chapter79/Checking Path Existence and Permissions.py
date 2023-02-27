import os
path = "C:\Program Files\Internet Explorer"

print(os.access(path, os.F_OK)) # existence of path
print(os.access(path, os.R_OK)) # readiability of path
print(os.access(path, os.W_OK)) # whether it is writable or not
print(os.access(path, os.X_OK)) #whether it is executable or not