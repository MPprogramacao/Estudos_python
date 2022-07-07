import requests
from bs4 import BeautifulSoup

requestsDoSite = requests.get("https://agrural.com.br/precossojaemilho/")

soup = BeautifulSoup(requestsDoSite.text, 'html.parser')

tds = []

data_soja = ""; estados_soja = []; praca_soja = []; compra_soja = []; dia_soja = []; semana_soja = []; mes_soja = []
data_milho = ""; estados_milho = []; praca_milho = []; compra_milho = []; dia_milho = []; semana_milho = []; mes_milho = []

j = 0

for td in soup.find_all('td'):    
       tds.append(td.text)
       #print(str(j) + "-" + td.text)
       j+=1

def soja():
    #Pegando data de cotação
    data_soja = tds[1]
    print("Soja – mercado disponível: " + data_soja)
    
    i=0; c = 1; min = 7; max = 190; e = ""
    
    for t in range(len(tds)) :    

        if((i > min) and (i <= max)):
            
            #Pegando as siglas dos estados
            if((len(tds[i]) == 2) and (tds[i] !=  int)):
                estados_soja.append(tds[i])                
                e = tds[i]                      

            #Pegando praça, compra, dia, semana, mes
            elif((len(tds[i]) >= 2) and (tds[i] !=  int)):

                if(c == 1):
                    praca_soja.append(tds[i])
                    print("Praça: " + e + " - "+ tds[i])
                    c = 2
                elif(c == 2):
                    compra_soja.append(tds[i])
                    print("Compra: " + tds[i])
                    c = 3
                elif(c == 3):
                    dia_soja.append(tds[i])
                    print("Dia: " + tds[i])
                    c = 4
                elif(c == 4):
                    semana_soja.append(tds[i])
                    print("Semana: " + tds[i])
                    c = 5
                elif(c == 5):
                    mes_soja.append(tds[i])
                    print("Mês: " + tds[i])
                    c = 1                
        i+=1

def milho():
    data_milho =  tds[193]
    print("\nMilho – mercado disponível: " + data_milho)

    i=0; c = 1; min = 199; max = 403; e = ""
    
    for t in range(len(tds)) :    

        if((i > min) and (i <= max)):
            
            #Pegando as siglas dos estados
            if((len(tds[i]) == 2) and (tds[i] !=  int)):
                estados_milho.append(tds[i])                
                e = tds[i]                      

            #Pegando praça, compra, dia, semana, mes
            elif((len(tds[i]) >= 2) and (tds[i] !=  int)):

                if(c == 1):
                    praca_milho.append(tds[i])
                    print("Praça: " + e + " - "+ tds[i])
                    c = 2
                elif(c == 2):
                    compra_milho.append(tds[i])
                    print("Compra: " + tds[i])
                    c = 3
                elif(c == 3):
                    dia_milho.append(tds[i])
                    print("Dia: " + tds[i])
                    c = 4
                elif(c == 4):
                    semana_milho.append(tds[i])
                    print("Semana: " + tds[i])
                    c = 5
                elif(c == 5):
                    mes_milho.append(tds[i])
                    print("Mês: " + tds[i])
                    c = 1                
        i+=1

soja()
milho()