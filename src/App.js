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
import Downloads from './pages/Downloads';
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
      case 'downloads':
        return <Downloads onNavigate={handlePageNavigation} />;
      case 'coming-soon':
        return <ComingSoon onNavigate={handlePageNavigation} />;
      case 'c-cube':
        return renderCCubeApp();
      default:
        return <Landing onAppSelect={handlePageNavigation} onNavigate={handlePageNavigation} />;
    }
  };

  // Main website with proper URL routing
  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle />
      <Router>
        <Routes>
          {/* Website routes with proper URLs */}
          <Route path="/" element={
            <>
              <Header currentPage="landing" onNavigate={handlePageNavigation} />
              <Landing onAppSelect={handlePageNavigation} onNavigate={handlePageNavigation} />
            </>
          } />
          <Route path="/learn" element={
            <>
              <Header currentPage="content" onNavigate={handlePageNavigation} />
              <Learn onNavigate={handlePageNavigation} />
            </>
          } />
          <Route path="/about" element={
            <>
              <Header currentPage="about" onNavigate={handlePageNavigation} />
              <AboutUs onNavigate={handlePageNavigation} />
            </>
          } />
          <Route path="/apps" element={
            <>
              <Header currentPage="community" onNavigate={handlePageNavigation} />
              <Community onNavigate={handlePageNavigation} />
            </>
          } />
          <Route path="/faq" element={
            <>
              <Header currentPage="faq" onNavigate={handlePageNavigation} />
              <FAQ onNavigate={handlePageNavigation} />
            </>
          } />
          <Route path="/download" element={
            <>
              <Header currentPage="downloads" onNavigate={handlePageNavigation} />
              <Downloads onNavigate={handlePageNavigation} />
            </>
          } />
          <Route path="/coming-soon" element={
            <>
              <Header currentPage="coming-soon" onNavigate={handlePageNavigation} />
              <ComingSoon onNavigate={handlePageNavigation} />
            </>
          } />
          
          {/* C-Cube app routes (without header) */}
          <Route path="/c-cube/*" element={renderCCubeApp()} />
          
          {/* Fallback to home page */}
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
}

export default App;
