import React from 'react';
import styled from 'styled-components';
import Footer from '../components/Footer_New';

const ContentContainer = styled.div`
  min-height: 100vh;
  background: rgba(26, 26, 46, 0.7);
  position: relative;
  overflow-x: hidden;
  padding: 80px 20px 40px;
  color: #e0e0e0;
  
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="%23ffffff10" stroke-width="0.5"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
    opacity: 0.3;
    pointer-events: none;
    z-index: 0;
  }
`;

const ContentCard = styled.div`
  max-width: 800px;
  margin: 0 auto;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  padding: 40px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
  position: relative;
  z-index: 1;
`;

const Header = styled.div`
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 60px 40px;
  text-align: center;
`;

const Title = styled.h1`
  font-size: 2.5rem;
  margin-bottom: 30px;
  text-align: center;
  background: linear-gradient(135deg, #4ade80, #06b6d4);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 700;
  letter-spacing: -0.5px;
`;

const Subtitle = styled.p`
  font-size: 1.2rem;
  opacity: 0.9;
  max-width: 600px;
  margin: 0 auto;
  font-weight: 400;
  line-height: 1.6;
`;

const ContentBody = styled.div`
  padding: 60px 40px;

  @media (max-width: 768px) {
    padding: 40px 20px;
  }
`;

const Section = styled.section`
  margin-bottom: 50px;

  &:last-child {
    margin-bottom: 0;
  }
`;

const SectionTitle = styled.h2`
  font-size: 2rem;
  color: #e0e0e0;
  margin-bottom: 20px;
  border-bottom: 3px solid #4ade80;
  padding-bottom: 10px;
  font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  font-weight: 600;
`;

const SectionContent = styled.div`
  font-size: 1.1rem;
  line-height: 1.8;
  color: #b0b0b0;

  p {
    margin: 15px 0;
  }

  ul, ol {
    margin: 15px 0;
    padding-left: 25px;
  }

  li {
    margin: 8px 0;
  }

  strong {
    color: #e0e0e0;
    font-weight: 600;
  }
`;

const ContentText = styled.div`
  font-size: 1.1rem;
  line-height: 1.8;
  color: #b0b0b0;
  margin-bottom: 20px;

  h2 {
    color: #e0e0e0;
    margin: 30px 0 15px 0;
    font-size: 1.5rem;
    font-weight: 600;
  }

  h3 {
    color: #d0d0d0;
    margin: 25px 0 10px 0;
    font-size: 1.2rem;
    font-weight: 500;
  }

  ul, ol {
    margin: 15px 0;
    padding-left: 25px;
  }

  li {
    margin: 8px 0;
  }

  p {
    margin: 15px 0;
  }

  strong {
    color: #e0e0e0;
    font-weight: 600;
  }

  code {
    background: rgba(255, 255, 255, 0.1);
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'Share Tech Mono', monospace;
    color: #4ade80;
  }

  blockquote {
    border-left: 3px solid #4ade80;
    padding-left: 20px;
    margin: 20px 0;
    background: rgba(74, 222, 128, 0.1);
    padding: 15px 20px;
    border-radius: 8px;
  }
`;

const HighlightBox = styled.div`
  background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
  border-left: 4px solid #667eea;
  padding: 25px;
  margin: 30px 0;
  border-radius: 8px;
`;

const Grid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin: 30px 0;
`;

const Card = styled.div`
  background: #f8f9fa;
  padding: 25px;
  border-radius: 8px;
  border: 1px solid #e1e8ed;
`;

const CardTitle = styled.h3`
  color: #2c3e50;
  margin-bottom: 15px;
  font-size: 1.3rem;
`;

const CardContent = styled.p`
  color: #666;
  line-height: 1.6;
`;

const Content = () => {
  return (
    <>
      <ContentContainer className="website-page">
        <ContentCard>
          <Header>
            <Title>Blockchain Education Hub</Title>
            <Subtitle>
              Comprehensive educational content about blockchain technology, cryptocurrency, and decentralized finance
            </Subtitle>
          </Header>

          <ContentBody>
            <Section>
            <SectionTitle>Understanding Blockchain Technology</SectionTitle>
            <SectionContent>
              <p>
                Blockchain technology represents a paradigm shift in how we think about data storage, 
                verification, and trust. At its core, blockchain is a distributed ledger technology 
                that maintains a continuously growing list of records, called blocks, which are linked 
                and secured using cryptography.
              </p>
              
              <HighlightBox>
                <strong>Key Principle:</strong> Blockchain eliminates the need for trusted intermediaries 
                by creating a system where trust is built into the technology itself through 
                cryptographic proof and consensus mechanisms.
              </HighlightBox>

              <p>
                Each block contains a cryptographic hash of the previous block, a timestamp, and 
                transaction data. This design makes the blockchain inherently resistant to modification 
                of data, as changing any information in a block would require changing all subsequent blocks.
              </p>
            </SectionContent>
          </Section>

          <Section>
            <SectionTitle>Cryptocurrency Fundamentals</SectionTitle>
            <SectionContent>
              <p>
                Cryptocurrency is a digital or virtual form of currency that uses cryptography for security. 
                Unlike traditional currencies issued by governments (fiat currencies), cryptocurrencies 
                operate on decentralized networks based on blockchain technology.
              </p>

              <Grid>
                <Card>
                  <CardTitle>🔐 Security</CardTitle>
                  <CardContent>
                    Cryptocurrencies use advanced cryptographic techniques to secure transactions 
                    and control the creation of new units.
                  </CardContent>
                </Card>
                <Card>
                  <CardTitle>🌐 Decentralization</CardTitle>
                  <CardContent>
                    No central authority controls the network. Instead, it's maintained by 
                    a distributed network of computers (nodes).
                  </CardContent>
                </Card>
                <Card>
                  <CardTitle>🔍 Transparency</CardTitle>
                  <CardContent>
                    All transactions are recorded on a public ledger that anyone can verify, 
                    providing unprecedented transparency.
                  </CardContent>
                </Card>
                <Card>
                  <CardTitle>💫 Immutability</CardTitle>
                  <CardContent>
                    Once confirmed, transactions cannot be reversed or altered, providing 
                    a permanent and tamper-proof record.
                  </CardContent>
                </Card>
              </Grid>
            </SectionContent>
          </Section>

          <Section>
            <SectionTitle>Wallet Security Best Practices</SectionTitle>
            <SectionContent>
              <p>
                Proper wallet security is crucial for protecting your cryptocurrency assets. 
                Understanding different types of wallets and security measures can help you 
                make informed decisions about storing and managing your digital assets.
              </p>

              <ul>
                <li><strong>Cold Storage:</strong> Keep the majority of your funds in offline wallets that are not connected to the internet</li>
                <li><strong>Hot Wallets:</strong> Use online wallets only for small amounts needed for regular transactions</li>
                <li><strong>Backup Recovery Phrases:</strong> Always backup your seed phrases and store them securely offline</li>
                <li><strong>Multi-Signature:</strong> Consider using multi-signature wallets for additional security layers</li>
                <li><strong>Regular Updates:</strong> Keep your wallet software updated to the latest version</li>
                <li><strong>Verify Addresses:</strong> Always double-check recipient addresses before sending transactions</li>
              </ul>

              <HighlightBox>
                <strong>Remember:</strong> The C-cube ecosystem provides safe learning environments 
                where you can practice these concepts without risking real funds. Always use educational 
                tools to understand these principles before managing real cryptocurrency.
              </HighlightBox>
            </SectionContent>
          </Section>

          <Section>
            <SectionTitle>Decentralized Finance (DeFi)</SectionTitle>
            <SectionContent>
              <p>
                Decentralized Finance, or DeFi, refers to financial services built on blockchain 
                technology that operate without traditional intermediaries like banks or brokers. 
                DeFi protocols use smart contracts to automate financial services and create 
                new financial products.
              </p>

              <p>
                Common DeFi applications include:
              </p>

              <ul>
                <li><strong>Decentralized Exchanges (DEXs):</strong> Trade cryptocurrencies directly with other users</li>
                <li><strong>Lending Protocols:</strong> Lend your crypto assets to earn interest or borrow against collateral</li>
                <li><strong>Yield Farming:</strong> Provide liquidity to earn rewards in the form of additional tokens</li>
                <li><strong>Synthetic Assets:</strong> Create digital representations of real-world assets</li>
                <li><strong>Insurance Protocols:</strong> Protect your DeFi investments against smart contract risks</li>
              </ul>

              <p>
                While DeFi offers exciting opportunities, it also comes with risks including 
                smart contract vulnerabilities, impermanent loss, and regulatory uncertainty. 
                Education and careful research are essential before participating in DeFi protocols.
              </p>
            </SectionContent>
          </Section>

          <Section>
            <SectionTitle>Getting Started Safely</SectionTitle>
            <SectionContent>
              <p>
                The world of blockchain and cryptocurrency can seem overwhelming at first, 
                but with the right approach and educational tools, anyone can learn to 
                navigate this space safely and confidently.
              </p>

              <HighlightBox>
                <strong>Educational First Approach:</strong> Always start with educational tools 
                and simulations before using real cryptocurrency. The C-cube ecosystem is 
                designed to provide safe learning environments for all experience levels.
              </HighlightBox>

              <p>
                Our educational applications are designed to help you:
              </p>

              <ul>
                <li>Understand fundamental concepts through hands-on practice</li>
                <li>Learn security best practices in a risk-free environment</li>
                <li>Explore advanced topics like DeFi and smart contracts safely</li>
                <li>Build confidence before working with real cryptocurrency</li>
                <li>Stay updated with the latest developments in blockchain technology</li>
              </ul>
            </SectionContent>
          </Section>
        </ContentBody>
      </ContentCard>
      </ContentContainer>
      <Footer />
    </>
  );
};

export default Content;