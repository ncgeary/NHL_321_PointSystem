from bs4 import BeautifulSoup
import numpy as np
from urllib.request import urlopen
from html.parser import HTMLParser


url = 'https://www.hockey-reference.com/leagues/NHL_2019_standings.html'
soup = BeautifulSoup(urlopen(url), "html.parser")

for caption in soup.find_all('caption'):
    if caption.get_text() == 'Expanded Standings Table':
        table = caption.find_parent('table', {"id":"standings"})


all_teams = []
with open('NHL_Standings.txt','w') as r:
    for row in table.find_all('tr'):
        for cell in row.find_all('td'):
            all_teams.append(cell.text)
            # just to throw it into a text file
            r.write(cell.text.ljust(5))
        r.write('\n')



np.split(all_teams, 31)

print(all_teams)
