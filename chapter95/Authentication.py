from requests import post 
from requests.auth import HTTPDigestAuth
foo = post('http://google.com', auth=HTTPDigestAuth('natas0', 'natas0'))




#Proxies
import requests

proxies = {
   'http': 'http://proxy.example.com:8080',
   'https': 'http://secureproxy.example.com:8090',
}

url = 'http://mywebsite.com/example'

response = requests.post(url, proxies=proxies)