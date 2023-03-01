from requests import post
foo = post('http://httpbin.org/post', data={'data' : 'value'}) 
print(foo.status_code)
