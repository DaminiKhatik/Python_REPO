# importing required modules
from zipfile import ZipFile
file_name = "C:/Users/MyHP\Desktop/PYTHONbook/chapter131/cakeshop.zip"
# opening the zip file in READ mode
with ZipFile('C:/Users/MyHP\Desktop/PYTHONbook/chapter131/cakeshop.zip', 'r') as zip:
	
	zip.printdir()
	print('Extracting all the files now...')
	zip.extractall()
	print('Done!')
