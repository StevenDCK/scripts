import xlwt

Excel = xlwt.Workbook(encoding = 'ascii')
Table = Excel.add_sheet('Table1')
Table.write(0, 0, label = 'Hello Worlds')
Excel.save('dbs.xls')