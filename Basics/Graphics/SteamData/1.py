import plotly.graph_objs as go


def double_bubble_sort(main_list, sub_list, n=20):
    length = len(main_list)
    ogr = len(main_list) - 1
    while ogr > length - n - 1:
        i = 0
        while i < ogr:
            if main_list[i] > main_list[i + 1]:
                main_list[i], main_list[i + 1] = main_list[i + 1], main_list[i]
                sub_list[i], sub_list[i + 1] = sub_list[i + 1], sub_list[i]
            i += 1
        ogr -= 1


def build_developers_games_counts_graphic():
    developers_counts = {}
    with open('steam.csv', encoding='utf-8') as file:
        headers = file.readline().rstrip().split(',')
        developer_index = headers.index('developer')
        problems_count = 0

        for line_number, line in enumerate(file):
            try:
                developer = line.rstrip().split(',')[developer_index]
                if developer in developers_counts:
                    developers_counts[developer] += 1
                else:
                    developers_counts[developer] = 1
            except Exception as e:
                print(f'Помилка в лінії {line_number + 1}: {e}')
                problems_count += 1

            if line_number % 5000 == 0:
                print(f'Done with {line_number}')
    print("Всього розробників: ", len(developers_counts))
    print(f'Файл обробився. Кількість помилок: {problems_count}')
    developers = list(developers_counts.keys())
    counts = list(developers_counts.values())

    double_bubble_sort(counts, developers, 25)

    top_developers = developers[-25:]
    top_counts = counts[-25:]

    diag = go.Pie(labels=top_developers, values=top_counts)
    go.Figure(data=[diag]).write_html('developers_games_amounts.html', auto_open=True)


build_developers_games_counts_graphic()
