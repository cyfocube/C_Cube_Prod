import styled, { keyframes } from 'styled-components';

// Keyframes
export const buttonGlow = keyframes`
  0%, 100% { box-shadow: 0 0 5px rgba(0, 204, 51, 0.2), 0 0 0px rgba(0, 204, 51, 0); }
  50% { box-shadow: 0 0 15px rgba(0, 204, 51, 0.5), 0 0 10px rgba(0, 204, 51, 0.2); }
`;

export const buttonScan = keyframes`
  0% { background-position: 0% 0%; }
  100% { background-position: 0% 100%; }
`;

export const glow = keyframes`
  0%, 100% { box-shadow: 0 0 5px rgba(0, 204, 51, 0.2); }
  50% { box-shadow: 0 0 15px rgba(0, 204, 51, 0.4); }
`;

export const scanline = keyframes`
  0% { transform: translateY(-100%); }
  100% { transform: translateY(100%); }
`;

export const inputScan = keyframes`
  0% { background-position: 0 0; }
  100% { background-position: 0 100%; }
`;

export const blink = keyframes`
  0%, 100% { opacity: 1; }
  50% { opacity: 0.6; }
`;

export const pulse = keyframes`
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.03); opacity: 0.9; }
`;

export const scan = keyframes`
  0% { background-position: 0% 0%; }
  100% { background-position: 0% 100%; }
`;

export const loadingDots = keyframes`
  0% { content: ""; }
  25% { content: "."; }
  50% { content: ".."; }
  75% { content: "..."; }
  100% { content: ""; }
`;

export const loadingText = keyframes`
  0%, 100% { opacity: 1; }
  50% { opacity: 0.7; }
`;

export const alertPulse = keyframes`
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.02); }
`;

// Layout Components
export const ConsoleFrame = styled.div`
  max-width: 1040px;
  margin: 0 auto;
  border: 2px solid ${({ theme }) => theme.colors.primary};
  border-radius: 4px;
  padding: 10px;
  position: relative;
  background-color: rgba(0, 0, 0, 0.5);
  box-shadow: 0 0 30px rgba(0, 204, 51, 0.25);
  
  &::before {
    content: "C-CUBE TERMINAL v1.3.37";
    position: absolute;
    top: -12px;
    left: 20px;
    background-color: ${({ theme }) => theme.colors.dark};
    color: ${({ theme }) => theme.colors.primary};
    padding: 2px 10px;
    font-family: ${({ theme }) => theme.fonts.code};
    font-size: 0.8rem;
    letter-spacing: 1px;
  }
  
  &::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    background: repeating-linear-gradient(
      0deg,
      rgba(0, 204, 51, 0.03) 0px,
      rgba(0, 204, 51, 0.03) 1px,
      transparent 1px,
      transparent 2px
    );
  }
`;

export const WalletContainer = styled.div`
  max-width: 1000px;
  margin: 0 auto;
`;

export const Card = styled.div`
  background-color: ${({ theme }) => theme.colors.cardBackground};
  border: 1px solid ${({ theme }) => theme.colors.primary};
  border-radius: 4px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 0 15px rgba(0, 255, 65, 0.2);
  position: relative;
  overflow: hidden;
  
  &::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
      linear-gradient(90deg, ${({ theme }) => theme.colors.overlay} 1px, transparent 1px),
      linear-gradient(${({ theme }) => theme.colors.overlay} 1px, transparent 1px);
    background-size: 20px 20px;
    pointer-events: none;
  }
  
  &::after {
    content: "SECURE";
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 0.6rem;
    color: ${({ theme }) => theme.colors.primary};
    border: 1px solid ${({ theme }) => theme.colors.primary};
    padding: 2px 6px;
    letter-spacing: 1px;
    opacity: 0.7;
  }
`;

// Typography
export const Title = styled.h2`
  color: ${({ theme }) => theme.colors.primary};
  margin-bottom: 1.5rem;
  font-family: ${({ theme }) => theme.fonts.code};
  letter-spacing: 1px;
  position: relative;
  display: inline-block;
  text-shadow: 0 0 5px ${({ theme }) => theme.colors.primary};
  
  &::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: -5px;
    width: 100%;
    height: 1px;
    background-color: ${({ theme }) => theme.colors.primary};
    box-shadow: 0 0 5px ${({ theme }) => theme.colors.primary};
  }
`;

export const Subtitle = styled.h3`
  color: ${({ theme }) => theme.colors.text};
  margin-bottom: 1rem;
  font-family: ${({ theme }) => theme.fonts.code};
  letter-spacing: 1px;
`;

// Wallet Components
export const WalletInfo = styled.div`
  margin-bottom: 2rem;
  position: relative;
`;

export const NetworkBadge = styled.div`
  display: inline-flex;
  align-items: center;
  margin-bottom: 10px;
  padding: 5px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 500;
  background-color: ${({ color }) => color || '#627EEA'}22;
  color: ${({ color }) => color || '#627EEA'};
  border: 1px solid ${({ color }) => color || '#627EEA'}44;
  
  &:before {
    content: "";
    display: inline-block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background-color: ${({ color }) => color || '#627EEA'};
    margin-right: 6px;
  }
`;

export const WalletAddress = styled.div`
  background-color: ${({ theme }) => theme.colors.dark};
  padding: 1rem;
  border-radius: 2px;
  font-family: ${({ theme }) => theme.fonts.code};
  word-break: break-all;
  margin-bottom: 1rem;
  border: 1px solid ${({ theme }) => theme.colors.primary};
  position: relative;
  color: ${({ theme }) => theme.colors.primary};
  overflow: hidden;
  
  &::before {
    content: "ADDRESS";
    position: absolute;
    top: -8px;
    left: 10px;
    background-color: ${({ theme }) => theme.colors.dark};
    padding: 0 5px;
    font-size: 0.7rem;
    color: ${({ theme }) => theme.colors.primary};
  }
  
  &::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: repeating-linear-gradient(
      45deg,
      transparent,
      transparent 10px,
      rgba(0, 255, 65, 0.03) 10px,
      rgba(0, 255, 65, 0.03) 20px
    );
    pointer-events: none;
  }
`;

export const WalletControls = styled.div`
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
`;

export const QRCodeContainer = styled.div`
  display: flex;
  justify-content: center;
  margin: 1rem 0;
  padding: 1.25rem;
  background-color: black;
  border: 1px solid ${({ theme }) => theme.colors.primary};
  border-radius: 4px;
  width: fit-content;
  position: relative;
  box-shadow: 0 0 20px rgba(0, 204, 51, 0.2);
  animation: ${pulse} 4s infinite ease-in-out;
  
  &::before {
    content: "SCAN FOR ADDRESS";
    position: absolute;
    top: -10px;
    left: 50%;
    transform: translateX(-50%);
    background-color: ${({ theme }) => theme.colors.dark};
    color: ${({ theme }) => theme.colors.primary};
    padding: 2px 8px;
    font-size: 0.7rem;
    font-family: ${({ theme }) => theme.fonts.code};
    letter-spacing: 1px;
    border: 1px solid ${({ theme }) => theme.colors.primary};
  }
  
  &::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(
      to bottom,
      rgba(0, 204, 51, 0.1) 10%,
      transparent 10%,
      transparent
    );
    background-size: 100% 1000%;
    animation: ${scan} 5s linear infinite;
    pointer-events: none;
  }
`;

// Interactive Components
export const Button = styled.button`
  background-color: ${({ theme, secondary, danger }) => 
    danger ? theme.colors.dark : secondary ? theme.colors.dark : theme.colors.dark};
  color: ${({ theme, danger }) => danger ? theme.colors.danger : theme.colors.primary};
  padding: 0.75rem 1.5rem;
  border-radius: 2px;
  font-family: ${({ theme }) => theme.fonts.code};
  font-weight: bold;
  border: 1px solid ${({ theme, danger }) => danger ? theme.colors.danger : theme.colors.primary};
  letter-spacing: 1px;
  text-transform: uppercase;
  position: relative;
  overflow: hidden;
  transition: all 0.3s ease;
  cursor: pointer;
  animation: ${buttonGlow} 4s infinite ease-in-out;
  text-shadow: 0 0 5px ${({ theme, danger }) => danger ? theme.colors.danger : theme.colors.primary};
  
  &:hover {
    box-shadow: 0 0 15px ${({ theme, danger }) => danger ? theme.colors.danger : theme.colors.primary};
    background-color: ${({ theme, danger }) => 
      danger ? 'rgba(255, 7, 58, 0.1)' : 'rgba(0, 204, 51, 0.1)'};
  }
  
  &:active {
    transform: translateY(1px);
    box-shadow: 0 0 25px ${({ theme, danger }) => danger ? theme.colors.danger : theme.colors.primary};
  }
  
  &::before {
    content: "";
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 2px;
    background-color: ${({ theme, danger }) => danger ? theme.colors.danger : theme.colors.primary};
    transition: all 0.5s ease;
    box-shadow: 0 0 10px ${({ theme, danger }) => danger ? theme.colors.danger : theme.colors.primary};
  }
  
  &::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(
      to bottom,
      ${({ theme, danger }) => danger ? 'rgba(255, 7, 58, 0.1)' : 'rgba(0, 204, 51, 0.1)'} 10%,
      transparent 10%,
      transparent
    );
    background-size: 100% 1000%;
    animation: ${buttonScan} 3s linear infinite;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.3s;
  }
  
  &:hover::after {
    opacity: 1;
  }
  
  &:hover::before {
    left: 0;
  }
  
  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
    animation: none;
    &:hover {
      box-shadow: none;
      background-color: ${({ theme }) => theme.colors.dark};
    }
    &::after {
      display: none;
    }
  }
`;

// Tab Components
export const TabContainer = styled.div`
  display: flex;
  margin-bottom: 1.5rem;
  border-bottom: 1px solid ${({ theme }) => theme.colors.primary};
  position: relative;
  
  &::after {
    content: "";
    position: absolute;
    bottom: -1px;
    left: 0;
    width: 100%;
    height: 1px;
    box-shadow: 0 0 5px ${({ theme }) => theme.colors.primary};
  }
`;

export const TabButton = styled.button`
  flex: 1;
  background: none;
  border: none;
  padding: 1rem;
  color: ${({ active, theme }) => active ? theme.colors.primary : theme.colors.mutedText};
  border-bottom: ${({ active, theme }) => active ? `2px solid ${theme.colors.primary}` : 'none'};
  font-weight: ${({ active }) => active ? 'bold' : 'normal'};
  font-family: ${({ theme }) => theme.fonts.code};
  letter-spacing: 1px;
  text-transform: uppercase;
  position: relative;
  transition: all 0.3s ease;
  font-size: 0.8rem;
  
  &:hover {
    color: ${({ theme }) => theme.colors.primary};
    background-color: rgba(0, 255, 65, 0.05);
  }
  
  ${({ active, theme }) => active && `
    &::before {
      content: "◢◣";
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
      color: ${theme.colors.primary};
      font-size: 0.6rem;
      letter-spacing: -3px;
    }
  `}
`;

// Alias for backwards compatibility
export const Tab = TabButton;

export const TabContent = styled.div`
  padding: 1rem;
  margin-bottom: 1.5rem;
  background-color: rgba(0, 0, 0, 0.2);
  border: 1px solid ${({ theme }) => theme.colors.primary}33;
  border-radius: 4px;
  position: relative;
  
  &::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(
      transparent 50%,
      rgba(0, 255, 65, 0.05) 50%
    );
    background-size: 100% 4px;
    pointer-events: none;
  }
`;

// Form Components
export const FormGroup = styled.div`
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  position: relative;
`;

export const Label = styled.label`
  font-weight: bold;
  color: ${({ theme }) => theme.colors.primary};
  font-family: ${({ theme }) => theme.fonts.code};
  font-size: 0.9rem;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  
  &::after {
    content: " //";
    opacity: 0.6;
  }
`;

export const InputWrapper = styled.div`
  position: relative;
  width: 100%;
  
  &::before {
    content: ">";
    position: absolute;
    left: 8px;
    top: 50%;
    transform: translateY(-50%);
    color: ${({ theme, error }) => error ? theme.colors.danger : theme.colors.primary};
    font-family: ${({ theme }) => theme.fonts.code};
    font-weight: bold;
    z-index: 1;
    pointer-events: none;
  }
`;

export const Input = styled.input`
  padding: 0.75rem 0.75rem 0.75rem 1.5rem;
  border-radius: 2px;
  border: 1px solid ${({ theme, error }) => error ? theme.colors.danger : theme.colors.primary};
  background-color: rgba(0, 0, 0, 0.7);
  color: ${({ theme }) => theme.colors.primary};
  font-family: ${({ theme }) => theme.fonts.code};
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  letter-spacing: 1px;
  width: 100%;
  
  &::placeholder {
    color: ${({ theme }) => theme.colors.primary}70;
    letter-spacing: 0;
  }
  
  &:focus {
    border-color: ${({ theme }) => theme.colors.primary};
    outline: none;
    animation: ${glow} 2s infinite;
    background: linear-gradient(
      to bottom,
      rgba(0, 255, 65, 0.05) 50%,
      transparent 50%
    );
    background-size: 100% 4px;
    animation: ${inputScan} 20s linear infinite, ${glow} 2s infinite;
  }
  
  &::placeholder {
    color: ${({ theme }) => theme.colors.mutedText};
    opacity: 0.5;
  }
  
  &:hover::after,
  &:focus::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background-color: rgba(0, 255, 65, 0.2);
    animation: ${scanline} 2s linear infinite;
  }
`;

export const TextAreaWrapper = styled.div`
  position: relative;
  width: 100%;
  
  &::before {
    content: ">";
    position: absolute;
    left: 8px;
    top: 11px;
    color: ${({ theme, error }) => error ? theme.colors.danger : theme.colors.primary};
    font-family: ${({ theme }) => theme.fonts.code};
    font-weight: bold;
    z-index: 1;
    pointer-events: none;
  }
`;

export const TextArea = styled.textarea`
  padding: 0.75rem 0.75rem 0.75rem 1.5rem;
  border-radius: 2px;
  border: 1px solid ${({ theme, error }) => error ? theme.colors.danger : theme.colors.primary};
  background-color: rgba(0, 0, 0, 0.7);
  color: ${({ theme }) => theme.colors.primary};
  min-height: 100px;
  font-family: ${({ theme }) => theme.fonts.code};
  resize: vertical;
  transition: all 0.3s ease;
  letter-spacing: 1px;
  line-height: 1.5;
  position: relative;
  width: 100%;
  
  &::placeholder {
    color: ${({ theme }) => theme.colors.primary}70;
    letter-spacing: 0;
  }
  
  &:focus {
    border-color: ${({ theme }) => theme.colors.primary};
    outline: none;
    animation: ${glow} 2s infinite;
    background: linear-gradient(
      to bottom,
      rgba(0, 255, 65, 0.05) 50%,
      transparent 50%
    );
    background-size: 100% 4px;
    animation: ${inputScan} 20s linear infinite, ${glow} 2s infinite;
  }
  
  &::placeholder {
    color: ${({ theme }) => theme.colors.mutedText};
    opacity: 0.5;
  }
`;

// Checkbox and Radio Components
export const CheckboxContainer = styled.div`
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
`;

export const Checkbox = styled.input`
  width: 18px;
  height: 18px;
  margin-right: 10px;
  cursor: pointer;
`;

export const CheckboxLabel = styled.span`
  color: ${({ theme }) => theme.colors.text};
  font-size: 14px;
`;

export const RadioGroup = styled.div`
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1rem;
`;

export const RadioOption = styled.div`
  display: flex;
  align-items: center;
`;

export const RadioInput = styled.input`
  width: 18px;
  height: 18px;
  margin-right: 10px;
  cursor: pointer;
`;

export const RadioLabel = styled.span`
  color: ${({ theme }) => theme.colors.text};
  font-size: 14px;
`;

// Message Components
export const ErrorMessage = styled.div`
  color: ${({ theme }) => theme.colors.danger};
  padding: 1rem;
  border: 1px solid ${({ theme }) => theme.colors.danger};
  border-radius: 2px;
  margin-bottom: 1rem;
  background-color: rgba(255, 7, 58, 0.05);
  font-family: ${({ theme }) => theme.fonts.code};
  position: relative;
  box-shadow: 0 0 15px rgba(255, 7, 58, 0.15);
  
  &::before {
    content: "ERROR //";
    font-weight: bold;
    display: block;
    margin-bottom: 0.5rem;
    letter-spacing: 1px;
    animation: ${blink} 2s infinite;
  }
`;

export const SuccessMessage = styled.div`
  color: ${({ theme }) => theme.colors.success};
  padding: 1rem;
  border: 1px solid ${({ theme }) => theme.colors.success};
  border-radius: 2px;
  margin-bottom: 1rem;
  background-color: rgba(51, 255, 51, 0.05);
  font-family: ${({ theme }) => theme.fonts.code};
  position: relative;
  box-shadow: 0 0 15px rgba(51, 255, 51, 0.15);
  
  &::before {
    content: "SUCCESS //";
    font-weight: bold;
    display: block;
    margin-bottom: 0.5rem;
    letter-spacing: 1px;
  }
`;

export const WarningText = styled.div`
  color: ${({ theme }) => theme.colors.danger};
  margin-bottom: 1.25rem;
  font-weight: bold;
  font-family: ${({ theme }) => theme.fonts.code};
  padding: 0.75rem;
  border-left: 3px solid ${({ theme }) => theme.colors.danger};
  background: rgba(255, 7, 58, 0.05);
  display: flex;
  align-items: center;
  letter-spacing: 0.5px;
  animation: ${alertPulse} 2s infinite ease-in-out;
  
  &::before {
    content: "⚠️";
    margin-right: 8px;
    font-size: 1.1rem;
  }
`;

export const InfoText = styled.p`
  margin-bottom: 1rem;
  line-height: 1.8;
  font-size: 0.9rem;
  color: ${({ theme }) => theme.colors.text};
  padding: 0.5rem 0.5rem 0.5rem 1rem;
  border-left: 2px solid ${({ theme }) => theme.colors.primary};
  background: linear-gradient(
    to right,
    rgba(0, 204, 51, 0.05),
    transparent 80%
  );
  font-family: ${({ theme }) => theme.fonts.sans};
`;

// Loading Component
export const Loading = styled.span`
  position: relative;
  display: inline-block;
  color: inherit;
  animation: ${loadingText} 2s infinite;
  
  &::after {
    content: "";
    display: inline-block;
    width: 1em;
    animation: ${loadingDots} 1.5s infinite;
    text-align: left;
  }
`;

// Private Key and Mnemonic Displays
export const PrivateKeyDisplay = styled.div`
  background-color: rgba(255, 7, 58, 0.05);
  border: 1px solid ${({ theme }) => theme.colors.danger};
  padding: 1.5rem;
  border-radius: 2px;
  margin: 1rem 0;
  position: relative;
  font-family: ${({ theme }) => theme.fonts.code};
  color: ${({ theme }) => theme.colors.danger};
  box-shadow: 0 0 10px rgba(255, 7, 58, 0.2);
  
  &::before {
    content: "TOP SECRET";
    position: absolute;
    top: -10px;
    left: 10px;
    background-color: ${({ theme }) => theme.colors.dark};
    color: ${({ theme }) => theme.colors.danger};
    padding: 2px 8px;
    font-size: 0.7rem;
    letter-spacing: 1px;
    border: 1px solid ${({ theme }) => theme.colors.danger};
    animation: ${blink} 2s infinite;
  }
`;

export const MnemonicDisplay = styled.div`
  background-color: rgba(255, 153, 0, 0.05);
  border: 1px solid ${({ theme }) => theme.colors.warning};
  padding: 1.5rem;
  border-radius: 2px;
  margin: 1rem 0;
  position: relative;
  word-break: break-word;
  line-height: 1.8;
  font-family: ${({ theme }) => theme.fonts.code};
  color: ${({ theme }) => theme.colors.warning};
  box-shadow: 0 0 10px rgba(255, 153, 0, 0.2);
  
  &::before {
    content: "RECOVERY KEY";
    position: absolute;
    top: -10px;
    left: 10px;
    background-color: ${({ theme }) => theme.colors.dark};
    color: ${({ theme }) => theme.colors.warning};
    padding: 2px 8px;
    font-size: 0.7rem;
    letter-spacing: 1px;
    border: 1px solid ${({ theme }) => theme.colors.warning};
  }
`;
