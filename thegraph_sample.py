from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

sample_transport=RequestsHTTPTransport(
    url='https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2',
    verify=True,
    retries=5,
)
client = Client(
    transport=sample_transport
)

liquidity = []
volume = []
transactions = []
x = 11276855

while x > 11250000: 
    query = gql('''
    query {
    uniswapFactory(id: "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f", block: {number: ''' + str(x) + '''}) {
        totalVolumeUSD
        totalLiquidityUSD
        txCount
    }
    }
    ''')
    response = client.execute(query)
    liquidity_value = response['uniswapFactory']['totalLiquidityUSD']
    volume_value = response['uniswapFactory']['totalVolumeUSD']
    transactions_value = response['uniswapFactory']['txCount']
    liquidity.insert(0, liquidity_value)
    volume.append(volume_value)
    transactions.append(transactions_value)
    x=x-1000
    print(x)
print(liquidity)

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# normalize or standardize data as
'''
liquidity = [float(i) for i in liquidity]
volume = [float(i) for i in volume]
transactions = [float(i) for i in transactions]
liquidity = [float(i)/sum(liquidity) for i in liquidity]
volume = [float(i)/sum(volume) for i in volume]
transactions = [float(i)/sum(transactions) for i in transactions]
#title = 'Uniswap Liquidity Over Time'
labels = ['Liquidity', 'Volume', 'Transactions']
'''
x = np.arange(len(liquidity))

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(x=x, y=liquidity, name="Liquidity"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=x, y=volume, name="Volume"),
    secondary_y=True,
)

'''
fig.add_trace(
    go.Scatter(x=x, y=transactions, name="Transactions"),
    secondary_y=True,
)
'''

# Add figure title
fig.update_layout(
    title_text="Uniswap Liquidity vs Volume"
)

# Set x-axis title
fig.update_xaxes(title_text="Blocks")

# Set y-axes titles
fig.update_yaxes(title_text="Liquidity", secondary_y=False)
fig.update_yaxes(title_text="Volume", secondary_y=True)

fig.show()