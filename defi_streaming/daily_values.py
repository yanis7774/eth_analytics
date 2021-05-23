# This script helps you find the cumulative values from contracts over 24 hours
# This is useful for counting unique users, transaction volume, etc. 
from web3 import Web3

# Import Alchemy API Key
from dotenv import dotenv_values
config = dotenv_values("../.env")

# I prefer Alchemy as the pricing plans are friendly for people who aren't loaded : )
w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/' + config['API_KEY']))

# Get the block number for the latest block
latest_block = w3.eth.block_number
block = latest_block

# Read data from last 6,500 blocks to get 24 hours of transactions 
while block > (latest_block - 6500):
    # Read data from the latest block
    current_block = w3.eth.getBlock(block)

    # Read transactions from this block
    block_transactions = current_block['transactions']
    print(block_transactions)
    block - 1