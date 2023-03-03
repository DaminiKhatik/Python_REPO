
import zipfile
from zipfile import ZipFile

with zipfile.ZipFile("C:/Users/MyHP\Desktop/PYTHONbook/chapter131/cakeshop.zip") as zip: 
    zip.printdir()
"""get a list of ﬁlenames with the namelist method."""