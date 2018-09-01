import math
import csv
import xlrd

def evalInt(value):
    """
    If submitted value can be converted to int, the respective int is returned.
    Else math.nan is returned.
    """
    try:
        return int(value)
    except ValueError:
        return math.nan

categories = dict()
with open('data/table.csv', newline='\n', encoding='UTF-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        categories[row[0]] = [int(x) for x in row[1:]]


book = xlrd.open_workbook('data/consolidated.xls')
first_sheet = book.sheet_by_index(0)

lines = list()
for n in range(first_sheet.nrows):
    label = first_sheet.cell(n, 0).value
    if label in categories.keys():
        for i,y in enumerate(range(2010, 2017)):
            data = [y] + [evalInt(x.value) for x in first_sheet.row_slice(rowx=n, start_colx=5*i+1, end_colx=5*i+6)]
            line = categories[label] + data
            lines.append(line)

with open('data/data.csv', 'a', newline='\n', encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerows(lines)
