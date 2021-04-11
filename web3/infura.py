import infura

ifr = infura.Client(
    project_id='',
    project_secret='',
    network='mainnet',
    cache_expire_after=5,
)

gas_price = ifr.eth_get_gas_price()

balance = ifr.eth_get_balance('0x')

block_number = ifr.eth_get_block_number()


import json 

ABI = json.loads('[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf",
                    "outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')

from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'))

# Get information about the latest block
w3.eth.getBlock('latest')

# Get the ETH balance of an address 
w3.eth.getBalance('YOUR_ADDRESS_HERE')

wallet_address = 'YOUR_ADDRESS_HERE'
wallet_address = Web3.toChecksumAddress(wallet_address)

token_contract_address = '0xc011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f'
token_contract_address = Web3.toChecksumAddress(token_contract_address)

# define contract
contract = w3.eth.contract(token_contract_address, abi=ABI)

# call contract and get data from balanceOf for argument wallet_address
raw_balance = contract.functions.balanceOf(wallet_address).call()

# convert the value from Wei to Ether
synthetix_value = Web3.fromWei(raw_balance, 'ether')