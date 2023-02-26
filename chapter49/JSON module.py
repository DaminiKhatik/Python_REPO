#Storing data in a ﬁle

import json
d = {
    'foo': 'bar',
     'alice': 1,
     'wonderland': [1, 2, 3] 
     }

with open('a.txt', 'w') as f:    
    json.dump(d, f)
    
    
    #Retrieving data from a ﬁle
import json
with open('a.txt', 'r') as f:  
    d = json.load(f) 
    
    #Formatting JSON output
import json
data = {"cats": [{"name": "Tubbs", "color": "white"}, {"name": "Pepper", "color": "black"}]}
print(json.dumps(data)) 


#`load` vs `loads`, `dump` vs `dumps`
import json
data = {u"foo": u"bar", u"baz": []}
json_string = json.dumps(data) # u'{"foo": "bar", "baz": []}' 
print(json.dumps(data))
json.loads(json_string) # {u"foo": u"bar", u"baz": []}
print(json_string)

#JSON encoding custom objects


import json 
from datetime import datetime
data = {'datetime': datetime(2016, 9, 26, 4, 44, 0)} 

class DatetimeJSONEncoder(json.JSONEncoder):    
    def default(self, obj):       
        try:          
            return obj.isoformat() 
            except AttributeError:            
            return super(DatetimeJSONEncoder, self).default(obj)
            encoder = DatetimeJSONEncoder() 
            print(encoder.encode(data)) 


# Creating JSON from Python dict
import json 
d = {    'foo': 'bar', 
'alice': 1,  
'wonderland': [1, 2, 3] 
} 
print(json.dumps(d))


#Creating Python dict from JSON
import json 
s = '{"wonderland": [1, 2, 3], "foo": "bar", "alice": 1}' 
print(json.loads(s))
