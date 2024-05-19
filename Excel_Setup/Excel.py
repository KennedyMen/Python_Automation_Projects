import pandas as pd

df = pd.read_excel(
    '/Users/033103kennedymensah/Automation/Excel_Setup/supermarket_sales.xlsx')
gf = df[['Gender', 'Product line', 'Total']]
print(df)

pivot_table = gf.pivot_table(
    index='Gender', columns="Product line", values='Total', aggfunc='sum').round(0)
pivot_table.to_excel('pivot_table.xlsx', 'Report', startrow=4)
