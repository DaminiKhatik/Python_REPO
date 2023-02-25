# Using the print function

print("you can enter here what you want to print")

#Input from a File
# import fileinput
import fileinput

# Using fileinput.input() method
for line in fileinput.input(files ='hello.txt'):
	print(line)

#Read from stdin

import sys

for line in sys.stdin:

 print(f'Input : {line}')
 
 #Using input() and raw_input()


val1 = input("Enter the name: ")
 
# print the type of input value
print(type(val1))
print(val1)
 
 #raw_input()
name = raw_input("Enter a name : ")
print(type(name))

# Printing a string without a newline at the end
print("Hello, ", end="\n") 
print("World!") 

print("Hello, ", end="") 
print("World!") 