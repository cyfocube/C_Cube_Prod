#!/usr/bin/env node

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

console.log('🚀 Starting C-Cube Desktop Build Process...\n');

// Ensure directories exist
const directories = ['dist', 'assets', 'public/downloads'];
directories.forEach(dir => {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
    console.log(`✅ Created directory: ${dir}`);
  }
});

// Step 1: Build React app
console.log('📦 Building React application...');
try {
  execSync('npm run react-build', { stdio: 'inherit' });
  console.log('✅ React build completed successfully\n');
} catch (error) {
  console.error('❌ React build failed:', error.message);
  process.exit(1);
}

// Step 2: Build desktop applications
console.log('🖥️  Building desktop applications...');

const platform = process.platform;
const buildCommands = {
  darwin: 'electron-builder --mac',
  win32: 'electron-builder --win',
  linux: 'electron-builder --linux'
};

try {
  // Build for current platform
  if (buildCommands[platform]) {
    console.log(`Building for ${platform}...`);
    execSync(buildCommands[platform], { stdio: 'inherit' });
  }

  // If on macOS, also try to build for Windows (requires wine)
  if (platform === 'darwin') {
    console.log('🍷 Attempting to build Windows version...');
    try {
      execSync('electron-builder --win', { stdio: 'inherit' });
    } catch (winError) {
      console.log('ℹ️  Windows build skipped (requires Wine on macOS)');
    }
  }

  console.log('\n✅ Desktop build completed successfully!');
  
  // List generated files
  console.log('\n📁 Generated files:');
  const distFiles = fs.readdirSync('dist');
  distFiles.forEach(file => {
    const filePath = path.join('dist', file);
    const stats = fs.statSync(filePath);
    const sizeInMB = (stats.size / 1024 / 1024).toFixed(2);
    console.log(`   ${file} (${sizeInMB} MB)`);
  });

} catch (error) {
  console.error('❌ Desktop build failed:', error.message);
  process.exit(1);
}

console.log('\n🎉 Build process completed!');
console.log('📂 Check the "dist" folder for your desktop applications.');