#Store data
import pickle 


data={'a':'some_value', 
      'b':[9,4,7],    
      'c':['some_str','another_str','spam','ham'], 
      'd':{'key':'nested_dictionary'},     }

file=open('C:/Users/MyHP/Desktop/PYTHONbook/chapter166/hello.txt','wb')  #file object in binary write mode 
pickle.dump(data,file)      #dump the data in the file object 
file.close() 

#Load data

data={'b': [9, 4, 7], 'a': 'some_value', 'd': {'key': 'nested_dictionary'}, 'c': ['some_str', 'another_str', 'spam', 'ham']}

import pickle 
file=open('C:/Users/MyHP/Desktop/PYTHONbook/chapter166/hello.txt','rb')  #file object in binary read mode 
data1=pickle.load(file)      #load the data back 
file.close()

