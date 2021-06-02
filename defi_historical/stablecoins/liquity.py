import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px
import requests
import json 
from datetime import datetime


troves_data = pd.read_csv('data/liquity_troves.csv')  
tvl = requests.get('https://api.llama.fi/protocol/alchemix')
tvl = tvl.json()
tvl = tvl['tvl']
date = []
value = []
for x in tvl: 
    date.append(datetime.fromtimestamp(int(x['date'])))
    value.append(x['totalLiquidityUSD'])

fig = px.line(troves_data, x="hour", y="troves")
#fig = px.line(ohm_apy_data, x="evt_block_time", y="apy")

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
            size=22,
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
            size=22,
            color='grey',
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
