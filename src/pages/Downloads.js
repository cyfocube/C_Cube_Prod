import React, { useState, useEffect } from 'react';
import styled from 'styled-components';

const DownloadsContainer = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  min-height: 100vh;
`;

const Header = styled.div`
  text-align: center;
  margin-bottom: 3rem;
`;

const Title = styled.h1`
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
  font-size: 2.5rem;
  color: #00ffff;
  margin-bottom: 1rem;
  text-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
`;

const Subtitle = styled.p`
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
  font-size: 1.2rem;
  color: #888;
  line-height: 1.6;
`;

const DownloadSection = styled.div`
  background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
  border: 1px solid #333;
  border-radius: 15px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
`;

const SectionTitle = styled.h2`
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
  color: #00ffff;
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
`;

const DownloadGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
`;

const DownloadCard = styled.div`
  background: #2a2a2a;
  border: 1px solid #444;
  border-radius: 10px;
  padding: 1.5rem;
  transition: all 0.3s ease;

  &:hover {
    border-color: #00ffff;
    box-shadow: 0 5px 15px rgba(0, 255, 255, 0.2);
  }
`;

const PlatformIcon = styled.div`
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #00ffff;
`;

const PlatformName = styled.h3`
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
  color: #fff;
  margin-bottom: 0.5rem;
  font-size: 1.2rem;
`;

const PlatformDescription = styled.p`
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
  color: #888;
  font-size: 0.9rem;
  margin-bottom: 1rem;
`;

const DownloadButton = styled.button`
  width: 100%;
  background: linear-gradient(135deg, #00ffff 0%, #0066cc 100%);
  color: #000;
  border: none;
  padding: 12px 24px;
  border-radius: 8px;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1rem;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0, 255, 255, 0.3);
  }

  &:disabled {
    background: #444;
    color: #888;
    cursor: not-allowed;
    transform: none;
    box-shadow: none;
  }
`;

const StatusText = styled.p`
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
  text-align: center;
  color: #888;
  margin-top: 1rem;
  font-style: italic;
`;

const ReleaseInfo = styled.div`
  background: #1a1a1a;
  border: 1px solid #333;
  border-radius: 10px;
  padding: 1.5rem;
  margin-bottom: 2rem;
`;

const Downloads = () => {
  const [availableDownloads, setAvailableDownloads] = useState([]);
  const [loading, setLoading] = useState(true);

  const platforms = [
    {
      id: 'macos-intel',
      name: 'macOS (Intel)',
      icon: '🍎',
      description: 'For Intel-based Mac computers',
      filePattern: '.dmg',
      fileName: 'C-Cube Cold Wallet-1.0.0.dmg'
    },
    {
      id: 'macos-apple',
      name: 'macOS (Apple Silicon)',
      icon: '🍎',
      description: 'For M1/M2 Mac computers',
      filePattern: '.dmg',
      fileName: 'C-Cube Cold Wallet-1.0.0-arm64.dmg'
    },
    {
      id: 'windows',
      name: 'Windows',
      icon: '🪟',
      description: 'For Windows 10/11 (64-bit)',
      filePattern: '.exe',
      fileName: 'C-Cube Cold Wallet Setup 1.0.0.exe'
    },
    {
      id: 'linux',
      name: 'Linux',
      icon: '🐧',
      description: 'For Ubuntu/Debian-based distributions',
      filePattern: '.AppImage',
      fileName: 'C-Cube Cold Wallet-1.0.0.AppImage'
    }
  ];

  useEffect(() => {
    checkAvailableDownloads();
  }, []);

  const checkAvailableDownloads = async () => {
    setLoading(true);
    try {
      // Simplified approach: Set known available downloads
      // macOS downloads are confirmed to be available (130MB+ files)
      // Windows installer is also available (720MB file)
      const knownAvailableFiles = [
        'C-Cube Cold Wallet-1.0.0.dmg',           // macOS Intel - 133MB
        'C-Cube Cold Wallet-1.0.0-arm64.dmg',    // macOS Apple Silicon - 130MB
        'C-Cube Cold Wallet Setup 1.0.0.exe'     // Windows installer - 720MB
      ];
      
      const downloads = platforms.map(platform => ({
        ...platform,
        available: knownAvailableFiles.includes(platform.fileName),
        version: '1.0.0'
      }));
      
      setAvailableDownloads(downloads);
      
      // Optional: Log for debugging on production
      console.log('Downloads status:', downloads.map(d => ({ name: d.name, available: d.available })));
      
    } catch (error) {
      console.error('Error setting up downloads:', error);
      
      // Even if there's an error, show known available platforms
      const downloads = platforms.map(platform => ({
        ...platform,
        available: [
          'C-Cube Cold Wallet-1.0.0.dmg', 
          'C-Cube Cold Wallet-1.0.0-arm64.dmg',
          'C-Cube Cold Wallet Setup 1.0.0.exe'
        ].includes(platform.fileName),
        version: '1.0.0'
      }));
      
      setAvailableDownloads(downloads);
    } finally {
      setLoading(false);
    }
  };

  const handleDownload = (platform) => {
    if (!platform.available) {
      return;
    }
    
    // Create a direct download link
    const downloadUrl = `/downloads/${platform.fileName}`;
    
    // Create a temporary link and trigger download
    const link = document.createElement('a');
    link.href = downloadUrl;
    link.download = platform.fileName;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <DownloadsContainer>
      <Header>
        <Title>Download C-Cube Cold Wallet</Title>
        <Subtitle>
          Secure offline cold wallet application for multiple blockchains.<br/>
          Available for Windows, macOS, and Linux platforms.
        </Subtitle>
      </Header>

      <ReleaseInfo>
        <SectionTitle>Latest Release - Version 1.0.0</SectionTitle>
        <p style={{ 
          fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif",
          color: '#888', 
          lineHeight: 1.6 
        }}>
          • Enhanced security features<br/>
          • Multi-blockchain support (Bitcoin, Ethereum, and more)<br/>
          • Offline transaction signing<br/>
          • QR code generation and scanning<br/>
          • Comprehensive learning materials included
        </p>
      </ReleaseInfo>

      <DownloadSection>
        <SectionTitle>Desktop Applications</SectionTitle>
        <p style={{ 
          fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif",
          color: '#888', 
          marginBottom: '1rem' 
        }}>
          Download the desktop version for the ultimate security and offline functionality.
        </p>
        
        {loading ? (
          <StatusText>Checking available downloads...</StatusText>
        ) : (
          <DownloadGrid>
            {availableDownloads.map((platform) => {
              return (
                <DownloadCard key={platform.id}>
                  <PlatformIcon>{platform.icon}</PlatformIcon>
                  <PlatformName>{platform.name}</PlatformName>
                  <PlatformDescription>{platform.description}</PlatformDescription>
                  <DownloadButton
                    onClick={() => handleDownload(platform)}
                    disabled={!platform.available}
                  >
                    {platform.available ? 'Download Now' : 'Coming Soon'}
                  </DownloadButton>
                  {/* Debug info - remove after testing */}
                  {process.env.NODE_ENV === 'development' && (
                    <div style={{ fontSize: '0.8rem', color: '#666', marginTop: '0.5rem' }}>
                      Debug: {platform.fileName} - {platform.available ? 'Available' : 'Not Available'}
                    </div>
                  )}
                </DownloadCard>
              );
            })}
          </DownloadGrid>
        )}
      </DownloadSection>

      <DownloadSection>
        <SectionTitle>Installation Instructions</SectionTitle>
        <div style={{ 
          fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif",
          color: '#888', 
          lineHeight: 1.8 
        }}>
          <h4 style={{ 
            fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif",
            color: '#00ffff', 
            marginBottom: '0.5rem' 
          }}>macOS:</h4>
          <p>1. Download the appropriate .dmg file for your Mac<br/>
          2. Open the downloaded file<br/>
          3. Drag C-Cube to your Applications folder<br/>
          4. <strong style={{color: '#ff9900'}}>Important:</strong> If you see a security warning, go to System Preferences → Security & Privacy → General and click "Open Anyway"</p>

          <h4 style={{ 
            fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif",
            color: '#00ffff', 
            marginTop: '1.5rem', 
            marginBottom: '0.5rem' 
          }}>Windows:</h4>
          <p>1. Download the .exe installer<br/>
          2. Run the installer as Administrator<br/>
          3. Follow the installation wizard<br/>
          4. Launch from Start Menu or Desktop shortcut</p>

          <h4 style={{ 
            fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif",
            color: '#00ffff', 
            marginTop: '1.5rem', 
            marginBottom: '0.5rem' 
          }}>Linux:</h4>
          <p>1. Download the .AppImage file<br/>
          2. Make it executable: chmod +x filename.AppImage<br/>
          3. Run the application: ./filename.AppImage</p>
        </div>
      </DownloadSection>

      <DownloadSection>
        <SectionTitle>Security Notice</SectionTitle>
        <div style={{ 
          fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif",
          color: '#888', 
          lineHeight: 1.8, 
          background: '#1a1a1a', 
          padding: '1rem', 
          borderRadius: '8px', 
          border: '1px solid #333' 
        }}>
          <p style={{ 
            fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif",
            color: '#ff9900', 
            fontWeight: 'bold', 
            marginBottom: '0.5rem' 
          }}>⚠️ macOS Security Warning</p>
          <p>macOS may show a security warning because our applications aren't code-signed with an Apple Developer certificate. This is normal for open-source applications.</p>
          <p><strong>To resolve:</strong> System Preferences → Security & Privacy → General → Click "Open Anyway"</p>
          <p style={{ 
            fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif",
            marginTop: '1rem', 
            fontSize: '0.9rem' 
          }}>
            <strong>Why this happens:</strong> Code signing requires a paid Apple Developer account. The app is completely safe - it's built directly from this open-source project.
          </p>
        </div>
      </DownloadSection>
    </DownloadsContainer>
  );
};

export default Downloads;