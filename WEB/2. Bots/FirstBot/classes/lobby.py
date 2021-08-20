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
        # логіка перевірки кількості гравців
