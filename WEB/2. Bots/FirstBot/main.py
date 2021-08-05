import requests
import json
import time
from sensitive_data import TOKEN  # Створіть файл sensitive_data.py і вставте туди змінну з токеном свого бота (створіть його в botfather)


MY_CHAT_ID = '358463252'
BASE_URL = 'https://api.telegram.org'


def print_dict(dct):
    print(json.dumps(dct, indent=4, ensure_ascii=False))


def send_message(chat_id, text):
    # requests.get(f'{BASE_URL}/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}')
    requests.get(f'{BASE_URL}/bot{TOKEN}/sendMessage', params={'chat_id': chat_id, 'text': text})


def get_updates(last_update_id):
    response = requests.get(f'{BASE_URL}/bot{TOKEN}/getUpdates?offset={last_update_id + 1}')
    data = response.json()

    return data['result']


def echo_answer_to_message(chat_id, text):
    send_message(chat_id, text)


def calculator_answer_to_message(chat_id, text):
    try:
        if '+' in text:
            numbers = text.split('+')
            sum_ = 0
            for num in numbers:
                sum_ += float(num)

            send_message(chat_id, text + ' = ' + str(sum_))
        else:
            send_message(chat_id, 'Спробуйте надіслати приклад з +')
    except Exception as error:
        print(f'Error: {error}')
        send_message(chat_id, 'Сталася якась помилка:(')


def answer_to_new_messages(last_update_id_another):
    updates = get_updates(last_update_id_another)

    for update in updates:
        if 'message' in update:
            chat_id = update['message']['chat']['id']
            text = update['message']['text']
            calculator_answer_to_message(chat_id, text)
            last_update_id_another = update['update_id']
    return last_update_id_another


def run():
    print('Bot started')
    last_update_id = 0  # Ідентифікатор останнього повідомлення, на яке відповів наш бот (потрібно для відмежовування нових оновлень від старих)
    while True:
        last_update_id = answer_to_new_messages(last_update_id)
        time.sleep(0.3)


# run()
send_message('358463252', 'Hello')
