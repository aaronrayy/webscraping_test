import imp
from bs4 import BeautifulSoup
import requests
#website = requests.get('https://www.wikipedia.org')
website = requests.get('https://www.quantamagazine.org')
#print(website)
soup = BeautifulSoup(website.content, 'html.parser')

h2tags = soup.find_all('h2')
# for tags in h2tags:
#     print(tags, "\n")

print(soup.prettify())