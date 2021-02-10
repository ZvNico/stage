import cloudscraper
import re
from bs4 import BeautifulSoup

sheetsURL = "https://docs.google.com/spreadsheets/d/1uqlsKnuBwPOkGb60LqGywf0n5zJ7q1tD7T0Yoxmwf1o/edit#gid=77107931"


def search_results(quoiqui, ou):
    def page_result(url, page):
        if page != 1:
            url = f"{url}&page={page}"

        results = []

        r = scraper.get(url).text.replace('\n', '')

        soup = BeautifulSoup(r, features='lxml')
        print(soup)
        soup = soup.find(id='listResults').find('ul').find_all('li', id=re.compile('^bi-bloc-'))

        for elt in soup:
            result = {
                'entreprise': elt.find(class_=re.compile('denomination-links')).text,
                'domaine': elt.find(class_=re.compile('activites')).text.replace('\xa0', ''),
            }

            temp = elt.find('strong', class_="num")
            if temp: result['fixe'] = temp.text

            """temp = elt.find(class_=re.compile('SEL-email'))
            if temp: result['email'] = temp.find(class_='pj-lb pj-link')"""

            temp = elt.find_all('li', class_=re.compile('site-internet'))
            if temp: result['sites'] = [site.find('a', class_=re.compile('site-internet')) for site in temp]

            results.append(result)

        print(url)

        return results

    url = f"https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui={quoiqui}&ou={ou}&univers=pagesjaunes"
    scraper = cloudscraper.create_scraper()
    results = []
    for i in range(1, 2):
        results.extend(page_result(url, i))
    for elt in results:
        print(elt)
    return results


def google_sheets_integration():
    pass
