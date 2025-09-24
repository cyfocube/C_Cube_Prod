# macOS Security Guide for C-Cube Cold Wallet

## Installing Unsigned Applications on macOS

When you download and try to run the C-Cube Cold Wallet on macOS, you may see this warning:

> "Apple could not verify 'C-Cube Cold Wallet' is free of malware that may harm your Mac or compromise your privacy."

This is normal for unsigned applications. Here's how to safely install and run the app:

## Method 1: Using System Preferences (Recommended)

1. **After the warning appears**, click "Cancel" (don't move to trash)
2. Open **System Preferences** → **Security & Privacy**
3. In the **General** tab, you'll see a message about "C-Cube Cold Wallet"
4. Click **"Open Anyway"**
5. You may see another dialog - click **"Open"** to confirm

## Method 2: Using Terminal (Alternative)

If Method 1 doesn't work, you can use Terminal:

```bash
# Navigate to where you downloaded the app (usually Applications)
cd /Applications

# Remove the quarantine attribute
sudo xattr -rd com.apple.quarantine "C-Cube Cold Wallet.app"
```

## Method 3: Right-Click Method

1. **Right-click** the C-Cube Cold Wallet app
2. Select **"Open"** from the context menu
3. In the dialog that appears, click **"Open"**

## Why This Happens

- The app isn't code-signed with an Apple Developer certificate
- This is common for open-source and development applications
- The security warning is macOS being cautious, not an indication of malware

## Verification Steps

To verify the app is legitimate:

1. Check that you downloaded it from the official C-Cube website
2. The app should be exactly as built from this open-source project
3. You can review the source code in this repository

## For Developers

To create properly signed applications:

1. Obtain an Apple Developer account ($99/year)
2. Generate a "Developer ID Application" certificate
3. Update the build configuration with your certificate details
4. The build process will automatically sign the app

## Next Steps

Once you've successfully opened the app:
- The warning won't appear again for this specific version
- You can use the app normally
- Future updates may require repeating these steps unless properly signed