class User:
    def __init__(self, chat_id, phone_number=None, nickname=None, balance=0, rating=5, purchases_history=None):
        self.chat_id = chat_id
        self.phone_number = phone_number
        self.nickname = nickname
        self.balance = balance
        self.rating = rating
        if purchases_history is None:
            purchases_history = []
        self.purchases_history = purchases_history
        self.next_message_handler = None
