import plotly.graph_objs as go


def build_users_coins_graphic():
    names = []
    coins = []

    with open('users.csv', 'rt') as file:
        headers = file.readline().rstrip().split(', ')
        name_index = headers.index('name')
        coins_index = headers.index('coins')

        for line in file:
            line_list = line.rstrip().split(', ')
            names.append(line_list[name_index])
            coins.append(int(line_list[coins_index]))

    print(names, coins)
    diag = go.Bar(x=names, y=coins, name='Імена-монети')
    go.Figure(data=[diag]).write_html('users_coins.html', auto_open=True)


def build_hobbies_counts_graphic():
    hobbies_counts = {}
    with open('users.csv', encoding='utf-8') as csv_file:
        headers = csv_file.readline().rstrip().split(', ')
        hobbies_index = headers.index('hobbies')

        for line in csv_file:
            hobbies = line.rstrip().split(', ')[hobbies_index].split('; ')
            for hobby in hobbies:
                if hobby in hobbies_counts:
                    hobbies_counts[hobby] += 1
                else:
                    hobbies_counts[hobby] = 1

    hobbies = list(hobbies_counts.keys())
    counts = list(hobbies_counts.values())
    diag = go.Pie(labels=hobbies, values=counts, name='Кількості хоббі')
    go.Figure(data=[diag]).write_html('hobbies.html', auto_open=True)


build_hobbies_counts_graphic()
