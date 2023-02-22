def a1():
	name = "hello" # Our local variable

	def bar():
		nonlocal name		 # Reference name in the upper scope
		name = 'hello,world ' # Overwrite this variable
		print(name)
		
	# Calling inner function
	bar()
	
	# Printing local variable
	print(name)

a1()
