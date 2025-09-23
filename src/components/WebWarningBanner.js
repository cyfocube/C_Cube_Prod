import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import EnvironmentDetection from '../utils/EnvironmentDetection';

const WarningBanner = styled.div`
  background: linear-gradient(135deg, #ff6b6b, #ee5a24);
  color: white;
  padding: 12px 20px;
  text-align: center;
  position: relative;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  z-index: 1000;
  font-size: 14px;
  display: ${props => props.show ? 'block' : 'none'};
`;

const WarningContent = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
`;

const WarningText = styled.div`
  flex: 1;
  min-width: 200px;
`;

const CloseButton = styled.button`
  background: rgba(255, 255, 255, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: white;
  padding: 4px 12px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 12px;
  transition: background 0.2s ease;

  &:hover {
    background: rgba(255, 255, 255, 0.3);
  }
`;

const WebWarningBanner = () => {
  const [show, setShow] = useState(false);
  const [dismissed, setDismissed] = useState(false);

  useEffect(() => {
    // Show warning if running in web environment and not previously dismissed
    if (EnvironmentDetection.isWeb() && !dismissed) {
      const dismissedKey = 'webWarningDismissed';
      const isDismissed = localStorage.getItem(dismissedKey) === 'true';
      
      if (!isDismissed) {
        setShow(true);
        // Show the storage warning in console
        EnvironmentDetection.showWebStorageWarning();
      }
    }
  }, [dismissed]);

  const handleDismiss = () => {
    setShow(false);
    setDismissed(true);
    localStorage.setItem('webWarningDismissed', 'true');
  };

  if (!EnvironmentDetection.isWeb() || !show) {
    return null;
  }

  return (
    <WarningBanner show={show}>
      <WarningContent>
        <WarningText>
          <strong>🌐 Web Version Notice:</strong> You're using C-Cube in a web browser. 
          This is an educational tutorial wallet. Data is stored in browser storage. 
          For enhanced security features, consider the desktop application.
        </WarningText>
        <CloseButton onClick={handleDismiss}>
          Dismiss
        </CloseButton>
      </WarningContent>
    </WarningBanner>
  );
};

export default WebWarningBanner;