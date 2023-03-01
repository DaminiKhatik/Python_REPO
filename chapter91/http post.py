import urllib 
query_parms = {'username':'stackoverflow', 'password':'me.me'}
encoded_parms = urllib.urlencode(query_parms) 
response = urllib.urlopen("https://stackoverflow.com/users/login", encoded_parms)
response.code 