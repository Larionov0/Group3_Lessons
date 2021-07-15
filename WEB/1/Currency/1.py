import requests
import plotly.graph_objs as go
import json
import time


base_url = 'https://api.privatbank.ua/p24api/exchange_rates'


def print_dict(dct):
    print(json.dumps(dct, indent=4))


def get_exchange_rate_for_year(year, currency):
    response = requests.get(f"{base_url}?json&date=01.01.{year}")
    data = response.json()
    # print_dict(data)

    exchanges = data['exchangeRate']
    for currency_info in exchanges:
        if currency_info.get('currency') == currency:
            price = currency_info['saleRateNB']
            return price


def get_currency_prices(currency, year_start=2015, year_end=2021):
    prices = {}
    year = year_start

    t_start = time.time()
    cur_time = t_start
    while year <= year_end:
        print('Дістаємо інформацію за рік: ', year)
        price = get_exchange_rate_for_year(year, currency)
        prices[year] = price
        year += 1
        cur_time_ = time.time()
        print(f'Дістали за {cur_time_ - cur_time} сек')
        cur_time = cur_time_
    print(f'Всього пройшло: {time.time() - t_start} секунд')
    return prices


def get_currency_info(currency='EUR'):
    years_prices = get_currency_prices(currency)
    years = list(years_prices.keys())
    prices = list(years_prices.values())

    diag = go.Bar(x=years, y=prices, name=f'{currency} prices')
    go.Figure(data=[diag]).write_html(f'{currency}_prices.html', auto_open=True)


get_currency_info('RUB')
