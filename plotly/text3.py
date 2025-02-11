import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

trace1 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 3, 2, 4, 3, 4, 6, 5]
)

trace2 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 4, 5, 1, 2, 2, 3, 4, 2]
)

data = [trace1, trace2]

layout = go.Layout(
    showlegend=False,
    annotations=[
        dict(
            x=2,
            y=5,
            xref='x',
            yref='y',
            text='dict Text',
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-40
        )
    ]
)

fig = go.Figure(data=data, layout=layout)
iplot(fig)