import requests
import json
import time
from sensitive_data import TOKEN
from typing import List, Optional, Any


def print_dict(dct):
    print(json.dumps(dct, indent=4, ensure_ascii=False))


def check_if_ok(response_data):
    if response_data['ok'] is False:
        raise Exception(f'Something with message: {response_data}')


class User:
    def __init__(self, chat_id, phone_number=None, name=None, surname=None, balance=0, rating=5, purchases_history=None):
        self.chat_id = chat_id
        self.phone_number = phone_number
        self.name = name
        self.surname = surname
        self.balance = balance
        self.rating = rating
        if purchases_history is None:
            purchases_history = []
        self.purchases_history = purchases_history
        self.next_message_handler = None


class Bot:
    BASE_URL = 'https://api.telegram.org'

    def __init__(self, token):
        self.token = token
        self.last_update_id = 0
        self.users: List[User] = []

    def send_message(self, chat_id, text):
        response = requests.get(f"{self.BASE_URL}/bot{self.token}/sendMessage", params={'chat_id': chat_id, 'text': text})
        result = response.json()
        check_if_ok(result)

    def get_updates(self) -> List[dict]:
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
        print('Bot runs')
        while True:
            self.answer_to_new_messages()
            time.sleep(0.5)

    def create_base_user(self, chat_id):
        new_user = User(chat_id)
        self.users.append(new_user)
        return new_user

    def identify_user(self, chat_id) -> User:
        for user in self.users:
            if user.chat_id == chat_id:
                return user
        # Якщо юзера з таким чат айді не було знайдено
        return self.create_base_user(chat_id)

    def answer_to_message(self, chat_id, text):
        user = self.identify_user(chat_id)
        # self.send_message(chat_id, f'Ви - {user.chat_id} (рейтинг = {user.rating})')
        if user.next_message_handler is None:
            self.main_menu(user)
        else:
            user.next_message_handler(user, text)

    def main_menu(self, user):
        self.send_message(user.chat_id, '---= Головне меню =---\n'
                                        '1 - чоловічий одяг\n'
                                        '2 - жіночий одяг\n'
                                        '3 - дитячий одяг\n'
                                        '4 - купальники\n'
                                        '5 - про нас\n'
                                        '6 - мій аккаунт\n'
                                        'Ваш вибір: ')
        user.next_message_handler = self.main_menu_handler

    def main_menu_handler(self, user, text):
        if text == '1':
            self.mens_clothes_menu(user)
        elif text == '2':
            pass
        elif text == '3':
            pass
        elif text == '4':
            pass
        elif text == '5':
            self.rules_menu(user)

    def rules_menu(self, user):
        self.send_message(user.chat_id, f'---= Про нас =---\n'
                                        f'0 - назад\n'
                                        f'1 - загальні правила\n'
                                        f'2 - залишити заявку\n'
                                        f'3 - доставка\n'
                                        f'4 - контакти\n'
                                        f'5 - історія')
        user.next_message_handler = self.rules_menu_handler

    def rules_menu_handler(self, user, text):
        if text == '1':
            self.send_message(user.chat_id, 'Загальні правила: \n'
                                            'блаблаюбла\n'
                                            '-=-=-=-=-=-')
            self.rules_menu(user)
        elif text == '2':
            pass
        elif text == '3':
            pass
        elif text == '4':
            pass
        elif text == '5':
            pass
        elif text == '0':
            self.main_menu(user)

    def mens_clothes_menu(self, user):
        self.send_message(user.chat_id, '---= Чоловічий одяг =---\n'
                                   '0 - назад\n'
                                   '1 - піджаки\n'
                                   '2 - сорочки\n'
                                   '3 - літній одяг\n'
                                   '4 - штани\n'
                                   'Ваш вибір: ')
        user.next_message_handler = self.mens_clothes_menu_handler

    def mens_clothes_menu_handler(self, user, text):
        if text == '0':
            self.main_menu(user)
        elif text == '1':
            pass
        elif text == '2':
            pass
        elif text == '3':
            pass
        elif text == '4':
            pass
        elif text == '5':
            pass
        elif text == '6':
            pass


bot = Bot(TOKEN)
bot.run()
