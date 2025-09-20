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
`;

const PromptContainer = styled.div`
  background-color: ${({ theme }) => theme.colors.cardBackground};
  padding: 2rem;
  border-radius: 8px;
  max-width: 600px;
  width: 90%;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
`;

const Title = styled.h2`
  color: ${({ theme }) => theme.colors.danger};
  margin-bottom: 1.5rem;
  text-align: center;
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
    color: ${({ theme }) => theme.colors.warning};
  }
`;

const CheckboxContainer = styled.div`
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  
  input {
    margin-right: 10px;
  }
`;

const Button = styled.button`
  background-color: ${({ theme, disabled }) => disabled ? theme.colors.secondary : theme.colors.primary};
  color: white;
  width: 100%;
  padding: 0.75rem;
  font-size: 1rem;
  font-weight: bold;
  border-radius: 4px;
  cursor: ${({ disabled }) => disabled ? 'not-allowed' : 'pointer'};
  opacity: ${({ disabled }) => disabled ? 0.7 : 1};
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
