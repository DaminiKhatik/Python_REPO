import urllib
import urllib.request
request_url = urllib.request.urlopen('https://google.com')
print(request_url.read())
