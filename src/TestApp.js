import React from 'react';

function TestApp() {
  return (
    <div style={{ 
      padding: '50px', 
      textAlign: 'center', 
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      color: 'white',
      minHeight: '100vh',
      fontSize: '24px'
    }}>
      <h1>🚀 CyFoCube Website Test</h1>
      <p>If you can see this, the React app is working!</p>
      <p>Current time: {new Date().toLocaleString()}</p>
    </div>
  );
}

export default TestApp;