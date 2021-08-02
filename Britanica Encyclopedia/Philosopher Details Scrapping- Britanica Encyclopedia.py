# Practice #3 Part-2
# Scrap Britannica Encyclopedia
# Single philosopher scrap

import requests
from bs4 import BeautifulSoup

web = requests.get('https://www.britannica.com/topic/list-of-philosophers-2027173')
soup = BeautifulSoup(web.text, 'html.parser')
link_list = soup.select('section a')
#print(link_list)
for link in link_list[2:]:
    website = requests.get(link.attrs['href'])
    soup = BeautifulSoup(website.text, 'html.parser')
    name = soup.find('h1').text
    topic = soup.find(class_='topic-identifier').text
    summary = soup.select_one('.topic-paragraph').text.strip()
    try:
        image = soup.select_one('.card img').attrs['src']
    except AttributeError as e:
        image = 'No Image'
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
    print('\n***************************************\n')
