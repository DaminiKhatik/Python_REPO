 
x = 10.0
print("Type of a: ", type(x))
  
y =9
print("\nType of b: ", type(y))
  
z = 2 + 9j
print("\nType of c: ", type(z))
print("----------------------------------------")


Stringone = "hiiiiii"
print(Stringone) 
    

# with triple Quotes 
Stringtwo = '''hi'My name is"damini"'''
print(Stringtwo) 
print(type(Stringtwo))
  
# Quotes allows multiple lines 
String1 = '''i am 
            Damini'''
print("\nCreating a multiline String: ") 
print(String1) 

#Built-in Types
#Booleans
print(" Python program to demonstrate boolean type")
  
print(type(True))
print(type(False))
print("----------------------------------------")
x=False
y=True
x or y       # if x is False then y otherwise x
print(type(x))
print(x)
x and y      # if x is False then x otherwise y
print(type(y),x)
not x        # if x is True then False, otherwise True
print(type(x),x)

print("boolean values are used in arithmetic operations(1 and 0 for True and False)")
a=True + False == 1   
b=True * True == 1    
print(a)
print(b)
print("----------------------------------------")
# Python program to demonstrate numeric value