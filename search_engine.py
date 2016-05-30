import requests
from bs4 import BeautifulSoup

def downloadURL(url):
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception("Non-OK status code: {}".format(r.status_code))
    return r.text

def parseHTML(html):
    bs = BeautifulSoup(html, 'lxml')
    return bs.select('div.usertext-body')[1].text
