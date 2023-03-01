#Custom Exception
class CustomError(Exception):      
    pass
x = 1
if x == 1:    
    raise CustomError('This is custom error')

############################
#Catch custom Exception
class CustomError(Exception):     
    pass
try: 
    raise CustomError('Can you catch me ?') 
except CustomError as e:   
    print ('Catched CustomError :{}'.format(e)) 
except Exception as e:   
    print ('Generic exception: {}'.format(e))
