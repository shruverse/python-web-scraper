import requests
from bs4 import BeautifulSoup
import csv

url = 'https://carat.fandom.com/wiki/Seventeen_Wiki'

page = requests.get(url).text

soup = BeautifulSoup(page, 'html.parser')

current_div = soup.find('div', class_='wds-is-current')
table_rows = current_div.find_all('tr')

data = []

for row in table_rows:
    albums = row.find_all('a', href=True)
    for album in albums:
        album_name = album.get('title')
        data.append([album_name])
        print(album_name)

with open('album_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Album Released this year'])
    writer.writerows(data)

