'''
***All credit for data sourced for this project goes to exchangerates.org.uk***

This function scrapes conversion rates between GBP(£) and some of the most 
common currencies in the world. The function takes one argument, gbp, that 
must be either an integar or a float. 
'''

def currency_func(gbp):

    import requests
    from bs4 import BeautifulSoup
    
    URL = 'https://www.exchangerates.org.uk/'
    page = requests.get(URL,'html.parser')
    soup = BeautifulSoup(page.content, 'html.parser')
    
    #grabbing the desired div and table for which the desired data is housed
    table = soup.find('table')
    
    #grabbing all of the desired table data 
    eur_exch = float(table.find_all('td')[3].text)
    usd_exch = float(table.find_all('td')[8].text)
    nzd_exch = float(table.find_all('td')[13].text)
    aud_exch = float(table.find_all('td')[18].text)
    cad_exch = float(table.find_all('td')[23].text)
    jpy_exch = float(table.find_all('td')[28].text)
    zar_exch = float(table.find_all('td')[33].text)
    aed_exch = float(table.find_all('td')[38].text)
    inr_exch = float(table.find_all('td')[43].text)
    try_exch = float(table.find_all('td')[48].text)
    chf_exch = float(table.find_all('td')[53].text)
    
    exchange_rates = [eur_exch, usd_exch, nzd_exch, aud_exch, cad_exch,
                      jpy_exch, zar_exch, aed_exch, inr_exch, try_exch,
                      chf_exch]
    
    return [gbp * x for x in exchange_rates]