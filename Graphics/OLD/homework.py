import plotly.graph_objs as go
buki = [
    {
        "тип": "казявка",
        "имя": "Бузявка",
        "кусючесть": 4
    },
    {
        "тип": "муравей",
        "имя": "Боровей",
        "кусючесть": 8
    },
    {
        "тип": "казявка",
        "имя": "Лизявка",
        "кусючесть": 3
    },
    {
        "тип": "казявка",
        "имя": "Жизявка",
        "кусючесть": 5
    },
    {
        "тип": "муравей",
        "имя": "Боверой",
        "кусючесть": 11
    },
    {
        "тип": "бабочка",
        "имя": "Аня",
        "кусючесть": 1
    },
    {
        "тип": "бабочка",
        "имя": "Ваня",
        "кусючесть": 0
    },
]
types = ['казявка', 'муравей', 'бабочка']
counts = []
count_kaziawka_kus = 0
count_murawei_kus = 0
count_babochka_kus = 0
count_kaziawka = 0
count_murawei = 0
count_babochka = 0
for buka in buki:
    type_ = buka["тип"]
    kusuchest = buka["кусючесть"]
    if type_ == "казявка":

        count_kaziawka_kus += kusuchest
        count_kaziawka += 1
    elif type_ == "муравей":

        count_murawei_kus += kusuchest
        count_murawei += 1
    elif type_ == "бабочка":

        count_babochka_kus += kusuchest
        count_babochka += 1

serednia_kaziawka = count_kaziawka_kus/count_kaziawka
counts.append(serednia_kaziawka)
serednia_murawei = count_murawei_kus/count_murawei
counts.append(serednia_murawei)
serednia_babochka = count_babochka_kus/count_babochka
counts.append(serednia_babochka)

diag = go.Pie(labels=types, values=counts)
fig = go.Figure(data=[diag])
fig.write_html('nasekomie.html', auto_open = True)