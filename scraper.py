import requests
from bs4 import BeautifulSoup

URL = "https://medium.com"

def scraper():
    # r = requests.get(URL)

    # soup = BeautifulSoup(r.content, 'html5lib')

    # # Scraping code here...
    # posts = []

    # table = soup.select('div.oc.r.af.u')

    # for row in table:
    #     print(row, '\n=================\n')

    # Returning dummy data
    return [
        'Hello there',
        'How are you',
        'What time is it'
    ]
