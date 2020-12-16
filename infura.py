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