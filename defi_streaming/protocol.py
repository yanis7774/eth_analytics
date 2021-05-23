# This script uses Web3 to check how many transactions from the prior block belong to the defined smart contract.
# This is useful for counting unique users, transaction volume, etc. 
from web3 import Web3

# Import Alchemy API Key
from dotenv import dotenv_values
config = dotenv_values("../.env")

# I prefer Alchemy as the pricing plans are friendly for people who aren't loaded : )
w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/' + config['API_KEY']))

# Get information about the latest block
latest_block = w3.eth.block_number

# Read data from the latest block
block = w3.eth.getBlock(latest_block)
block_transactions = block['transactions']

uni_history = []

for x in block_transactions:
    #block = w3.eth.get_transaction(x.hex())
    #0x52261237e2dded3bb787c6ee710b42936a517ea7de0d811b7e0d2633c33e0870
    block = w3.eth.get_transaction('0x995588fab6e5518310ae8cd8215c31673c0c11a97bfdee5e6e5b2ffb3b12610e')
    print(block)
    # check if transaction is through Uniswap v2
    if block['to'] == '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D':
        uni_history.append('yes')
    else: 
        uni_history.append('no')

print(uni_history)
