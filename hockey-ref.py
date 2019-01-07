from bs4 import BeautifulSoup
from urllib.request import urlopen
from html.parser import HTMLParser


#Just starting with Jan 1 date to test out grathering data
#Using ESPN scoring because of how their HTML is set up
#Easier to find winners/losers
url = 'https://www.hockey-reference.com/leagues/NHL_2019_standings.html'
soup = BeautifulSoup(urlopen(url), "html.parser")

table = soup.find("table",{"id":"standings"})

name=[]
overall=[]
shootout=[]
overtime=[]

for data in table:
    for rows in table.find_all("tr"):
        name.append(table.find("td",{"data-stat":"team_name"}).a.text)
        overall.append(table.find("td",{"data-stat":"Overall"}).text)
        shootout.append(table.find("td",{"data-stat":"Shootout"}).text)
        overtime.append(table.find("td",{"data-stat":"ot"}).text)

print(name)
print(overall)
print(shootout)
print(overtime)
