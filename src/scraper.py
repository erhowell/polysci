from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests, sys




mainUrl = 'http://www.riksdagen.se/sv/global/sok/?q=&doktyp=prop&p='

def crawl(currentPage, hrefs=[]):
    try:
        response =requests.get(mainUrl+ str(currentPage))
        soup = BeautifulSoup(response.text,"html.parser")
        a = soup.findAll("a", {"class": "link-file"})
        hrefs.append([link.get('href').split('/')[-1] for link in a] if len(a) > 0 else [])
        print(currentPage)
        return hrefs
    except Exception as e:
        print(f"An exception occurred: {e}")
        return hrefs


def getCount():
    try:
        response =requests.get(mainUrl)
        soup = BeautifulSoup(response.text,"html.parser")
        return soup.find("span", {"class": "hits"}).text[1:-1]
    except Exception as e:
        print(f"An exception occurred: {e}")


