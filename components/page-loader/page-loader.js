if (sessionStorage.getItem('hasSeenLoader')) {
    document.documentElement.classList.add('skip-loader');
  }

const scriptStartTime = Date.now();
  const minimumLoaderTime = 2000; 

  window.addEventListener('load', () => {
    if (document.documentElement.classList.contains('skip-loader')) {
      return; 
    }

    const svgElement = document.querySelector('.draw-svg');
    const loaderOverlay = document.getElementById('page-loader-overlay');

    const timeElapsed = Date.now() - scriptStartTime;
    const timeRemaining = Math.max(0, minimumLoaderTime - timeElapsed);

    setTimeout(() => {
      svgElement.classList.add('is-loaded');
      
      setTimeout(() => {
        loaderOverlay.classList.add('fade-out');
        
        setTimeout(() => {
          loaderOverlay.remove();
          sessionStorage.setItem('hasSeenLoader', 'true');
        }, 800); 

      }, 1000); 

    }, timeRemaining);
  });

