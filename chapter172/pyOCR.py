from PIL import Image
import sys
import pyocr
import pyocr.builders

txt = tool.image_to_string( Image.open('C:/Users/MyHP/Desktop/PYTHONbook/chapter172/images2.png'),  lang=lang, builder=pyocr.builders.TextBuilder() ) 
print(txt)

word_boxes = tool.image_to_string(Image.open('C:/Users/MyHP/Desktop/PYTHONbook/chapter172/images2.png'),    lang="eng",    builder=pyocr.builders.WordBoxBuilder() ) 
print(word_boxes)

line_and_word_boxes = tool.image_to_string( Image.open('C:/Users/MyHP/Desktop/PYTHONbook/chapter172/images2.png'), lang="fra",    builder=pyocr.builders.LineBoxBuilder() ) 
print(line_and_word_boxes)

digits = tool.image_to_string( Image.open('C:/Users/MyHP/Desktop/PYTHONbook/chapter172/images2.png'),    lang="eng",    builder=pyocr.tesseract.DigitBuilder() ) 
print(digits)