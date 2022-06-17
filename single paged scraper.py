# PURPOSE:
# The purpose of this file is to test webscraping and then move the text contents into a textfile.
# After being able to complete this task, I'll try to move on to scraping all the files.
import requests
from bs4 import BeautifulSoup

# URL = "https://www.utdallas.edu/fact-sheets/ah/ba-latin-american-studies/"
URL = "https://catalog.utdallas.edu/now/undergraduate/programs/ah/latin-american-studies"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
courses = soup.find_all("p", class_=[f'xind-{x}' for x in range(0, 7)])
title = soup.find_all("h2", class_="xind-1")
print(title[-1].text)
with open(f'pages\{title[-1].text}.txt', 'w') as file:
    file.write(f'URL: {URL}\n')
    for course in courses:
        file.write(course.text + '\n')