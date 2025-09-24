import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider } from 'styled-components';
import { GlobalStyle, theme } from './styles/GlobalStyle';
import Layout from './components/Layout';
import { AppProvider } from './context/AppContext';
import EnvironmentDetection from './utils/EnvironmentDetection';
import WebWarningBanner from './components/WebWarningBanner';
import Header from './components/Header_New';

// Import pages
import WelcomeScreen from './pages/WelcomeScreen';
import SetupWallet from './pages/SetupWallet';
import ColdWallet from './pages/ColdWallet';
import Broadcast from './pages/Broadcast';
import Resources from './pages/Resources';
import Landing from './pages/Landing_New';
import Content from './pages/Content';
import Learn from './pages/Learn';
import AboutUs from './pages/AboutUs';
import Community from './pages/Community';
import FAQ from './pages/FAQ_Fixed';
import ComingSoon from './pages/ComingSoon';
import SecurityPrompt from './components/SecurityPrompt';

function App() {
  const [currentPage, setCurrentPage] = useState('landing'); // Start with landing page
  const [isWebEnvironment, setIsWebEnvironment] = useState(false);
  
  // C-Cube wallet state
  const [isSetup, setIsSetup] = useState(false);
  const [isSecurityPromptAcknowledged, setIsSecurityPromptAcknowledged] = useState(false);
  const [hasInitialChoice, setHasInitialChoice] = useState(false);

  useEffect(() => {
    const envInfo = EnvironmentDetection.getEnvironmentInfo();
    setIsWebEnvironment(envInfo.isWeb);
    
    // Check if the user has already set up the wallet (only for C-Cube app)
    const hasSetupWallet = localStorage.getItem('walletSetup');
    if (hasSetupWallet === 'true') {
      setIsSetup(true);
    }
    
    // Check if user has made an initial wallet choice
    const walletAction = localStorage.getItem('walletAction');
    if (walletAction === 'create' || walletAction === 'recover') {
      setHasInitialChoice(true);
    }
    
    // Log environment info for debugging
    console.log('Environment:', envInfo);
  }, []);

  const handlePageNavigation = (page) => {
    setCurrentPage(page);
    // Reset security prompt for C-Cube if navigating away from it
    if (page !== 'c-cube') {
      setIsSecurityPromptAcknowledged(false);
    }
  };

  // Render C-Cube wallet app with its original logic
  const renderCCubeApp = () => {
    // Handle initial security prompt for C-Cube
    if (!isSecurityPromptAcknowledged) {
      return (
        <SecurityPrompt onAcknowledge={() => setIsSecurityPromptAcknowledged(true)} />
      );
    }

    return (
      <AppProvider>
        {isWebEnvironment && <WebWarningBanner />}
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
    );
  };

  // Render website structure for main pages
  const renderWebsitePages = () => {
    switch (currentPage) {
      case 'landing':
        return <Landing onAppSelect={handlePageNavigation} onNavigate={handlePageNavigation} />;
      case 'content':
        return <Learn onNavigate={handlePageNavigation} />;
      case 'about':
        return <AboutUs onNavigate={handlePageNavigation} />;
      case 'community':
        return <Community onNavigate={handlePageNavigation} />;
      case 'faq':
        return <FAQ onNavigate={handlePageNavigation} />;
      case 'coming-soon':
        return <ComingSoon onNavigate={handlePageNavigation} />;
      case 'c-cube':
        return renderCCubeApp();
      default:
        return <Landing onAppSelect={handlePageNavigation} onNavigate={handlePageNavigation} />;
    }
  };

  // For C-Cube app, don't show the main header
  if (currentPage === 'c-cube') {
    return (
      <ThemeProvider theme={theme}>
        <GlobalStyle />
        {renderWebsitePages()}
      </ThemeProvider>
    );
  }

  // For all other pages, show the website structure with header
  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle />
      <Header currentPage={currentPage} onNavigate={handlePageNavigation} />
      {renderWebsitePages()}
    </ThemeProvider>
  );
}

export default App;
