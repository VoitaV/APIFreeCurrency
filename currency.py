#currency converter
import requests

CUR_KEY = 'fca_live_ILOya4jdS0YzwvACs7Lp6FLYZQb6b8dZfyIo9LeA'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={CUR_KEY}'

CURRENCIES = ['USD', 'CAD', 'EUR']

def convert_currancy(base):
    currencies = ','.join(CURRENCIES)
    url = f'{BASE_URL}&base_currency={base}&currencies={currencies}'

    try:
        responce = requests.get(url)
        data = responce.json()
        return data['data']
    except:
        print('Invalid currency')
        return None
while True:
    base = input('Input the base currency (q for quit): ').upper()
    if base == 'Q':
        break
    data = convert_currancy(base)
    if not data:
        continue
    del data[base]
    for ticker, value in data.items():
            print(f'{ticker}, {value}')