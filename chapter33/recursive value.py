# importing the sys module
import sys
sys.setrecursionlimit(10**6)

def fact(n):

	if(n == 0):
		return 1

	return n * fact(n - 1)

if __name__ == '__main__':

	# taking input
	f = int(input('Enter the number: \n'))

	print(fact(f))
