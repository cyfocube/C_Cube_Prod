import React from 'react';
import { TabContainer, Tab } from './WalletStyles';

const TabNavigation = ({ 
  activeTab, 
  onTabChange, 
  isWalletEncrypted 
}) => {
  const tabs = [
    { id: 'info', label: 'Wallet Info', alwaysShow: true },
    { id: 'decrypt', label: 'Decrypt Wallet', showIf: isWalletEncrypted },
    { id: 'export', label: 'Export Private Key', alwaysShow: true },
    { id: 'recovery', label: 'Recovery Phrase', alwaysShow: true },
    { id: 'sign', label: 'Sign Transaction', alwaysShow: true },
    { id: 'tokens', label: 'Token Management', alwaysShow: true },
    { id: 'createWallet', label: 'New Wallet', alwaysShow: true }
  ];

  return (
    <TabContainer>
      {tabs.map(tab => {
        // Show tab if it should always show or if its condition is met
        if (tab.alwaysShow || tab.showIf) {
          return (
            <Tab 
              key={tab.id}
              active={activeTab === tab.id} 
              onClick={() => onTabChange(tab.id)}
            >
              {tab.label}
            </Tab>
          );
        }
        return null;
      })}
    </TabContainer>
  );
};

export default TabNavigation;
