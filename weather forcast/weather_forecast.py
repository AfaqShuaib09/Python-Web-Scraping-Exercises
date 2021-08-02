# Exercise no 1
# scrap forecast.weather.gov

import requests
from bs4 import BeautifulSoup
import pandas

# Request a web to get all of its contents using its url
web = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.6683&lon=-120.66')
#web = requests.get('https://forecast.weather.gov/MapClick.php?lat=33.2044&lon=-95.9997#.YPRDUOgzbDc')
soup = BeautifulSoup(web.text, 'html.parser')

title = soup.find('title') # to get the title element of web
print('******************', title.text, '*******************')
div_weather_container = soup.find(id='seven-day-forecast')
#print(div_weather_container)
location_city = div_weather_container.find(class_='panel-title').text.strip()
#location_city = div_weather_container.select_one('h2').text.strip()
print('Location: ', location_city)
print('-------------------------------------------\n')
weather_weekly_data = div_weather_container.find(id='seven-day-forecast-body')
weather_items = weather_weekly_data.find_all(class_='tombstone-container')
#print(weather_items)
for i in range(0,len(weather_items)):
    print('period-name: ', weather_items[i].find(class_='period-name').text)
    print('Desc: ',weather_items[i].find(class_='short-desc').text)
    print('Temperature: ', weather_items[i].find(class_='temp').text, '\n')

print('-------------------------------------------\n')

# List comprehension to populate the list
period_names = [item.find(class_='period-name').get_text() for item in weather_items]
short_desc = [item.find(class_='short-desc').get_text() for item in weather_items]
temp = [item.find(class_='temp').get_text() for item in weather_items]

weather_table = pandas.DataFrame(
    {
        'Period Name': period_names,
        'Description': short_desc,
        'Temperature': temp
    }
)
weather_table.to_csv(location_city+'_weather.csv')




