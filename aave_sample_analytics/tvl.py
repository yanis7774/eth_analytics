# Get the total value locked in Aave, includes staked Aave and outstanding collateral 

import requests
import json 
from datetime import datetime


tvl = requests.get('https://api.llama.fi/protocol/aave').json()['tvl']
dates = []
values = []
for x in tvl: 
    dates.append(datetime.fromtimestamp(int(x['date'])))
    values.append(x['totalLiquidityUSD'])


import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=dates, y=values,
                    mode='lines',
                    name='lines',
                    line_color='blue'))

fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linewidth=2,
        zeroline=True,
        linecolor='#F4F4F4',
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=14,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        showticklabels=True,
        gridcolor='#F4F4F4',
        tickfont=dict(
            family='Arial',
            size=14,
            color='blue',
        ),
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    autosize=True,

    plot_bgcolor='white'
)

'''
fig.add_layout_image(
    dict(
        source="https://images.plot.ly/language-icons/api-home/python-logo.png",
        xref="x",
        yref="y",
        x=0,
        y=3,
        sizex=2,
        sizey=2,
        sizing="stretch",
        opacity=0.5,
        layer="below")
)
'''
fig.show()