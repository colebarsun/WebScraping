import requests
from bs4 import BeautifulSoup

# Send req to website

url = 'http://books.toscrape.com/'
response = requests.get(url)

# parse HTML content

soup = BeautifulSoup(response.text, 'html.parser')

#step 3: Find the data wanting to extract 
#book info is in article

books = soup.find_all('article', class_='product_pod')


#extract and print titles

for book in books:
    title = book.find('h3').find('a')['title']
    price = book.find('p', class_='price_color').text
    print(f"Title: {title}, Price: {price}")