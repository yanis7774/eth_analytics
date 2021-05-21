# We use Infura to access blockchain data as needed from an Infura node. 
import infura
ifr = infura.Client(
    project_id='',
    project_secret='',
    network='mainnet',
    cache_expire_after=5,
)

# web3.py gives us all sorts of great functionality for interaction with EVM compatible blockchains 
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/118e6472b95c47f9b590765c76334131'))

# Get information about the latest block
latest_block = w3.eth.block_number

# Using gql for accessing the GraphQL in The Graph, use whatever lib you prefer
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# first we use the URL provided by The Graph for the individual subgraph we care about. 
# See https://thegraph.com/explorer/subgraph/graphprotocol/compound-v2?query=All%20Markets for an example
sample_transport=RequestsHTTPTransport(
    url='https://api.thegraph.com/subgraphs/name/graphprotocol/compound-v2',
    verify=True,
    retries=5,
)
client = Client(
    transport=sample_transport
)

supply = []
borrow = []
blocks = []
# The Graph is usually a block or two behind so we can subtract from our block number or just catch an exception in our query
x = latest_block-5
days = 90
# In this example I naively loop over blocks in increments of 5760 (roughly the amount of blocks/day)
while days>0: 
    # standard GraphQL formatting, see available queries for this particular subgraph here: https://thegraph.com/explorer/subgraph/graphprotocol/compound-v2?query=All%20Markets
    query = gql('''
    query {
    markets(first: 7, where: {symbol: "cUSDC"}, block: {number: ''' + str(x) + '''}) {
        borrowRate
        collateralFactor
        name
        reserves
        supplyRate
        symbol
        exchangeRate
        totalBorrows
        totalSupply
        underlyingName
        underlyingPrice
        underlyingSymbol
        reserveFactor
        underlyingPriceUSD
    }
    }
    ''')
    response = client.execute(query)
    totalSupply = response['markets'][0]['totalSupply']
    totalBorrows = response['markets'][0]['totalBorrows']
    borrowRate = response['markets'][0]['borrowRate']
    supplyRate = response['markets'][0]['supplyRate']
    exchangeRate = response['markets'][0]['exchangeRate']
    supply.append(float(supplyRate)*100)
    blocks.append(x)
    #borrow.append(totalBorrows)

    # need to multiply by exchangeRate as it's using the value of the cTokens rather than the underlying 
    print("Total Supply/Collateral: " + str(float(totalSupply)*float(exchangeRate)) + " in block " + str(x))
    print("Total Borrow: " + totalBorrows + " in block " + str(x))
    print("Borrow Rate: " + borrowRate + " in block " + str(x))
    print("Supply Rate: " + supplyRate + " in block " + str(x))
    print("Utilization: " + str(float(totalBorrows)/(float(x)*float(exchangeRate))*100) + "in block " + str(latest_block))
    
    # if daily then 5760 block increment
    x=x-5760
    days=days-1

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=blocks, y=supply,
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
