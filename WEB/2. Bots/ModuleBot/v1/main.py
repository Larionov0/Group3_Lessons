import telebot
from secret import TOKEN


bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привіт! Вітаємо в нашому боті. Тут можна то сьо.')


@bot.message_handler(commands=['helloer'])
def helloer_handler(message):
    bot.send_message(message.chat.id, 'Hello:)')


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text
    if 'привіт' in text.lower():
        bot.send_message(message.chat.id, 'Доброго дня!')
    else:
        bot.send_message(message.chat.id, text)


bot.infinity_polling()
