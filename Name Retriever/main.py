import requests
from bs4 import BeautifulSoup

r = requests.get('https://namecensus.com/most_common_surnames.htm').text
soup = BeautifulSoup(r)
alist = soup.find_all('td')
x = []
for i in range(len(alist)-1):
    if i%4 == 0:
        x.append(alist[i].text)
y = open('lastnames1.txt', 'w')
for i in x:
    y.write(i+'\n')