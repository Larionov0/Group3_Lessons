import plotly.graph_objs as go
from plotly.subplots import make_subplots


diag1 = go.Bar(x=['a', 'b', 'c', 'd'], y=[5, 2, 6, 1], name='Літери1')
diag2 = go.Bar(x=['v', 't', 'w', 'y'], y=[6, 2, 5, 1], name='Літери2')

fig = make_subplots(rows=2, cols=2)
fig.append_trace(diag1, 1, 1)
fig.append_trace(diag2, 2, 2)

fig.write_html('many_diags.html', auto_open=True)
