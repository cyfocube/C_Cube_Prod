import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import AppWallet from './AppWallet';
import reportWebVitals from './reportWebVitals';

// Detect if running in Electron
const isElectron = () => {
  const userAgent = navigator.userAgent.toLowerCase();
  return userAgent.indexOf(' electron/') > -1;
};

// Use wallet app for Electron, website app for web
const AppToRender = isElectron() ? AppWallet : App;

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <AppToRender />
  </React.StrictMode>
);

reportWebVitals();
