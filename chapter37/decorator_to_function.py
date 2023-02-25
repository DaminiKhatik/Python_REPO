def my_decorator(func):
	def wrapper_function(*args, **kwargs):
		print("*"*10)
		func(*args, **kwargs)
		print("*"*10)
	return wrapper_function


def say_hello():
	print("Hello !")

@my_decorator
def say_bye():
	print("Bye !")


say_hello = my_decorator(say_hello)
say_hello()
say_bye()
