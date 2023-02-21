from datetime import datetime 
datetime_for_string = datetime(2016,10,1,0,0) 
print(datetime_for_string)
datetime_string_format = '%b %d %Y, %H:%M:%S' 
print(datetime_string_format)
datetime.strftime(datetime_for_string,datetime_string_format)