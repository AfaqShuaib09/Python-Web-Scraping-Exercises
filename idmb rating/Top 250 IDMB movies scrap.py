# Practice #3 Part-2
# Scrapping IDMB site
# Single movie

import requests
from bs4 import BeautifulSoup
website = requests.get('https://www.imdb.com/search/title/?groups=top_250&')
soup_obj = BeautifulSoup(website.text,'html.parser')
movie_list = soup_obj.find_all(class_='lister-item')
for movie in movie_list:
    headers = {'Accept-Language': 'en-US'}
    web = requests.get('https://www.imdb.com' + movie.find('a').attrs['href'], headers=headers)
    soup = BeautifulSoup(web.text, 'html.parser')
    print('IDMB Page Title: ', soup.title.text.split(' -')[0].strip())
    title_header = soup.select_one('.TitleBlock__Container-sc-1nlhx7j-0 h1').text
    print('Movie Name: ', title_header)
    ulist = soup.select_one('.TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-2 ul')
    list_item = ulist.find_all('li')
    m_year = list_item[0].find('a').text
    movie_category = list_item[1].find('a').text
    movie_duration = list_item[2].text
    print(f'Movie Year: {m_year}\nMovie Category: {movie_category}\nMovie Duration: {movie_duration}')

    genres = soup.find(class_='ipc-chip-list')
    genere_list = genres.find_all('a')
    print('Related Genres: ')
    for genre in genere_list:
        print(genre.text)

    rating = soup.find(class_='AggregateRatingButton__RatingScore-sc-1ll29m0-1')
    print(f'Rating: {rating.text}/10 *')

    cast = soup.find(class_='ipc-page-section')
    actor_names = soup.find_all(class_='StyledComponents__ActorName-y9ygcu-1')
    character_names = soup.find_all(class_='StyledComponents__CharacterNameWithoutAs-y9ygcu-5')
    print('***************** Cast **********************')
    for i in range(0,len(actor_names)):
        print(f'{actor_names[i].text} as {character_names[i].text}')
    print('\n ---------------------------------- \n')