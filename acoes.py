import yfinance as yf
import pandas_datareader as pdr
import matplotlib.pyplot as plt



entrada=input("Insira o ticket da ação: ")
inicio = input("Insira a data de ínicio: AAAA-MM-DD: ")
fim = input("Insira a data de fim: AAAA-MM-DD: ")
data = pdr.get_data_yahoo(f'{entrada}.SA',start=inicio, end=fim)
    
escolha=input("O que você deseja? \n 1- Verificar máximas\n 2- Verificar Mínimas \n 3- Verificar cotações de abertura \n 4- Verificar Fechamento \n Favor faça sua escolha:  ")
if(escolha=='1'):
              dado='High'
              title='MÁXIMAS'
if(escolha=='2'):
              dado='Low'
              title='MÍNIMAS'
if(escolha=='3'):
              dado='Open'
              title='ABERTURA'
if(escolha=='4'):
              dado='Close'
              title='FECHAMENTO'
              

baixa=(data[f'{dado}'].plot())
plt.style.use("ggplot")
plt.title(f"{title}")
plt.xlabel("DATA")
plt.ylabel(f"VALOR DO(A) {title}")
baixa.get_figure().show()
