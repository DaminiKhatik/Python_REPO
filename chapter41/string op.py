txt = "Hello" [::-1]
print(txt)


#Replace all occurrences of one substring with another substring
input_string = "hiiiihellohiiii"
s1 = "hiiii"
s2 = "abcd"
input_string = input_string.replace(s1, s2)
print(input_string)


#Testing what a string is composed of
a="Hello World".isalpha()
print(a)

b="Hello2World".isalpha()
print(b)

c="HelloWorld!".isalpha()
print(c)

d="HelloWorld".isalpha() 
print(d)

e="Hello world".islower() 
print(e)

e1="hello world".islower() 
print(e1)

f="HELLO WORLD".isupper() 
print(f)

f1="HELLO worLD".isupper() 
print(f1)


