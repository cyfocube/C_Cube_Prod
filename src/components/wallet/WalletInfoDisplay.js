import React from 'react';
import QRCode from 'qrcode.react';
import {
  WalletInfo,
  NetworkBadge,
  Subtitle,
  WalletAddress,
  QRCodeContainer
} from './WalletStyles';

const WalletInfoDisplay = ({ 
  activeWallet, 
  selectedNetwork 
}) => {
  return (
    <WalletInfo>
      {selectedNetwork.isMultiChainView ? (
        <NetworkBadge color={selectedNetwork.color || '#00CC33'}>
          Multi-Chain View
        </NetworkBadge>
      ) : (
        <NetworkBadge color={selectedNetwork.color || '#627EEA'}>
          {selectedNetwork.name} ({selectedNetwork.symbol})
        </NetworkBadge>
      )}
      <Subtitle>{activeWallet.name}</Subtitle>
      {activeWallet.isMultiChain && (
        <div style={{
          display: 'inline-block',
          padding: '2px 8px',
          marginLeft: '10px',
          backgroundColor: 'rgba(0, 204, 51, 0.2)',
          color: '#00cc33',
          borderRadius: '4px',
          fontSize: '0.7rem',
          fontWeight: 'bold',
          textTransform: 'uppercase'
        }}>
          Multi-Chain
        </div>
      )}
      <WalletAddress>
        {activeWallet.address}
      </WalletAddress>
      
      <QRCodeContainer>
        <QRCode 
          value={activeWallet.address} 
          size={180}
          bgColor="#000000"
          fgColor="#00cc33"
          level="H"
          includeMargin={true}
          renderAs="svg"
          imageSettings={{
            src: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iIzAwZmY0MSI+PHBhdGggZD0iTTEyIDJMNC41IDIwLjI5bDcuNS00LjYydi00LjgxYzEuNzggMCAzLjIgMS4zIDMuMiAyLjkgMCAuOTUtLjQ2IDEuNzUtMS4xNyAyLjI1bDUuNTEgMS4zYy44MS0uNjEgMS40Ny0xLjQ2IDEuODUtMi41LjM5LTEuMDUuMzktMi4xOCAwLTMuMjMtLjk5LTIuNjQtMy42Ny00LjUtNi44LTQuNTJWNy43OUwxOS41IDMuNzFsLTcuNS00LjY1VjJaIi8+PC9zdmc+",
            height: 20,
            width: 20,
            excavate: true
          }}
        />
      </QRCodeContainer>
    </WalletInfo>
  );
};

export default WalletInfoDisplay;
