
def Recur_facto(n):

	if (n == 0):
		return 1

	return n * Recur_facto(n-1)

# print the result
print(Recur_facto(6))
