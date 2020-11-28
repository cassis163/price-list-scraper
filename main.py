import scraper
import formatter
import os
from datetime import date

file_name = date.today().strftime('%Y-%m-%d')
file_dir = os.getcwd() + '/excel/' + file_name + '.xlsx'

df = scraper.get_dataframe()

df_out = df.drop(columns=['Soort'])
df_out.to_excel(file_dir, index=None)

formatter.wrap_text(file_dir)
formatter.add_headers(file_dir, df['Soort'])

# Open the Excel file in Microsoft Excel
os.system('start "excel" "%s"' % file_dir)