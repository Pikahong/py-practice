# Extract table of national capitals from Wikipedia

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://en.wikipedia.org/wiki/List_of_national_capitals'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')
data = []
table = soup.find('table', attrs={'class': 'wikitable sortable'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows[1:]:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

title = [ele.text.strip() for ele in rows[0].find_all('th')]

df = pd.DataFrame(data, columns=title)
df['Country/Territory'].fillna(method='ffill', inplace=True)
df.to_csv('List_of_national_capitals.csv', index=False)


match = df[title[0]].str.match('')
df = df[match]
print(df)
