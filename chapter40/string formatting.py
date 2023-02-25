#basic of  String Formatting
print('We all are {}.'.format('equal'))


foo = 1
bar = 'bar'
baz = 3.14
print('{}, {} and {}'.format(foo, bar, baz)) 

#Alignment and padding

left_alignment = "Left Text"
center_alignment = "Centered Text"
right_alignment = "Right Text"

# printing out aligned text
print(f"{left_alignment : <20}{center_alignment : ^15}{right_alignment : >20}")


# Creating a string variable
str = "helllllooooo"

# Printing the output of ljust() method
print(str.ljust(20, 'f'))

#left padding with f