import React from 'react';

function MinimalApp() {
  return (
    <div style={{
      background: 'red',
      color: 'white',
      padding: '50px',
      fontSize: '24px',
      minHeight: '100vh'
    }}>
      <h1>MINIMAL TEST - CyFoCube</h1>
      <p>If you see this red page, React is working!</p>
      <p>Time: {new Date().toLocaleString()}</p>
    </div>
  );
}

export default MinimalApp;