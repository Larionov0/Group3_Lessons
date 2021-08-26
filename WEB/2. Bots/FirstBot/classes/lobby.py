class Lobby:
    def __init__(self, id, name, players_count, players=None, is_in_game=False, password=None):
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

        # логіка перевірки кількості гравців

    def remove_player(self, player):
        self.players.remove(player)
        player.lobby = None

#
# if __name__ == '__main__':
#     lobby = Lobby(1, 'Китайське', 4)
#     user = User(12351)
#
#     lobby.add_player(user)
#
#     user.lobby.players_count = 15
#     print(lobby.players_count)
