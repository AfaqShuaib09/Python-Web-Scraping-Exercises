# Practice #3
# Scrap Britannica Encyclopedia
# Single philosopher scrap

import requests
from bs4 import BeautifulSoup

website = requests.get(
    'https://www.britannica.com/biography/Mortimer-J-Adler')
soup = BeautifulSoup(website.text, 'html.parser')
name = soup.find('h1').text
topic = soup.find(class_='topic-identifier').text
summary = soup.select_one('.topic-paragraph').text.strip()
image = soup.select_one('.card img').attrs['src']

print('Philosopher Name: ', name)
print("Topic Identifier: ", topic)
print("Topic Summary: ", summary)
print(f'Img src: {image}')
details_div = soup.find(class_='facts-list')
facts = details_div.find_all(class_='js-fact')
#print(details_div)
for fact in facts:
    try:
        headings = fact.select_one('dt').text
        print(headings)
        details = fact.find('dd').get_text().strip()
        facts_list = fact.find_all(class_='fact-item')
        print(details.replace('\n',' | '))
        #print(facts_list[0].text,'\n******************\n')
    except Exception as e:
        pass
