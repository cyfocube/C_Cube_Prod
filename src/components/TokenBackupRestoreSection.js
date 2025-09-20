import React, { useState } from 'react';
import styled from 'styled-components';
import TokenStorage from '../utils/TokenStorage';

const ButtonContainer = styled.div`
  display: flex;
  gap: 0.5rem;
  margin-top: 1rem;
  margin-bottom: 1rem;
`;

const Button = styled.button`
  background-color: rgba(0, 0, 0, 0.6);
  border: 1px solid ${({ theme }) => theme.colors.primary};
  color: ${({ theme }) => theme.colors.primary};
  font-family: ${({ theme }) => theme.fonts.code};
  padding: 0.6rem 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
  border-radius: 2px;
  font-size: 0.85rem;
  
  &:hover {
    background-color: rgba(0, 204, 51, 0.2);
  }
  
  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
`;

const MessageBox = styled.div`
  margin-top: 0.5rem;
  padding: 0.5rem;
  border-radius: 2px;
  font-size: 0.85rem;
  font-family: ${({ theme }) => theme.fonts.code};
  
  ${({ type }) => 
    type === 'success' 
      ? 'background-color: rgba(0, 204, 51, 0.1); color: #00cc33; border: 1px solid rgba(0, 204, 51, 0.3);'
      : 'background-color: rgba(255, 0, 0, 0.1); color: #ff3333; border: 1px solid rgba(255, 0, 0, 0.3);'
  }
`;

const TokenBackupRestoreSection = ({ userTokens, setUserTokens }) => {
  const [message, setMessage] = useState(null);
  const [loading, setLoading] = useState(false);
  
  const handleExport = async () => {
    if (!window.electron) {
      setMessage({
        type: 'error',
        text: 'Token export is only available in the desktop app'
      });
      return;
    }
    
    setLoading(true);
    setMessage(null);
    
    try {
      const result = await TokenStorage.exportTokens(userTokens);
      
      if (result.success) {
        setMessage({
          type: 'success',
          text: 'Tokens successfully exported!'
        });
      } else {
        setMessage({
          type: 'error',
          text: result.message || 'Failed to export tokens'
        });
      }
    } catch (error) {
      console.error('Token export failed:', error);
      setMessage({
        type: 'error',
        text: `Export failed: ${error.message}`
      });
    } finally {
      setLoading(false);
    }
  };
  
  const handleImport = async () => {
    if (!window.electron) {
      setMessage({
        type: 'error',
        text: 'Token import is only available in the desktop app'
      });
      return;
    }
    
    setLoading(true);
    setMessage(null);
    
    try {
      const result = await TokenStorage.importTokens();
      
      if (result.success) {
        // Merge imported tokens with existing ones, avoiding duplicates
        const existingTokens = new Map(userTokens.map(token => [
          `${token.address.toLowerCase()}-${token.networkId}`, token
        ]));
        
        result.data.forEach(token => {
          const key = `${token.address.toLowerCase()}-${token.networkId}`;
          if (!existingTokens.has(key)) {
            existingTokens.set(key, token);
          }
        });
        
        const mergedTokens = Array.from(existingTokens.values());
        setUserTokens(mergedTokens);
        
        setMessage({
          type: 'success',
          text: `Successfully imported ${result.data.length} tokens!`
        });
      } else {
        setMessage({
          type: 'error',
          text: result.message || 'Failed to import tokens'
        });
      }
    } catch (error) {
      console.error('Token import failed:', error);
      setMessage({
        type: 'error',
        text: `Import failed: ${error.message}`
      });
    } finally {
      setLoading(false);
    }
  };
  
  return (
    <div>
      <h4 style={{ marginBottom: '0.5rem', fontFamily: 'monospace' }}>Token Backup & Restore</h4>
      <p style={{ fontSize: '0.85rem', marginBottom: '0.75rem' }}>
        Export your token list to keep a backup or import tokens from another installation.
      </p>
      
      <ButtonContainer>
        <Button onClick={handleExport} disabled={loading || userTokens.length === 0}>
          {loading ? 'Processing...' : 'Export Tokens'}
        </Button>
        <Button onClick={handleImport} disabled={loading}>
          {loading ? 'Processing...' : 'Import Tokens'}
        </Button>
      </ButtonContainer>
      
      {message && (
        <MessageBox type={message.type}>
          {message.text}
        </MessageBox>
      )}
    </div>
  );
};

export default TokenBackupRestoreSection;
