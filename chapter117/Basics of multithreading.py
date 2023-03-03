
import threading

def print_square(num):
	# function to print square of given num
	print("Square: {}" .format(num * num))


if __name__ =="__main__":
	# creating thread
	t = threading.Thread(target=print_square, args=(5,))
	

	# starting thread 1
	t.start()

	# wait until thread 1 is completely executed
	t.join()
	
	# both threads completely executed
	print("Done!")
