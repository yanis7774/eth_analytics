# This script uses Web3 to check how many transactions from the prior block belong to the defined smart contract.
# This is useful for counting unique users, transaction volume, etc. 
from web3 import Web3

# I prefer Alchemy as the pricing plans are friendly for people who aren't loaded : )
w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/YOUR_PROJECT_ID'))

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