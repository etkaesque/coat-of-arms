from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://lt.wikipedia.org/wiki/S%C4%85ra%C5%A1as:Lietuvos_herbai'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find_all('table')[2]
table_rows = table.find_all('tr')

scooped_data = []

for row in table_rows:

    td = row.find('td')
    if not td:
        continue
 
    span = td.find('span')

    title = td.findChildren('a', recursive=False)[0].get_text()

    if span and span.a:
        href = span.a.get('href')
        scooped_data.append({'title': title, 'picture': href})
           
    else:
        continue

df = pd.DataFrame(scooped_data)
df.to_csv(r'./herbai.csv', index=False)