 # join Path
import os
path = "/desktop"
print(os.path.join(path, "Downloads", "file.txt", "/home"))



#Path Component Manipulation
import os
inputFilepath = 'C:/Users/cirus/Desktop/tutorialsPoint.pdf'
# Printing the given input path
print("Give Input Path is:",inputFilepath)
print("Base Name of the given path is :",os.path.basename(inputFilepath))


#Get the parent directory
os.path.abspath(os.path.join(PATH_TO_GET_THE_PARENT, os.pardir)) 

# If the given path exists
path = '/home/john/temp' 
os.path.exists(path)

#check if the given path is a directory, ﬁle, symbolic link, mount point etc
#to check if the given path is a directory
dirname = '/home/john/python'
os.path.isdir(dirname)
#to check if the given path is a ﬁle
filename = dirname + 'main.py' 
os.path.isfile(filename)
#to check if the given path is symbolic link
symlink = dirname + 'some_sym_link' 
os.path.islink(symlink)
#to check if the given path is a mount point
mount_path = '/home'
os.path.ismount(mount_path) 


# Absolute Path from Relative Path
os.getcwd()
os.path.abspath('foo') 