import mmap
with open('filename.ext', 'r') as fd: 
    # 0: map the whole file  
    mm = mmap.mmap(fd.fileno(), 0)
 
 #Checking if a ﬁle is empty
import os 
def is_empty_file(fpath):   
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0


#Read a ﬁle between a range of lines
import itertools
with open('myfile.txt', 'r') as f: 
    for line in itertools.islice(f, 12, 30):
        
#Copy a directory tree
    import shutil source='//192.168.1.2/Daily Reports'
    destination='D:\\Reports\\Today' 
    
    # Copying contents of one ﬁle to a dierent ﬁle
with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file: 
    for line in in_file:   
        out_file.write(line)
