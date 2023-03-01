import xml.etree.ElementTree as ET
p=ET.Element('parent')
c = ET.SubElement(p, 'child1')
c1 = ET.SubElement(p, 'child2')


#dump() function is used to dump xml elements.
ET.dump(p) 
tree = ET.ElementTree(p) 
tree.write("hello.xml")

#Comment() function is used to insert comments in xml ﬁle.
comment = ET.Comment('this is my xml file') 
p.append(comment) 