from bs4 import BeautifulSoup as BS
import requests

url = requests.get("https://sinoptik.ua/погода-нижний-новгород")
soup = BS(url.text, features="html.parser")
arr = []
for el in soup.find('div', {'class': 'description'}):
    arr.append(el)
phrase = arr[2]

