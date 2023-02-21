from datetime import datetime, timedelta 
now = datetime.now() 
then = datetime(2016, 5, 23) 
pdelta = now-then
print(pdelta.days) # 60 
print(pdelta.seconds) # 40826
