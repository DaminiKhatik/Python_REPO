import gzip 
import os
f_in = open('C:/Users/MyHP/Desktop/PYTHONbook/chapter133/hellow.txt')
f_out = gzip.open('C:/Users/MyHP/Desktop/PYTHONbook/chapter133/hellow.txt.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()