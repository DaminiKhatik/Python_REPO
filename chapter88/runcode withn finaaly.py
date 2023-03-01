try:  
    data = {1: 'one', 2: 'two'}  
    print(data[1])
except KeyError as e: 
    print('key not found') 
else:  
    print("Yeah ! Your answer")
finally:
    print("your answer is here")
