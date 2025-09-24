#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

console.log('📋 Preparing build for electron-builder...\n');

// Copy electron files to build directory
const electronSource = 'electron';
const electronDest = 'build/electron';

if (!fs.existsSync('build')) {
  console.error('❌ Build directory not found. Run "npm run react-build" first.');
  process.exit(1);
}

// Create electron directory in build
if (!fs.existsSync(electronDest)) {
  fs.mkdirSync(electronDest, { recursive: true });
}

// Copy electron files
const electronFiles = fs.readdirSync(electronSource);
electronFiles.forEach(file => {
  const srcPath = path.join(electronSource, file);
  const destPath = path.join(electronDest, file);
  
  fs.copyFileSync(srcPath, destPath);
  console.log(`✅ Copied: ${file}`);
});

console.log('\n🎉 Build preparation completed!');