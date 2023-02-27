#Basic Slicing
a = "abcdef" 
print(a[-1])        
print(a[:]  )       
print(a[::])      
print(a[3:]  )      
print(a[:4])        

print(a[::2] ) 

print(a[1:4:2]) 
print(a[:-1])
print(a[3:1:-1])
print(a[::-1] )


#Reversing an object
s = 'reverse me!'
print(s[::-1])    # '!em esrever'


# Slice assignment
lst = [1, 2, 3]
lst[1:3] = [4, 9,5]
print(lst)#This means that if you have a list, you can replace multiple members in a single assignment

lst = [1, 2, 3, 4, 5] 
lst[1:4] = [6] 
print(lst) # Out: [1, 6, 5]

lst = [1, 2, 3] 
lst[:] = [4, 5, 6]
print(lst) # Out: [4, 5, 6]

lst = [1, 2, 3] 
lst[-2:] = [4, 5, 6]
print(lst) 


#Making a shallow copy of an array
arr = ['a', 'b', 'c'] 
copy = arr[:] 
print(arr)
print(copy)  
copy.append('d')  
print(copy)  



