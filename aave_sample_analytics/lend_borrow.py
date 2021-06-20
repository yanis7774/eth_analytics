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

contract_address = Web3.toChecksumAddress('0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9')
# Address field should be the checksum address at which the contract was deployed
aave_lending_pool_contract = w3.eth.contract(address=contract_address, abi=abi)
# past blocks, requires archive node, requires add-on in Infura, included in free mode in Alchemy
dai_pool_data = aave_lending_pool_contract.functions.getReserveData('0x6B175474E89094C44Da98b954EedeAC495271d0F').call(block_identifier=-10)
zrx_pool_data = aave_lending_pool_contract.functions.getReserveData('0xE41d2489571d322189246DaFA5ebDe1F4699F498').call(block_identifier=-10)
bal_pool_data = aave_lending_pool_contract.functions.getReserveData('0xba100000625a3754423978a60c9317c58a424e3d').call(block_identifier=-10)
bat_pool_data = aave_lending_pool_contract.functions.getReserveData('0x0D8775F648430679A709E98d2b0Cb6250d2887EF').call(block_identifier=-10)
crv_pool_data = aave_lending_pool_contract.functions.getReserveData('0xD533a949740bb3306d119CC777fa900bA034cd52').call(block_identifier=-10)
enj_pool_data = aave_lending_pool_contract.functions.getReserveData('0xF629cBd94d3791C9250152BD8dfBDF380E2a3B9c').call(block_identifier=-10)
gem_pool_data = aave_lending_pool_contract.functions.getReserveData('0x056Fd409E1d7A124BD7017459dFEa2F387b6d5Cd').call(block_identifier=-10)
kyb_pool_data = aave_lending_pool_contract.functions.getReserveData('0xdd974D5C2e2928deA5F71b9825b8b646686BD200').call(block_identifier=-10)
link_pool_data = aave_lending_pool_contract.functions.getReserveData('0x514910771AF9Ca656af840dff83E8264EcF986CA').call(block_identifier=-10)
mana_pool_data = aave_lending_pool_contract.functions.getReserveData('0x0F5D2fB29fb7d3CFeE444a200298f468908cC942').call(block_identifier=-10)
mkr_pool_data = aave_lending_pool_contract.functions.getReserveData('0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2').call(block_identifier=-10)
ren_pool_data = aave_lending_pool_contract.functions.getReserveData('0x408e41876cCCDC0F92210600ef50372656052a38').call(block_identifier=-10)
snx_pool_data = aave_lending_pool_contract.functions.getReserveData('0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F').call(block_identifier=-10)
susd_pool_data = aave_lending_pool_contract.functions.getReserveData('0x57Ab1ec28D129707052df4dF418D58a2D46d5f51').call(block_identifier=-10)
tusd_pool_data = aave_lending_pool_contract.functions.getReserveData('0x0000000000085d4780B73119b644AE5ecd22b376').call(block_identifier=-10)
uni_pool_data = aave_lending_pool_contract.functions.getReserveData('0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984').call(block_identifier=-10)
usdc_pool_data = aave_lending_pool_contract.functions.getReserveData('0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48').call(block_identifier=-10)
usdt_pool_data = aave_lending_pool_contract.functions.getReserveData('0xdAC17F958D2ee523a2206206994597C13D831ec7').call(block_identifier=-10)
wbtc_pool_data = aave_lending_pool_contract.functions.getReserveData('0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599').call(block_identifier=-10)
weth_pool_data = aave_lending_pool_contract.functions.getReserveData('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2').call(block_identifier=-10)
xsushi_pool_data = aave_lending_pool_contract.functions.getReserveData('0x8798249c2E607446EfB7Ad49eC89dD1865Ff4272').call(block_identifier=-10)
yfi_pool_data = aave_lending_pool_contract.functions.getReserveData('0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e').call(block_identifier=-10)

print(zrx_pool_data)