import React, { useState } from 'react';
import styled from 'styled-components';
import Footer from '../components/Footer_New';

const FAQContainer = styled.div`
  min-height: 100vh;
  background: #0a0a0a;
  padding: 80px 20px 40px;
  color: #e0e0e0;
`;

const FAQCard = styled.div`
  max-width: 800px;
  margin: 0 auto;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  padding: 40px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
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

const TestContent = styled.div`
  padding: 20px;
  text-align: center;
`;

const FAQ = () => {
  const [testState] = useState('FAQ Test Page');

  return (
    <>
      <FAQContainer className="website-page">
        <FAQCard>
          <Title>FAQ Test Page</Title>
          <TestContent>
            <p>This is a test FAQ page to check if the basic structure works.</p>
            <p>State value: {testState}</p>
            <h3>Test Questions:</h3>
            <div style={{ marginTop: '20px', textAlign: 'left' }}>
              <h4>Question 1: What is this test?</h4>
              <p>This is a simple test to verify the FAQ page structure works correctly.</p>
              
              <h4>Question 2: Is the styling working?</h4>
              <p>If you can see this content with dark background and proper styling, then yes!</p>
              
              <h4>Question 3: Are components rendering?</h4>
              <p>If this text is visible, React components are rendering properly.</p>
            </div>
          </TestContent>
        </FAQCard>
      </FAQContainer>
      <Footer />
    </>
  );
};

export default FAQ;