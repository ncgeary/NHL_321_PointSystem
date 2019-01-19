from bs4 import BeautifulSoup
from urllib.request import urlopen
from html.parser import HTMLParser


StDate = '20181004' #Start Date of NHL
#not working atm
#ToDate = current_time.strftime('%Y%m%d')
TestDate = '20190101'

#Just starting with Jan 1 date to test out grathering data
#Using ESPN scoring because of how their HTML is set up
#Easier to find winners/losers
url = 'http://www.espn.com/nhl/scoreboard?date='+TestDate
soup = BeautifulSoup(urlopen(url), "html.parser")

gameids = []
teams=[]
for gameid in soup.find_all("div",{"class":"final"}):
    gameids.append(gameid.get('id'))
    for gameid in gameids:
        winner = soup.find("tr",{"class":"winner"})
        loser = soup.find("tr",{"class":"loser"})
        for team in winner:
            teams.append(winner.find("div",{"class":"logo-small"}).a.text)
        for team in loser:
            teams.append(loser.find("div",{"class":"logo-small"}).a.text)




print(gameids)
print(teams)
