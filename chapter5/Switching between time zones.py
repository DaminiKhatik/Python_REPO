from datetime import datetime 
from dateutil import tz


utc = tz.tzutc() 
print(utc)

local = tz.tzlocal()
print(local)

utc_now = datetime.utcnow() 

print(utc_now)

utc_now = utc_now.replace(tzinfo=utc) 
print(utc_now)

local_now = utc_now.astimezone(local)
print(local_now)