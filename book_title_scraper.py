import requests
from bs4 import BeautifulSoup

# Send req to website

url = 'http://books.toscrape.com/'
response = requests.get(url)

# parse HTML content

soup = BeautifulSoup(response.text, 'html.parser')

#step 3: Find the data wanting to extract (book titles)
#book titles are in <h3> tags

books = soup.find_all('h3')

#extract and print titles

for book in books:
    title = book.find('a')['title'] # get title from <a> tag within <h3>
    print(title)