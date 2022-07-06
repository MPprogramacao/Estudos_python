import requests
from bs4 import BeautifulSoup

requestsDoSite = requests.get("https://www.w3schools.com/python/module_requests.asp");
soup = BeautifulSoup(requestsDoSite.text, 'html.parser')

print(soup.prettify())