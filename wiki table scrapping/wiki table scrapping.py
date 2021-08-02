# Practice #3
# Scrap wiki table
import requests
from bs4 import BeautifulSoup
import pandas as pd

website = requests.get(
    'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_and_their_capitals_in_native_languages')
soup = BeautifulSoup(website.text, 'html.parser')
# print(soup)
country_lst = list()
capital_lst = list()
native_lang = list()
wikipedia_table = soup.select('.wikitable')
for table in wikipedia_table:
    table_rows = table.select('tr')[1:]
    for row in table_rows:
        table_data = row.select('td')
        country = table_data[2].text
        capital = table_data[3].text
        official_native_lang = table_data[4].text
        #print(f'Country: {country}, Capital: {capital}, Offical Native Language: {official_native_lang.strip()}')
        country_lst.append(country)
        capital_lst.append(capital)
        native_lang.append(official_native_lang)

wiki_table = pd.DataFrame({
    'Country ': country_lst,
    'Capital ': capital_lst,
    'Native /Official Language': native_lang
})
wiki_table.to_csv('List_of_countries_and_dependencies_and_their_capitals_in_native_languages.csv')
print(wiki_table)

