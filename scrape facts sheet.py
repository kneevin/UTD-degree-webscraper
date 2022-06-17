# https://www.utdallas.edu/wp-sitemap-posts-fact_sheets-1.xml
# PURPOSE:
# The point of this is to grab links to all of the maps 
import requests
from bs4 import BeautifulSoup

URL = "https://www.utdallas.edu/wp-sitemap-posts-fact_sheets-1.xml"
page = requests.get(URL)
soup = BeautifulSoup(page.text, features='xml')
urls = soup.find_all('loc')
with open(''):
    for url in urls:
        print(url.text)