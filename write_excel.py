#!/usr/bin/python
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell
from xlsxwriter.utility import xl_range

# Create a workbook and add a worksheet.
yingbook = xlsxwriter.Workbook('test.xlsx')
yingsheet = yingbook.add_worksheet()

# Some data we want to write to the worksheet.
expenses = (
                ['Rent', 1000],
                ['Gas',   100],
                ['Food',  300],
                ['Gym',    50],
                )

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item, cost in (expenses):
        yingsheet.write(row, col, item)
        yingsheet.write(row, col + 1, cost)
        row += 1

# Write a total using a formula.
yingsheet.write(row, 0, 'Total')
yingsheet.write(row, 1, '=SUM(B1:B4)')

# Add another sheet named "mysheet"
mysheet = yingbook.add_worksheet("mysheet")
mysheet.write(0, 0, 'test')

row += 1
# let one cell equal to another cell
yingsheet.write(row, 0, '=A1')
row += 1
# let one cell in one sheet equal to cell in another sheet
yingsheet.write(row, 0, '=mysheet!A1')

cell = xl_rowcol_to_cell(0, 0)          # A1
cell_range = xl_range(0, 0, 9, 0)       # A1:A10
# SUM(A1:A10)
yingsheet.write(row, 1, '=SUM(' + cell_range +')')

yingbook.close()
