import React from 'react';
import styled from 'styled-components';
import CyFoCubeLogo from './CyFoCubeLogo';

const FooterContainer = styled.footer`
  background: #0a0a0a;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding: 60px 20px 30px;
  color: #e0e0e0;
`;

const FooterContent = styled.div`
  max-width: 1200px;
  margin: 0 auto;
`;

const FooterTop = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 40px;
  margin-bottom: 40px;

  @media (max-width: 768px) {
    grid-template-columns: 1fr;
    gap: 30px;
  }
`;

const FooterSection = styled.div`
  h4 {
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 20px;
    color: #ffffff;
  }

  ul {
    list-style: none;
    
    li {
      margin-bottom: 12px;
      
      a {
        color: #a0a0a0;
        text-decoration: none;
        font-size: 0.9rem;
        transition: color 0.3s ease;

        &:hover {
          color: #667eea;
        }
      }
    }
  }
`;

const FooterBrand = styled.div`
  display: flex;
  flex-direction: column;
  
  .logo-container {
    margin-bottom: 16px;
  }

  h3 {
    font-size: 1.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 16px;
    display: none; /* Hide text since we're using logo */
  }

  p {
    color: #a0a0a0;
    line-height: 1.6;
    font-size: 0.9rem;
  }
`;

const SocialLinks = styled.div`
  display: flex;
  gap: 16px;
  margin-top: 20px;
`;

const SocialLink = styled.a`
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #a0a0a0;
  text-decoration: none;
  transition: all 0.3s ease;
  font-size: 1.2rem;

  &:hover {
    background: rgba(102, 126, 234, 0.1);
    border-color: rgba(102, 126, 234, 0.3);
    color: #667eea;
    transform: translateY(-2px);
  }
`;

const FooterBottom = styled.div`
  padding-top: 30px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px;

  @media (max-width: 768px) {
    flex-direction: column;
    text-align: center;
  }
`;

const Copyright = styled.p`
  color: #666;
  font-size: 0.85rem;
  margin: 0;
`;

const FooterLinks = styled.div`
  display: flex;
  gap: 30px;
  
  a {
    color: #a0a0a0;
    text-decoration: none;
    font-size: 0.85rem;
    transition: color 0.3s ease;

    &:hover {
      color: #667eea;
    }
  }

  @media (max-width: 768px) {
    flex-direction: column;
    gap: 10px;
  }
`;

const Footer = () => {
  return (
    <FooterContainer className="website-page">
      <FooterContent>
        <FooterTop>
          <FooterBrand>
            <div className="logo-container">
              <CyFoCubeLogo size="normal" />
            </div>
            <h3>CyFoCube</h3>
            <p>
              The complete cybersecurity platform for the digital age. 
              Secure your crypto, protect your data, and take control of your digital future.
            </p>
            <SocialLinks>
              <SocialLink href="#" aria-label="Twitter">
                🐦
              </SocialLink>
              <SocialLink href="#" aria-label="Discord">
                💬
              </SocialLink>
              <SocialLink href="#" aria-label="GitHub">
                📁
              </SocialLink>
              <SocialLink href="#" aria-label="Telegram">
                ✈️
              </SocialLink>
            </SocialLinks>
          </FooterBrand>

          <FooterSection>
            <h4>Platform</h4>
            <ul>
              <li><a href="#">C-Cube Wallet</a></li>
              <li><a href="#">File Encryption Tool</a></li>
              <li><a href="#">Network Security Scanner</a></li>
              <li><a href="#">Blockchain Explorer</a></li>
              <li><a href="#">Digital Identity Manager</a></li>
              <li><a href="#">Secure Communications</a></li>
            </ul>
          </FooterSection>

          <FooterSection>
            <h4>Resources</h4>
            <ul>
              <li><a href="#">Documentation</a></li>
              <li><a href="#">API Reference</a></li>
              <li><a href="#">Security Guides</a></li>
              <li><a href="#">Best Practices</a></li>
              <li><a href="#">Community</a></li>
              <li><a href="#">Support</a></li>
            </ul>
          </FooterSection>

          <FooterSection>
            <h4>Company</h4>
            <ul>
              <li><a href="#">About Us</a></li>
              <li><a href="#">Blog</a></li>
              <li><a href="#">Careers</a></li>
              <li><a href="#">Press Kit</a></li>
              <li><a href="#">Contact</a></li>
            </ul>
          </FooterSection>
        </FooterTop>

        <FooterBottom>
          <Copyright>
            © 2025 CyFoCube. All rights reserved.
          </Copyright>
          <FooterLinks>
            <a href="#">Privacy Policy</a>
            <a href="#">Terms of Service</a>
            <a href="#">Cookie Policy</a>
          </FooterLinks>
        </FooterBottom>
      </FooterContent>
    </FooterContainer>
  );
};

export default Footer;