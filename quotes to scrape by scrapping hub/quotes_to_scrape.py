# Excercise no 2
# Scrap https://quotes.toscrape.com
# Scrapping All the quotes from the web site handling pagination

from bs4 import BeautifulSoup
import requests

flag = True
page_count = 1
print("**************** Quotes to Scrape ******************")
print('\n--------------------------------\n')
while flag:
    web = requests.get('https://quotes.toscrape.com/page/'+ str(page_count)+ '/')
    soup_obj = BeautifulSoup(web.text,'html.parser')
    quotes = soup_obj.select('.quote')
    for quote in quotes:
        quote_text = quote.select_one('.text').text
        print("Quote: ~", quote_text)
        author_name = quote.select_one('.author').text
        print('Author Name: ', author_name)
        tags = quote.select('.tag')
        tag_list = [tag.text for tag in tags]
        print("Tags: ", tag_list)
        print('\n--------------------------------\n')
    next_button = soup_obj.select_one('.next a')
    page_count = page_count + 1
    if next_button:
        flag = True
    else:
        flag = False



