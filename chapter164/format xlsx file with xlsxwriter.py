import xlsxwriter
from openpyxl import Workbook 

workbook = xlsxwriter.Workbook("C:/Users/MyHP/Desktop/PYTHONbook/chapter164/datafile.xlsx")

percent_format = workbook.add_format({'num_format': '0%'})

percent_with_decimal = workbook.add_format({'num_format': '0.0%'})

bold = workbook.add_format({'bold': True})

red_font = workbook.add_format({'font_color': 'red'})
remove_format = workbook.add_format()

print(workbook)
worksheet = workbook.add_worksheet()
# set the width of column A 
wroksheet=worksheet.set_column('A:A', 30, )
# set column B to 20 and include the percent format we created earlier
wroksheet=worksheet.set_column('B:B', 20, percent_format)
# remove formatting from the first row (change in height=None) 
wroksheet=worksheet.set_row('0:0', None, remove_format)
workbook.close() 