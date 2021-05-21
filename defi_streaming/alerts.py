# Sample for creating alerts to monitor some value every x blocks 
from web3 import Web3
import threading 
import os 

# Import Alchemy API Key
from dotenv import dotenv_values
config = dotenv_values("../.env")

# I prefer Alchemy as the pricing plans are friendly for people who aren't loaded : )
w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/' + config['API_KEY']))

# this function checks the number of Uniswap v2 transactions in the latest block every 30 seconds
def scan_blocks(): 
    threading.Timer(30, scan_blocks).start()
    # Get information about the latest block
    latest_block = w3.eth.block_number

    # Read data from the latest block
    block = w3.eth.getBlock(latest_block)
    block_transactions = block['transactions']

    uni_history = []


    for x in block_transactions:
        block = w3.eth.get_transaction(x.hex())
        
        # check if transaction is through Uniswap v2
        if block['to'] == '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D':
            uni_history.append('yes')
    print("Number of Uniswap v2 Swaps: " + str(len(uni_history)))

scan_blocks()
