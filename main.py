import scraper
import formatter
from datetime import date
from os import getcwd
from subprocess import Popen

file_name = date.today().strftime('%Y-%m-%d')
file_dir = getcwd() + '/excel/' + file_name + '.xlsx'

df = scraper.get_dataframe()

df_out = df.drop(columns=['Soort'])
df_out.to_excel(file_dir, index=None)

formatter.wrap_text(file_dir)
formatter.add_headers(file_dir, df['Soort'])

# Open the Excel file in Microsoft Excel
Popen(file_dir)