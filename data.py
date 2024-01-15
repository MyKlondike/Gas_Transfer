class Chains:
    def __init__(self, evm_ch, rpc, scan, token, chain_id):
        self.evm_ch = evm_ch
        self.rpc = rpc
        self.scan = scan
        self.token = token
        self.chain_id = chain_id


chains_dict = {
    'ethereum': Chains('ethereum', 'https://rpc.ankr.com/eth', 'https://etherscan.io/tx', 'ETH', 1),
    'optimism': Chains('optimism', 'https://rpc.optimism.gateway.fm', 'https://optimistic.etherscan.io/tx', 'ETH', 10),
    'bsc': Chains('bsc', 'https://rpc.ankr.com/bsc', 'https://bscscan.com/tx', 'BNB', 56),
    'polygon': Chains('polygon', 'https://rpc.ankr.com/polygon', 'https://polygonscan.com/tx', 'MATIC', 137),
    'polygon_zkevm': Chains('polygon_zkevm', 'https://zkevm-rpc.com', 'https://zkevm.polygonscan.com/tx', 'ETH', 1101),
    'arbitrum': Chains('arbitrum', 'https://rpc.ankr.com/arbitrum', 'https://arbiscan.io/tx', 'ETH', 42161),
    'avalanche': Chains('avalanche', 'https://avalanche-c-chain.publicnode.com', 'https://snowtrace.io/tx', 'AVAX', 43114),
    'fantom': Chains('fantom', 'https://rpc.ftm.tools', 'https://ftmscan.com/tx', 'FTM', 250),
    'nova': Chains('nova', 'https://nova.arbitrum.io/rpc', 'https://nova.arbiscan.io/tx', 'ETH', 42170),
    'zksync': Chains('zksync', 'https://mainnet.era.zksync.io', 'https://explorer.zksync.io/tx', 'ETH', 324),
    'celo': Chains('celo', 'https://1rpc.io/celo', 'https://celoscan.io/tx', 'CELO', 42220),
    'gnosis': Chains('gnosis', 'https://rpc.ankr.com/gnosis', 'https://gnosisscan.io/tx', 'xDAI', 100),
    'core': Chains('core', 'https://rpc.coredao.org', 'https://scan.coredao.org/tx', 'CORE', 1116),
    'harmony': Chains('harmony', 'https://api.harmony.one', 'https://explorer.harmony.one/tx', 'ONE', 1666600000),
    'moonbeam': Chains('moonbeam', 'https://rpc.ankr.com/moonbeam', 'https://moonscan.io/tx', 'GLMR', 1284),
    'moonriver': Chains('moonriver', 'https://moonriver.public.blastapi.io', 'https://moonriver.moonscan.io/tx', 'MOVR', 1285),
    'linea': Chains('linea', 'https://rpc.linea.build', 'https://lineascan.build/tx', 'ETH', 59144),
    'base': Chains('base', 'https://mainnet.base.org', 'https://basescan.org/tx', 'ETH', 8453),
    'zora': Chains('zora', 'https://rpc.zora.energy', 'https://explorer.zora.energy/tx', 'ETH', 7777777),
    'klaytn': Chains('klaytn', 'https://open-platform.nodereal.io/4585ad55d874415c840b3af281dde1a2/klaytn/', 'https://scope.klaytn.com/tx/', 'klaytn', 8217),
    'scroll': Chains('scroll', 'https://rpc.scroll.io', 'https://scrollscan.com/tx', 'ETH', 534352),
}
