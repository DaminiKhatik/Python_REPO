import zipfile

fh = open('C:/Users/MyHP\Desktop/PYTHONbook/chapter131/cakeshop.zip', 'rb')
z = zipfile.ZipFile(fh)
for name in z.namelist():
    outpath = "C:/Users/MyHP\Desktop/PYTHONbook/chapter132"
    z.extract(name, outpath)
fh.close()