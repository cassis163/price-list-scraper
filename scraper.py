import pandas as pd
from requests import get
from bs4 import BeautifulSoup

def scrape():
    '''
    Returns a BeautifulSoup result of the price list
    '''

    html = get('http://www.zuidbos.nl/bestellijst.php').text
    soup = BeautifulSoup(html, 'html.parser')

    return soup.find_all('table', {'class': 'table_lijst'})[0]

def get_dataframe():
    '''
    Returns the price list as a DataFrame
    '''

    price_list = scrape()
    df = pd.DataFrame(columns=[
        'Soort',
        'Naam',
        'Prijs',
        'Afkomst',
        'Keurmerk'
    ])

    # Iterate through each row and skip the header
    for tr in price_list.find_all('tr', recursive=False)[1:]:
        values = [td.text for td in tr.find_all('td', recursive=False)[2:]]

        # Add the row to the dataframe
        df = df.append({
            'Soort': values[0],
            'Naam': values[1],
            'Prijs': values[2],
            'Afkomst': values[3],
            'Keurmerk': values[4]
        }, ignore_index=True)

    return df
