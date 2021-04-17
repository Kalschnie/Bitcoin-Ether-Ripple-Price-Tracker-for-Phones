import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
from pushover import Client
Url='https://www.bitcoin.de/de'
page= requests.get(Url)
soup= BeautifulSoup(page.content,'html.parser')
Preis=soup.find(id='ticker_price').text
print('Bitcoin:',Preis)
Url2='https://www.bitcoin.de/de/etheur/market'
page= requests.get(Url2)
soup= BeautifulSoup(page.content,'html.parser')
Preis2=soup.find(id='ticker_price').text
print('Ethereum:',Preis2)
Url3='https://www.bitcoin.de/de/xrpeur/market'
page= requests.get(Url3)
soup= BeautifulSoup(page.content,'html.parser')
Preis3=soup.find(id='ticker_price').text
print('Ripple:',Preis3)
client = Client("ID", api_token="Token")
client.send_message(Preis3, title='Ripple:')
client.send_message(Preis2, title='Ethereum:')
client.send_message(Preis, title='Bitcoin:')
