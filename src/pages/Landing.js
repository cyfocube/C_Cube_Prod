import React from 'react';
import styled from 'styled-components';
import Footer from '../components/Footer';

const LandingContainer = styled.div`
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
`;

const HeroSection = styled.section`
  padding: 100px 20px;
  text-align: center;
  max-width: 1200px;
  margin: 0 auto;
`;

const HeroTitle = styled.h1`
  font-size: 3.5rem;
  font-weight: 700;
  margin-bottom: 20px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);

  @media (max-width: 768px) {
    font-size: 2.5rem;
  }
`;

const HeroSubtitle = styled.p`
  font-size: 1.4rem;
  margin-bottom: 40px;
  opacity: 0.9;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
  font-weight: 400;
  line-height: 1.6;

  @media (max-width: 768px) {
    font-size: 1.2rem;
  }
`;

const AppsSection = styled.section`
  padding: 80px 20px;
  background: white;
  color: #333;
`;

const SectionTitle = styled.h2`
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 20px;
  color: #2c3e50;
`;

const SectionSubtitle = styled.p`
  text-align: center;
  font-size: 1.2rem;
  margin-bottom: 60px;
  color: #7f8c8d;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
`;

const AppsGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  max-width: 1200px;
  margin: 0 auto;
`;

const AppCard = styled.div`
  background: white;
  border-radius: 12px;
  padding: 30px;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid #e1e8ed;

  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
  }
`;

const AppIcon = styled.div`
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
  font-size: 1.5rem;
`;

const AppTitle = styled.h3`
  font-size: 1.5rem;
  margin-bottom: 15px;
  color: #2c3e50;
`;

const AppDescription = styled.p`
  color: #7f8c8d;
  line-height: 1.6;
  margin-bottom: 20px;
`;

const AppButton = styled.button`
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  transition: opacity 0.3s ease;

  &:hover {
    opacity: 0.9;
  }

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
`;

const ComingSoonBadge = styled.span`
  background: #f39c12;
  color: white;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
  margin-left: 10px;
`;

const Landing = ({ onAppSelect }) => {
  return (
    <LandingContainer className="website-page">
      <HeroSection>
        <HeroTitle>Welcome to CyFoCube</HeroTitle>
        <HeroSubtitle>
          Your Complete Cybersecurity & Finance Platform
        </HeroSubtitle>
        <p style={{ fontSize: '1.1rem', marginBottom: '40px', opacity: 0.8 }}>
          Secure. Private. Powerful. Experience the future of digital asset management 
          with our suite of cutting-edge applications.
        </p>
      </HeroSection>

      <AppsSection>
        <SectionTitle>Educational Applications</SectionTitle>
        <SectionSubtitle>
          Explore our collection of educational blockchain applications designed to help you learn cryptocurrency and blockchain technology safely.
        </SectionSubtitle>

        <AppsGrid>
          <AppCard>
            <AppIcon>🔒</AppIcon>
            <AppTitle>C-Cube Tutorial Wallet</AppTitle>
            <AppDescription>
              Learn cryptocurrency wallet management safely with our educational cold wallet simulator. 
              Practice transactions, understand security, and master blockchain interactions without risking real funds.
            </AppDescription>
            <AppButton onClick={() => onAppSelect('ccube-wallet')}>
              Launch Tutorial Wallet
            </AppButton>
          </AppCard>

          <AppCard>
            <AppIcon>📊</AppIcon>
            <AppTitle>
              Portfolio Tracker
              <ComingSoonBadge>Coming Soon</ComingSoonBadge>
            </AppTitle>
            <AppDescription>
              Track and analyze cryptocurrency portfolios with advanced analytics. 
              Learn about DeFi protocols, yield farming, and investment strategies in a safe environment.
            </AppDescription>
            <AppButton disabled>
              Coming Soon
            </AppButton>
          </AppCard>

          <AppCard>
            <AppIcon>🎓</AppIcon>
            <AppTitle>
              Blockchain Academy
              <ComingSoonBadge>Coming Soon</ComingSoonBadge>
            </AppTitle>
            <AppDescription>
              Interactive courses and tutorials covering blockchain fundamentals, smart contracts, 
              and cryptocurrency concepts. Learn at your own pace with hands-on exercises.
            </AppDescription>
            <AppButton disabled>
              Coming Soon
            </AppButton>
          </AppCard>

          <AppCard>
            <AppIcon>🔄</AppIcon>
            <AppTitle>
              DeFi Simulator
              <ComingSoonBadge>Coming Soon</ComingSoonBadge>
            </AppTitle>
            <AppDescription>
              Experience decentralized finance protocols safely. Practice lending, borrowing, 
              and yield farming with simulated tokens to understand DeFi mechanics.
            </AppDescription>
            <AppButton disabled>
              Coming Soon
            </AppButton>
          </AppCard>

          <AppCard>
            <AppIcon>🛡️</AppIcon>
            <AppTitle>
              Security Trainer
              <ComingSoonBadge>Coming Soon</ComingSoonBadge>
            </AppTitle>
            <AppDescription>
              Learn cryptocurrency security best practices through interactive scenarios. 
              Understand wallet security, phishing protection, and safe trading practices.
            </AppDescription>
            <AppButton disabled>
              Coming Soon
            </AppButton>
          </AppCard>

          <AppCard>
            <AppIcon>⚡</AppIcon>
            <AppTitle>
              Lightning Network Lab
              <ComingSoonBadge>Coming Soon</ComingSoonBadge>
            </AppTitle>
            <AppDescription>
              Explore Bitcoin's Lightning Network with educational tools and simulations. 
              Learn about payment channels, routing, and instant Bitcoin transactions.
            </AppDescription>
            <AppButton disabled>
              Coming Soon
            </AppButton>
          </AppCard>
        </AppsGrid>
      </AppsSection>
      <Footer />
    </LandingContainer>
  );
};

export default Landing;