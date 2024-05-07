import requests
from bs4 import BeautifulSoup as BS
from openpyxl import Workbook

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def get_data(html):
    soup = BS(html, 'html.parser')
    container = soup.find('div', class_='container-fluid my-3x md:my-4x')
    posts = container.find_all('a', class_='p-2x flex flex-col gap-y-2x')

    data = []
    for post in posts:
        prices = post.find('div', class_='flex gap-x-0.5x')
        price = prices.find('span', class_='whitespace-nowrap text-title_4').text.strip().replace(" ", "")
        price_m = prices.find('p', class_='text-gray__dark_1 whitespace-nowrap text-caption').text.strip()
        location = post.find('p', class_="whitespace-nowrap text-gray__dark_2 truncate text-caption").text.strip()
        apartments = post.find('p', class_="whitespace-nowrap truncate text-body_2").text.strip()
        area = post.find('p', class_="text-gray__dark_2 text-caption").text.strip()
        
        data.append([price, price_m, apartments, location])
    return data[:20]


# def save_txt(data, filename = 'test.txt'):
#     with open(filename, 'w', encoding='utf-8') as file:
#         file.write('Price\tPrice per m2\tapartments\tlocation\n')
    #     for item in data:
    #         file.write('\t'.join(item) + '\n')
    # print(f'data is saved in {filename}')

def save_in_excel(data, filename = 'datas.xlsx'):
    wb = Workbook()
    ws = wb.active
    
    # Записываем заголовки
    ws.append(['Price', 'Price per m2', 'Title', 'Location'])
    
    # Записываем данные
    for row in data:
        ws.append(row)
    
    # Сохраняем в файл
    wb.save(filename)
    print(f"Data saved to {filename}")


def main():
    URL = 'https://aqarmap.com.eg/en/for-sale/property-type/cairo/new-cairo/'
    html = get_html(URL)
    if html:
        data = get_data(html)
        save_in_excel(data)
    else:
        print("Failed to fetch HTML data")

if __name__ == '__main__':
    main()