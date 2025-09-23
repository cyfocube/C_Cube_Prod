/**
 * TokenStorage.js
 * Utility for persistent storage of token data in the Cold Wallet app
 */

import EnvironmentDetection from './EnvironmentDetection';

// Detect if we're in an Electron environment
const isElectron = () => {
  return EnvironmentDetection.isElectron();
};

class TokenStorage {
  /**
   * Save tokens to persistent storage
   * @param {Array} tokens - Array of token objects to save
   * @returns {Promise} - Result of the save operation
   */
  static async saveTokens(tokens) {
    if (isElectron()) {
      try {
        // First save to app data directory for regular persistence
        await window.electron.saveToAppData({
          fileName: 'user-tokens.json',
          data: JSON.stringify(tokens)
        });
        
        // Also save to localStorage as backup
        localStorage.setItem('userTokens', JSON.stringify(tokens));
        
        return { success: true };
      } catch (error) {
        console.error('Failed to save tokens to app data:', error);
        
        // Fall back to localStorage
        localStorage.setItem('userTokens', JSON.stringify(tokens));
        return { 
          success: false, 
          fallbackSuccess: true,
          message: 'Saved to localStorage only' 
        };
      }
    } else {
      // Web mode - use localStorage only
      localStorage.setItem('userTokens', JSON.stringify(tokens));
      return { success: true };
    }
  }

  /**
   * Load tokens from persistent storage
   * @returns {Promise<Array>} - Array of token objects
   */
  static async loadTokens() {
    if (isElectron()) {
      try {
        // Try to load from app data directory first
        const result = await window.electron.loadFromAppData({
          fileName: 'user-tokens.json'
        });
        
        if (result.success) {
          return JSON.parse(result.data);
        }
        
        // Fall back to localStorage if app data load failed
        const savedTokens = localStorage.getItem('userTokens');
        return savedTokens ? JSON.parse(savedTokens) : [];
      } catch (error) {
        console.error('Failed to load tokens from app data:', error);
        
        // Fall back to localStorage
        const savedTokens = localStorage.getItem('userTokens');
        return savedTokens ? JSON.parse(savedTokens) : [];
      }
    } else {
      // Web mode - use localStorage only
      const savedTokens = localStorage.getItem('userTokens');
      return savedTokens ? JSON.parse(savedTokens) : [];
    }
  }

  /**
   * Export tokens to a user-selected file
   * @param {Array} tokens - Array of token objects to export
   * @returns {Promise} - Result of the export operation
   */
  static async exportTokens(tokens) {
    if (!isElectron()) {
      throw new Error('Token export is only available in the desktop app');
    }

    try {
      // First get file path from dialog
      const exportResult = await window.electron.exportTokens();
      
      if (!exportResult.success) {
        return exportResult;
      }
      
      // Then save data to that path
      const saveResult = await window.electron.saveTokenData({
        filePath: exportResult.filePath,
        data: JSON.stringify(tokens, null, 2) // Pretty print with indentation
      });
      
      return saveResult;
    } catch (error) {
      console.error('Token export failed:', error);
      return {
        success: false,
        message: `Export failed: ${error.message}`
      };
    }
  }

  /**
   * Import tokens from a user-selected file
   * @returns {Promise<Object>} - Result with imported tokens if successful
   */
  static async importTokens() {
    if (!isElectron()) {
      throw new Error('Token import is only available in the desktop app');
    }

    try {
      return await window.electron.importTokens();
    } catch (error) {
      console.error('Token import failed:', error);
      return {
        success: false,
        message: `Import failed: ${error.message}`
      };
    }
  }
}

export default TokenStorage;
