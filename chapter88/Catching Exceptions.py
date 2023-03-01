try:   
    x = 5 / 0 
except ZeroDivisionError as e: 
 print("Got a divide by zero! The exception was:", e) 
 x = 0 
finally:    
    print("The END") 
    
    
    
    x = 5
y = "hello"
z = x + y # Raises a TypeError: unsupported operand type(s) for +: 'int' and 'str'
