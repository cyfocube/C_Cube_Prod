import React, { useState } from 'react';

function BasicApp() {
  const [page, setPage] = useState('home');

  const styles = {
    container: {
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      color: 'white',
      fontFamily: 'Arial, sans-serif',
      padding: '20px'
    },
    header: {
      textAlign: 'center',
      padding: '20px 0'
    },
    title: {
      fontSize: '3rem',
      margin: '0 0 20px 0',
      textShadow: '2px 2px 4px rgba(0,0,0,0.3)'
    },
    nav: {
      display: 'flex',
      justifyContent: 'center',
      gap: '20px',
      marginBottom: '40px'
    },
    button: {
      background: 'white',
      color: '#667eea',
      border: 'none',
      padding: '12px 24px',
      borderRadius: '8px',
      fontSize: '1rem',
      cursor: 'pointer',
      fontWeight: '600'
    },
    content: {
      maxWidth: '800px',
      margin: '0 auto',
      background: 'rgba(255,255,255,0.1)',
      padding: '30px',
      borderRadius: '12px',
      backdropFilter: 'blur(10px)'
    }
  };

  const renderContent = () => {
    switch(page) {
      case 'home':
        return (
          <div style={styles.content}>
            <h2>🚀 Welcome to C-cube</h2>
            <p>Educational blockchain platform for safe learning.</p>
            <p>Navigate using the buttons above to explore our platform.</p>
            <p><strong>Current Status:</strong> Website is working! Time: {new Date().toLocaleString()}</p>
          </div>
        );
      case 'apps':
        return (
          <div style={styles.content}>
            <h2>🔐 Our Applications</h2>
            <div style={{marginTop: '20px'}}>
              <div style={{background: 'rgba(255,255,255,0.2)', padding: '20px', borderRadius: '8px', marginBottom: '15px'}}>
                <h3>C-Cube Cold Wallet</h3>
                <p>Learn cryptocurrency storage and security</p>
              </div>
              <div style={{background: 'rgba(255,255,255,0.2)', padding: '20px', borderRadius: '8px'}}>
                <h3>DeFi Simulator (Coming Soon)</h3>
                <p>Explore decentralized finance safely</p>
              </div>
            </div>
          </div>
        );
      case 'learn':
        return (
          <div style={styles.content}>
            <h2>📚 Learn Blockchain</h2>
            <p>Comprehensive educational content about blockchain technology, cryptocurrency, and DeFi.</p>
            <ul style={{textAlign: 'left', lineHeight: '1.8'}}>
              <li>Blockchain fundamentals</li>
              <li>Cryptocurrency basics</li>
              <li>Wallet security</li>
              <li>DeFi concepts</li>
            </ul>
          </div>
        );
      default:
        return (
          <div style={styles.content}>
            <h2>Page Not Found</h2>
            <p>The requested page could not be found.</p>
          </div>
        );
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <h1 style={styles.title}>C-cube</h1>
        <nav style={styles.nav}>
          <button 
            style={{...styles.button, background: page === 'home' ? '#667eea' : 'white', color: page === 'home' ? 'white' : '#667eea'}}
            onClick={() => setPage('home')}
          >
            Home
          </button>
          <button 
            style={{...styles.button, background: page === 'learn' ? '#667eea' : 'white', color: page === 'learn' ? 'white' : '#667eea'}}
            onClick={() => setPage('learn')}
          >
            Learn
          </button>
          <button 
            style={{...styles.button, background: page === 'apps' ? '#667eea' : 'white', color: page === 'apps' ? 'white' : '#667eea'}}
            onClick={() => setPage('apps')}
          >
            Apps
          </button>
        </nav>
      </div>
      {renderContent()}
    </div>
  );
}

export default BasicApp;