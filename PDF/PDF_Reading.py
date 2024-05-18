import camelot


tables = camelot.read_pdf('foo.pdf', pages='1',)
print(tables)

tables.export('foo.csv', f='csv', compress=True)  # json, excel, html
tables[0].to_csv('foo.csv')  # to_json, to_excel, to_html
