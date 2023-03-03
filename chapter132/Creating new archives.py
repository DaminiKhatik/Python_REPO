import zipfile
from zipfile import ZipFile
zipObj = ZipFile('myzip.zip', 'w')
# Add multiple files to the zip
zipObj.write('C:/Users/MyHP/Desktop/PYTHONbook/chapter130/data.csv')

# close the Zip File
zipObj.close()