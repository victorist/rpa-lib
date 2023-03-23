import camelot
import pandas as pd
tables = camelot.read_pdf('rpa-lib/pdf_processing/Ticket Sales Report DEC. 2022 HRG.pdf')

print("_"*80)
print("Кол-во таблиц в документе:", tables)
print("_"*80)
print("анализ конвертации:\n")
print(tables[0].parsing_report)

# Export one table
tables[0].to_excel('rpa-lib/pdf_processing/table_from_pdf-1.xls')

# Data frame
df_table0 = tables[0].df


# Export to the file. If compress option is True, the file will be comressed
tables.export('rpa-lib/pdf_processing/table_from_pdf.csv', f='csv', compress=False)
