# makedirs - recursive directory creation
import os
os.makedirs("./dir2/subdir1") 
os.makedirs("./dir2/subdir2")


#Create a directory


import os
directory = "helloworld"
parent_dir = "D:"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
print("Directory '% s' created" % directory)


###Get current directory
print(os.getcwd()) 

####Remove a directory
os.rmdir(path)

###Follow a symlink (POSIX)
print(os.readlink(path_to_symlink)) 


###Change permissions on a ﬁle

import os
import sys
import stat

# Setting the given file to be read by the owner.
os.chmod("C:\Users\Lenovo\Downloads\Work TP\trial.py", stat.S_IREAD)
print("The file can only be ready by owner")

# Setting the given file to be read by group.
os.chmod("C:\Users\Lenovo\Downloads\Work TP\trial.py", stat.S_IRGRP )
print("The file access gets changed, now it can be read by group.")

# Setting the given file to be read, write and execute by group.
os.chmod("C:\Users\Lenovo\Downloads\Work TP\trial.py", stat.S_IRWXG )
print("The file can be read, write and execute by group")

# Setting the given file to be read, write and execute by others.
os.chmod("C:\Users\Lenovo\Downloads\Work TP\trial.py", stat.S_IRWXO )
print("The file access gets changed, now it can be read, write and execute by others.")
