// Environment detection utilities for C-Cube
export const isElectron = () => {
  return window && window.electron;
};

export const isWeb = () => {
  return !isElectron();
};

export const isMobile = () => {
  return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
};

export const isLocalhost = () => {
  return Boolean(
    window.location.hostname === 'localhost' ||
    window.location.hostname === '[::1]' ||
    window.location.hostname.match(
      /^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/
    )
  );
};

export const getPlatform = () => {
  if (isElectron()) return 'electron';
  if (isMobile()) return 'mobile';
  return 'web';
};

export const getStorageType = () => {
  if (isElectron()) return 'electron-store';
  return 'localStorage';
};

// Web-specific storage limitations warning
export const showWebStorageWarning = () => {
  if (isWeb() && !localStorage.getItem('webStorageWarningShown')) {
    console.warn('⚠️ C-Cube Web Version: Data is stored in browser localStorage. For production use, consider the desktop application for enhanced security.');
    localStorage.setItem('webStorageWarningShown', 'true');
  }
};

// Check if running in a secure context (HTTPS)
export const isSecureContext = () => {
  return window.isSecureContext || isLocalhost();
};

// Main environment info function
export const getEnvironmentInfo = () => {
  return {
    isElectron: isElectron(),
    isWeb: isWeb(),
    isMobile: isMobile(),
    isLocalhost: isLocalhost(),
    platform: getPlatform(),
    storageType: getStorageType(),
    isSecureContext: isSecureContext()
  };
};

export default {
  isElectron,
  isWeb,
  isMobile,
  isLocalhost,
  getPlatform,
  getStorageType,
  showWebStorageWarning,
  isSecureContext,
  getEnvironmentInfo
};