# Excercise no 2
# Scrap https://quotes.toscrape.com
# using CSS selector method

from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

web = requests.get('https://quotes.toscrape.com')
soup_obj = BeautifulSoup(web.text, 'html.parser')

# title = soup_obj.select('title') # Get list of elements having title tag
title = soup_obj.select_one('title').text # Title tag element
print(title)
print('\n--------------------------------\n')
quotes = soup_obj.select('.quote')
quotes_list = list()
author_list = list()
Tags = list()
row_list = list()
row_list.append(["Quotes","Author", "Tags"])
for quote in quotes:
    quote_text = quote.select_one('.text').text
    print("Quote: ~", quote_text)
    author_name = quote.select_one('.author').text
    print('Author Name: ', author_name)
    tags = quote.select('.tag')
    tag_list = [tag.text for tag in tags]
    print("Tags: ", tag_list)
    quotes_list.append(quote_text)
    author_list.append(author_name)
    Tags.append(tag_list)
    row_list.append([quote_text,author_name,tag_list])
    print('\n--------------------------------\n')

# Writing csv using panda library
Quotes_table = pd.DataFrame(
    {
        "Quotes": quotes_list,
        "Author": author_list,
        'Tags': Tags
    }
)
# print(Quotes_table)
Quotes_table.to_csv('quotes.csv')

# writing csv using csv module
with open('my_quote.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)