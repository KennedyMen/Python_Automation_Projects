import camelot
from pathlib import Path


tables = camelot.read_pdf('foo.pdf', pages='1',)
print(tables)

tables.export('foo.csv', f='csv', compress=True)  # json, excel, html
filepath = Path('/Users/033103kennedymensah/Automation/PDF/foo.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
tables[0].to_csv(filepath)  # to_json, to_excel, to_html
