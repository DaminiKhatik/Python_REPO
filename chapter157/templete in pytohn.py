"""Simple data output program using template
"""

from string import Template
data = dict(item = "candy", price = 8, qty = 2)
# define the template 
t = Template("Simrann bought $qty $item for $price dollar")
print(t.substitute(data))

"""Changing delimiter
"""

from string import Template
class MyOtherTemplate(Template):  
     delimiter = "#"
data = dict(id = 465, name = "damini")
t = MyOtherTemplate("My name is #name and I have the id: #id") 
print(t.substitute(data))
