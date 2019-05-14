from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests, sys



def crawl(url, depth, maxdepth, visited):
    if depth == 0:
        print("URLs linked in this document are:")
        print(url)
        visited.append(url)
        return crawl(url, depth+1, maxdepth, visited =[])
    if depth <= maxdepth:
        try:
            response =requests.get(url)
            soup = BeautifulSoup(response.text,"html.parser")
            links = soup.find_all('a')
            if links:
                    for a in links:
                        test_url =a.get('href')
                        if "#" not in test_url and test_url != "/" and test_url != None:
                            if not urlparse(test_url).netloc:
                                test_url = url +test_url
                            if (test_url not in visited) :
                                tabs = '\t'* depth
                                printLine = tabs + test_url
                                print(printLine)
                                visited.append(test_url)
                                crawl(test_url, depth+1, maxdepth, visited = [])
            else:
                print("No hyperlinks were found in this document")
        except Exception as e:
            print(f"An exception occurred: {e}")
    else:
        return 1

#crawl("https://cs.usu.edu",0, 2,visited=[])
    
if len(sys.argv) < 2:
    print("Error: no URL supplied")
    sys.exit()
else:
    if sys.argv[1].find("https://") == -1:
        print("Error: Invalid URL supplied.")
        print("Please supply an absolute URL to this program")
        sys.exit()
    else:
        url = sys.argv[1]
        if len(sys.argv) == 3:
            maxdepth = sys.argv[2]
        else:
            maxdepth = 3
        try:
            # TODO: what if an error happens?
            response = requests.get(url)
            print("Crawling from "+ url + " to a maximum distance of "+ str(maxdepth) +" link" )     
            crawl(url, 0, int(maxdepth),visited =[])
        except Exception as e:
            print(f"Failed to get {url} because {e}")
    