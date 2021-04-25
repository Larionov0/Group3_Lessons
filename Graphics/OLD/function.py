import plotly.graph_objs as go


def y(x):
    return 2 * x ** 3 - x ** 2 + 2 * x + 10


x_list = []
y_list = []
for x in range(-10, 11):
    y_value = y(x)
    x_list.append(x)
    y_list.append(y_value)

diag = go.Scatter(x=x_list, y=y_list)
go.Figure(data=[diag]).write_html('graphic.html', auto_open=True)
