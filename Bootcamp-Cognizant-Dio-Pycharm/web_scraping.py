import requests
from bs4 import BeautifulSoup


site = requests.get('https://www.climatempo.com.br').content

soup = BeautifulSoup(site, 'html.parser')

print(soup.prettify())
print(soup.find('title').string)
