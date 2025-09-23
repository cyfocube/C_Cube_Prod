import React, { useState } from 'react';
import styled from 'styled-components';

const Container = styled.div`
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 50px;
  text-align: center;
  font-family: Arial, sans-serif;
`;

const Title = styled.h1`
  font-size: 3rem;
  margin-bottom: 20px;
`;

const Button = styled.button`
  background: white;
  color: #667eea;
  border: none;
  padding: 15px 30px;
  border-radius: 8px;
  font-size: 1.2rem;
  cursor: pointer;
  margin: 10px;
  
  &:hover {
    background: #f0f0f0;
  }
`;

const PageContent = styled.div`
  background: white;
  color: #333;
  padding: 30px;
  border-radius: 12px;
  margin: 20px auto;
  max-width: 800px;
`;

function App() {
  const [currentPage, setCurrentPage] = useState('home');

  const renderContent = () => {
    switch (currentPage) {
      case 'home':
        return (
          <Container>
            <Title>🚀 CyFoCube Platform</Title>
            <p>Welcome to the CyFoCube educational blockchain platform!</p>
            <Button onClick={() => setCurrentPage('about')}>About</Button>
            <Button onClick={() => setCurrentPage('apps')}>Apps</Button>
          </Container>
        );
      case 'about':
        return (
          <Container>
            <Title>About CyFoCube</Title>
            <PageContent>
              <h2>Educational Blockchain Platform</h2>
              <p>CyFoCube provides safe, educational tools for learning about blockchain technology and cryptocurrency.</p>
              <Button onClick={() => setCurrentPage('home')}>← Back to Home</Button>
            </PageContent>
          </Container>
        );
      case 'apps':
        return (
          <Container>
            <Title>Our Applications</Title>
            <PageContent>
              <h2>Educational Tools</h2>
              <div style={{ display: 'grid', gap: '20px', margin: '20px 0' }}>
                <div style={{ padding: '20px', background: '#f8f9fa', borderRadius: '8px' }}>
                  <h3>🔐 C-Cube Cold Wallet</h3>
                  <p>Learn cryptocurrency storage and security</p>
                </div>
                <div style={{ padding: '20px', background: '#f8f9fa', borderRadius: '8px' }}>
                  <h3>📊 DeFi Simulator (Coming Soon)</h3>
                  <p>Explore decentralized finance safely</p>
                </div>
              </div>
              <Button onClick={() => setCurrentPage('home')}>← Back to Home</Button>
            </PageContent>
          </Container>
        );
      default:
        return (
          <Container>
            <Title>Page Not Found</Title>
            <Button onClick={() => setCurrentPage('home')}>← Back to Home</Button>
          </Container>
        );
    }
  };

  return renderContent();
}

export default App;