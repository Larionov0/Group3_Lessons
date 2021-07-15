import plotly.graph_objs as go


x_list = [1, 2, 3, 4, 5, 3]
y_list = [1, 4, 3, 7, 2, 3]

diag = go.Scatter(x=x_list, y=y_list)
go.Figure(data=[diag]).write_html('graphic.html', auto_open=True)
