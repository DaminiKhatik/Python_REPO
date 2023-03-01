try:

     x = int(input('Enter a positive integer: '))

     if x <= 0:

         raise ValueError('It is not a positive number!')

except ValueError as val_e:

    print(val_e)