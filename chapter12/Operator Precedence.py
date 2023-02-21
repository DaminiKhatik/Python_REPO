# Simple Operator Precedence Examples in python

a, b, c, d = 2, 3, 5, 7 
a1=a ** (b + c) # parentheses 
print(a1)
a2=a * b ** c # exponent: same as `a * (b ** c)` 
print(a2)

a3=a + b * c / d # multiplication / division: same as `a + (b * c / d)` 
print(a3)
