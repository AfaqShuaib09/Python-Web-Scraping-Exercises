# Excercise no 2
# Scrap https://quotes.toscrape.com
#

from bs4 import BeautifulSoup
import requests

web = requests.get('https://quotes.toscrape.com')
soup = BeautifulSoup(web.text, 'html.parser')
tag_box = soup.select_one('.tags-box')
print('**************', tag_box.select_one('h2').text,'***************')
top_ten_tags = tag_box.select('.tag')
for tag in top_ten_tags:
    print(tag.text)
#print(tag_box)