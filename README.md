# C-Cube Tutorial Wallet

A cross-platform educational cryptocurrency wallet application for learning blockchain technology safely. Available as both a desktop application and web application.

## ⚠️ Important: Educational Use Only

**C-Cube is a tutorial wallet designed for learning purposes only. Do not use it with real cryptocurrency.**

- 🎓 **Educational Tool**: Learn about cryptocurrency wallets safely
- 🔒 **Security Learning**: Understand cold wallet concepts
- 🌐 **Multi-Platform**: Available on desktop (Electron) and web browsers
- ⚠️ **No Real Funds**: Never send real cryptocurrency to C-Cube addresses

## Features

### Resources Menu
- Comprehensive educational guides and tutorials
- Security best practices for real cryptocurrency use
- FAQs about blockchain technology and wallet security
- Information about cold wallet vs hot wallet concepts

### Cold Wallet Menu
- Learn to generate new tutorial wallets securely (Ethereum, Polygon, BSC, Arbitrum, Optimism)
- Practice wallet encryption with strong password protection
- Understand private key management and backup procedures
- Learn to sign transactions offline without exposing private keys

### Broadcast Menu
- Practice broadcasting test transactions
- Learn to verify transaction details before broadcasting
- Understand network selection and RPC endpoints
- Practice with multiple blockchain networks

## Educational Security Features

- Demonstrates separation of offline (private key) operations from online (broadcasting) operations
- Learn about AES-256 encryption for wallet storage
- Understand how private keys should never leave your device
- Practice with air-gapped computer concepts

## Platform Support

### Desktop Application (Recommended for Learning)
- Enhanced security features
- Native file system access
- Offline functionality
- Cross-platform: Windows, macOS, Linux

### Web Application
- Browser-based learning
- Instant access, no installation required
- localStorage for educational data persistence
- All modern browsers supported

## Requirements

- Node.js 14.x or later
- npm 6.x or later

## Installation and Setup

### Development Mode

1. Clone the repository:
```bash
git clone https://github.com/yourusername/secure-cold-wallet.git
cd secure-cold-wallet
```

### Development Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/c-cube.git
cd c-cube
```

2. Install dependencies:
```bash
npm install
```

## Running the Application

### Desktop Application (Development)
```bash
npm start
```

### Web Application (Development)
```bash
npm run start-web
```

### Web Application (Local Production Test)
```bash
npm run preview
```

## Building for Production

### Desktop Application
Build the desktop application for your current platform:
```bash
npm run build
```

The packaged application will be available in the `dist` directory.

### Web Application
Build for web deployment:
```bash
npm run build-web
```

The web-ready files will be in the `build` directory.

## Deployment Options

### Web Deployment

#### 1. Netlify
1. Connect your GitHub repository to Netlify
2. Set build command to `npm run build-web`
3. Set publish directory to `build`
4. Deploy automatically on push

#### 2. Vercel
1. Connect your GitHub repository to Vercel
2. Vercel will automatically detect the React app
3. Deploy automatically on push

#### 3. GitHub Pages
1. Push your code to GitHub
2. Enable GitHub Actions (included workflow will auto-deploy)
3. Enable GitHub Pages in repository settings
4. Choose GitHub Actions as the source

#### 4. Manual Web Server
```bash
npm run build-web
# Upload contents of 'build' directory to your web server
```

### Desktop Application Building

## Building for Different Platforms

### Windows
```bash
npm run electron-build -- --win
```

### macOS
```bash
npm run electron-build -- --mac
```

### Linux
```bash
npm run electron-build -- --linux
```

## Educational Security Recommendations

1. **Learn with Testnets**: Practice with test networks before using real cryptocurrency
2. **Understand Cold Storage**: Learn the difference between hot and cold wallets
3. **Practice Good Habits**: Always encrypt wallets and backup recovery phrases (even for learning)
4. **Study Transaction Flow**: Understand how transactions are signed and broadcast
5. **Security Mindset**: Develop security-first thinking for real cryptocurrency use

## Web vs Desktop Differences

### Desktop Application
- ✅ Enhanced security features
- ✅ File system access for secure storage
- ✅ Native operating system integration
- ✅ True offline capability
- ✅ Recommended for learning best practices

### Web Application
- ✅ Instant access, no installation
- ✅ Cross-platform compatibility
- ✅ Automatic updates
- ⚠️ Browser localStorage (less secure than desktop)
- ⚠️ Requires internet connection
- ⚠️ Educational use only

## Available Scripts

### Development
- `npm run start-web` - Start web development server
- `npm start` - Start desktop development (Electron + React)
- `npm run react-start` - Start React development server only

### Building
- `npm run build-web` - Build for web deployment
- `npm run build` - Build desktop application
- `npm run electron-build` - Build Electron app only

### Deployment
- `npm run preview` - Build and serve web version locally
- `npm run serve` - Serve built web version

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Areas for Contribution
- Additional blockchain network support
- Enhanced educational content
- Security improvements
- UI/UX improvements
- Documentation improvements

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

**⚠️ EDUCATIONAL SOFTWARE DISCLAIMER**

This software is provided "as is" for educational purposes only, without warranty of any kind. Use at your own risk for learning only.

**IMPORTANT EDUCATIONAL NOTICES:**
- This is a tutorial wallet for learning purposes only
- Do NOT use with real cryptocurrency or funds
- The authors shall not be liable for any loss of funds
- Always use proper production wallets for real cryptocurrency
- This software is designed to teach concepts, not store real value

**For Real Cryptocurrency Use:**
- Use established, audited wallet software
- Never share private keys or seed phrases with anyone
- Always ensure you're using official software from trusted sources
- Follow proper security practices learned through this educational tool
