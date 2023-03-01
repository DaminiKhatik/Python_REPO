
import urllib
import urllib.request 
response = urllib.request.urlopen("http://stackoverflow.com/") 
data = response.read()
encoding = response.info().getencoding() 
html = data.decode(encoding)