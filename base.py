from bs4 import BeautifulSoup
from urllib.request import urlopen
from html.parser import HTMLParser


StDate = '20181004' #Start Date of NHL
#ToDate = current_time.strftime('%Y%m%d')
TestDate = '20190101'

#Just starting with Jan 1 date to test out grathering data
#Using ESPN scoring because of how their HTML is set up
#Easier to find winners/losers
url = 'http://www.espn.com/nhl/scoreboard?date='+TestDate
soup = BeautifulSoup(urlopen(url), "html.parser")

winners = soup.find_all("tr",{"class":"winner"})

#print(len(winners))
