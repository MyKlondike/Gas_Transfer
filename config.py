from data import *

ASSET = "0x912ce59144191c1204e64559fe8253a0e49e6548" # Если значение ASSET = "" отправляем GAS !!!

asset_amount = 0  # Если значение asset_amount = "0" отправляем весь баланс !!!

# Настройки бездействия:
delay_from = 30
delay_to = 300

CHECK_GWEI = True
MAX_GWEI = 25
CHAIN_GAS = 0.2
RETRY_COUNT = 1

''' 
================== Настройки сети ==================
'ethereum', 'optimism', 'bsc', 'polygon', 'polygon_zkevm', 'arbitrum', 'avalanche', 'fantom', 'nova', 
'zksync', 'celo', 'gnosis', 'core', 'harmony', 'moonbeam', 'moonriver', 'linea', 'base', 'zora', 'klaytn', 'scroll'

Используйте chain_name для выбора блокчейна:
'''

chain_names = ['arbitrum',]
current_chains = [chains_dict.get(chain_name) for chain_name in chain_names]

for current_chain in current_chains:
    if current_chain:
        rpc = current_chain.rpc
        scan = current_chain.scan
        id = current_chain.chain_id
    else:
        print(f"Блокчейн {current_chain} не задан в словаре chains_dict.")