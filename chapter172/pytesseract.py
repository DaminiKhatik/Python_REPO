
from PIL import Image
import pytesseract
  
string = pytesseract.image_to_string('C:/Users/MyHP/Desktop/PYTHONbook/chapter172/images2.png')
print(string)