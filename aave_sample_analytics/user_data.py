# We use an Alchemy node to call smart contracts directly. Fairer pricing plans. 
import json
# web3.py gives us all sorts of great functionality for interaction with EVM compatible blockchains 
from web3 import Web3

# Import Alchemy API Key
from dotenv import dotenv_values
config = dotenv_values("../.env")

# I prefer Alchemy as the pricing plans are friendly for people who aren't loaded : )
w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/' + config['API_KEY']))

with open("abi.json") as f:
    abi = json.load(f)

# lending pool contract address 
contract_address = Web3.toChecksumAddress('0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9')
user_address = Web3.toChecksumAddress('')
# Address field should be the checksum address at which the contract was deployed
aave_lending_pool_contract = w3.eth.contract(address=contract_address, abi=abi)
# past blocks, requires archive node, requires add-on in Infura, included in free mode in Alchemy
user_data = aave_lending_pool_contract.functions.getUserAccountData(user_address).call()
print(user_data)