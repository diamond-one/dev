#Create a dictionary of animators , and the animators start with no shots/frames/seconds
#create a dictornay of shots from an excel, each shot has frames/seconds attached to it
#Assign shots to animators and it adds to their overall seconds
#Shots given out, reduce the amount of seconds left in episode counter.
#

import openpyxl

import math

wb = openpyxl.load_workbook('test.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
# sheet['D1'].value = 'bazinga'
# wb.save('test1.xlsx')

# total = sheet[D:]

#here you iterate over the rows in the specific column
for rows in range(2,sheet.max_row+1):
    for row in "D":  #Here you can add or reduce the columns
        frames = "{}{}".format(row, rows)
        print (sheet[frames].value) # the value of the specific cell


#Animators
assignee = {
    "Eric : ,"
    "Mary : ,"
    "John : ,"}


