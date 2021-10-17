import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from secret import TOKEN

bot = telebot.TeleBot(token=TOKEN)

data = {
    'mens_clothes': [
        {
            'name': 'капці чорні',
            'price': 150,
            'bought': 31
        },
        {
            'name': 'штани зелені',
            'price': 250,
            'bought': 3
        },
        {
            'name': 'футболка з жирафою',
            'price': 140,
            'bought': 5
        },
        {
            'name': 'шорти спортивні',
            'price': 140,
            'bought': 11
        },
    ]
}


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
    bot.register_next_step_handler_by_chat_id(message.chat.id,
                                              main_menu_handler)  # Сказали боту запам'ятати, що наступне повідомлення цього юзера буде оброблюватися в хендлері main_menu_handler


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
        men_clothes(message)
    elif text == 'назад':
        main_menu(message)


def gen_mens_shop_keyboard():
    keyboard = InlineKeyboardMarkup()
    i = 0
    for product in data['mens_clothes']:
        keyboard.add(InlineKeyboardButton(
            f"{product['name']} ({product['price']} грн) (кулено: {product['bought']})",
            callback_data=str(i)  # індекс товару у списку
        ))
        i += 1
    keyboard.add(InlineKeyboardButton('Назад', callback_data='back'))
    return keyboard


def men_clothes(message):
    bot.send_message(message.chat.id, 'Ви зайшли в чоловічий одяг')
    keyboard = gen_mens_shop_keyboard()
    bot.send_message(message.chat.id, 'Виберіть товар:', reply_markup=keyboard)


@bot.callback_query_handler(lambda call: True)
def mens_shop_handler(query):
    if query.data == 'back':
        bot.answer_callback_query(query.id)  # прибираємо значок годинника
        return main_menu(query.message)

    index = int(query.data)
    product = data['mens_clothes'][index]
    product['bought'] += 1
    # bot.send_message(query.message.chat.id, 'Товар куплено успішно!')

    keyboard = gen_mens_shop_keyboard()
    bot.answer_callback_query(query.id)  # прибираємо значок годинника
    bot.edit_message_text(query.message.text + '!', chat_id=query.message.chat.id,
                          message_id=query.message.id, reply_markup=keyboard)


bot.infinity_polling()
