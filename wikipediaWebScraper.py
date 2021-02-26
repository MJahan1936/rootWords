import requests
import pandas

website_url = requests.get('https://en.wikipedia.org/wiki/List_of_Greek_and_Latin_roots_in_English/A%E2%80%93G').text

from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url, 'lxml')
#print(soup.prettify())

My_table = soup.find('table', {'class': 'wikitable sortable'})

links = My_table.findAll('a')

Roots = []

for link in links:
    Roots.append(link.get('title'))

print(Roots)
