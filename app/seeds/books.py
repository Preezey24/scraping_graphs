from bs4 import BeautifulSoup
import requests

for page in range(1,11): 
    html_text = requests.get(f'http://books.toscrape.com/catalogue/page-{page}.html').text
    soup = BeautifulSoup(html_text, 'lxml')
    books = soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    for book in books: 
        print(book.article.h3.text)
        print(book.find('div', class_='product_price').find('p', class_='price_color').text[2:])
        print(book.article.div.p.text)
    print(f'Page: {page}')
   