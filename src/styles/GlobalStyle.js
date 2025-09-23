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
    main: "'Share Tech Mono', 'Courier New', monospace", // Keep original for C-Cube wallet
    modern: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif",
    heading: "'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif",
    code: "'Share Tech Mono', 'Monaco', 'Inconsolata', 'Roboto Mono', 'Courier New', monospace",
  },
  breakpoints: {
    mobile: '576px',
    tablet: '768px',
    desktop: '992px',
    largeDesktop: '1200px',
  },
};

export const GlobalStyle = createGlobalStyle`
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  html, body {
    height: 100%;
    font-family: ${({ theme }) => theme.fonts.main}; /* This keeps Share Tech Mono for C-Cube wallet */
    background-color: ${({ theme }) => theme.colors.background};
    background-image: url('/Images/Bakgrd3.png');
    background-size: cover;
    background-position: right;
    background-repeat: no-repeat;
    background-attachment: fixed;
    color: ${({ theme }) => theme.colors.text};
    position: relative;
    overflow-x: hidden;
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  /* Fade overlay for background image */
  html::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(10, 10, 10, 0.7);
    z-index: -3;
    pointer-events: none;
  }

  /* Website-specific modern typography - only for website pages */
  .website-page {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    
    h1, h2, h3, h4, h5, h6 {
      font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-weight: 600;
      line-height: 1.3;
    }

    h1 {
      font-size: 2.5rem;
      font-weight: 700;
    }

    h2 {
      font-size: 2rem;
      font-weight: 600;
    }

    h3 {
      font-size: 1.5rem;
      font-weight: 600;
    }

    p {
      line-height: 1.7;
      font-weight: 400;
    }

    button {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-weight: 500;
    }
  }

  /* Keep original C-Cube wallet styling */
  code, pre {
    font-family: ${({ theme }) => theme.fonts.code};
  }
  }

  body::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -2;
    background:
      linear-gradient(rgba(0, 255, 65, 0.02) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0, 255, 65, 0.02) 1px, transparent 1px);
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
    z-index: -2;
    opacity: 0.1;
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
