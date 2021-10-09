import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from secret import TOKEN


bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привіт! Вітаємо в нашому боті. Тут можна то сьо.')


@bot.message_handler(commands=['helloer'])
def helloer_handler(message):
    bot.send_message(message.chat.id, 'Hello:)')


@bot.message_handler(content_types=['text'])
def main_menu(message):
    keyboard = ReplyKeyboardMarkup()
    keyboard.row(KeyboardButton('Магазин'), KeyboardButton('Про нас'))
    keyboard.row(KeyboardButton('Підтримка'))
    bot.send_message(message.chat.id, '--= Головне меню =--', reply_markup=keyboard)
    bot.register_next_step_handler_by_chat_id(message.chat.id, main_menu_handler)  # Сказали боту запам'ятати, що наступне повідомлення цього юзера буде оброблюватися в хендлері main_menu_handler


def main_menu_handler(message):
    text = message.text
    if text == 'Магазин':
        store_menu(message)
    elif text == 'Про нас':
        pass
    elif text == 'Підтримка':
        pass


def store_menu(message):
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.row(KeyboardButton('жіночий одяг'), KeyboardButton('чоловічий одяг'), KeyboardButton('дитячий одяг'))
    keyboard.row(KeyboardButton('назад'))
    bot.send_message(message.chat.id, '--= Магазин =--', reply_markup=keyboard)
    bot.register_next_step_handler_by_chat_id(message.chat.id, store_menu_handler)


def store_menu_handler(message):
    text = message.text
    if text == 'жіночий одяг':
        bot.send_message(message.chat.id, 'Ви зайшли в жіночий одяг')
    elif text == 'чоловічий одяг':
        bot.send_message(message.chat.id, 'Ви зайшли в чоловічий одяг')
    elif text == 'назад':
        main_menu(message)


def men_clothes(message):
    keyboard = InlineKeyboardMarkup()


bot.infinity_polling()
