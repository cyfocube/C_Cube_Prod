// Definition of supported blockchain networks
const networks = [
  {
    id: 'multi-chain',
    name: 'Multi-Chain',
    chainId: 0,
    symbol: 'MULTI',
    rpcUrl: '',
    blockExplorer: '',
    color: '#00CC33',
    description: 'View all multi-chain wallets',
    isTestnet: false,
    isMultiChainView: true
  },
  {
    id: 'ethereum',
    name: 'Ethereum',
    chainId: 1,
    symbol: 'ETH',
    rpcUrl: 'https://ethereum.publicnode.com',
    blockExplorer: 'https://etherscan.io',
    color: '#627EEA',
    description: 'Ethereum Mainnet',
    isTestnet: false
  },
  {
    id: 'bsc',
    name: 'Binance Smart Chain',
    chainId: 56,
    symbol: 'BNB',
    rpcUrl: 'https://bsc.publicnode.com',
    blockExplorer: 'https://bscscan.com',
    color: '#F0B90B',
    description: 'Binance Smart Chain Mainnet',
    isTestnet: false
  },
  {
    id: 'base',
    name: 'Base',
    chainId: 8453,
    symbol: 'ETH',
    rpcUrl: 'https://mainnet.base.org',
    blockExplorer: 'https://basescan.org',
    color: '#0052FF',
    description: 'Base Mainnet (Coinbase L2)',
    isTestnet: false
  },
  {
    id: 'polygon',
    name: 'Polygon',
    chainId: 137,
    symbol: 'MATIC',
    rpcUrl: 'https://polygon-rpc.com',
    blockExplorer: 'https://polygonscan.com',
    color: '#8247E5',
    description: 'Polygon Mainnet',
    isTestnet: false
  },
  {
    id: 'arbitrum',
    name: 'Arbitrum',
    chainId: 42161,
    symbol: 'ETH',
    rpcUrl: 'https://arb1.arbitrum.io/rpc',
    blockExplorer: 'https://arbiscan.io',
    color: '#2D374B',
    description: 'Arbitrum One',
    isTestnet: false
  },
  {
    id: 'optimism',
    name: 'Optimism',
    chainId: 10,
    symbol: 'ETH',
    rpcUrl: 'https://mainnet.optimism.io',
    blockExplorer: 'https://optimistic.etherscan.io',
    color: '#FF0420',
    description: 'Optimism Mainnet',
    isTestnet: false
  },
  {
    id: 'avalanche',
    name: 'Avalanche',
    chainId: 43114,
    symbol: 'AVAX',
    rpcUrl: 'https://api.avax.network/ext/bc/C/rpc',
    blockExplorer: 'https://snowtrace.io',
    color: '#E84142',
    description: 'Avalanche C-Chain',
    isTestnet: false
  }
];

export const getNetworkById = (id) => {
  return networks.find(network => network.id === id) || networks[0];
};

export const getNetworkByChainId = (chainId) => {
  return networks.find(network => network.chainId === chainId) || networks[0];
};

export default networks;
