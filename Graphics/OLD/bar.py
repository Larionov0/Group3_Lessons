import plotly.graph_objs as go


names = ['Mark', 'Bob', 'Alice', 'Ann', 'Roman']
marks = [80, 40, 25, 54, 42]

diag = go.Bar(x=names, y=marks)
fig = go.Figure(data=[diag])
fig.write_html('marks.html', auto_open=True)
