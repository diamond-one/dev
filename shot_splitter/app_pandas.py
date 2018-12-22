import numpy

# import pandas as pd
# df = pd.ExcelFile("test.xlsx")
# sheet = df.sheet_names()
# print (sheet)

import openpyxl
wb = openpyxl.load_workbook('test1.xlsx')
sheet = wb.active

for cellObj in sheet.columns:
        print(cellObj.value)

# for cellObj in sheet.columns[3]:
#         print(cellObj.value)

#
# #here you iterate over the rows in the specific column
# for rows in range(2,sheet.max_row+1):
#     for row in "D":  #Here you can add or reduce the columns
#         frames = "{}{}".format(row, rows)
#         print (sheet[frames].value) # the value of the specific cell
#Finding the number of rows (Pandas)
# rownum = sheet.range('A1').end('down').last_cell.row


