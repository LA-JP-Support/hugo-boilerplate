/**
 * Back to Top Button Functionality
 * Handles the visibility and scroll behavior of the back-to-top button.
 */
document.addEventListener('DOMContentLoaded', () => {
  const backToTopBtn = document.getElementById('back-to-top-btn');
  
  if (!backToTopBtn) return;

  const scrollThreshold = 300; // Show button after scrolling this many pixels

  const toggleVisibility = () => {
    if (window.scrollY > scrollThreshold) {
      backToTopBtn.classList.remove('translate-y-12', 'opacity-0', 'invisible');
      backToTopBtn.classList.add('translate-y-0', 'opacity-100', 'visible');
    } else {
      backToTopBtn.classList.remove('translate-y-0', 'opacity-100', 'visible');
      backToTopBtn.classList.add('translate-y-12', 'opacity-0', 'invisible');
    }
  };

  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  };

  // Throttle scroll event for better performance
  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(() => {
        toggleVisibility();
        ticking = false;
      });
      ticking = true;
    }
  });

  backToTopBtn.addEventListener('click', (e) => {
    e.preventDefault();
    scrollToTop();
  });
});
