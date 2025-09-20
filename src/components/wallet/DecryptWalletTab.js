import React from 'react';
import {
  FormGroup,
  Label,
  InputWrapper,
  Input,
  Button,
  Loading,
  SuccessMessage
} from './WalletStyles';

const DecryptWalletTab = ({
  isWalletEncrypted,
  decryptedWallet,
  password,
  setPassword,
  handleDecryptWallet,
  loading,
  setDecryptedWallet,
  setSuccess
}) => {
  if (isWalletEncrypted && !decryptedWallet) {
    return (
      <div>
        <FormGroup>
          <Label htmlFor="password">Enter Password</Label>
          <InputWrapper>
            <Input 
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </InputWrapper>
        </FormGroup>
        <Button onClick={handleDecryptWallet} disabled={loading}>
          {loading ? <Loading>Decrypting</Loading> : 'Decrypt Wallet'}
        </Button>
      </div>
    );
  }

  if (decryptedWallet) {
    return (
      <div>
        <SuccessMessage>Wallet has been temporarily decrypted for this session.</SuccessMessage>
        <Button onClick={() => {
          setDecryptedWallet(null);
          setPassword('');
          setSuccess('');
        }}>
          Lock Wallet
        </Button>
      </div>
    );
  }

  return null;
};

export default DecryptWalletTab;
