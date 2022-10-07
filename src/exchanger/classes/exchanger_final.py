from src.exchanger.classes.exchange import Exchange
from src.exchanger.classes.avaliable import Avaliable
from src.exchanger.classes.exchanger_usd import ExchangerUsd
from src.exchanger.classes.exchanger_uah import ExchangerUah

from pathlib import Path

import json
import requests
import csv
import os

cwd = os.getcwd()
exchange_rate_csv = os.path.join(cwd + '/const', 'exchange_rate_data.csv')
available_currency_csv = os.path.join(cwd + '/const', 'available_currency.csv')

try:
    get_request = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    if get_request.status_code != 200:
        raise Exception('API request unsuccessful.')
    else:
        dict_exchanges = json.loads(get_request.content)
        with open(exchange_rate_csv, 'w') as csv_file:
            val = ['ccy', 'base_ccy', 'buy', 'sale']
            j = csv.DictWriter(csv_file, fieldnames=val)
            j.writeheader()
            for i in dict_exchanges:
                if i['ccy'] == 'USD':
                    j.writerow(i)
except requests.exceptions.ConnectionError:
    print('\nNo internet connection, program will not work correctly!\n')


def result():
    results = []
    with open(exchange_rate_csv) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            results.append(row)
    return results


def available_currency():
    available_currency = []
    with open(available_currency_csv) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            available_currency.append(row)
    return available_currency


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ExchangerFinal(metaclass=SingletonMeta):

    def __init__(self):
        self.exchanges = [Exchange(i['ccy'], i['base_ccy'], float(i['buy']), float(i['sale'])) for i in result()]
        self.avaliables = [Avaliable(i['currency'], float(i['available'])) for i in available_currency()]

    @staticmethod
    def greeting():
        print('Welcome to Money Exchange!',
              'Exit: STOP',
              'If you want to see USD to UAH, print "COURSE USD".',
              'If you want to see UAH to USD, print "COURSE UAH".',
              'To exchange USD to UAH print "EXCHANGE USD ... ".',
              'To exchange UAH to USD print "EXCHANGE UAH ... ".', sep='\n')

    def print_exchange_status(self, exchange, avaliables, val):
        self.avaliables = [Avaliable(i['currency'], float(i['available'])) for i in available_currency()]
        for i in exchange:
            for a in self.avaliables:
                if i.ccy == val:
                    if a.currency != val:
                        print(f'\nRATE: {i.buy}, AVALIABLE: {round(a.available, 2)}\n')

                elif i.base_ccy == val:
                    if a.currency != val:
                        print(f'\nRATE: {i.sale}, AVALIABLE: {round(a.available, 2)}\n')

                else:
                    print(f'\nINVALID CURRENCY {val}\n')
                    break

    def exchanger(self, exchange, avaliables, val):
        self.avaliables = [Avaliable(i['currency'], float(i['available'])) for i in available_currency()]
        val_lst = []
        for i in exchange:
            for a in self.avaliables:
                val_lst.append(a.currency)
                if i.ccy == val[0] and val_lst != val[0]:
                    ExchangerUah.exchanger_uah(self, exchange, avaliables, val)
                    break
                elif i.base_ccy == val[0] and val_lst != val[0]:
                    ExchangerUsd.exchanger_usd(self, exchange, avaliables, val)
                    break
                else:
                    print(f'\nINVALID CURRENCY {val[0]}\n')
                    break
