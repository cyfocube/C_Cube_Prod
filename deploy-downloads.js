#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

console.log('📦 Deploying desktop applications to downloads folder...\n');

const distDir = 'dist';
const downloadsDir = 'public/downloads';

// Ensure downloads directory exists
if (!fs.existsSync(downloadsDir)) {
  fs.mkdirSync(downloadsDir, { recursive: true });
}

// Copy files from dist to public/downloads
if (fs.existsSync(distDir)) {
  const files = fs.readdirSync(distDir);
  let copiedFiles = 0;

  files.forEach(file => {
    const srcPath = path.join(distDir, file);
    const destPath = path.join(downloadsDir, file);
    
    // Only copy installer files (dmg, exe, AppImage, deb)
    const installerExtensions = ['.dmg', '.exe', '.AppImage', '.deb'];
    const isInstaller = installerExtensions.some(ext => file.endsWith(ext));
    
    if (isInstaller) {
      try {
        fs.copyFileSync(srcPath, destPath);
        const stats = fs.statSync(srcPath);
        const sizeInMB = (stats.size / 1024 / 1024).toFixed(2);
        console.log(`✅ Copied: ${file} (${sizeInMB} MB)`);
        copiedFiles++;
      } catch (error) {
        console.error(`❌ Failed to copy ${file}:`, error.message);
      }
    }
  });

  if (copiedFiles === 0) {
    console.log('ℹ️  No installer files found in dist folder.');
    console.log('   Run "npm run build-desktop-app" first to generate installers.');
  } else {
    console.log(`\n🎉 Successfully deployed ${copiedFiles} installer(s) to public/downloads/`);
  }
} else {
  console.error('❌ dist folder not found. Run the build process first.');
  process.exit(1);
}