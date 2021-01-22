import requests
import time

import datetime

from bs4 import BeautifulSoup

from selenium import webdriver

import re

def connect_and_fetch(URL):
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--incognito")
    options.add_argument("--headless")
    driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)

    driver.get(URL)

    SCROLL_PAUSE_TIME = 0.5

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(SCROLL_PAUSE_TIME)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, "lxml")
    matches = soup.select('div[class="EventDate"]')

    return matches

def update_csv(matches):

    with open('recorded_matches.csv', 'w') as file:

monthdict = {
    1: "janeiro",
    2: "fevereiro",
    3: "março",
    4: "abril",
    5: "maio",
    6: "junho",
    7: "julho",
    8: "agosto",
    9: "setembro",
    10: "outubro",
    11: "novembro",
    12: "dezembro",
}

data = datetime.datetime.now()
dia = str(data.day) + " de " + monthdict[data.month]
URL = "https://lolesports.com/schedule?leagues=cblol-brazil,lcs,lec,lck,lpl"

#matches = connect_and_fetch(URL)
update_csv([])
#for day in matches[0].next_siblings:
#    print(day.text)
#    print()
