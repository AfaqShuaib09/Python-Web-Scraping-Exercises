# Excercise no 2
# Scrap https://quotes.toscrape.com
# using find method

from bs4 import BeautifulSoup
import pandas
import requests

web = requests.get('https://quotes.toscrape.com') # get the html of the website
soup = BeautifulSoup(web.text, 'html.parser')
#print(soup)
title = soup.find('title').text
print('***************', title, '*******************')

# To find the first occurrence of 'a' tag on the current url
# first_link = soup.find('a')
# print(first_link.text)

# To get the first quote from the web site
# quote = soup.find(class_='text')
# print(quote.text)

# to get the login link
# login_link = soup.find(href='/login')
# print(login_link)

# To get All the links from the page
# links = soup.find_all('a')
# print(links)
# for link in links:
#     print(link.text)


first_quote = soup.find(class_='quote')
quote = first_quote.find(class_='text').text
author = first_quote.find(class_='author').text
tags = first_quote.find_all(class_='tag')
print('quote: ~', quote)
print("Author Name: ", author)
print("The Quote belongs to: ")
for tag in tags:
    print(tag.text)

