import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.goodreads.com/quotes"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
print(soup.title.string)
quotes = []

table = soup.find('div', attrs = {'class':'quote'})

for row in table.find_all('div', attrs = {'class':'smallText'}):
	quote = {}
    # quote[' Quote'] = row.text
	quote[' Likes'] = row.a['href']
    quotes.append(quote)


   filename = 'Popular_Quotes.csv'
   with open(filename, 'w', newline='') as f:
	 w = csv.DictWriter(f, [' Likes'])
	 w.writeheader()
	 for quote in quotes:
		w.writerow(quote)
    
    f = open("file.csv", "w")
    f.write("Every,word,will,go,in,separate,column\n")
    f.write("This,will,go,in,next,row")
    f.close()

    with open("file.csv", "w") as f:
    f.write("Every,word,will,go,in,separate,column\n")
    f.write("This,will,go,in,next,row")
