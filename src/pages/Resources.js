import React from 'react';
import styled from 'styled-components';
import { PageBackground, PageContent } from '../components/shared/PageBackground';

const ResourcesContainer = styled.div`
  max-width: 900px;
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
`;

const Subtitle = styled.h3`
  color: ${({ theme }) => theme.colors.text};
  margin-bottom: 1rem;
  margin-top: 2rem;
  border-bottom: 1px solid ${({ theme }) => theme.colors.border};
  padding-bottom: 0.5rem;
`;

const List = styled.ul`
  margin-left: 1.5rem;
  margin-bottom: 1.5rem;
`;

const ListItem = styled.li`
  margin-bottom: 0.75rem;
  line-height: 1.6;
`;

const Section = styled.section`
  margin-bottom: 2rem;
`;

const Quote = styled.blockquote`
  border-left: 4px solid ${({ theme }) => theme.colors.primary};
  padding-left: 1rem;
  margin: 1.5rem 0;
  color: ${({ theme }) => theme.colors.mutedText};
  font-style: italic;
`;

const Callout = styled.div`
  background-color: ${({ theme, warning }) => warning ? theme.colors.warning : theme.colors.info}20;
  border-left: 4px solid ${({ theme, warning }) => warning ? theme.colors.warning : theme.colors.info};
  padding: 1rem;
  margin: 1.5rem 0;
  border-radius: 0 4px 4px 0;
`;

const TabContainer = styled.div`
  display: flex;
  margin-bottom: 1.5rem;
  border-bottom: 1px solid ${({ theme }) => theme.colors.border};
`;

const Tab = styled.button`
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

const Resources = () => {
  const [activeTab, setActiveTab] = React.useState('guide');

  return (
    <PageBackground>
      <PageContent>
        <ResourcesContainer>
      <Card>
        <Title>Resources</Title>
        
        <TabContainer>
          <Tab 
            active={activeTab === 'guide'} 
            onClick={() => setActiveTab('guide')}
          >
            User Guide
          </Tab>
          <Tab 
            active={activeTab === 'security'} 
            onClick={() => setActiveTab('security')}
          >
            Security Tips
          </Tab>
          <Tab 
            active={activeTab === 'faq'} 
            onClick={() => setActiveTab('faq')}
          >
            FAQ
          </Tab>
          <Tab 
            active={activeTab === 'about'} 
            onClick={() => setActiveTab('about')}
          >
            About
          </Tab>
        </TabContainer>
        
        {activeTab === 'guide' && (
          <Section>
            <Subtitle>Getting Started</Subtitle>
            <p>Welcome to C-Cube! This application allows you to securely create and manage cryptocurrency wallets offline, keeping your private keys safe from online threats.</p>
            
            <Subtitle>Creating a New Wallet</Subtitle>
            <List>
              <ListItem><strong>Navigate to the "Cold Wallet" tab</strong> if you don't already have a wallet set up.</ListItem>
              <ListItem><strong>Choose "Create New Wallet"</strong> to generate a new wallet with a random private key.</ListItem>
              <ListItem><strong>Set a strong password</strong> to encrypt your wallet (strongly recommended).</ListItem>
              <ListItem><strong>Back up your private key or seed phrase</strong> in a secure location.</ListItem>
            </List>
            
            <Callout>
              Remember: Your private key is your access to your funds. If you lose it, you lose access to your wallet permanently.
            </Callout>
            
            <Subtitle>Signing Transactions</Subtitle>
            <List>
              <ListItem><strong>Navigate to the "Cold Wallet" tab</strong> and select your wallet.</ListItem>
              <ListItem><strong>Click "Sign Transaction"</strong> to begin creating a new transaction.</ListItem>
              <ListItem><strong>Enter the recipient address</strong> and the amount you want to send.</ListItem>
              <ListItem><strong>Review the transaction details carefully</strong> before signing.</ListItem>
              <ListItem><strong>Enter your wallet password</strong> if your wallet is encrypted.</ListItem>
              <ListItem><strong>Click "Sign Transaction"</strong> to generate a signed transaction.</ListItem>
              <ListItem><strong>Copy the signed transaction data</strong> to broadcast later.</ListItem>
            </List>
            
            <Subtitle>Broadcasting Transactions</Subtitle>
            <List>
              <ListItem><strong>Move to an online device</strong> or connect to the internet.</ListItem>
              <ListItem><strong>Navigate to the "Broadcast" tab</strong>.</ListItem>
              <ListItem><strong>Paste your signed transaction</strong> into the text field.</ListItem>
              <ListItem><strong>Click "Verify Transaction"</strong> to check the details are correct.</ListItem>
              <ListItem><strong>Select an Ethereum node</strong> to use for broadcasting.</ListItem>
              <ListItem><strong>Click "Broadcast Transaction"</strong> to send your transaction to the network.</ListItem>
            </List>
            
            <Callout warning>
              Always verify the transaction details carefully before broadcasting. Cryptocurrency transactions cannot be reversed once confirmed on the blockchain.
            </Callout>
          </Section>
        )}
        
        {activeTab === 'security' && (
          <Section>
            <Subtitle>Cold Wallet Security</Subtitle>
            <p>A cold wallet is a cryptocurrency wallet that is never connected to the internet, keeping your private keys completely offline and safe from online threats.</p>
            
            <Subtitle>Best Practices</Subtitle>
            <List>
              <ListItem><strong>Use a dedicated offline device</strong> for maximum security. Ideally, this computer should never connect to the internet.</ListItem>
              <ListItem><strong>Always encrypt your wallet</strong> with a strong password that includes a mix of letters, numbers, and special characters.</ListItem>
              <ListItem><strong>Store backup copies of your private key or seed phrase</strong> in multiple secure physical locations (e.g., safe deposit box).</ListItem>
              <ListItem><strong>Consider using a hardware wallet</strong> for additional security if managing significant assets.</ListItem>
              <ListItem><strong>Never share your private key or seed phrase</strong> with anyone, under any circumstances.</ListItem>
              <ListItem><strong>Be wary of physical security</strong> - ensure no one can see your screen when viewing private keys.</ListItem>
            </List>
            
            <Subtitle>Threats to Be Aware Of</Subtitle>
            <List>
              <ListItem><strong>Phishing attacks</strong> - Never enter your private key on websites or in response to emails.</ListItem>
              <ListItem><strong>Malware</strong> - Keep your offline system free from malicious software.</ListItem>
              <ListItem><strong>Social engineering</strong> - Be suspicious of anyone asking for wallet information, even if they appear to be from a legitimate organization.</ListItem>
              <ListItem><strong>Physical theft</strong> - Secure your backup materials and devices.</ListItem>
            </List>
            
            <Callout>
              Remember: The most secure wallet is one where the private key has never been exposed to an internet-connected device.
            </Callout>
            
            <Subtitle>Secure Backup Methods</Subtitle>
            <List>
              <ListItem><strong>Paper backups</strong> - Write down your private key or seed phrase on paper and store in a waterproof, fireproof container.</ListItem>
              <ListItem><strong>Metal backups</strong> - Use metal plates designed for seed phrase storage to protect against fire and water damage.</ListItem>
              <ListItem><strong>Distributed storage</strong> - Consider splitting your seed phrase into multiple parts stored in different locations (using advanced seed splitting techniques).</ListItem>
            </List>
            
            <Quote>
              "The only truly secure cryptocurrency is one where you control the private keys, and those keys have never been exposed to potential threats."
            </Quote>
          </Section>
        )}
        
        {activeTab === 'faq' && (
          <Section>
            <Subtitle>Frequently Asked Questions</Subtitle>
            
            <Subtitle>General Questions</Subtitle>
            <p><strong>Q: What is a cold wallet?</strong></p>
            <p>A: A cold wallet is a cryptocurrency wallet that is kept entirely offline, protecting your private keys from online threats like hackers and malware. This application helps you create and manage cold wallets securely.</p>
            
            <p><strong>Q: How is this different from other wallet applications?</strong></p>
            <p>A: This application is designed to be used offline, focusing on security rather than convenience. It separates the wallet creation and transaction signing (offline) from the transaction broadcasting (online) to maximize security.</p>
            
            <p><strong>Q: Which cryptocurrencies are supported?</strong></p>
            <p>A: Currently, the application supports Ethereum. Support for Bitcoin and other cryptocurrencies may be added in future updates.</p>
            
            <Subtitle>Security Questions</Subtitle>
            <p><strong>Q: How secure is this wallet?</strong></p>
            <p>A: The security of this wallet depends largely on how you use it. For maximum security, use it on a completely offline computer, encrypt your wallet with a strong password, and keep secure backups of your private key.</p>
            
            <p><strong>Q: Is my private key sent anywhere?</strong></p>
            <p>A: No. Your private key never leaves your device and is not transmitted over the internet. When broadcasting transactions, only the signed transaction data is sent, which does not contain your private key.</p>
            
            <p><strong>Q: Should I encrypt my wallet?</strong></p>
            <p>A: Yes, we strongly recommend encrypting your wallet with a strong password to add an additional layer of security.</p>
            
            <Subtitle>Usage Questions</Subtitle>
            <p><strong>Q: What if I forget my password?</strong></p>
            <p>A: If you forget the password used to encrypt your wallet, there is no way to recover it. This is why it's crucial to securely back up both your private key/seed phrase and your password.</p>
            
            <p><strong>Q: Can I use this wallet on multiple devices?</strong></p>
            <p>A: Yes, but you would need to import your private key on each device. Remember that each time you expose your private key to a new device, especially one connected to the internet, you increase the security risk.</p>
            
            <p><strong>Q: How do I check my wallet balance?</strong></p>
            <p>A: Since this is a cold wallet application focused on security, it doesn't directly check balances. You can check your balance by entering your public address (not your private key) on a blockchain explorer like Etherscan.</p>
            
            <Callout>
              If you have additional questions that aren't answered here, please refer to the documentation or contact support.
            </Callout>
          </Section>
        )}
        
        {activeTab === 'about' && (
          <Section>
            <Subtitle>About C-Cube</Subtitle>
            <p>C-Cube is an open-source educational wallet application designed to help users learn about cryptocurrency storage safely. Built with React and available as both a desktop application (Electron) and web application, it works across Windows, macOS, Linux, and all modern web browsers.</p>
            
            <Subtitle>Our Philosophy</Subtitle>
            <p>We believe that education should be the foundation of cryptocurrency security. By creating a tutorial wallet solution that demonstrates cold wallet functionality in a safe learning environment, we aim to teach users about security best practices without risking real funds.</p>
            
            <Quote>
              "Education is the best security. Every feature in this application has been designed to teach cryptocurrency safety in a risk-free environment."
            </Quote>
            
            <Subtitle>Technology</Subtitle>
            <List>
              <ListItem><strong>React & Modern Web Technologies</strong> - For a responsive user experience across desktop and web</ListItem>
              <ListItem><strong>Electron (Desktop)</strong> - For enhanced security and native desktop features</ListItem>
              <ListItem><strong>ethers.js</strong> - For educational blockchain wallet operations</ListItem>
              <ListItem><strong>AES Encryption</strong> - For demonstrating secure wallet storage practices</ListItem>
              <ListItem><strong>Educational Offline-First Design</strong> - To teach users about cold wallet security concepts</ListItem>
            </List>
            
            <Subtitle>Privacy Policy</Subtitle>
            <p>We don't collect any user data. All tutorial wallet information remains on your local device and is never transmitted to our servers or any third parties. This is an educational tool - your learning privacy is entirely in your hands.</p>
            
            <Subtitle>Open Source</Subtitle>
            <p>This application is open source, allowing the community to verify our security claims and contribute to improving the software. The source code is available on GitHub.</p>
            
            <Callout>
              While we strive to create the most secure application possible, security also depends on how you use this tool. Always follow the recommended security practices.
            </Callout>
            
            <Subtitle>Version</Subtitle>
            <p>C-Cube v1.0.0</p>
          </Section>
        )}
      </Card>
        </ResourcesContainer>
      </PageContent>
    </PageBackground>
  );
};

export default Resources;
