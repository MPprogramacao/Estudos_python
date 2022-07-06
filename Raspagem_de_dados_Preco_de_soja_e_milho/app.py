import requests
from bs4 import BeautifulSoup

requestsDoSite = requests.get("https://agrural.com.br/precossojaemilho/")

soup = BeautifulSoup(requestsDoSite.text, 'html.parser')

tds = []

data_soja = ""; estados_soja = []; praca_soja = []; compra_soja = []; dia_soja = []; semana_soja = []; mes_soja = []

for td in soup.find_all('td'):    
       tds.append(td.text)

def soja():
    #Pegando data de cotação
    data_soja = tds[1]
    print("Soja – mercado disponível: " + data_soja)
    
    i=0; c = 1; max = 190; e = ""
    
    for t in range(len(tds)) :    

        if((i > 7) and (i <= max)):
            
            #Pegando as siglas dos estados
            if((len(tds[i]) == 2) and (tds[i] !=  int)):
                estados_soja.append(tds[i])                
                e = tds[i]                      

            #Pegando praçca, compra, dia, semana, mes
            elif((len(tds[i]) >= 2) and (tds[i] !=  int)):

                if(c == 1):
                    praca_soja.append(tds[i])
                    print("Praça : " + e + " - "+ tds[i])
                    c = 2
                elif(c == 2):
                    compra_soja.append(tds[i])
                    print("Compra : " + tds[i])
                    c = 3
                elif(c == 3):
                    dia_soja.append(tds[i])
                    print("Dia : " + tds[i])
                    c = 4
                elif(c == 4):
                    semana_soja.append(tds[i])
                    print("Semana : " + tds[i])
                    c = 5
                elif(c == 5):
                    mes_soja.append(tds[i])
                    print("Mês : " + tds[i])
                    c = 1                
        i+=1

soja()