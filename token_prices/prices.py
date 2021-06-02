from pycoingecko import CoinGeckoAPI
from datetime import datetime
cg = CoinGeckoAPI()
tokens = cg.get_coins_list()
print(tokens)
date = []
eth_price = []
solana_price = []
avalanche_price = []
binance_price = []
terrausd_price = []

eth_price_history = cg.get_coin_market_chart_by_id(id='ethereum', vs_currency='usd', days='10')
price_dict = eth_price_history['prices']
for x in price_dict: 
    date.append(datetime.fromtimestamp(x[0]/1000))
    eth_price.append(x[1])

solana_price_history = cg.get_coin_market_chart_by_id(id='solana', vs_currency='usd', days='10')
price_dict = solana_price_history['prices']
for x in price_dict: 
    solana_price.append(x[1])

print(eth_price)

avalanche_price_history = cg.get_coin_market_chart_by_id(id='avalanche-2', vs_currency='usd', days='10')
price_dict = avalanche_price_history['prices']
for x in price_dict: 
    avalanche_price.append(x[1])


binance_price_history = cg.get_coin_market_chart_by_id(id='binancecoin', vs_currency='usd', days='10')
price_dict = binance_price_history['prices']
for x in price_dict: 
    binance_price.append(x[1])

terrausd_price_history = cg.get_coin_market_chart_by_id(id='terrausd', vs_currency='usd', days='15', time='1h')
price_dict = terrausd_price_history['prices']
for x in price_dict: 
    terrausd_price.append(x[1])


import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(specs=[[{"secondary_y": True}]])

'''
fig.add_trace(go.Scatter(x=date, y=eth_price,
                    mode='lines',
                    name='ETH Price',
                    line_color='blue'))
fig.add_trace(go.Scatter(x=date, y=solana_price,
                    mode='lines',
                    name='SOL Price',yaxis='y2'))
fig.add_trace(go.Scatter(x=date, y=avalanche_price,
                    mode='lines',
                    name='AVAX Price',yaxis='y3'))
fig.add_trace(go.Scatter(x=date, y=binance_price,
                    mode='lines',
                    name='BNB Price',yaxis='y4'))
'''
fig.add_trace(go.Scatter(x=date, y=terrausd_price,
                    mode='lines',
                    name='TerraUSD Price',
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
            color='blue',
        ),
    ),
    yaxis2=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        showticklabels=True,
        gridcolor='#F4F4F4',
        tickfont=dict(
            family='Arial',
            size=22,
            color='blue',
        ),
    ),
    yaxis3=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        showticklabels=True,
        gridcolor='#F4F4F4',
        tickfont=dict(
            family='Arial',
            size=22,
            color='blue',
        ),
    ),
    yaxis4=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        showticklabels=True,
        gridcolor='#F4F4F4',
        tickfont=dict(
            family='Arial',
            size=22,
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