const { app, BrowserWindow, ipcMain, dialog } = require('electron');
const path = require('path');
const isDev = require('electron-is-dev');
const { autoUpdater } = require('electron-updater');
const log = require('electron-log');
const fs = require('fs');
const os = require('os');

// Configure logging
log.transports.file.level = 'info';
autoUpdater.logger = log;

let mainWindow;

function createWindow() {
  // Create the browser window.
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      enableRemoteModule: false,
      preload: path.join(__dirname, 'preload.js'),
    },
  });

  // Load the app
  const startUrl = isDev
    ? 'http://localhost:3000'
    : `file://${path.join(__dirname, '../build/index.html')}`;

  mainWindow.loadURL(startUrl);

  // Open DevTools automatically if in development
  if (isDev) {
    mainWindow.webContents.openDevTools({ mode: 'detach' });
  }

  // Handle window closed
  mainWindow.on('closed', () => {
    mainWindow = null;
  });

  // Check for updates if not in dev mode
  if (!isDev) {
    autoUpdater.checkForUpdatesAndNotify();
  }
}

// Create window when Electron is ready
app.whenReady().then(createWindow);

// Quit when all windows are closed
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});

// Auto-updater events
autoUpdater.on('update-available', () => {
  log.info('Update available');
});

autoUpdater.on('update-downloaded', () => {
  log.info('Update downloaded');
});

// IPC event handlers for secure transaction broadcasting
ipcMain.handle('broadcast-transaction', async (event, txData) => {
  log.info('Broadcast transaction request received');
  // Implementation of secure transaction broadcasting would go here
  return { success: true, message: 'Transaction broadcast (simulated)' };
});

// Get app version
ipcMain.handle('get-app-version', () => {
  return app.getVersion();
});

// Get application data path
const getAppDataPath = () => {
  const userDataPath = app.getPath('userData');
  const coldWalletDataPath = path.join(userDataPath, 'ColdWalletData');
  
  // Create the directory if it doesn't exist
  if (!fs.existsSync(coldWalletDataPath)) {
    fs.mkdirSync(coldWalletDataPath, { recursive: true });
  }
  
  return coldWalletDataPath;
};

// Token data export/import handlers
ipcMain.handle('export-tokens', async () => {
  try {
    const result = await dialog.showSaveDialog({
      title: 'Export Token Data',
      defaultPath: path.join(os.homedir(), 'Documents', 'cold-wallet-tokens.json'),
      buttonLabel: 'Export',
      filters: [
        { name: 'JSON Files', extensions: ['json'] }
      ]
    });
    
    if (result.canceled) {
      return { success: false, message: 'Export cancelled' };
    }
    
    // The renderer process will provide the token data to write
    return { 
      success: true, 
      filePath: result.filePath
    };
  } catch (error) {
    log.error('Error in export-tokens:', error);
    return { 
      success: false, 
      message: `Export failed: ${error.message}` 
    };
  }
});

ipcMain.handle('save-token-data', async (event, { filePath, data }) => {
  try {
    fs.writeFileSync(filePath, data, 'utf-8');
    return { success: true, message: 'Token data saved successfully' };
  } catch (error) {
    log.error('Error in save-token-data:', error);
    return { 
      success: false, 
      message: `Failed to save token data: ${error.message}` 
    };
  }
});

ipcMain.handle('import-tokens', async () => {
  try {
    const result = await dialog.showOpenDialog({
      title: 'Import Token Data',
      buttonLabel: 'Import',
      filters: [
        { name: 'JSON Files', extensions: ['json'] }
      ],
      properties: ['openFile']
    });
    
    if (result.canceled || result.filePaths.length === 0) {
      return { success: false, message: 'Import cancelled' };
    }
    
    const filePath = result.filePaths[0];
    const fileContent = fs.readFileSync(filePath, 'utf-8');
    
    // Try to parse the content as JSON to validate it
    const tokenData = JSON.parse(fileContent);
    
    // Basic validation
    if (!Array.isArray(tokenData)) {
      throw new Error('Invalid token data format');
    }
    
    return { 
      success: true, 
      data: tokenData 
    };
  } catch (error) {
    log.error('Error in import-tokens:', error);
    return { 
      success: false, 
      message: `Import failed: ${error.message}` 
    };
  }
});

// Save to app data directory
ipcMain.handle('save-to-app-data', async (event, { fileName, data }) => {
  try {
    const filePath = path.join(getAppDataPath(), fileName);
    fs.writeFileSync(filePath, data, 'utf-8');
    return { success: true, filePath };
  } catch (error) {
    log.error('Error saving to app data:', error);
    return { success: false, message: error.message };
  }
});

// Load from app data directory
ipcMain.handle('load-from-app-data', async (event, { fileName }) => {
  try {
    const filePath = path.join(getAppDataPath(), fileName);
    if (!fs.existsSync(filePath)) {
      return { success: false, message: 'File does not exist' };
    }
    
    const data = fs.readFileSync(filePath, 'utf-8');
    return { success: true, data };
  } catch (error) {
    log.error('Error loading from app data:', error);
    return { success: false, message: error.message };
  }
});
// These will be implemented in a secure manner to ensure private keys never leave the device
