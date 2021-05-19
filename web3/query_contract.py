# We use Infura to access blockchain data as needed from an Infura node. 
import infura
import json
ifr = infura.Client(
    project_id='',
    project_secret='',
    network='mainnet',
    cache_expire_after=5,
)

# web3.py gives us all sorts of great functionality for interaction with EVM compatible blockchains 
from web3 import Web3

# uses alchemy, feel free to switch with infura
w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/PROJECT_ID'))

with open("abi.json") as f:
    abi = json.load(f)

contract_address = Web3.toChecksumAddress('0x5d3a536e4d6dbd6114cc1ead35777bab948e3643')
# Address field should be the checksum address at which the ERC20 contract was deployed
compound_dai_contract = w3.eth.contract(address=contract_address, abi=abi)
# past blocks, requires archive node
total_supply = compound_dai_contract.functions.totalSupply().call(block_identifier=-100000)
#total_supply = compound_dai_contract.functions.totalSupply().call(block_identifier='latest')

# total supply in cDAI, use conversion factor
print(total_supply/46.72)