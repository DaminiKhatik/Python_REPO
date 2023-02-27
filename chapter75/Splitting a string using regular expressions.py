#Splitting a string using regular expressions

import re 
data = re.split(r'\s+', 'James 94 Samantha 417 hiiiii Scarlett 74')
print( data )