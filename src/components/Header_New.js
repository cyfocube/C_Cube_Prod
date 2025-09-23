import React, { useState } from 'react';
import styled from 'styled-components';
import CyFoCubeLogo from './CyFoCubeLogo';

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
  position: absolute;
  left: 0px;
  z-index: 10;
`;

const LogoText = styled.span`
  /* Removed - now handled by CyFoCubeLogo component */
`;

const Nav = styled.nav`
  display: flex;
  align-items: center;
  gap: 20px;

  @media (max-width: 768px) {
    display: ${props => props.isOpen ? 'flex' : 'none'};
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: rgba(10, 10, 10, 0.98);
    backdrop-filter: blur(20px);
    flex-direction: column;
    padding: 20px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
  }
`;

const NavItem = styled.button`
  background: none;
  border: none;
  color: #e0e0e0;
  cursor: pointer;
  padding: 10px 16px;
  margin: 0;
  border-radius: 8px;
  font-size: 0.95rem;
  font-weight: 500;
  transition: all 0.3s ease;
  position: relative;

  &:hover {
    background: linear-gradient(135deg, #8b7355, #1a1a1a);
    color: white;
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(139, 115, 85, 0.1);
  }

  &.active {
    background: linear-gradient(135deg, #a68660, #000000);
    color: white;
  }

  @media (max-width: 768px) {
    width: 100%;
    text-align: left;
    padding: 12px 16px;
  }
`;

const AppsDropdown = styled.div`
  position: relative;
`;

const AppsDropdownMenu = styled.div`
  position: absolute;
  top: 100%;
  right: 0;
  background: rgba(10, 10, 10, 0.98);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 12px 0;
  min-width: 280px;
  margin-top: 8px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);

  @media (max-width: 768px) {
    position: static;
    background: rgba(255, 255, 255, 0.05);
    margin: 8px 0;
    box-shadow: none;
  }
`;

const DropdownItem = styled.button`
  width: 100%;
  background: none;
  border: none;
  color: #e0e0e0;
  cursor: pointer;
  padding: 8px 16px;
  text-align: left;
  font-size: 0.9rem;
  font-weight: 400;
  transition: all 0.3s ease;
  margin: 2px 8px;
  border-radius: 8px;
  width: calc(100% - 16px);

  &:hover {
    background: linear-gradient(135deg, #8b7355, #1a1a1a);
    color: white;
  }

  &.available {
    color: #a68660;
    font-weight: 500;
  }

  &.coming-soon {
    opacity: 0.6;
  }
`;

const MobileMenuButton = styled.button`
  display: none;
  background: none;
  border: none;
  color: #e0e0e0;
  font-size: 1.5rem;
  cursor: pointer;
  padding: 8px;
  border-radius: 6px;
  transition: all 0.3s ease;

  &:hover {
    background: rgba(255, 255, 255, 0.1);
  }

  @media (max-width: 768px) {
    display: block;
  }
`;

const LaunchAppButton = styled.button`
  background: linear-gradient(135deg, #8b7355, #1a1a1a);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 8px rgba(139, 115, 85, 0.15);
    background: linear-gradient(135deg, #a68660, #000000);
  }

  @media (max-width: 768px) {
    width: 100%;
    margin-top: 10px;
  }
`;

const Header = ({ currentPage, setCurrentPage, onNavigate }) => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [showAppsDropdown, setShowAppsDropdown] = useState(false);

  const handleNavClick = (page) => {
    setMobileMenuOpen(false);
    setShowAppsDropdown(false);
    if (onNavigate) onNavigate(page);
    if (setCurrentPage) setCurrentPage(page);
  };

  const handleLaunchApp = () => {
    setMobileMenuOpen(false);
    setShowAppsDropdown(false);
    if (onNavigate) onNavigate('c-cube');
  };

  return (
    <HeaderContainer className="website-page">
      <HeaderContent>
        <Logo>
          <CyFoCubeLogo onClick={() => handleNavClick('landing')} />
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
          <NavItem
            className={currentPage === 'faq' ? 'active' : ''}
            onClick={() => handleNavClick('faq')}
          >
            FAQ
          </NavItem>

          <AppsDropdown>
            <NavItem onClick={() => setShowAppsDropdown(!showAppsDropdown)}>
              Apps ▼
            </NavItem>
            {showAppsDropdown && (
              <AppsDropdownMenu>
                <DropdownItem 
                  className="available"
                  onClick={() => handleNavClick('c-cube')}
                >
                  C-Cube Wallet
                </DropdownItem>
                <DropdownItem 
                  className="coming-soon"
                  onClick={() => handleNavClick('coming-soon')}
                >
                  File Encryption Tool
                </DropdownItem>
                <DropdownItem 
                  className="coming-soon"
                  onClick={() => handleNavClick('coming-soon')}
                >
                  Network Security Scanner
                </DropdownItem>
                <DropdownItem 
                  className="coming-soon"
                  onClick={() => handleNavClick('coming-soon')}
                >
                  Blockchain Explorer
                </DropdownItem>
                <DropdownItem 
                  className="coming-soon"
                  onClick={() => handleNavClick('coming-soon')}
                >
                  Digital Identity Manager
                </DropdownItem>
                <DropdownItem 
                  className="coming-soon"
                  onClick={() => handleNavClick('coming-soon')}
                >
                  Secure Communication Hub
                </DropdownItem>
              </AppsDropdownMenu>
            )}
          </AppsDropdown>

          <LaunchAppButton onClick={handleLaunchApp}>
            Launch App
          </LaunchAppButton>
        </Nav>

        <MobileMenuButton onClick={() => setMobileMenuOpen(!mobileMenuOpen)}>
          ☰
        </MobileMenuButton>
      </HeaderContent>
    </HeaderContainer>
  );
};

export default Header;