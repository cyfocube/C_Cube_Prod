import React from 'react';
import { WalletControls, Button } from './WalletStyles';

const WalletControlsPanel = ({
  networkWallets,
  activeWallet,
  isWalletEncrypted,
  decryptedWallet,
  onSwitchWallet,
  onSetActiveTab
}) => {
  return (
    <WalletControls>
      {networkWallets.length > 1 && (
        <Button 
          secondary
          onClick={onSwitchWallet}
        >
          Switch Wallet
        </Button>
      )}
      
      {isWalletEncrypted && !decryptedWallet && (
        <Button 
          onClick={() => onSetActiveTab('decrypt')}
        >
          Decrypt Wallet
        </Button>
      )}
      
      <Button
        secondary
        onClick={() => onSetActiveTab('export')}
      >
        View Private Key
      </Button>
      
      <Button
        onClick={() => onSetActiveTab('sign')}
      >
        Sign Transaction
      </Button>
      
      <Button
        secondary
        onClick={() => onSetActiveTab('createWallet')}
      >
        Create New Wallet
      </Button>
    </WalletControls>
  );
};

export default WalletControlsPanel;
