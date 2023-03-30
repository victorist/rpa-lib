import camelot
from ctypes.util import find_library
import pandas as pd

dir_pdf_table = "rpa-lib/pdf_processing/azurair_manifests/pdf_table/"
pdf_table = "ZF 2847 29.03.23.pdf"

print("#" * 100)
print("Проверка наличия библиотекаи ",find_library("gs"))
print("_pip" * 100)

tables = camelot.read_pdf(dir_pdf_table + pdf_table)

print("_"*80)
print("Кол-во таблиц в документе:", tables.n)
print("_"*80)
print("анализ конвертации:\n")
print(tables[0].parsing_report)
print("_"*80)


# Export one table
tables[0].to_excel(dir_pdf_table + "table_from_" + pdf_table + ".xlsx")


# Export to the file. If compress option is True, the file will be comressed
tables.export(dir_pdf_table + "table_from_" + pdf_table + ".csv", f='csv', compress=False)

# Data frame
df_table = tables[0].df
print(df_table)