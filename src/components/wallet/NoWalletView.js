import React from 'react';
import CyberSecurityHeader from '../CyberSecurityHeader';
import {
  ConsoleFrame,
  WalletContainer,
  Card,
  Title,
  NetworkBadge,
  TabContainer,
  TabButton,
  TabContent,
  FormGroup,
  Label,
  Input,
  TextArea,
  Button,
  CheckboxContainer,
  Checkbox,
  CheckboxLabel,
  RadioGroup,
  RadioOption,
  RadioInput,
  RadioLabel
} from './WalletStyles';

const NoWalletView = ({
  selectedNetwork,
  activeTab,
  setActiveTab,
  usePasswordForNewWallet,
  setUsePasswordForNewWallet,
  isMultiChain,
  setIsMultiChain,
  newWalletPassword,
  setNewWalletPassword,
  confirmNewWalletPassword,
  setConfirmNewWalletPassword,
  privateKey,
  setPrivateKey,
  mnemonic,
  setMnemonic,
  importType,
  setImportType,
  handleCreateWallet,
  handleImportWallet,
  loading
}) => {
  return (
    <ConsoleFrame>
      <WalletContainer>
        <CyberSecurityHeader 
          title="C-CUBE" 
          subtitle="Offline cryptocurrency storage with enhanced security protocols"
        />
        <Card>
          <Title>
            {selectedNetwork.isMultiChainView 
              ? 'No Multi-Chain Wallets Available' 
              : `No ${selectedNetwork.name} Wallet Available`}
          </Title>
          <NetworkBadge color={selectedNetwork.color}>
            {selectedNetwork.isMultiChainView 
              ? 'Multi-Chain View'
              : `${selectedNetwork.name} (${selectedNetwork.symbol})`}
          </NetworkBadge>
          <p>
            {selectedNetwork.isMultiChainView 
              ? 'No multi-chain wallets found. Create one below.'
              : `No wallets found for the ${selectedNetwork.name} network.`}
          </p>
          <p>Please create or import a wallet to continue.</p>
          <TabContainer>
            <TabButton 
              active={activeTab === 'create'}
              onClick={() => setActiveTab('create')}
            >
              Create New Wallet
            </TabButton>
            <TabButton 
              active={activeTab === 'import'}
              onClick={() => setActiveTab('import')}
            >
              Import Wallet
            </TabButton>
          </TabContainer>
          
          {activeTab === 'create' && (
            <TabContent>
              <Title>Create New Wallet</Title>
              <FormGroup>
                <Label>Wallet Options</Label>
                <CheckboxContainer>
                  <Checkbox
                    type="checkbox"
                    checked={usePasswordForNewWallet}
                    onChange={(e) => setUsePasswordForNewWallet(e.target.checked)}
                  />
                  <CheckboxLabel>Encrypt wallet with password</CheckboxLabel>
                </CheckboxContainer>
                <CheckboxContainer>
                  <Checkbox
                    type="checkbox"
                    checked={selectedNetwork.isMultiChainView || isMultiChain}
                    onChange={(e) => setIsMultiChain(e.target.checked)}
                    disabled={selectedNetwork.isMultiChainView}
                  />
                  <CheckboxLabel>
                    {selectedNetwork.isMultiChainView 
                      ? "Multi-chain wallet (automatically selected in Multi-Chain view)" 
                      : "Create as multi-chain wallet (usable on all networks)"}
                  </CheckboxLabel>
                </CheckboxContainer>
              </FormGroup>
              
              {usePasswordForNewWallet && (
                <>
                  <FormGroup>
                    <Label>Password</Label>
                    <Input
                      type="password"
                      value={newWalletPassword}
                      onChange={(e) => setNewWalletPassword(e.target.value)}
                      placeholder="Enter a strong password"
                    />
                  </FormGroup>
                  <FormGroup>
                    <Label>Confirm Password</Label>
                    <Input
                      type="password"
                      value={confirmNewWalletPassword}
                      onChange={(e) => setConfirmNewWalletPassword(e.target.value)}
                      placeholder="Confirm your password"
                    />
                  </FormGroup>
                </>
              )}
              
              <Button
                onClick={handleCreateWallet}
                disabled={loading}
              >
                {loading ? 'Creating...' : 'Create Wallet'}
              </Button>
            </TabContent>
          )}
          
          {activeTab === 'import' && (
            <TabContent>
              <Title>Import Wallet</Title>
              <RadioGroup>
                <RadioOption>
                  <RadioInput
                    type="radio"
                    name="importType"
                    checked={importType === 'privateKey'}
                    onChange={() => setImportType('privateKey')}
                  />
                  <RadioLabel>Private Key</RadioLabel>
                </RadioOption>
                <RadioOption>
                  <RadioInput
                    type="radio"
                    name="importType"
                    checked={importType === 'mnemonic'}
                    onChange={() => setImportType('mnemonic')}
                  />
                  <RadioLabel>Recovery Phrase</RadioLabel>
                </RadioOption>
              </RadioGroup>
              
              {importType === 'privateKey' && (
                <FormGroup>
                  <Label>Private Key</Label>
                  <Input
                    type="password"
                    value={privateKey}
                    onChange={(e) => setPrivateKey(e.target.value)}
                    placeholder="Enter your private key"
                  />
                </FormGroup>
              )}
              
              {importType === 'mnemonic' && (
                <FormGroup>
                  <Label>Recovery Phrase</Label>
                  <TextArea
                    value={mnemonic}
                    onChange={(e) => setMnemonic(e.target.value)}
                    placeholder="Enter your 12 or 24 word recovery phrase"
                    rows={3}
                  />
                </FormGroup>
              )}
              
              <FormGroup>
                <Label>Wallet Options</Label>
                <CheckboxContainer>
                  <Checkbox
                    type="checkbox"
                    checked={usePasswordForNewWallet}
                    onChange={(e) => setUsePasswordForNewWallet(e.target.checked)}
                  />
                  <CheckboxLabel>Encrypt wallet with password</CheckboxLabel>
                </CheckboxContainer>
                <CheckboxContainer>
                  <Checkbox
                    type="checkbox"
                    checked={selectedNetwork.isMultiChainView || isMultiChain}
                    onChange={(e) => setIsMultiChain(e.target.checked)}
                    disabled={selectedNetwork.isMultiChainView}
                  />
                  <CheckboxLabel>
                    {selectedNetwork.isMultiChainView 
                      ? "Multi-chain wallet (automatically selected in Multi-Chain view)" 
                      : "Create as multi-chain wallet (usable on all networks)"}
                  </CheckboxLabel>
                </CheckboxContainer>
              </FormGroup>
              
              {usePasswordForNewWallet && (
                <>
                  <FormGroup>
                    <Label>Password</Label>
                    <Input
                      type="password"
                      value={newWalletPassword}
                      onChange={(e) => setNewWalletPassword(e.target.value)}
                      placeholder="Enter a strong password"
                    />
                  </FormGroup>
                  <FormGroup>
                    <Label>Confirm Password</Label>
                    <Input
                      type="password"
                      value={confirmNewWalletPassword}
                      onChange={(e) => setConfirmNewWalletPassword(e.target.value)}
                      placeholder="Confirm your password"
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
            </TabContent>
          )}
        </Card>
      </WalletContainer>
    </ConsoleFrame>
  );
};

export default NoWalletView;
