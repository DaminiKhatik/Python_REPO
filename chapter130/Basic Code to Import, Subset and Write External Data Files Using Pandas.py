import os 
print (os.getcwd()) 

os.chdir('C:/Users/MyHP\Desktop/PYTHONbook/chapter130') 
print (os.getcwd()) 
import pandas as pd

my_data = pd.read_csv("data.csv") 
print(my_data)

a=my_data.shape       # number of rows and columns in data set # (4, 3)
print(a)
b=my_data.shape[0]    # number of rows in data set # 4
print(b)
c=my_data.shape[1]    # number of columns in data set 
print(c)
d=my_data[0:2]        # Select the first two rows 
print(d)

e=my_data[1:3]        # Select the second and third rows 
print(e)

# Select the first two elements of the first column 
f=my_data.iloc[0:2, 0:1] 
print(f)

# Select the first three elements of the variables y and z
i=my_data.loc[0:2, ['y', 'z']]
print(i)