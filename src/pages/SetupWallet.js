import React, { useState, useContext } from 'react';
import styled from 'styled-components';
import AppContext from '../context/AppContext';
import { ethers } from 'ethers';

const SetupContainer = styled.div`
  max-width: 800px;
  margin: 0 auto;
`;

const Card = styled.div`
  background-color: ${({ theme }) => theme.colors.cardBackground};
  border-radius: 8px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
`;

const Title = styled.h2`
  color: ${({ theme }) => theme.colors.primary};
  margin-bottom: 1.5rem;
  text-align: center;
`;

const Subtitle = styled.h3`
  margin-bottom: 1rem;
  color: ${({ theme }) => theme.colors.text};
`;

const TabContainer = styled.div`
  display: flex;
  margin-bottom: 1.5rem;
  border-bottom: 1px solid ${({ theme }) => theme.colors.border};
`;

const Tab = styled.button`
  flex: 1;
  background: none;
  border: none;
  padding: 1rem;
  color: ${({ active, theme }) => active ? theme.colors.primary : theme.colors.text};
  border-bottom: ${({ active, theme }) => active ? `2px solid ${theme.colors.primary}` : 'none'};
  font-weight: ${({ active }) => active ? 'bold' : 'normal'};

  &:hover {
    color: ${({ theme }) => theme.colors.primary};
  }
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
  gap: 1rem;
`;

const FormGroup = styled.div`
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
`;

const Label = styled.label`
  font-weight: bold;
`;

const Input = styled.input`
  padding: 0.75rem;
  border-radius: 4px;
  border: 1px solid ${({ theme, error }) => error ? theme.colors.danger : theme.colors.border};
  background-color: ${({ theme }) => theme.colors.background};
  color: ${({ theme }) => theme.colors.text};

  &:focus {
    border-color: ${({ theme }) => theme.colors.primary};
    outline: none;
  }
`;

const TextArea = styled.textarea`
  padding: 0.75rem;
  border-radius: 4px;
  border: 1px solid ${({ theme, error }) => error ? theme.colors.danger : theme.colors.border};
  background-color: ${({ theme }) => theme.colors.background};
  color: ${({ theme }) => theme.colors.text};
  min-height: 100px;
  font-family: ${({ theme }) => theme.fonts.code || 'monospace'};
  resize: vertical;

  &:focus {
    border-color: ${({ theme }) => theme.colors.primary};
    outline: none;
  }
`;

const Checkbox = styled.div`
  display: flex;
  align-items: center;
  gap: 0.5rem;
`;

const Button = styled.button`
  background-color: ${({ theme }) => theme.colors.primary};
  color: white;
  padding: 0.75rem;
  border-radius: 4px;
  font-weight: bold;
  margin-top: 1rem;

  &:hover {
    background-color: ${({ theme }) => theme.colors.info};
  }
`;

const ErrorMessage = styled.div`
  color: ${({ theme }) => theme.colors.danger};
  font-size: 0.875rem;
  margin-top: 0.25rem;
`;

const InfoText = styled.p`
  margin-bottom: 1rem;
  line-height: 1.6;
`;

const SetupWallet = ({ onSetupComplete }) => {
  const { createEthereumWallet, importWalletFromPrivateKey, importWalletFromMnemonic, selectedNetwork } = useContext(AppContext);
  const [isMultiChain, setIsMultiChain] = useState(false);
  const [activeTab, setActiveTab] = useState(() => {
    // Initialize tab based on user's choice from welcome screen
    const walletAction = localStorage.getItem('walletAction');
    return walletAction === 'recover' ? 'import' : 'create';
  });
  const [importType, setImportType] = useState(() => {
    // If user chose recover, default to mnemonic import
    const walletAction = localStorage.getItem('walletAction');
    return walletAction === 'recover' ? 'mnemonic' : 'privateKey';
  });
  const [usePassword, setUsePassword] = useState(true);
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [privateKey, setPrivateKey] = useState('');
  const [mnemonic, setMnemonic] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handlePasswordToggle = () => {
    setUsePassword(!usePassword);
  };

  const validatePassword = () => {
    if (!usePassword) return true;
    if (password.length < 8) {
      setError('Password must be at least 8 characters long');
      return false;
    }
    if (password !== confirmPassword) {
      setError('Passwords do not match');
      return false;
    }
    return true;
  };

  const validatePrivateKey = () => {
    if (!privateKey) {
      setError('Please enter a private key');
      return false;
    }
    
    try {
      // Check if it's a valid Ethereum private key
      if (!privateKey.startsWith('0x')) {
        setPrivateKey(`0x${privateKey}`);
      }
      
      new ethers.Wallet(privateKey.startsWith('0x') ? privateKey : `0x${privateKey}`);
      return true;
    } catch (err) {
      setError('Invalid private key format');
      return false;
    }
  };
  
  const validateMnemonic = () => {
    if (!mnemonic) {
      setError('Please enter a recovery phrase');
      return false;
    }
    
    try {
      // Check if it's a valid mnemonic phrase (usually 12 or 24 words)
      const words = mnemonic.trim().split(/\s+/);
      if (words.length !== 12 && words.length !== 24) {
        setError('Recovery phrase must be 12 or 24 words');
        return false;
      }
      
      // Attempt to create a wallet from the mnemonic to validate it
      ethers.Wallet.fromMnemonic(mnemonic.trim());
      return true;
    } catch (err) {
      setError('Invalid recovery phrase');
      return false;
    }
  };

  const handleCreateWallet = async (e) => {
    e.preventDefault();
    setError('');
    
    if (!validatePassword()) return;
    
    setLoading(true);
    try {
      await createEthereumWallet(usePassword ? password : null, selectedNetwork.id, isMultiChain);
      localStorage.setItem('walletSetup', 'true');
      localStorage.removeItem('walletAction'); // Clear the initial action
      onSetupComplete();
    } catch (err) {
      setError(`Failed to create wallet: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  const handleImportWallet = async (e) => {
    e.preventDefault();
    setError('');
    
    if (!validatePassword()) return;
    
    // Validate based on import type
    if (importType === 'privateKey') {
      if (!validatePrivateKey()) return;
    } else {
      if (!validateMnemonic()) return;
    }
    
    setLoading(true);
    try {
      if (importType === 'privateKey') {
        await importWalletFromPrivateKey(privateKey, usePassword ? password : null, selectedNetwork.id, isMultiChain);
      } else {
        await importWalletFromMnemonic(mnemonic.trim(), usePassword ? password : null, selectedNetwork.id, isMultiChain);
      }
      
      localStorage.setItem('walletSetup', 'true');
      localStorage.removeItem('walletAction'); // Clear the initial action
      onSetupComplete();
    } catch (err) {
      setError(`Failed to import wallet: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <SetupContainer>
      <Card>
        <Title>
          {activeTab === 'create' ? 'Create New Secure Wallet' : 'Recover Your Wallet'}
        </Title>
        <InfoText>
          {activeTab === 'create' 
            ? 'Your new wallet will be created securely on this device. Make sure to save your recovery phrase afterwards.'
            : 'Enter your recovery phrase to restore your wallet. This will give you access to your funds.'}
        </InfoText>

        {/* Only show tabs if not coming from welcome screen direct choice */}
        {!localStorage.getItem('walletAction') && (
          <TabContainer>
            <Tab 
              active={activeTab === 'create'} 
              onClick={() => setActiveTab('create')}
            >
              Create New Wallet
            </Tab>
            <Tab 
              active={activeTab === 'import'} 
              onClick={() => setActiveTab('import')}
            >
              Recover Existing Wallet
            </Tab>
          </TabContainer>
        )}

        {activeTab === 'create' ? (
          <Form onSubmit={handleCreateWallet}>
            <Subtitle>Create a New Ethereum Wallet</Subtitle>
            
            <FormGroup>
              <Checkbox>
                <input 
                  type="checkbox" 
                  id="encrypt" 
                  checked={usePassword} 
                  onChange={handlePasswordToggle}
                />
                <Label htmlFor="encrypt">Encrypt wallet with password (recommended)</Label>
              </Checkbox>
            </FormGroup>
            
            {usePassword && (
              <>
                <FormGroup>
                  <Label htmlFor="password">Password</Label>
                  <Input 
                    id="password"
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    error={error.includes('Password')}
                    required={usePassword}
                  />
                </FormGroup>
                
                <FormGroup>
                  <Label htmlFor="confirmPassword">Confirm Password</Label>
                  <Input 
                    id="confirmPassword"
                    type="password"
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    error={error.includes('Passwords')}
                    required={usePassword}
                  />
                </FormGroup>
              </>
            )}
            
            {error && <ErrorMessage>{error}</ErrorMessage>}
            
            <Button type="submit" disabled={loading}>
              {loading ? 'Creating...' : 'Create Wallet'}
            </Button>
          </Form>
        ) : (
          <Form onSubmit={handleImportWallet}>
            <Subtitle>Recover Your Ethereum Wallet</Subtitle>
            
            {/* Only show import type tabs if not coming directly from welcome screen */}
            {!localStorage.getItem('walletAction') && (
              <FormGroup>
                <TabContainer>
                  <Tab 
                    active={importType === 'privateKey'} 
                    onClick={() => setImportType('privateKey')}
                  >
                    Private Key
                  </Tab>
                  <Tab 
                    active={importType === 'mnemonic'} 
                    onClick={() => setImportType('mnemonic')}
                  >
                    Recovery Phrase
                  </Tab>
                </TabContainer>
              </FormGroup>
            )}
            
            {importType === 'privateKey' ? (
              <FormGroup>
                <Label htmlFor="privateKey">Private Key</Label>
                <Input 
                  id="privateKey"
                  type="password"
                  value={privateKey}
                  onChange={(e) => setPrivateKey(e.target.value)}
                  error={error.includes('private key')}
                  required
                  placeholder="0x..."
                />
                <InfoText>
                  Enter your Ethereum private key. This will be stored securely on your device.
                </InfoText>
              </FormGroup>
            ) : (
              <FormGroup>
                <Label htmlFor="mnemonic">Recovery Phrase</Label>
                <TextArea 
                  id="mnemonic"
                  value={mnemonic}
                  onChange={(e) => setMnemonic(e.target.value)}
                  error={error.includes('recovery phrase')}
                  required
                  placeholder="Enter your 12 or 24 word recovery phrase, separated by spaces"
                />
                <InfoText>
                  Enter your recovery phrase (12 or 24 words separated by spaces). This will be stored securely on your device.
                </InfoText>
              </FormGroup>
            )}
            
            <FormGroup>
              <Checkbox>
                <input 
                  type="checkbox" 
                  id="encrypt" 
                  checked={usePassword} 
                  onChange={handlePasswordToggle}
                />
                <Label htmlFor="encrypt">Encrypt wallet with password (recommended)</Label>
              </Checkbox>
            </FormGroup>
            
            {usePassword && (
              <>
                <FormGroup>
                  <Label htmlFor="password">Password</Label>
                  <Input 
                    id="password"
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    error={error.includes('Password')}
                    required={usePassword}
                  />
                </FormGroup>
                
                <FormGroup>
                  <Label htmlFor="confirmPassword">Confirm Password</Label>
                  <Input 
                    id="confirmPassword"
                    type="password"
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    error={error.includes('Passwords')}
                    required={usePassword}
                  />
                </FormGroup>
              </>
            )}
            
            {error && <ErrorMessage>{error}</ErrorMessage>}
            
            <Button type="submit" disabled={loading}>
              {loading ? 'Importing...' : 'Import Wallet'}
            </Button>
          </Form>
        )}
      </Card>
    </SetupContainer>
  );
};

export default SetupWallet;
