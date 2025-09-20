import { createGlobalStyle } from 'styled-components';

export const theme = {
  colors: {
    primary: '#00cc33', // Toned down Matrix green
    secondary: '#0b2a02', // Dark green
    success: '#2ecc40', // Toned down Bright green
    danger: '#ff073a', // Digital red
    warning: '#ff9900', // Alert amber
    info: '#00ccff', // Cyber blue
    light: '#f8f9fa',
    dark: '#0a0a0a',
    background: '#0c0c0c', // Near black
    cardBackground: '#141414', // Dark slate
    text: '#00cc33', // Toned down Matrix green text
    mutedText: '#4e9a06', // Muted green
    border: '#00ff41', // Bright green borders
    highlight: '#00ff4133', // Semi-transparent green
    accent: '#ff073a', // Red accent
    gridLines: '#141414', // Grid lines
    overlay: 'rgba(0, 255, 65, 0.05)', // Very subtle green overlay
  },
  fonts: {
    main: "'Share Tech Mono', 'Courier New', monospace",
    code: "'Share Tech Mono', 'Courier New', monospace",
  },
  breakpoints: {
    mobile: '576px',
    tablet: '768px',
    desktop: '992px',
    largeDesktop: '1200px',
  },
};

export const GlobalStyle = createGlobalStyle`
  @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  html, body {
    height: 100%;
    font-family: ${({ theme }) => theme.fonts.main};
    background-color: ${({ theme }) => theme.colors.background};
    color: ${({ theme }) => theme.colors.text};
    position: relative;
    overflow-x: hidden;
  }

  body::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    background:
      linear-gradient(rgba(0, 255, 65, 0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0, 255, 65, 0.03) 1px, transparent 1px);
    background-size: 20px 20px;
    pointer-events: none;
  }

  /* Create random digital noise effect */
  body::after {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.05'/%3E%3C/svg%3E");
    z-index: -1;
    opacity: 0.3;
    pointer-events: none;
  }

  #root {
    height: 100%;
    position: relative;
  }

  a {
    text-decoration: none;
    color: ${({ theme }) => theme.colors.primary};
    transition: color 0.3s;

    &:hover {
      color: ${({ theme }) => theme.colors.info};
    }
  }

  button {
    cursor: pointer;
    font-family: ${({ theme }) => theme.fonts.main};
    border: none;
    border-radius: 4px;
    padding: 8px 16px;
    font-size: 1rem;
    transition: background-color 0.3s, transform 0.2s;

    &:hover {
      transform: translateY(-2px);
    }

    &:active {
      transform: translateY(0);
    }

    &:disabled {
      cursor: not-allowed;
      opacity: 0.7;
    }
  }

  input, textarea, select {
    font-family: ${({ theme }) => theme.fonts.main};
    font-size: 1rem;
    padding: 8px 12px;
    border-radius: 4px;
    border: 1px solid ${({ theme }) => theme.colors.border};
    background-color: ${({ theme }) => theme.colors.cardBackground};
    color: ${({ theme }) => theme.colors.text};
    transition: border-color 0.3s;

    &:focus {
      border-color: ${({ theme }) => theme.colors.primary};
      outline: none;
    }
  }

  code {
    font-family: ${({ theme }) => theme.fonts.code};
    background-color: ${({ theme }) => theme.colors.cardBackground};
    padding: 2px 4px;
    border-radius: 3px;
  }

  ::-webkit-scrollbar {
    width: 8px;
    height: 8px;
  }

  ::-webkit-scrollbar-track {
    background: ${({ theme }) => theme.colors.background};
  }

  ::-webkit-scrollbar-thumb {
    background: ${({ theme }) => theme.colors.border};
    border-radius: 4px;
  }

  ::-webkit-scrollbar-thumb:hover {
    background: ${({ theme }) => theme.colors.primary};
  }
`;
