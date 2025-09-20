const { contextBridge, ipcRenderer } = require('electron');

// Expose protected methods that allow the renderer process to use
// specific electron APIs without exposing the entire API
contextBridge.exposeInMainWorld('electron', {
  // Broadcasting transactions only - no private key operations here
  broadcastTransaction: (txData) => ipcRenderer.invoke('broadcast-transaction', txData),
  
  // Only expose what's necessary - security by design
  getAppVersion: () => ipcRenderer.invoke('get-app-version'),
  checkForUpdates: () => ipcRenderer.send('check-for-updates'),
  
  // Event handlers
  onUpdateAvailable: (callback) => ipcRenderer.on('update-available', callback),
  onUpdateDownloaded: (callback) => ipcRenderer.on('update-downloaded', callback),
  
  // Token data persistence
  exportTokens: () => ipcRenderer.invoke('export-tokens'),
  saveTokenData: (data) => ipcRenderer.invoke('save-token-data', data),
  importTokens: () => ipcRenderer.invoke('import-tokens'),
  
  // App data directory storage
  saveToAppData: (data) => ipcRenderer.invoke('save-to-app-data', data),
  loadFromAppData: (data) => ipcRenderer.invoke('load-from-app-data', data),
  
  // Never expose anything related to private keys or wallet generation
  // Those operations are handled entirely in the renderer process
  // with no IPC communication for security
});
