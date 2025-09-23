import React, { useState } from 'react';
import styled from 'styled-components';

const HeaderContainer = styled.header`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: rgba(10, 10, 10, 0.95);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.3s ease;
`;

const HeaderContent = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: space-between;
`;

const Logo = styled.div`
  display: flex;
  align-items: center;
  cursor: pointer;
  transition: opacity 0.3s ease;

  &:hover {
    opacity: 0.8;
  }
`;

const LogoText = styled.span`
  font-size: 1.8rem;
  font-weight: 700;
  background: linear-gradient(135deg, #667eea, #764ba2);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-decoration: none;
`;

const HeaderContent = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 70px;
`;

const Logo = styled.div`
  display: flex;
  align-items: center;
  cursor: pointer;
`;

const LogoText = styled.span`
  font-size: 1.8rem;
  font-weight: 700;
  color: white;
  text-decoration: none;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
`;

const Nav = styled.nav`
  display: flex;
  align-items: center;
  gap: 30px;

  @media (max-width: 768px) {
    display: ${props => props.isOpen ? 'flex' : 'none'};
    position: absolute;
    top: 70px;
    left: 0;
    right: 0;
    background: white;
    flex-direction: column;
    padding: 20px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    gap: 20px;
  }
`;

const NavItem = styled.button`
  background: none;
  border: none;
  color: white;
  cursor: pointer;
  padding: 10px 15px;
  margin: 0 5px;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 500;
  transition: all 0.3s ease;
  position: relative;

  &:hover {
    background: rgba(255, 255, 255, 0.1);
    transform: translateY(-1px);
  }

  &.active {
    background: rgba(255, 255, 255, 0.2);
  }

  @media (max-width: 768px) {
    margin: 5px 0;
    padding: 12px 20px;
    text-align: left;
    width: 100%;
  }
`;

const DropdownContainer = styled.div`
  position: relative;
`;

const DropdownContent = styled.div`
  position: absolute;
  top: 100%;
  left: 0;
  min-width: 200px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  padding: 10px 0;
  z-index: 1001;
  display: ${props => props.isOpen ? 'block' : 'none'};

  @media (max-width: 768px) {
    position: static;
    box-shadow: none;
    background: #f8f9fa;
    border-radius: 6px;
    margin-top: 10px;
  }
`;

const DropdownItem = styled.button`
  width: 100%;
  padding: 12px 20px;
  text-align: left;
  background: none;
  border: none;
  color: #2c3e50;
  font-size: 0.95rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
  display: flex;
  align-items: center;
  gap: 10px;

  &:hover {
    background: #f8f9fa;
  }
`;

const DropdownIcon = styled.span`
  font-size: 1.1rem;
`;

const DropdownArrow = styled.span`
  margin-left: 5px;
  font-size: 0.8rem;
  transform: ${props => props.isOpen ? 'rotate(180deg)' : 'rotate(0deg)'};
  transition: transform 0.3s ease;
`;

const MobileMenuButton = styled.button`
  display: none;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #2c3e50;

  @media (max-width: 768px) {
    display: block;
  }
`;

const GetStartedButton = styled.button`
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 6px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
  }
`;

const Header = ({ currentPage, onNavigate }) => {
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const handleResourceClick = (resource) => {
    setDropdownOpen(false);
    setMobileMenuOpen(false);
    onNavigate(resource);
  };

  const handleNavClick = (page) => {
    setMobileMenuOpen(false);
    setDropdownOpen(false);
    onNavigate(page);
  };

  const handleGetStarted = () => {
    setMobileMenuOpen(false);
    setDropdownOpen(false);
    onNavigate('c-cube');
  };

  return (
    <HeaderContainer className="website-page">
      <HeaderContent>
        <Logo onClick={() => handleNavClick('landing')}>
          <LogoText>CyFoCube</LogoText>
        </Logo>

        <Nav isOpen={mobileMenuOpen}>
          <NavItem
            className={currentPage === 'landing' ? 'active' : ''}
            onClick={() => handleNavClick('landing')}
          >
            Home
          </NavItem>

          <NavItem
            className={currentPage === 'content' ? 'active' : ''}
            onClick={() => handleNavClick('content')}
          >
            Learn
          </NavItem>

          <DropdownContainer>
            <NavItem
              onClick={() => setDropdownOpen(!dropdownOpen)}
              className={['c-cube', 'coming-soon'].includes(currentPage) ? 'active' : ''}
            >
              Apps
              <DropdownArrow isOpen={dropdownOpen}>▼</DropdownArrow>
            </NavItem>
            <DropdownContent isOpen={dropdownOpen}>
              <DropdownItem onClick={() => handleResourceClick('c-cube')}>
                <DropdownIcon>🔐</DropdownIcon>
                C-Cube Wallet
              </DropdownItem>
              <DropdownItem onClick={() => handleResourceClick('coming-soon')}>
                <DropdownIcon>📊</DropdownIcon>
                DeFi Simulator <span style={{color: '#999', fontSize: '0.8rem'}}>(Coming Soon)</span>
              </DropdownItem>
              <DropdownItem onClick={() => handleResourceClick('coming-soon')}>
                <DropdownIcon>🎓</DropdownIcon>
                Blockchain Academy <span style={{color: '#999', fontSize: '0.8rem'}}>(Coming Soon)</span>
              </DropdownItem>
              <DropdownItem onClick={() => handleResourceClick('coming-soon')}>
                <DropdownIcon>📈</DropdownIcon>
                Portfolio Tracker <span style={{color: '#999', fontSize: '0.8rem'}}>(Coming Soon)</span>
              </DropdownItem>
              <DropdownItem onClick={() => handleResourceClick('coming-soon')}>
                <DropdownIcon>🔍</DropdownIcon>
                Security Analyzer <span style={{color: '#999', fontSize: '0.8rem'}}>(Coming Soon)</span>
              </DropdownItem>
              <DropdownItem onClick={() => handleResourceClick('coming-soon')}>
                <DropdownIcon>🌐</DropdownIcon>
                Network Explorer <span style={{color: '#999', fontSize: '0.8rem'}}>(Coming Soon)</span>
              </DropdownItem>
            </DropdownContent>
          </DropdownContainer>

          <NavItem
            className={currentPage === 'faq' ? 'active' : ''}
            onClick={() => handleNavClick('faq')}
          >
            FAQ
          </NavItem>

          <GetStartedButton onClick={handleGetStarted}>
            Get Started
          </GetStartedButton>
        </Nav>

        <MobileMenuButton onClick={() => setMobileMenuOpen(!mobileMenuOpen)}>
          ☰
        </MobileMenuButton>
      </HeaderContent>
    </HeaderContainer>
  );
};

export default Header;