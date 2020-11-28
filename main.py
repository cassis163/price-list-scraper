import scraper
import text_fitter
from datetime import date
from os import getcwd

file_name = date.today().strftime('%Y-%m-%d')
file_dir = getcwd() + '/excel/' + file_name + '.xlsx'

df = scraper.get_dataframe()
df.to_excel(file_dir, index=None)

text_fitter.fit(file_dir)