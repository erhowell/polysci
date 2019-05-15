from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests, sys
import csv

mainUrl = 'http://www.riksdagen.se/sv/global/sok/?q=&doktyp=prop&p='
ids=[]

def crawl(page):
    try:
        response =requests.get(mainUrl+ str(page))
        soup = BeautifulSoup(response.text,"html.parser")
        links = soup.findAll("a", {"class": "link-file"})
        if links:
                for a in links:
                    ids.append(a.get('href').split('/')[-1])
        else:
            print("No hyperlinks were found in this document")
        print(len(ids))
        print(str(page) + '\n')

        crawl(page+1 )
    except Exception as e:
        print(f"An exception occurred: {e}")
        

crawl(1)
with open('data\ids.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(ids)

csvFile.close()
