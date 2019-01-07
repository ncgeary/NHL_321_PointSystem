from bs4 import BeautifulSoup as bs
soup = bs(html_doc, 'html.parser')

StDate = '20181004' #Start Date of NHL
ToDate = current_time.strftime('%Y%m%d')

#Just starting with Current date to test out grathering data
#Using ESPN scoring because of how their HTML is set up
#Easier to find winners/losers
url = 'http://www.espn.com/nhl/scoreboard?date='+ToDate
