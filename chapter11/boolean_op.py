#A simple example
x=8
if 3.14 < x < 3.142:  
    print("x is near pi")

# and
x = True 
y = True 
z = x and y
print(z)#true

x = False 
y = True 
z = x and y
print(z)#False

x = True 
y = False 
z = x and y
print(z)#False

x = False 
y = False 
z = x and y
print(z)#False



# or
x = True 
y = True 
z = x or y
print(z)#true

x = False 
y = True 
z = x or y
print(z)#true

x = True 
y = False 
z = x or y
print(z)#true

x = False 
y = False 
z = x or y
print(z)#False

#not
x = True 
y = not x 
print(y)
# y = False
x = False 
y = not x
print(y)
# y = True