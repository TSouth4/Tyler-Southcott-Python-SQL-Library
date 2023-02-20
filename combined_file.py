import time
from pathlib import Path
import xlwings as xw

source_dir = 'Timesheets'
excel_files = list(Path(source_dir).glob('*.xlsx'))
t = time.localtime()
timestamp = time.strftime('%Y-%m-%d', t)
combined_wb = xw.Book()

for excel_file in excel_files:
    wb = xw.Book(excel_file)
    for index, sheet in enumerate(wb.sheets):
        sheet.copy(after=combined_wb.sheets[0])
        if index > 0:
            combined_wb.sheets.active.name = wb.name + str(index)
        else:
            combined_wb.sheets.active.name = wb.name
    wb.close()

combined_wb.sheets[0].delete()
combined_wb.save(f'all_timesheets_{timestamp}.xlsx')
if len(combined_wb.app.books) == 1:
    combined_wb.app.quit()
else:
    combined_wb.close()



