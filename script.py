import requests
from bs4 import BeautifulSoup as bs
res = requests.get('https://www.ozbargain.com.au', verify = False)
print(res.text)

#r_dict=res.text.json()

if res:
    print('Response Succeeded')
    output = open('index.html', 'w')
    output.write(res.text)
    output.close()
else:
    print('Response Failed')

with open('index.html') as html_file:
    soup = bs(html_file, 'lxml')

#print(soup.prettify())
#match = soup.title.text
#match = soup.find('div', class_='node node-ozbdeal node-teaser')
match = soup.find_all('h2', class_='title')
#match = soup.find_all('div', class_='right')
print(match[0].prettify())


for node in match:
    print(node.a.text)
    #print(node.h2.text)
    
    print()
