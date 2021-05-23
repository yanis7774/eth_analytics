# This script can be used to view all the transactions from a specific ERC-20 token over a defined # of blocks.
# This is useful for counting volume of transfers, viewing where it's being used, etc. 
from web3 import Web3

# Import Alchemy API Key
from dotenv import dotenv_values
config = dotenv_values("../.env")

# I prefer Alchemy as the pricing plans are friendly for people who aren't loaded : )
w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/' + config['API_KEY']))

# Get the block number for the latest block
latest_block = w3.eth.block_number
# Get this block number in another variable we will increment 
block = latest_block

# Read data from last 270 blocks to get ~1 hour of data, change number to change historical length
num_blocks_to_scan = 1
# ERC-20 token you want to track transfers for, change address to view different token 
erc_20_address = '0x1f9840a85d5af5bf1d1762f925bdaddc4201f984'
erc_20_history = []

# add the contract addresses you care about as well as the logic below to add additional contracts
# if you do not add this logic the number of transfers will still be tracked but not the protocols to which it is sent 
uni_v2_history = []
uni_v2_address = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'
uni_v2_30_address = ''
#uni_v3_history = []
#metamask_router_history = []
#sushiswap_history = []
#compound_history = []
#aave_history = []

# Loop over num_blocks_to_scan starting from the latest mined block
while block > (latest_block - num_blocks_to_scan):
    # Read data from the latest block
    print(latest_block - num_blocks_to_scan)
    print(block)
    current_block = w3.eth.getBlock(block)

    # Read transactions from this block
    block_transactions = current_block['transactions']
    print(len(block_transactions))
    # Loop over all transactions in this block
    for x in block_transactions:
        # Get the data we need for each individual transaction 
        #print(x.hex())
        block_receipt = w3.eth.getTransactionReceipt(x.hex())
        
        try: 
            # Check if our ERC_20 of interest is being used 
            if str(block_receipt['logs'][0]['address']).lower() == erc_20_address:
                # track number of transfers 
                print('yes')
                erc_20_history.append("Uniswap Token Transfer")
                looping = True
                # view a list of all the EOAs and contracts the token goes through in this transaction
                # these nested loops are inefficient and can be improved, consider using checksum addresses instead of lowercasing everything, and fix these disasterous breaks xD
                for x in block_receipt['logs']:
                    for y in x['topics']:
                        contract_address = str(y.hex())[-40:]
                        contract_address = '0x' + contract_address
                        if contract_address.lower() == uni_v2_address.lower(): 
                            uni_v2_history.append('Uniswap Token Traded Through Uniswap V2')
                            print('yes')
                            looping = False
                            break
                    if not looping: 
                        break      
        except: 
            print('no erc-20 transfer')      
    print('subtract')   
    # increment block - 1 to move on to the next block and scan for transactions
    block -= 1

# print how many times the ERC_20 in question was transferred over the last num_blocks_to_scan
print(len(erc_20_history))
# print how many of those ERC_20 transactions were transactions through Uniswap v2
print(len(uni_v2_history))





