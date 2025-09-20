import React from 'react';
import {
  WarningText,
  Button,
  PrivateKeyDisplay,
  MnemonicDisplay
} from './WalletStyles';

const ExportKeyTab = ({
  showPrivateKey,
  setShowPrivateKey,
  showMnemonic,
  setShowMnemonic,
  isWalletEncrypted,
  decryptedWallet,
  activeWallet,
  mnemonic,
  onSetActiveTab
}) => {
  // Private Key Export
  if (showPrivateKey) {
    return (
      <div>
        <WarningText>⚠️ DO NOT SHARE THIS WITH ANYONE ⚠️</WarningText>
        <PrivateKeyDisplay>
          {decryptedWallet?.privateKey || activeWallet.privateKey}
        </PrivateKeyDisplay>
        <Button 
          onClick={() => setShowPrivateKey(false)}
        >
          Hide Private Key
        </Button>
      </div>
    );
  }

  // Private Key Warning and Button
  return (
    <div>
      <WarningText>⚠️ Security Warning</WarningText>
      <p>
        Your private key is the most sensitive data for your wallet. Anyone who has access to it has complete control over your funds.
        Only export your private key in a secure, offline environment. Never share it with anyone.
      </p>
      <br />
      {isWalletEncrypted && !decryptedWallet ? (
        <div>
          <p>You need to decrypt your wallet first to view the private key.</p>
          <Button 
            onClick={() => onSetActiveTab('decrypt')}
            style={{ marginTop: '1rem' }}
          >
            Decrypt Wallet
          </Button>
        </div>
      ) : (
        <Button 
          danger
          onClick={() => setShowPrivateKey(true)}
          style={{ marginTop: '1rem' }}
        >
          I Understand, Show Private Key
        </Button>
      )}
    </div>
  );
};

const RecoveryPhraseTab = ({
  showMnemonic,
  setShowMnemonic,
  isWalletEncrypted,
  decryptedWallet,
  activeWallet,
  mnemonic,
  onSetActiveTab
}) => {
  // Mnemonic Display
  if (showMnemonic) {
    const recoveryPhrase = decryptedWallet?.mnemonic || activeWallet.mnemonic || mnemonic;
    return (
      <div>
        <WarningText>⚠️ WRITE THIS DOWN AND KEEP IT SAFE ⚠️</WarningText>
        <MnemonicDisplay>
          {recoveryPhrase}
        </MnemonicDisplay>
        <p>These {recoveryPhrase.split(/\s+/).length} words are all someone needs to access your wallet. Keep them secure!</p>
        <Button 
          onClick={() => setShowMnemonic(false)}
          style={{ marginTop: '1rem' }}
        >
          Hide Recovery Phrase
        </Button>
      </div>
    );
  }

  // Mnemonic Warning and Button
  return (
    <div>
      <WarningText>⚠️ Security Warning</WarningText>
      <p>
        Your recovery phrase (mnemonic) is the most sensitive data for your wallet. Anyone who has access to it has complete control over your funds.
        Write down your recovery phrase and store it in a safe, offline location. Never share it with anyone.
      </p>
      <br />
      {isWalletEncrypted && !decryptedWallet ? (
        <div>
          <p>You need to decrypt your wallet first to view the recovery phrase.</p>
          <Button 
            onClick={() => onSetActiveTab('decrypt')}
            style={{ marginTop: '1rem' }}
          >
            Decrypt Wallet
          </Button>
        </div>
      ) : activeWallet.mnemonic || decryptedWallet?.mnemonic || mnemonic ? (
        <Button 
          danger
          onClick={() => setShowMnemonic(true)}
          style={{ marginTop: '1rem' }}
        >
          I Understand, Show Recovery Phrase
        </Button>
      ) : (
        <div>
          <p>This wallet does not have a recovery phrase stored. Only wallets created with this application or imported using a recovery phrase will have this information.</p>
        </div>
      )}
    </div>
  );
};

export { ExportKeyTab, RecoveryPhraseTab };
