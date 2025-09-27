import React from 'react';
import styled from 'styled-components';

const PromptOverlay = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  overflow-y: auto;
  
  @media (max-width: 768px) {
    align-items: flex-start;
    padding: 20px 0;
  }
`;

const PromptContainer = styled.div`
  background-color: ${({ theme }) => theme?.colors?.cardBackground || '#1a1a1a'};
  color: ${({ theme }) => theme?.colors?.text || '#ffffff'};
  padding: 2rem;
  border-radius: 8px;
  max-width: 600px;
  width: 90%;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  margin: auto;
  max-height: 90vh;
  overflow-y: auto;
  
  @media (max-width: 768px) {
    padding: 1.5rem;
    width: 95%;
    margin: 20px auto;
    max-height: calc(100vh - 40px);
  }
  
  @media (max-width: 480px) {
    padding: 1rem;
    border-radius: 4px;
    margin: 10px auto;
    max-height: calc(100vh - 20px);
  }
`;

const Title = styled.h2`
  color: ${({ theme }) => theme?.colors?.danger || '#dc3545'};
  margin-bottom: 1.5rem;
  text-align: center;
  
  @media (max-width: 768px) {
    font-size: 1.3rem;
    margin-bottom: 1rem;
  }
  
  @media (max-width: 480px) {
    font-size: 1.1rem;
    margin-bottom: 0.8rem;
  }
`;

const Content = styled.div`
  margin-bottom: 1.5rem;
  line-height: 1.6;

  p {
    margin-bottom: 1rem;
  }

  ul {
    margin-left: 1.5rem;
    margin-bottom: 1rem;
  }

  strong {
    color: ${({ theme }) => theme?.colors?.warning || '#ffc107'};
  }
  
  @media (max-width: 768px) {
    margin-bottom: 1rem;
    font-size: 0.95rem;
    
    p {
      margin-bottom: 0.8rem;
    }
    
    ul {
      margin-left: 1rem;
      margin-bottom: 0.8rem;
    }
  }
  
  @media (max-width: 480px) {
    font-size: 0.9rem;
    
    ul {
      margin-left: 0.8rem;
    }
  }
`;

const CheckboxContainer = styled.div`
  margin-bottom: 1.5rem;
  display: flex;
  align-items: flex-start;
  
  input {
    margin-right: 10px;
    margin-top: 2px;
    flex-shrink: 0;
  }
  
  label {
    line-height: 1.4;
  }
  
  @media (max-width: 768px) {
    margin-bottom: 1rem;
    
    label {
      font-size: 0.9rem;
    }
  }
  
  @media (max-width: 480px) {
    input {
      margin-right: 8px;
    }
    
    label {
      font-size: 0.85rem;
    }
  }
`;

const Button = styled.button`
  background-color: ${({ theme, disabled }) => 
    disabled 
      ? (theme?.colors?.secondary || '#6c757d') 
      : (theme?.colors?.primary || '#007bff')
  };
  color: white;
  width: 100%;
  padding: 0.75rem;
  font-size: 1rem;
  font-weight: bold;
  border-radius: 4px;
  cursor: ${({ disabled }) => disabled ? 'not-allowed' : 'pointer'};
  opacity: ${({ disabled }) => disabled ? 0.7 : 1};
  border: none;
  transition: all 0.3s ease;
  
  &:hover:not(:disabled) {
    opacity: 0.9;
    transform: translateY(-1px);
  }
  
  @media (max-width: 768px) {
    padding: 0.8rem;
    font-size: 0.95rem;
    margin-bottom: 1rem;
  }
  
  @media (max-width: 480px) {
    padding: 0.9rem;
    font-size: 0.9rem;
    margin-bottom: 1.5rem;
  }
`;

const SecurityPrompt = ({ onAcknowledge }) => {
  const [acknowledged, setAcknowledged] = React.useState(false);

  return (
    <PromptOverlay>
      <PromptContainer>
        <Title>⚠️ Security Warning ⚠️</Title>
        <Content>
          <p>You are about to use a cold wallet application designed for offline cryptocurrency storage. Please read and understand the following:</p>
          
          <ul>
            <li><strong>This application is most secure when used on an offline computer</strong> that never connects to the internet.</li>
            <li>Your private keys and seed phrases are stored only on your device and are encrypted.</li>
            <li>NEVER share your private keys or seed phrases with anyone.</li>
            <li>Always back up your private keys or seed phrases in a secure location.</li>
            <li>Verify transaction details carefully before signing.</li>
            <li>Consider using a hardware wallet for additional security.</li>
          </ul>
          
          <p>By proceeding, you acknowledge that you understand these security principles and that you are responsible for the security of your own funds.</p>
        </Content>

        <CheckboxContainer>
          <input 
            type="checkbox" 
            id="acknowledgment" 
            checked={acknowledged}
            onChange={() => setAcknowledged(!acknowledged)}
          />
          <label htmlFor="acknowledgment">I understand the security implications and will use this application responsibly.</label>
        </CheckboxContainer>

        <Button onClick={onAcknowledge} disabled={!acknowledged}>
          I Understand, Proceed to Application
        </Button>
      </PromptContainer>
    </PromptOverlay>
  );
};

export default SecurityPrompt;
