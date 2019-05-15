import scraper
import csv

print(len(hrefs))
ids = [h.split('/')[-1] for h in hrefs]
with open('data\ids.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(ids)

csvFile.close()
