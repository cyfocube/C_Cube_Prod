import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import styled from 'styled-components';
import { createSectionId } from '../utils/scrollUtils';

const NavigationContainer = styled.div`
  position: fixed;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 100;
  background: rgba(10, 10, 10, 0.9);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 12px 8px;
  min-width: 180px;

  @media (max-width: 1024px) {
    display: none;
  }
`;

const NavigationTitle = styled.div`
  color: #a68660;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 8px;
  padding: 0 8px;
  text-align: center;
`;

const SectionLink = styled(Link)`
  display: block;
  color: ${props => props.active ? '#ffffff' : '#e0e0e0'};
  background: ${props => props.active ? 'linear-gradient(135deg, #a68660, #000000)' : 'transparent'};
  text-decoration: none;
  padding: 8px 12px;
  margin: 2px 0;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 500;
  transition: all 0.3s ease;
  border-left: 2px solid ${props => props.active ? '#a68660' : 'transparent'};

  &:hover {
    background: ${props => props.active ? 'linear-gradient(135deg, #a68660, #000000)' : 'rgba(255, 255, 255, 0.1)'};
    color: white;
    border-left-color: #a68660;
    transform: translateX(2px);
  }
`;

const SectionNavigation = ({ sections, currentPage = 'learn' }) => {
  const location = useLocation();
  const currentHash = location.hash.substring(1);

  return (
    <NavigationContainer>
      <NavigationTitle>Sections</NavigationTitle>
      {sections.map(section => {
        const sectionId = typeof section === 'string' ? createSectionId(section) : section.id;
        const sectionLabel = typeof section === 'string' ? section : section.label;
        const isActive = currentHash === sectionId;

        return (
          <SectionLink
            key={sectionId}
            to={`${location.pathname}#${sectionId}`}
            active={isActive}
          >
            {sectionLabel}
          </SectionLink>
        );
      })}
    </NavigationContainer>
  );
};

export default SectionNavigation;