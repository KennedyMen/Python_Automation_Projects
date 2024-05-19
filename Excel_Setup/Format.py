from openpyxl import load_workbook
from openpyxl.styles import Font

wb = load_workbook(
    '/Users/033103kennedymensah/Automation/Excel_Setup/report.xlsx')
sheet = wb['Report']

sheet['A1'] = 'Sales Report'
sheet['A2'] = "January"
sheet['A1'].font = Font('Arial', size=20, bold=True)
sheet['A2'].font = Font('Arial', size=10, bold=True)

wb.save('report_January.xlsx')
