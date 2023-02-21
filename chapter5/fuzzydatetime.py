from dateutil.parser import parse
dt = parse("Today is January 1, 2047 at 8:21:00AM", fuzzy=True) 
print(dt)
