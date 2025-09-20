import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider } from 'styled-components';
import { GlobalStyle, theme } from './styles/GlobalStyle';
import Layout from './components/Layout';
import Resources from './pages/Resources';
import ColdWallet from './pages/ColdWallet';
import Broadcast from './pages/Broadcast';
import { AppProvider } from './context/AppContext';
import SetupWallet from './pages/SetupWallet';
import WelcomeScreen from './pages/WelcomeScreen';
import SecurityPrompt from './components/SecurityPrompt';

function App() {
  const [isSetup, setIsSetup] = useState(false);
  const [isSecurityPromptAcknowledged, setIsSecurityPromptAcknowledged] = useState(false);
  const [hasInitialChoice, setHasInitialChoice] = useState(false);

  // Check if the user has already set up the wallet
  React.useEffect(() => {
    const hasSetupWallet = localStorage.getItem('walletSetup');
    if (hasSetupWallet === 'true') {
      setIsSetup(true);
    }
    
    // Check if user has made an initial wallet choice
    const walletAction = localStorage.getItem('walletAction');
    if (walletAction === 'create' || walletAction === 'recover') {
      setHasInitialChoice(true);
    }
  }, []);

  // Handle initial security prompt
  if (!isSecurityPromptAcknowledged) {
    return (
      <ThemeProvider theme={theme}>
        <GlobalStyle />
        <SecurityPrompt onAcknowledge={() => setIsSecurityPromptAcknowledged(true)} />
      </ThemeProvider>
    );
  }

  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle />
      <AppProvider>
        <Router>
          <Layout>
            <Routes>
              {isSetup ? (
                // Wallet is already set up, show main app
                <>
                  <Route path="/resources" element={<Resources />} />
                  <Route path="/wallet" element={<ColdWallet />} />
                  <Route path="/broadcast" element={<Broadcast />} />
                  <Route path="*" element={<Navigate to="/wallet" replace />} />
                </>
              ) : hasInitialChoice ? (
                // User has chosen create/recover, but hasn't completed setup
                <>
                  <Route path="/setup" element={<SetupWallet onSetupComplete={() => setIsSetup(true)} />} />
                  <Route path="*" element={<Navigate to="/setup" replace />} />
                </>
              ) : (
                // User needs to choose between create and recover
                <>
                  <Route path="/welcome" element={<WelcomeScreen />} />
                  <Route path="/setup" element={<SetupWallet onSetupComplete={() => setIsSetup(true)} />} />
                  <Route path="*" element={<Navigate to="/welcome" replace />} />
                </>
              )}
            </Routes>
          </Layout>
        </Router>
      </AppProvider>
    </ThemeProvider>
  );
}

export default App;
