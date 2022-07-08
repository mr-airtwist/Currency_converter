# write your code here!
import json
import requests


user_currency = input().lower()
currency_cache = {}
currency = ''
while True:
    r = requests.get(f'http://www.floatrates.com/daily/{user_currency}.json')
    codes = json.loads(r.text)
    exchange_currency = input().lower()
    if exchange_currency == '':
        break
    if exchange_currency == 'usd':
        currency_cache[exchange_currency] = codes[exchange_currency]['rate']
    elif exchange_currency == 'eur':
        currency_cache[exchange_currency] = codes[exchange_currency]['rate']
    elif exchange_currency in currency_cache:
        currency_cache[exchange_currency] = codes[exchange_currency]['rate']
    else:
        currency = codes[exchange_currency]['rate']
    value = int(input())
    print("Checking the cache...")
    if exchange_currency in currency_cache:
        print("Oh! It is in the cache!")
        print(f"You received {value * float(currency_cache[exchange_currency])} {exchange_currency.upper()}.")
    else:
        print("Sorry, but it is not in the cache!")
        print(f"You received {value * float(currency)} {exchange_currency.upper()}.")
        currency_cache[exchange_currency] = codes[exchange_currency]['rate']
