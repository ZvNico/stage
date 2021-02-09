import cloudscraper
import re
from bs4 import BeautifulSoup

sheetsURL = "https://docs.google.com/spreadsheets/d/1uqlsKnuBwPOkGb60LqGywf0n5zJ7q1tD7T0Yoxmwf1o/edit#gid=77107931"


def searchResults(quoiqui, ou):
    url = f"https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui={quoiqui}&ou={ou}&univers=pagesjaunes"

    def pageResult(url, page):
        if page != 1:
            url = f"{url}&page={page}"
        r = scraper.get(url)
        soup = BeautifulSoup(r.text, features='lxml')
        soup = soup.find(id='listResults').find('ul').find_all('li', id=re.compile('^bi-bloc-'))
        for elt in soup:
            temp = elt.find(class_=re.compile('^denomination-links'))
        print(url)

    for i in range(1, 10):
        pageResult(url, i)


def googleSheetsIntegration():
    pass


scraper = cloudscraper.create_scraper()
searchResults('commerce', 'paris')
