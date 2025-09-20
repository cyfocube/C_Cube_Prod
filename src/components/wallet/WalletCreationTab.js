import React from 'react';
import {
  FormGroup,
  Label,
  Input,
  TextArea,
  Button,
  Loading,
  TabContainer,
  Tab,
  InfoText
} from './WalletStyles';

const WalletCreationTab = ({
  importType,
  setImportType,
  usePasswordForNewWallet,
  setUsePasswordForNewWallet,
  isMultiChain,
  setIsMultiChain,
  selectedNetwork,
  newWalletPassword,
  setNewWalletPassword,
  confirmNewWalletPassword,
  setConfirmNewWalletPassword,
  privateKey,
  setPrivateKey,
  mnemonic,
  setMnemonic,
  handleCreateWallet,
  handleImportWallet,
  loading
}) => {
  return (
    <div>
      <TabContainer>
        <Tab 
          active={importType === 'create'} 
          onClick={() => setImportType('create')}
        >
          Create New
        </Tab>
        <Tab 
          active={importType === 'privateKey'} 
          onClick={() => setImportType('privateKey')}
        >
          Import Private Key
        </Tab>
        <Tab 
          active={importType === 'mnemonic'} 
          onClick={() => setImportType('mnemonic')}
        >
          Import Recovery Phrase
        </Tab>
      </TabContainer>
      
      {importType === 'create' && (
        <>
          <FormGroup>
            <div style={{ display: 'flex', alignItems: 'center', marginBottom: '1rem' }}>
              <input
                type="checkbox"
                id="usePassword"
                checked={usePasswordForNewWallet}
                onChange={() => setUsePasswordForNewWallet(!usePasswordForNewWallet)}
                style={{ marginRight: '0.5rem' }}
              />
              <Label htmlFor="usePassword">Encrypt wallet with password</Label>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', marginBottom: '1rem' }}>
              <input
                type="checkbox"
                id="multiChain"
                checked={selectedNetwork.isMultiChainView || isMultiChain}
                onChange={() => setIsMultiChain(!isMultiChain)}
                disabled={selectedNetwork.isMultiChainView}
                style={{ marginRight: '0.5rem' }}
              />
              <Label htmlFor="multiChain">
                {selectedNetwork.isMultiChainView 
                  ? "Multi-chain wallet (automatically selected in Multi-Chain view)" 
                  : "Create as multi-chain wallet (usable on all networks)"}
              </Label>
            </div>
          </FormGroup>
          
          {usePasswordForNewWallet && (
            <>
              <FormGroup>
                <Label htmlFor="newWalletPassword">Password</Label>
                <Input
                  id="newWalletPassword"
                  type="password"
                  value={newWalletPassword}
                  onChange={(e) => setNewWalletPassword(e.target.value)}
                />
              </FormGroup>
              
              <FormGroup>
                <Label htmlFor="confirmNewWalletPassword">Confirm Password</Label>
                <Input
                  id="confirmNewWalletPassword"
                  type="password"
                  value={confirmNewWalletPassword}
                  onChange={(e) => setConfirmNewWalletPassword(e.target.value)}
                />
              </FormGroup>
            </>
          )}
          
          <Button
            onClick={handleCreateWallet}
            disabled={loading}
          >
            {loading ? <Loading>Creating</Loading> : 'Create New Wallet'}
          </Button>
        </>
      )}
      
      {importType === 'privateKey' && (
        <>
          <FormGroup>
            <Label htmlFor="privateKey">Private Key</Label>
            <Input 
              id="privateKey"
              type="password"
              value={privateKey}
              onChange={(e) => setPrivateKey(e.target.value)}
              placeholder="0x..."
            />
          </FormGroup>
          
          <FormGroup>
            <div style={{ display: 'flex', alignItems: 'center', marginBottom: '1rem' }}>
              <input
                type="checkbox"
                id="usePasswordImport"
                checked={usePasswordForNewWallet}
                onChange={() => setUsePasswordForNewWallet(!usePasswordForNewWallet)}
                style={{ marginRight: '0.5rem' }}
              />
              <Label htmlFor="usePasswordImport">Encrypt wallet with password</Label>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', marginBottom: '1rem' }}>
              <input
                type="checkbox"
                id="multiChainImport"
                checked={selectedNetwork.isMultiChainView || isMultiChain}
                onChange={() => setIsMultiChain(!isMultiChain)}
                disabled={selectedNetwork.isMultiChainView}
                style={{ marginRight: '0.5rem' }}
              />
              <Label htmlFor="multiChainImport">
                {selectedNetwork.isMultiChainView 
                  ? "Multi-chain wallet (automatically selected in Multi-Chain view)" 
                  : "Create as multi-chain wallet (usable on all networks)"}
              </Label>
            </div>
          </FormGroup>
          
          {usePasswordForNewWallet && (
            <>
              <FormGroup>
                <Label htmlFor="importPassword">Password</Label>
                <Input
                  id="importPassword"
                  type="password"
                  value={newWalletPassword}
                  onChange={(e) => setNewWalletPassword(e.target.value)}
                />
              </FormGroup>
              
              <FormGroup>
                <Label htmlFor="confirmImportPassword">Confirm Password</Label>
                <Input
                  id="confirmImportPassword"
                  type="password"
                  value={confirmNewWalletPassword}
                  onChange={(e) => setConfirmNewWalletPassword(e.target.value)}
                />
              </FormGroup>
            </>
          )}
          
          <Button
            onClick={handleImportWallet}
            disabled={loading}
          >
            {loading ? 'Importing...' : 'Import Wallet'}
          </Button>
        </>
      )}
      
      {importType === 'mnemonic' && (
        <>
          <FormGroup>
            <Label htmlFor="mnemonic">Recovery Phrase</Label>
            <TextArea 
              id="mnemonic"
              value={mnemonic}
              onChange={(e) => setMnemonic(e.target.value)}
              placeholder="Enter your 12 or 24 word recovery phrase, separated by spaces"
            />
            <InfoText>
              Enter your recovery phrase (12 or 24 words separated by spaces).
            </InfoText>
          </FormGroup>
          
          <FormGroup>
            <div style={{ display: 'flex', alignItems: 'center', marginBottom: '1rem' }}>
              <input
                type="checkbox"
                id="usePasswordMnemonic"
                checked={usePasswordForNewWallet}
                onChange={() => setUsePasswordForNewWallet(!usePasswordForNewWallet)}
                style={{ marginRight: '0.5rem' }}
              />
              <Label htmlFor="usePasswordMnemonic">Encrypt wallet with password</Label>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', marginBottom: '1rem' }}>
              <input
                type="checkbox"
                id="multiChainMnemonic"
                checked={selectedNetwork.isMultiChainView || isMultiChain}
                onChange={() => setIsMultiChain(!isMultiChain)}
                disabled={selectedNetwork.isMultiChainView}
                style={{ marginRight: '0.5rem' }}
              />
              <Label htmlFor="multiChainMnemonic">
                {selectedNetwork.isMultiChainView 
                  ? "Multi-chain wallet (automatically selected in Multi-Chain view)" 
                  : "Create as multi-chain wallet (usable on all networks)"}
              </Label>
            </div>
          </FormGroup>
          
          {usePasswordForNewWallet && (
            <>
              <FormGroup>
                <Label htmlFor="mnemonicPassword">Password</Label>
                <Input
                  id="mnemonicPassword"
                  type="password"
                  value={newWalletPassword}
                  onChange={(e) => setNewWalletPassword(e.target.value)}
                />
              </FormGroup>
              
              <FormGroup>
                <Label htmlFor="confirmMnemonicPassword">Confirm Password</Label>
                <Input
                  id="confirmMnemonicPassword"
                  type="password"
                  value={confirmNewWalletPassword}
                  onChange={(e) => setConfirmNewWalletPassword(e.target.value)}
                />
              </FormGroup>
            </>
          )}
          
          <Button
            onClick={handleImportWallet}
            disabled={loading}
          >
            {loading ? 'Importing...' : 'Import Wallet'}
          </Button>
        </>
      )}
    </div>
  );
};

export default WalletCreationTab;
