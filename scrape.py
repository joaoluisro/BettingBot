import requests
import datetime
from bs4 import BeautifulSoup
from requests_html import HTMLSession

monthdict = {
    1 : "Janeiro",
    2 : "Fevereiro",
    3 : "Março",
    4 : "Abril",
    5 : "Maio",
    6 : "Junho",
    7 : "Julho",
    8 : "Agosto",
    9 : "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
    }




data = datetime.datetime.now()
dia = str(data.day) + ' de ' + monthdict[data.month]
URL = 'https://lolesports.com/schedule?leagues=cblol-brazil,lcs,lec,lck,lpl'
page = requests.get(URL)

session = HTMLSession()
r = session.get(URL)

r.html.render()

r.html.search('E')[0]

soup = BeautifulSoup(page.content, 'lxml')
#tags = soup.select('div[class="EventMatch"]')
results = soup.find_all('div', class_="browserupgrade")
print(results)
#print(page.content)
