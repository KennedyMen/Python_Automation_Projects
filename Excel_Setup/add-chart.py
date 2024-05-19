from openpyxl import load_workbook

wb = load_workbook(
    '/Users/033103kennedymensah/Automation/Excel_Setup/pivot_table.xlsx')
sheet = wb['Report']
min_column = wb.active.min_column
max_column = wb.active.max_column
min_row = wb.active.min_row
max_row = wb.active.max_row

print(min_column)
print(max_column)
print(min_row)
print(max_row)
# --------------------------------------------------------------------------
