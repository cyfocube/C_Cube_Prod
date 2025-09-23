import React from 'react';
import styled from 'styled-components';

const CommunityContainer = styled.div`
  min-height: 100vh;
  background: transparent;
  color: #e0e0e0;
  overflow-x: hidden;
`;

const HeroSection = styled.section`
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(26, 26, 46, 0.7);
  position: relative;
  overflow: hidden;
  
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="%23ffffff10" stroke-width="0.5"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
    opacity: 0.3;
  }
`;

const HeroContent = styled.div`
  max-width: none;
  width: 100%;
  margin: 0;
  padding-left: 40px;
  padding-right: 20px;
  text-align: left;
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  min-height: 100vh;
  justify-content: flex-start;
  
  @media (max-width: 768px) {
    text-align: center;
    padding-left: 20px;
  }
`;

const TextContainer = styled.div`
  flex: none;
  max-width: 70%;
  padding: 0;
  margin: 0;
  
  @media (max-width: 768px) {
    max-width: 100%;
    text-align: center;
  }
`;

const HeroTitle = styled.h1`
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 24px;
  background: linear-gradient(135deg, #ffffff 0%, #a0a0a0 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  line-height: 1.1;
  white-space: nowrap;
  overflow: visible;

  @media (max-width: 768px) {
    font-size: 1.2rem;
  }
`;

const HeroSubtitle = styled.p`
  font-size: 1.1rem;
  margin-bottom: 40px;
  opacity: 0.8;
  max-width: 600px;
  line-height: 1.6;
  
  @media (max-width: 768px) {
    margin-left: auto;
    margin-right: auto;
  }
`;

const HeroStats = styled.div`
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 80px;
  max-width: 800px;
  
  @media (max-width: 768px) {
    margin-left: auto;
    margin-right: auto;
    max-width: 100%;
    gap: 15px;
  }
`;

const StatCard = styled.div`
  text-align: center;
  padding: 3px;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  transition: transform 0.3s ease;

  &:hover {
    transform: translateY(-4px);
  }
`;

const StatNumber = styled.div`
  font-size: 1.2rem;
  font-weight: 600;
  color: #667eea;
  margin-bottom: 0px;
  text-align: center;
  white-space: nowrap;
`;

const StatLabel = styled.div`
  font-size: 0.8rem;
  opacity: 0.7;
  text-transform: uppercase;
  letter-spacing: 1px;
`;

const SocialIcons = styled.div`
  display: flex;
  justify-content: center;
  gap: 12px;
  margin-top: 8px;
`;

const SocialIcon = styled.a`
  color: white;
  font-size: 1.2rem;
  transition: color 0.3s ease, transform 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  
  &:hover {
    color: #667eea;
    transform: scale(1.1);
  }
  
  svg {
    width: 20px;
    height: 20px;
    fill: currentColor;
  }
`;

const ContactIcon = styled.div`
  display: flex;
  justify-content: center;
  margin-top: 8px;
  color: white;
  
  svg {
    width: 20px;
    height: 20px;
    fill: currentColor;
  }
`;

const Community = ({ onNavigate }) => {
  return (
    <CommunityContainer className="website-page">
      <HeroSection>
        <HeroContent>
          <TextContainer>
            <HeroTitle>Join Our Security Community</HeroTitle>
            <HeroSubtitle>
              Connect with blockchain security enthusiasts, share knowledge, and grow together in a supportive environment. 
              Build lasting relationships while advancing your security expertise with our global community. Our community is growing 
              and we implore everyone to join this wave of security consciousness in web3.
            </HeroSubtitle>
            
            <HeroStats>
              <StatCard>
                <StatNumber>Growing Members</StatNumber>
                <SocialIcons>
                  <SocialIcon href="https://twitter.com" target="_blank" rel="noopener noreferrer">
                    <svg viewBox="0 0 24 24">
                      <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                    </svg>
                  </SocialIcon>
                  <SocialIcon href="https://facebook.com" target="_blank" rel="noopener noreferrer">
                    <svg viewBox="0 0 24 24">
                      <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                    </svg>
                  </SocialIcon>
                  <SocialIcon href="https://instagram.com" target="_blank" rel="noopener noreferrer">
                    <svg viewBox="0 0 24 24">
                      <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                    </svg>
                  </SocialIcon>
                  <SocialIcon href="https://linkedin.com" target="_blank" rel="noopener noreferrer">
                    <svg viewBox="0 0 24 24">
                      <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                    </svg>
                  </SocialIcon>
                </SocialIcons>
              </StatCard>
              <StatCard>
                <StatNumber>Contact the team</StatNumber>
                <ContactIcon>
                  <svg viewBox="0 0 24 24">
                    <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
                  </svg>
                </ContactIcon>
              </StatCard>
              <StatCard>
                <StatNumber>Share</StatNumber>
                <ContactIcon>
                  <svg viewBox="0 0 24 24">
                    <path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.50-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92s2.92-1.31 2.92-2.92-1.31-2.92-2.92-2.92z"/>
                  </svg>
                </ContactIcon>
              </StatCard>
            </HeroStats>
          </TextContainer>
        </HeroContent>
      </HeroSection>
    </CommunityContainer>
  );
};

export default Community;