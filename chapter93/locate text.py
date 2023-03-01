from bs4 import BeautifulSoup
data = """ 
<div>   
<label>Name:</label>    
damiiiiii khatikkk </div> """
soup = BeautifulSoup(data, "html.parser")
label = soup.find("label", text="Name:") 
print(label.next_sibling.strip())
