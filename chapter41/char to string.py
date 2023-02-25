translation_table = str.maketrans("aeiou", "12345") 
my_string = "This is a string!"
translated = my_string.translate(translation_table) 
print(translated)


#str.format and f-strings: Format values into a string

txt1 = "My name is {0}, I'm {1}".format("Jhoi",36)
#empty placeholders:
txt2 = "My name is {}, I'm {}".format("John",39)
print(txt1)
print(txt2)


