import requests
from bs4 import BeautifulSoup

URL = "https://medium.com"

def scraper():
    # r = requests.get(URL)
    # soup = BeautifulSoup(r.content, 'html5lib')
    posts = []

    posts = [
        { "url": 'qwertyu' },
        { "url": 'qwertyu' },
        { "url": 'qwertyu' },
        { "url": 'qwertyu' },
        { "url": 'qwertyu' },
        { "url": 'qwertyu' },
    ]

    # table = soup.select('div.oc.r.af.u')

    # for row in table:
    #     obj = {}
    #     link = row.a['href']
    #     if link[0] == '/':
    #         link = URL + link
    #     obj['url'] = link
    #     posts.append(obj)
    
    return posts
