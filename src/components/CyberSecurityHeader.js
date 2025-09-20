import React, { useState, useEffect } from 'react';
import styled, { keyframes } from 'styled-components';

const blink = keyframes`
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
`;

const typing = keyframes`
  from { width: 0 }
  to { width: 100% }
`;

const scanline = keyframes`
  0% { transform: translateY(0); }
  100% { transform: translateY(100vh); }
`;

const glitch = keyframes`
  0% { transform: translate(0); }
  20% { transform: translate(-2px, 2px); }
  40% { transform: translate(-2px, -2px); }
  60% { transform: translate(2px, 2px); }
  80% { transform: translate(2px, -2px); }
  100% { transform: translate(0); }
`;

const HeaderContainer = styled.div`
  position: relative;
  margin-bottom: 2rem;
  padding: 1.5rem;
  border: 1px solid ${({ theme }) => theme.colors.primary};
  background-color: ${({ theme }) => theme.colors.dark};
  overflow: hidden;
  
  &::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background: ${({ theme }) => theme.colors.primary};
    box-shadow: 0 0 10px 2px ${({ theme }) => theme.colors.primary};
    z-index: 1;
  }
  
  &::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: repeating-linear-gradient(
      transparent 0px,
      rgba(0, 204, 51, 0.02) 1px,
      transparent 2px
    );
    pointer-events: none;
  }
`;

const Title = styled.h1`
  font-family: ${({ theme }) => theme.fonts.code};
  color: ${({ theme }) => theme.colors.primary};
  text-shadow: 0 0 5px ${({ theme }) => theme.colors.primary};
  letter-spacing: 1px;
  font-size: 1.8rem;
  margin-bottom: 0.5rem;
  display: inline-block;
  position: relative;
  
  &::after {
    content: '_';
    animation: ${blink} 1s step-end infinite;
  }
  
  &:hover {
    animation: ${glitch} 0.2s ease-in-out;
  }
`;

const SecurityStatus = styled.div`
  font-family: ${({ theme }) => theme.fonts.code};
  font-size: 0.8rem;
  color: ${({ connected }) => (connected ? '#33ff33' : '#ff073a')};
  display: flex;
  align-items: center;
  margin-top: 0.5rem;
  
  &::before {
    content: "";
    display: inline-block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background-color: ${({ connected }) => (connected ? '#33ff33' : '#ff073a')};
    margin-right: 8px;
    box-shadow: 0 0 5px ${({ connected }) => (connected ? '#33ff33' : '#ff073a')};
    animation: ${blink} ${({ connected }) => (connected ? '2s' : '0.5s')} infinite;
  }
`;

const Scanline = styled.div`
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 20px;
  background: linear-gradient(to bottom, 
    rgba(0, 204, 51, 0.2), 
    transparent 80%, 
    transparent);
  opacity: 0.1;
  pointer-events: none;
  animation: ${scanline} 6s linear infinite;
  z-index: 2;
`;

const TypewriterText = styled.div`
  font-family: ${({ theme }) => theme.fonts.code};
  font-size: 0.9rem;
  color: ${({ theme }) => theme.colors.mutedText};
  overflow: hidden;
  white-space: nowrap;
  border-right: 2px solid ${({ theme }) => theme.colors.primary};
  animation: ${typing} 3.5s steps(60, end), ${blink} 1s step-end infinite;
  max-width: 600px;
  width: 100%;
`;

const DataSection = styled.div`
  font-family: ${({ theme }) => theme.fonts.code};
  font-size: 0.8rem;
  color: ${({ theme }) => theme.colors.mutedText};
  margin-top: 0.5rem;
  display: flex;
  gap: 1.5rem;
`;

const DataItem = styled.div`
  display: flex;
  align-items: center;
  gap: 0.5rem;
  
  span:first-child {
    color: ${({ theme }) => theme.colors.primary};
  }
`;

const CyberSecurityHeader = ({ title, subtitle }) => {
  const [date, setDate] = useState(new Date());
  const [connected, setConnected] = useState(true);
  
  useEffect(() => {
    const timer = setInterval(() => {
      setDate(new Date());
      // Randomly simulate connection changes for effect
      if (Math.random() > 0.98) {
        setConnected(prev => !prev);
        setTimeout(() => setConnected(true), 2000);
      }
    }, 1000);
    
    return () => clearInterval(timer);
  }, []);
  
  return (
    <HeaderContainer>
      <Scanline />
      <Title>{title}</Title>
      <TypewriterText>{subtitle}</TypewriterText>
      <DataSection>
        <DataItem>
          <span>SYS:</span>
          <span>COLD_STORAGE</span>
        </DataItem>
        <DataItem>
          <span>TIME:</span>
          <span>{date.toLocaleTimeString()}</span>
        </DataItem>
        <DataItem>
          <span>DATE:</span>
          <span>{date.toLocaleDateString()}</span>
        </DataItem>
      </DataSection>
      <SecurityStatus connected={connected}>
        {connected ? 'SECURE CONNECTION' : 'CONNECTION UNSTABLE'}
      </SecurityStatus>
    </HeaderContainer>
  );
};

export default CyberSecurityHeader;
