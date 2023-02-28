#The What, How, and When of Recursion
"""Recursion occurs when a function call causes that same function to be called again before the original function call terminates"""

#Sum of numbers from 1 to n

n = 0 
for i in range (1, n+1): 
    n += i
print(n)

# using a Tail-Recursive function.

# A tail recursive function
def Recur_facto(n, a = 1):

	if (n == 0):
		return a

	return Recur_facto(n - 1, n * a)


print(Recur_facto(9))
