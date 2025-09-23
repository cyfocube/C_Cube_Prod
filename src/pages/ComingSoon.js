import React from 'react';
import styled from 'styled-components';

const ComingSoonContainer = styled.div`
  min-height: 100vh;
  background: rgba(102, 126, 234, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
`;

const Content = styled.div`
  text-align: center;
  color: white;
  max-width: 600px;
`;

const Icon = styled.div`
  font-size: 4rem;
  margin-bottom: 30px;
  opacity: 0.9;
`;

const Title = styled.h1`
  font-size: 3rem;
  margin-bottom: 20px;
  font-weight: 700;
  font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

  @media (max-width: 768px) {
    font-size: 2.5rem;
  }
`;

const Subtitle = styled.h2`
  font-size: 1.5rem;
  margin-bottom: 30px;
  opacity: 0.9;
  font-weight: 400;
  font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

  @media (max-width: 768px) {
    font-size: 1.3rem;
  }
`;

const Description = styled.p`
  font-size: 1.2rem;
  line-height: 1.6;
  margin-bottom: 40px;
  opacity: 0.8;
  font-weight: 400;

  @media (max-width: 768px) {
    font-size: 1.1rem;
  }
`;

const FeaturesList = styled.div`
  text-align: left;
  margin: 40px 0;
  background: rgba(255, 255, 255, 0.1);
  padding: 30px;
  border-radius: 12px;
  backdrop-filter: blur(10px);
`;

const FeatureItem = styled.div`
  display: flex;
  align-items: center;
  margin-bottom: 15px;
  font-size: 1.1rem;

  &:last-child {
    margin-bottom: 0;
  }
`;

const FeatureIcon = styled.span`
  margin-right: 15px;
  font-size: 1.3rem;
`;

const BackButton = styled.button`
  background: rgba(255, 255, 255, 0.2);
  color: white;
  border: 2px solid rgba(255, 255, 255, 0.3);
  padding: 12px 24px;
  border-radius: 8px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);

  &:hover {
    background: rgba(255, 255, 255, 0.3);
    border-color: rgba(255, 255, 255, 0.5);
    transform: translateY(-2px);
  }
`;

const NotifyButton = styled.button`
  background: white;
  color: #667eea;
  border: none;
  padding: 12px 24px;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-left: 15px;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(255, 255, 255, 0.3);
  }

  @media (max-width: 768px) {
    margin-left: 0;
    margin-top: 15px;
  }
`;

const ButtonContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  gap: 15px;

  @media (max-width: 768px) {
    flex-direction: column;
  }
`;

const ComingSoon = ({ onNavigate }) => {
  const upcomingFeatures = [
    { icon: '🚀', text: 'Advanced educational simulations' },
    { icon: '🔍', text: 'Real-time market analysis tools' },
    { icon: '📊', text: 'Interactive learning dashboards' },
    { icon: '🛡️', text: 'Enhanced security features' },
    { icon: '🌐', text: 'Multi-network support' },
    { icon: '👥', text: 'Community learning features' }
  ];

  const handleNotifyMe = () => {
    alert('Thank you for your interest! We\'ll notify you when this feature becomes available.');
  };

  return (
    <ComingSoonContainer className="website-page">
      <ContentWrapper>
        <IconContainer>
          <Icon>�</Icon>
        </IconContainer>
        <Title>Coming Soon</Title>
        <Description>
          This exciting new feature is currently under development. 
          Stay tuned for updates as we continue to expand the CyFoCube ecosystem.
        </Description>
        <FeaturesList>
          <FeatureItem>🔐 Advanced encryption capabilities</FeatureItem>
          <FeatureItem>🛡️ Enhanced security protocols</FeatureItem>
          <FeatureItem>⚡ Lightning-fast performance</FeatureItem>
          <FeatureItem>🎯 User-friendly interface</FeatureItem>
        </FeaturesList>
        <NotifySection>
          <NotifyTitle>Get Notified</NotifyTitle>
          <NotifyText>
            Want to be the first to know when this feature launches?
          </NotifyText>
          <EmailInput placeholder="Enter your email address" />
          <NotifyButton>Notify Me</NotifyButton>
        </NotifySection>
      </ContentWrapper>
    </ComingSoonContainer>
  );
};

export default ComingSoon;