// Utility functions for handling URL hashes and smooth scrolling to sections

export const scrollToSection = (sectionId, offset = 80) => {
  const element = document.getElementById(sectionId);
  if (element) {
    const elementPosition = element.getBoundingClientRect().top;
    const offsetPosition = elementPosition + window.pageYOffset - offset;

    window.scrollTo({
      top: offsetPosition,
      behavior: 'smooth'
    });
  }
};

export const updateUrlHash = (hash) => {
  // Update URL hash without triggering page reload
  if (hash) {
    window.history.replaceState(null, null, `#${hash}`);
  } else {
    // Remove hash if hash is empty
    window.history.replaceState(null, null, window.location.pathname);
  }
};

export const getHashFromUrl = () => {
  return window.location.hash.substring(1); // Remove the # symbol
};

export const handleHashNavigation = () => {
  const hash = getHashFromUrl();
  if (hash) {
    // Small delay to ensure the DOM is fully rendered
    setTimeout(() => {
      scrollToSection(hash);
    }, 100);
  }
};

// Create section ID from section name (convert to lowercase, replace spaces with hyphens)
export const createSectionId = (sectionName) => {
  return sectionName.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '');
};

// Convert section ID back to display name
export const getSectionDisplayName = (sectionId) => {
  return sectionId.split('-').map(word => 
    word.charAt(0).toUpperCase() + word.slice(1)
  ).join(' ');
};