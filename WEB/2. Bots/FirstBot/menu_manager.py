class MenuManager:
    def __init__(self, bot):
        self.bot = bot

    def main_menu(self, user):
        self.bot.send_message(user.chat_id, '---= Головне меню =---\n'
                                            '1 - створити лобі\n'
                                            '2 - увійти в лобі\n'
                                            '3 - подивитися статистику\n'
                                            '4 - мій аккаунт\n'
                                            'Ваш вибір: ')
        user.next_message_handler = self.main_menu_handler

    def main_menu_handler(self, user, text):
        if text == '1':
            pass
        elif text == '2':
            self.find_lobby_menu(user)
        elif text == '3':
            pass
        elif text == '4':
            pass

    def find_lobby_menu(self, user):
        text = '0 - назад\n'
        for lobby in self.bot.lobbies:
            text += f"{lobby.id} - {lobby.name}  ({len(lobby.players)}/{lobby.players_count})\n"
        self.bot.send_message(user.chat_id, text)
        user.next_message_handler = self.find_lobby_menu_handler

    def find_lobby_menu_handler(self, user, text):
        if text == '0':
            return self.main_menu(user)

        lobby_id = int(text)
        for lobby in self.bot.lobbies:
            if lobby.id == lobby_id:
                break
        # FIXME: передбачити можливість неправильного вводу від користувача

        lobby.add_player(user)
        self.lobby_menu(user, lobby)

    def lobby_menu(self, user, lobby):
        users_text = ''
        for player in lobby.players:
            users_text += f'- {player.nickname}\n'

        text = f'---= Лоббі {lobby.name} =---\n' \
               f'Гравці в лобі:\n{users_text}\n' \
               f'0 - вийти з лобі'
        self.bot.send_message(user.chat_id, text)