import requests
import json
import time
from sensitive_data import TOKEN
from coctail_manager import CocktailManager


def print_dict(dct):
    print(json.dumps(dct, indent=4, ensure_ascii=False))


def check_if_ok(response_data):
    if response_data['ok'] is False:
        raise Exception(f'Something with message: {response_data}')


class Bot:
    BASE_URL = 'https://api.telegram.org'

    def __init__(self, token):
        self.token = token
        self.last_update_id = 0
        self.cocktail_manager = CocktailManager()

    def send_message(self, chat_id, text):
        response = requests.get(f"{self.BASE_URL}/bot{self.token}/sendMessage", params={'chat_id': chat_id, 'text': text})
        result = response.json()
        check_if_ok(result)

    def get_updates(self):
        response = requests.get(f"{self.BASE_URL}/bot{self.token}/getUpdates", params={'offset': self.last_update_id + 1})
        data = response.json()
        check_if_ok(data)
        return data['result']

    def answer_to_new_messages(self):
        updates = self.get_updates()

        for update in updates:
            chat_id = update['message']['chat']['id']
            text = update['message']['text']

            self.answer_to_message(chat_id, text)
            self.last_update_id = update['update_id']

    def run(self):
        while True:
            self.answer_to_new_messages()
            time.sleep(0.5)

    def answer_to_message(self, chat_id, text):
        if text == '/start':
            self.send_message(chat_id, 'Цей бот шукає рецепти напоїв. Пишітб назви напоїв (англ)')
        else:
            drinks = self.cocktail_manager.get_drinks(text)
            # text = 'Всі напої за вашим запитом: \n'
            for drink in drinks:
                text = ''
                text += drink.name + '\n'
                for ingr in drink.ingredients:
                    text += f'- {ingr}\n'
                text += drink.instructions + '\n'
                text += drink.img_src
                self.send_message(chat_id, text)
            # self.send_message(chat_id, text)


bot = Bot(TOKEN)
bot.run()
