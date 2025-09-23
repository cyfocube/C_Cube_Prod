import React from 'react';
import styled from 'styled-components';
import Footer from '../components/Footer_New';

const AboutContainer = styled.div`
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
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;

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
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
  
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
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
`;

const StatLabel = styled.div`
  font-size: 0.8rem;
  opacity: 0.7;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
`;

const MissionSection = styled.section`
  padding: 120px 20px;
  background: #0a0a0a;
`;

const SectionTitle = styled.h2`
  font-size: 3rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 60px;
  background: linear-gradient(135deg, #ffffff 0%, #a0a0a0 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
`;

const MissionGrid = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 40px;
`;

const MissionCard = styled.div`
  padding: 40px;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;

  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, #667eea, #764ba2);
  }

  &:hover {
    transform: translateY(-8px);
    border-color: rgba(102, 126, 234, 0.3);
    box-shadow: 0 20px 40px rgba(102, 126, 234, 0.1);
  }
`;

const MissionIcon = styled.div`
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #667eea, #764ba2);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  margin-bottom: 24px;
`;

const MissionTitle = styled.h3`
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 16px;
  color: #ffffff;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
`;

const MissionDescription = styled.p`
  opacity: 0.8;
  line-height: 1.6;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
`;

const ValuesSection = styled.section`
  padding: 120px 20px;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
`;

const ValuesGrid = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin-top: 60px;
`;

const ValueCard = styled.div`
  padding: 30px;
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 16px;
  text-align: center;
  transition: all 0.3s ease;

  &:hover {
    transform: translateY(-6px);
    border-color: rgba(102, 126, 234, 0.4);
    box-shadow: 0 16px 32px rgba(102, 126, 234, 0.15);
  }
`;

const ValueIcon = styled.div`
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #667eea, #764ba2);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  margin: 0 auto 20px;
`;

const ValueTitle = styled.h3`
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 12px;
  color: #ffffff;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
`;

const ValueDescription = styled.p`
  opacity: 0.8;
  line-height: 1.6;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
`;

const CTASection = styled.section`
  padding: 120px 20px;
  text-align: center;
  background: #0a0a0a;
`;

const CTAButton = styled.button`
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
  border: none;
  padding: 16px 40px;
  border-radius: 12px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 40px;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;

  &:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
  }
`;

const AboutUs = ({ onNavigate }) => {
  return (
    <AboutContainer>
      <HeroSection>
        <HeroContent>
          <TextContainer>
            <HeroTitle>About C-Cube Security</HeroTitle>
            <HeroSubtitle>
              C-Cube is an open-source security platform that combines cutting-edge technology with educational resources to democratize cybersecurity knowledge. We believe that everyone, regardless of their background or experience level, deserves access to powerful security tools and the knowledge to use them effectively.
            </HeroSubtitle>
            <HeroStats>
              <StatCard>
                <StatNumber>100%</StatNumber>
                <StatLabel>Open Source</StatLabel>
              </StatCard>
              <StatCard>
                <StatNumber>Free</StatNumber>
                <StatLabel>Education</StatLabel>
              </StatCard>
              <StatCard>
                <StatNumber>24/7</StatNumber>
                <StatLabel>Community</StatLabel>
              </StatCard>
            </HeroStats>
          </TextContainer>
        </HeroContent>
      </HeroSection>

      <MissionSection>
        <SectionTitle>Our Mission</SectionTitle>
        <MissionGrid>
          <MissionCard>
            <MissionIcon>🎯</MissionIcon>
            <MissionTitle>Democratize Security</MissionTitle>
            <MissionDescription>
              We're breaking down barriers to cybersecurity education by providing free, accessible tools and learning resources. Our goal is to empower individuals from all walks of life with the knowledge and tools they need to protect their digital assets and privacy.
            </MissionDescription>
          </MissionCard>
          <MissionCard>
            <MissionIcon>🔧</MissionIcon>
            <MissionTitle>Build Modern Tools</MissionTitle>
            <MissionDescription>
              Our team of dedicated creators develops innovative security solutions using the latest technologies. From cold wallet management to blockchain security, we create tools that are both powerful and user-friendly, making advanced security accessible to everyone.
            </MissionDescription>
          </MissionCard>
          <MissionCard>
            <MissionIcon>📚</MissionIcon>
            <MissionTitle>Educate & Empower</MissionTitle>
            <MissionDescription>
              Education is at the heart of everything we do. We provide comprehensive learning materials, interactive tutorials, and hands-on experiences that help people understand cybersecurity concepts and apply them in real-world scenarios.
            </MissionDescription>
          </MissionCard>
        </MissionGrid>
      </MissionSection>

      <ValuesSection>
        <SectionTitle>Our Values</SectionTitle>
        <ValuesGrid>
          <ValueCard>
            <ValueIcon>🌍</ValueIcon>
            <ValueTitle>Accessibility</ValueTitle>
            <ValueDescription>
              Security shouldn't be a privilege. We ensure our tools and educational content are accessible to people of all ages, backgrounds, and technical skill levels, fostering an inclusive cybersecurity community.
            </ValueDescription>
          </ValueCard>
          <ValueCard>
            <ValueIcon>🔓</ValueIcon>
            <ValueTitle>Transparency</ValueTitle>
            <ValueDescription>
              As an open-source project, transparency is fundamental to our approach. Every line of code, every decision, and every educational resource is open for review, contribution, and improvement by our community.
            </ValueDescription>
          </ValueCard>
          <ValueCard>
            <ValueIcon>🤝</ValueIcon>
            <ValueTitle>Community</ValueTitle>
            <ValueDescription>
              We believe in the power of collective knowledge. Our community-driven approach encourages collaboration, knowledge sharing, and mutual support among security enthusiasts and professionals worldwide.
            </ValueDescription>
          </ValueCard>
          <ValueCard>
            <ValueIcon>⚡</ValueIcon>
            <ValueTitle>Innovation</ValueTitle>
            <ValueDescription>
              Technology evolves rapidly, and so do security threats. We stay at the forefront of cybersecurity innovation, continuously developing new tools and techniques to address emerging challenges.
            </ValueDescription>
          </ValueCard>
          <ValueCard>
            <ValueIcon>🎓</ValueIcon>
            <ValueTitle>Continuous Learning</ValueTitle>
            <ValueDescription>
              The cybersecurity landscape is always changing. We promote a culture of continuous learning and adaptation, helping our community stay informed about the latest threats, tools, and best practices.
            </ValueDescription>
          </ValueCard>
          <ValueCard>
            <ValueIcon>🛡️</ValueIcon>
            <ValueTitle>Security First</ValueTitle>
            <ValueDescription>
              Security isn't just what we teach—it's how we operate. Every tool we build and every resource we create follows the highest security standards and best practices in the industry.
            </ValueDescription>
          </ValueCard>
        </ValuesGrid>
      </ValuesSection>

      <CTASection>
        <SectionTitle>Join Our Mission</SectionTitle>
        <HeroSubtitle style={{ maxWidth: '800px', margin: '0 auto 20px' }}>
          Whether you're a beginner looking to learn about cybersecurity or an expert wanting to contribute to the community, there's a place for you at C-Cube. Together, we can build a more secure digital world for everyone.
        </HeroSubtitle>
        <CTAButton onClick={() => onNavigate && onNavigate('content')}>
          Start Learning Today
        </CTAButton>
      </CTASection>

      <Footer />
    </AboutContainer>
  );
};

export default AboutUs;