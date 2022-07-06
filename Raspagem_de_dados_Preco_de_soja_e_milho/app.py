import requests
from bs4 import BeautifulSoup

requestsDoSite = requests.get("https://agrural.com.br/precossojaemilho/")
print(requestsDoSite)


soup = BeautifulSoup(requestsDoSite.text, 'html.parser')

data = ""
compra = []; dia = []; semana = []; mes = []

i = 0
for td in soup.find_all('td'):
    i+=1
    print(i)
    if(i == 2):
        print(td.get_text())
        data = td.get_text(); 
    if((i > 9)):
        print(td)
