import React, { useState } from 'react';
import styled from 'styled-components';
import { useNavigate } from 'react-router-dom';

const WelcomeContainer = styled.div`
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 60vh;
`;

const Card = styled.div`
  background-color: ${({ theme }) => theme.colors.cardBackground};
  border-radius: 8px;
  padding: 2rem;
  width: 100%;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
`;

const Title = styled.h1`
  color: ${({ theme }) => theme.colors.primary};
  margin-bottom: 1.5rem;
  font-size: 2rem;
`;

const Subtitle = styled.h2`
  color: ${({ theme }) => theme.colors.text};
  margin-bottom: 2rem;
  font-size: 1.2rem;
  font-weight: normal;
`;

const ButtonContainer = styled.div`
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-width: 400px;
  margin: 0 auto;
`;

const ActionButton = styled.button`
  background-color: ${({ primary, theme }) => 
    primary ? theme.colors.primary : theme.colors.secondary};
  color: white;
  padding: 1rem;
  border-radius: 4px;
  font-weight: bold;
  font-size: 1.1rem;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  
  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    background-color: ${({ primary, theme }) => 
      primary ? theme.colors.info : theme.colors.secondaryLight};
  }
`;

const ButtonIcon = styled.span`
  margin-right: 0.5rem;
  font-size: 1.2rem;
`;

const WelcomeScreen = () => {
  const navigate = useNavigate();

  const handleCreateNew = () => {
    localStorage.setItem('walletAction', 'create');
    navigate('/setup');
  };

  const handleRecover = () => {
    localStorage.setItem('walletAction', 'recover');
    navigate('/setup');
  };

  return (
    <WelcomeContainer>
      <Card>
        <Title>Welcome to C-Cube</Title>
        <Subtitle>
          Your secure offline cryptocurrency wallet solution. 
          Get started by creating a new wallet or recovering an existing one.
        </Subtitle>
        
        <ButtonContainer>
          <ActionButton primary onClick={handleCreateNew}>
            <ButtonIcon>➕</ButtonIcon> Create New Wallet
          </ActionButton>
          
          <ActionButton onClick={handleRecover}>
            <ButtonIcon>🔄</ButtonIcon> Recover Existing Wallet
          </ActionButton>
        </ButtonContainer>
      </Card>
    </WelcomeContainer>
  );
};

export default WelcomeScreen;
