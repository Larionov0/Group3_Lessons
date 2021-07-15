import requests
import json


base_url = 'https://api.openweathermap.org/data/2.5/weather'
appid = 'cb5c7fc26a28e83605cff4b8efb1b85f'


def print_dict(dct):
    print(json.dumps(dct, indent=4))


def main_menu():
    city_name = 'Kyiv'
    while True:
        url = f'{base_url}?q={city_name}&appid={appid}&units=metric'
        response = requests.get(url)
        data = response.json()  # перетворює JSON- строку в словник

        if data['cod'] == 200:
            temp = data['main']['temp']
            weather = data['weather'][0]['main']
        else:
            temp = 'Помилка :('
            weather = 'Помилка :('

        print('--= Синоптик =--')
        print('Місто: ' + city_name)
        print(f'Температура: {temp}')
        print(f"Погода: {weather}")
        print('1 - змінити місто')
        print('2 - вихід')

        choice = input('Ваш вибір: ')

        if choice == '1':
            city_name = input('Нове місто: ')
        elif choice == '2':
            break


main_menu()
