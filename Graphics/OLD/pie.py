import plotly.graph_objs as go


countries = ['Kotia', 'Anatia', 'Buratia', 'Illyatia', 'Romania']
squares = [80, 40, 25, 54, 42]

diag = go.Pie(labels=countries, values=squares)
fig = go.Figure(data=[diag])
fig.write_html('countries.html', auto_open=True)
