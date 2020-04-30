'''
***All credit for data sourced for this project goes to exchangerates.org.uk***

This program scrapes conversion rates between GBP(£) and some of the most 
common currencies in the world. 
'''

import requests
from bs4 import BeautifulSoup
URL = 'https://www.exchangerates.org.uk/'
page = requests.get(URL,'html.parser')
soup = BeautifulSoup(page.content, 'html.parser')

panel = soup.find('div',class_='css-panes-sml')
#grabs the desired div

table = soup.find('table')
#grabs the desired table

eur_exchrate = table.find_all('td')[3].text
usd_exchrate = table.find_all('td')[8].text
nzd_exchrate = table.find_all('td')[13].text
aud_exchrate = table.find_all('td')[18].text
cad_exchrate = table.find_all('td')[23].text
jpy_exchrate = table.find_all('td')[28].text
zar_exchrate = table.find_all('td')[33].text
aed_exchrate = table.find_all('td')[38].text
inr_exchrate = table.find_all('td')[43].text
try_exchrate = table.find_all('td')[48].text
chf_exchrate = table.find_all('td')[53].text

exchrate_list = [eur_exchrate, usd_exchrate, nzd_exchrate, aud_exchrate, 
                 cad_exchrate, jpy_exchrate, zar_exchrate, aed_exchrate, 
                 inr_exchrate, try_exchrate, chf_exchrate]


print(exchrate_list)
