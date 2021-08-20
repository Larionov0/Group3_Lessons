import requests
import json
import time
from sensitive_data import TOKEN
from typing import List, Optional, Any
from menu_manager import MenuManager
from classes.user import User
from classes.lobby import Lobby


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
        self.users: List[User] = []
        self.lobbies: List[Lobby] = [
            Lobby(1, 'Універсальне', 5),
            Lobby(2, 'Українське', 3)
        ]
        self.menu_manager = MenuManager(self)

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
            self.menu_manager.main_menu(user)
        else:
            user.next_message_handler(user, text)


bot = Bot(TOKEN)
bot.run()
