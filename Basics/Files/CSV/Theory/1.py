from json import dumps


def task1():
    """
    Вивести юзерів з найбільшою і найменшою кількістю монет
    """
    with open('users.csv', 'rt') as file:
        max_coins = 0
        max_username = ''

        headers = file.readline()

        for line in file:
            line_list = line.rstrip().split(', ')
            username = line_list[1]
            coins = int(line_list[2])
            if coins > max_coins:
                max_coins = coins
                max_username = username

        print(max_username, max_coins)


def task2():
    """
    Функція має повернути словник, ключами в якому є хоббі,
    а значеннями - кількості цих хоббі.
    """
    with open('users.csv', 'rt') as file:
        headers = file.readline().rstrip().split(', ')
        hobbies_index = headers.index('hobbies')

        hobbies_counts = {}

        for line in file:  # 3, Bob, 200, 12; 21; 41, gaming, books, fishing
            user_list = line.rstrip().split(', ')
            hobbies_str = user_list[hobbies_index]
            hobbies = hobbies_str.split('; ')
            for hobby in hobbies:
                if hobby not in hobbies_counts:
                    hobbies_counts[hobby] = 0
                hobbies_counts[hobby] += 1
    return hobbies_counts


def convert_users_file_to_articles_username_dict(filename='users.csv'):
    """
    Повертає словник.
    Ключі - айді статей
    Значення - імена авторів статей
    """
    articles_usernames = {}
    with open(filename, 'rt') as file:
        headers = file.readline().rstrip().split(', ')
        articles_index = headers.index('articles_ids')
        username_index = headers.index('name')

        for line in file:
            user_list = line.rstrip().split(', ')
            articles_ids = user_list[articles_index]
            username = user_list[username_index]

            for article_id in articles_ids.split('; '):
                if article_id.isdigit():
                    articles_usernames[article_id] = username
    return articles_usernames


def task3():
    """
    Функція має обробляти 2 файли: articles.csv & users.csv.
    Повертає словник, ключами в якому є жанри статей.
    Значеннями є списки з іменами юзерів, які писали хоч одну
    статтю в цьому жанрі

    {
        'programming': ['Klara', 'Ksenia'],
        'databases': ['Klara'],
        'ORM': ['Klara'],
        'fishing': ['Klara']
    }
    """
    final_dict = {}
    articles_usernames = convert_users_file_to_articles_username_dict()
    with open('articles.csv', 'rt', encoding='utf-8') as file:
        headers = file.readline().rstrip().split(', ')
        article_index = headers.index('id')
        genres_index = headers.index('genres')

        for line in file:
            article_list = line.rstrip().split(', ')  # ['21', 'kokoko', 'hunting; fishing; books']
            article_id = article_list[article_index]
            genres = article_list[genres_index]

            author_name = articles_usernames[article_id]

            for genre in genres.split('; '):
                if genre not in final_dict:
                    final_dict[genre] = []

                if author_name not in final_dict[genre]:
                    final_dict[genre].append(author_name)
    return final_dict


print(dumps(task3(), indent=4))
