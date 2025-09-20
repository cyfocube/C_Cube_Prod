# C-Cube

A cross-platform desktop cold wallet application for securely managing cryptocurrency offline.

## Features

### Resources Menu
- Comprehensive guides, FAQs, and security tips
- Detailed instructions for using the application safely
- Information about cold wallet security best practices

### Cold Wallet Menu
- Generate new wallets securely offline (Ethereum supported)
- Optional wallet encryption with strong password protection
- View and backup private keys securely
- Sign transactions offline without exposing private keys

### Broadcast Menu
- Broadcast previously signed transactions
- Verify transaction details before broadcasting
- Choose from multiple Ethereum nodes or use custom endpoints

## Security Features

- Complete separation of offline (private key) operations from online (broadcasting) operations
- AES-256 encryption for wallet storage
- Private keys never leave your device
- Designed to work on air-gapped computers

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

2. Install dependencies:
```bash
npm install
```

3. Run the application in development mode:
```bash
npm start
```

### Building for Production

Build the application for your current platform:
```bash
npm run build
```

The packaged application will be available in the `dist` directory.

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

## Security Recommendations

1. **Use on an Offline Computer**: For maximum security, use this application on a computer that never connects to the internet.
2. **Always Encrypt Your Wallet**: Use a strong, unique password to encrypt your wallet.
3. **Backup Your Private Keys**: Store backups of your private keys or seed phrases in secure, offline locations.
4. **Verify Transactions**: Always double-check transaction details before signing and broadcasting.
5. **Keep Software Updated**: Ensure you're using the latest version of the application.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This software is provided "as is", without warranty of any kind. Use at your own risk. The authors or copyright holders shall not be liable for any claim, damages, or other liability arising from the use of the software.

Never share your private keys or seed phrases with anyone. Always ensure you're using the official version of this software downloaded from trusted sources.
