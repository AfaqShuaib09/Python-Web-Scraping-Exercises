import pandas
import pandas as pd
import requests
import urllib.request
from bs4 import BeautifulSoup # for web scrapping
import re # to fine tune the scraps

web = requests.get('https://docs.python.org/3/library/random.html')
page = urllib.request.urlopen('https://docs.python.org/3/library/random.html')
soup = BeautifulSoup(page,'html.parser')

names = soup.body.findAll('dt')
function_names = re.findall('id="random.\w+"',str(names))
#print(function_names)

function_names = [function_name[4:-1] for function_name in function_names]
function_descriptions = soup.body.findAll('dd')
function_descriptions = [function_desc.text.replace('\n',' ') for function_desc in function_descriptions]

Function_desc_table = pandas.DataFrame({
    'Function-name' : function_names,
    'Function-Descriptions': function_descriptions
})

Function_desc_table.to_csv('random_module.csv')
print(Function_desc_table)

# To scrap a particular target element
element = soup.body.findAll('div', attrs={'id':'bookkeeping-functions'})
print(element)

