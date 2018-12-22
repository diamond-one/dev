# https://automatetheboringstuff.com/chapter12/

# Make a dictonary from excel

import openpyxl

wb = openpyxl.load_workbook('test.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
frames = {}

   # TODO: Fill in countyData with each county's population and tracts.

for row in range(2, sheet.max_row + 1):
       # Each row in the spreadsheet has data for one census tract.
       state  = sheet['B' + str(row)].value
       county = sheet['C' + str(row)].value
       pop    = sheet['D' + str(row)].value
