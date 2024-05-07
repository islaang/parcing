import requests
from bs4 import BeautifulSoup as BS

file = open('explame_html.html', encoding='utf-8')

html = file.read()

soup = BS(html, 'html.parser')

main_div = soup.find('div', class_='container')
navigation = main_div.find('div', class_='navigation')
ul = navigation.find('ul',class_='info')


content = main_div.find('div', class_='content')
# print(content)
posts = content.find_all('div', class_='post')

# for post in posts:
#     title = post.find('h2', class_='title').text
#     print(title)

# footer_info1 = soup.find('div', class_='footer')
# footer_info2 = footer_info1.find_all('p', class_='footer-box')
# for footer_info in footer_info2:
#     title = footer_info.find('p', class_='footer-title').text
#     print(title)

footer_info1 = soup.find('div', class_='footer')
footer_boxes = footer_info1.find_all('div', class_='footer-box')
for box in footer_boxes:
    title = box.find('p', class_='footer-title').text
    print(title)
