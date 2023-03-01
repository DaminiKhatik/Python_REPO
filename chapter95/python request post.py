# Simple Post
from requests import post
link = post('https://www.justdial.com/Nagpur/Canon-Image-Square-Near-Mahal-Mahal/0712PX712-X712-130120160002-Z6Y9_BZDET', data = {'key':'value'})
print(link)
print(link.headers)

#Form Encoded Data
from requests import post
payload = {'key1' : 'value1', 'key2' : 'value2'  }
foo = post('http://httpbin.org/post', data=payload)
print(foo)

