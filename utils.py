import requests
from bs4 import BeautifulSoup

sheetsURL = "https://docs.google.com/spreadsheets/d/1uqlsKnuBwPOkGb60LqGywf0n5zJ7q1tD7T0Yoxmwf1o/edit#gid=77107931"


def searchResults(quoiqui, ou):
    return f"https://www.pagesjaunes.fr/recherche/paris-saint-leon-31/commerce?quoiqui={quoiqui}&ou={ou}"


def googleSheetsIntegration():
    pass


def pageResult(url, page):
    r = requests.get(
        "https://www.commerces-ouverts.fr/ajax/map/gZ2.4499511718750004,48.90602845900595,2.217178344726563,48.81590713080018/boulangerie/1?=&ouverts=0&suggestions=&meilleurs=0")
    soup = BeautifulSoup(r.text)


pageResult(searchResults('commerce', 'paris'), 1)
