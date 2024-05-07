import requests
from bs4 import BeautifulSoup as BS

file = open('povtoreniye.html', encoding='utf-8')

html = file.read()

soup = BS(html, 'html.parser')

cards = soup.find_all('div', class_= 'card')
for x in cards:
    print(x.text)


# nav_link = soup.find_all('a', class_= 'nav_link')
# for link in nav_link:
#     print(link.text)

# ul = soup.find_all('ul', class_='dropdown-menu')
# for x in ul:
#     print(x.text)