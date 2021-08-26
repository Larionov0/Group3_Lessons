import json


def make_keyboard(list_keyboard):
    """
    keyboard = [
        ["Грати", "Магазин"],
        ["Моя корзина"],
        ["Друзі", "Підтримка"]
    ]
    f(keyboard)  -> JSON:
    {
      "keyboard": [
        [{"text": "Пошук лобі"}, {"text": "Створити лобі"}],
        [{"text": "Магазин"}],
        [{"text": "Підтримка"}]
      ]
    }
    """
    dct = {
        "keyboard": []
    }

    for row in list_keyboard:
        new_row = []
        for button_name in row:
            button = {'text': button_name}
            new_row.append(button)
        dct['keyboard'].append(new_row)
    return json.dumps(dct, ensure_ascii=False)


if __name__ == '__main__':
    print(make_keyboard([
        ["Грати", "Магазин"],
        ["Моя корзина"],
        ["Друзі", "Підтримка"]
    ]))
