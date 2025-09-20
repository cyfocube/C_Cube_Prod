import React from 'react';
import TokenBackupRestoreSection from '../TokenBackupRestoreSection';
import { Card } from './WalletStyles';

const TokenManagementTab = ({
  userTokens,
  setUserTokens,
  networks,
  removeToken
}) => {
  return (
    <div>
      <h3 style={{ marginBottom: '1rem', color: '#00cc33' }}>Token Management</h3>
      <p style={{ marginBottom: '1.5rem' }}>
        Manage your ERC-20 tokens and ensure they persist even if you reinstall the application.
      </p>
      
      <Card style={{ marginBottom: '2rem' }}>
        <TokenBackupRestoreSection 
          userTokens={userTokens} 
          setUserTokens={setUserTokens} 
        />
      </Card>
      
      <Card>
        <h4 style={{ marginBottom: '1rem', color: '#00cc33' }}>Your Saved Tokens</h4>
        {userTokens.length > 0 ? (
          <table style={{ width: '100%', borderCollapse: 'collapse' }}>
            <thead>
              <tr style={{ borderBottom: '1px solid rgba(0, 204, 51, 0.3)' }}>
                <th style={{ textAlign: 'left', padding: '0.5rem' }}>Symbol</th>
                <th style={{ textAlign: 'left', padding: '0.5rem' }}>Name</th>
                <th style={{ textAlign: 'left', padding: '0.5rem' }}>Network</th>
                <th style={{ textAlign: 'left', padding: '0.5rem' }}>Address</th>
                <th style={{ textAlign: 'center', padding: '0.5rem' }}>Decimals</th>
                <th style={{ textAlign: 'center', padding: '0.5rem' }}>Actions</th>
              </tr>
            </thead>
            <tbody>
              {userTokens.map(token => {
                const network = networks.find(n => n.id === token.networkId) || { name: 'Unknown' };
                return (
                  <tr key={token.id} style={{ borderBottom: '1px solid rgba(0, 204, 51, 0.1)' }}>
                    <td style={{ padding: '0.5rem' }}>{token.symbol}</td>
                    <td style={{ padding: '0.5rem' }}>{token.name || token.symbol}</td>
                    <td style={{ padding: '0.5rem' }}>{network.name}</td>
                    <td style={{ padding: '0.5rem', fontFamily: 'monospace', fontSize: '0.8rem' }}>
                      {`${token.address.substring(0, 6)}...${token.address.substring(token.address.length - 4)}`}
                    </td>
                    <td style={{ padding: '0.5rem', textAlign: 'center' }}>{token.decimals}</td>
                    <td style={{ padding: '0.5rem', textAlign: 'center' }}>
                      <button
                        onClick={() => removeToken(token.id)}
                        style={{
                          background: 'none',
                          border: 'none',
                          color: '#ff3333',
                          cursor: 'pointer',
                          fontSize: '0.8rem',
                          padding: '0.25rem 0.5rem',
                        }}
                      >
                        Remove
                      </button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        ) : (
          <p>No tokens saved yet. Add tokens in the "Sign Transaction" tab when sending tokens.</p>
        )}
      </Card>
    </div>
  );
};

export default TokenManagementTab;
