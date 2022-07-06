import requests
from bs4 import BeautifulSoup

requestsDoSite = requests.get("https://agrural.com.br/precossojaemilho/")
#print(requestsDoSite)


soup = BeautifulSoup(requestsDoSite.text, 'html.parser')

data = ""
praca = []; compra = []; dia = []; semana = []; mes = []

i = 2

'''
for td in soup.find_all('td'):
    i+=1
    #print(i)
    if(i == 2):
        #print(td.get_text())
        data = td.get_text()
    if(i == 3):        
        praca.append(td.get_text())
        print(td.get_text())        

    if(i == 4):
        praca.append(td.get_text())
        print(td.get_text())

    if(i == 5):
        praca.append(td.get_text())
        print(td.get_text())

    if(i == 6):
        praca.append(td.get_text())
        print(td.get_text())

    if(i == 7):
        praca.append(td.get_text())
        print(td.get_text())
        i=3

    i+=1'''

tds = []

estados_soja = []; praca_soja = []; compra_soja = []; dia_soja = []; semana_soja = []; mes_soja = []

for td in soup.find_all('td'):    
       tds.append(td.text)

def soja():
    data = tds[1]
    print(data)

    i=0; c = 1; max = 190
    

    for dadoTd in range(len(tds)):    

        if((i > 7) and (i <= max)):

            #Pegando as siglas dos estados
            if((len(tds[i]) == 2) and (tds[i] !=  int)):
                estados_soja.append(tds[i])       
                print(tds[i])

            #Pegando praçca, compra, dia, semana, mes
            elif((len(tds[i]) >= 2) and (tds[i] !=  int)):
                
                if(c == 1):
                    praca_soja.append(tds[i])
                    print("Praça : " + tds[i])
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