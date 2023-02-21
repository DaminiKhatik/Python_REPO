import time 
from datetime  import datetime 
seconds_since_epoch=time.time()  #1469182681.709
print(seconds_since_epoch)
utc_date=datetime.utcfromtimestamp(seconds_since_epoch)
print(utc_date)