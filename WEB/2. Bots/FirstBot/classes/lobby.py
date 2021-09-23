from tools.keyboards import make_keyboard
import random


PHRASES = {
    'mafia': 'Ти мафія - _ -    Повбивай їх усіх!',
    'citizen': 'Ти - мирний житель. Постій! Не виходь з гри. У тебе є важлива місія - зупини мафію'
}


class Lobby:
    def __init__(self, bot, id, name, players_count, players=None, is_in_game=False, password=None):
        self.bot = bot
        self.id = id
        self.name = name
        self.players_count = players_count
        if players is None:
            players = []
        self.players = players
        self.is_in_game = is_in_game
        self.password = password

    def add_player(self, player):
        self.players.append(player)
        player.lobby = self

        for player in self.players:
            self.lobby_menu(player)

        if len(self.players) == self.players_count:
            self.start_game()

    def remove_player(self, player):
        self.players.remove(player)
        player.lobby = None

        for player in self.players:
            self.lobby_menu(player)

    # menu - handlers
    def lobby_menu(self, user):
        users_text = ''
        for player in self.players:
            users_text += f'- {player.nickname}\n'

        text = f'---= Лоббі {self.name} =---\n' \
               f'Гравці в лобі:\n{users_text}\n'
        self.bot.send_message(user.chat_id, text, make_keyboard([['Вийти']]))
        user.next_message_handler = self.lobby_menu_handler

    def lobby_menu_handler(self, user, text):
        if text == 'Вийти':
            self.remove_player(user)
            return self.bot.menu_manager.main_menu(user)

    def distribute_roles(self):
        for player in self.players:
            player.role = 'citizen'
        mafia = random.choice(self.players)
        mafia.role = 'mafia'

    def notify_everyone_about_roles(self):
        for player in self.players:
            self.bot.send_message(player.chat_id, PHRASES[player.role])

    def start_game(self):
        self.is_in_game = True

        for player in self.players:
            self.bot.send_message(player.chat_id, 'Гра почалась')

        self.distribute_roles()
        self.notify_everyone_about_roles()
        for player in self.players:
            self.day_menu(player)

    def day_menu(self, user):
        text = '----| День |----\n' \
               'Спілкуйтеся та голосуйте'
        self.bot.send_message(user.chat_id, text)
        user.next_message_handler = self.day_menu_handler

    def day_menu_handler(self, user, text):
        for player in self.players:
            if player != user:
                self.bot.send_message(player.chat_id, f'{user.nickname}: {text}')

#
# if __name__ == '__main__':
#     lobby = Lobby(1, 'Китайське', 4)
#     user = User(12351)
#
#     lobby.add_player(user)
#
#     user.lobby.players_count = 15
#     print(lobby.players_count)
