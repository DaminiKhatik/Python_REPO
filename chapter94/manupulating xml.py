#Opening and reading using an ElementTree

import xml.etree.ElementTree as ET 
tree = ET.parse("hello.xml") 
root = tree.getroot("hello.xml")
print(root) 
# print the attributes of the first tag 
print(root[0].attribute) 
# print the text contained within first subtag of the 5th tag from the parent 
print(root[5][0].text) 
