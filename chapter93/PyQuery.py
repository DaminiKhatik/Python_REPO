from PyQuery import PyQuery 

html = """ 
<h1>Sales</h1>
<table id="table"> 
<tr>   
<td>Lorem</td>  
<td>46</td> </tr>
<tr>  
<td>Ipsum</td>
<td>12</td> 
</tr> 
<tr> 
<td>Dolor</td> 
<td>27</td> 
</tr> 
<tr> 
<td>Sit</td>
<td>90</td>
</tr> 
</table> """

doc = PyQuery("html.parcer")
title = doc('h1').text()
print (title)
table_data = []
rows = doc('#table > tr')
for row in rows: 
    name = PyQuery(row).find('td').eq(0).text()   
    value = PyQuery(row).find('td').eq(1).text()
    print ("%s\t  %s" % (name, value) )