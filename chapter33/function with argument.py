def my_function(fname):
  print(fname + " hiiiii")

my_function("devil")
my_function("Toshib")
my_function("shehnaz")


#Iterable and dictionary unpacking
d = {'k1':10, 'k2':20, 'k3':30}
new = {'k0':0, **d}
print(new) 



#Deﬁning a function with multiple arguments
# function definitio
def displayArgument(**arguments):
	for arg in arguments.items():
		print(arg)

# function call
displayArgument(argument1 ="welocme", argument2 = "to",
				argument3 ="BIT")
