document.addEventListener("DOMContentLoaded", () => {
    const navbar = document.getElementById('main-navbar');
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const hamburgerLines = mobileMenuBtn.querySelectorAll('.hamburger-line');
    
    // Mobile Menu
    let isMenuOpen = false;

    function toggleMobileMenu() {
        isMenuOpen = !isMenuOpen;
        navbar.setAttribute('data-menu-open', isMenuOpen);
        
        if (isMenuOpen) {
            mobileMenu.classList.remove('invisible', '-translate-y-4', 'opacity-0');
            mobileMenu.classList.add('visible', 'translate-y-0', 'opacity-100');
            
            // Animate hamburger -> X
            hamburgerLines[0].classList.replace('-translate-y-1.5', 'rotate-45');
            hamburgerLines[1].classList.add('opacity-0');
            hamburgerLines[2].classList.replace('translate-y-1.5', '-rotate-45');
        } else {
            mobileMenu.classList.remove('visible', 'translate-y-0', 'opacity-100');
            mobileMenu.classList.add('invisible', '-translate-y-4', 'opacity-0');
            
            // Animate X -> hamburger
            hamburgerLines[0].classList.replace('rotate-45', '-translate-y-1.5');
            hamburgerLines[1].classList.remove('opacity-0');
            hamburgerLines[2].classList.replace('-rotate-45', 'translate-y-1.5');
        }
    }

    mobileMenuBtn.addEventListener('click', toggleMobileMenu);

    document.querySelectorAll('.mobile-link').forEach(link => {
        link.addEventListener('click', () => {
            if (isMenuOpen) toggleMobileMenu();
        });
    });

    const dropdownContainers = document.querySelectorAll('.mobile-dropdown-container');
    
    dropdownContainers.forEach(container => {
        const btn = container.querySelector('.mobile-dropdown-btn');
        const content = container.querySelector('.dropdown-content');
        const chevron = container.querySelector('.chevron');
        
        btn.addEventListener('click', () => {
            const isOpen = container.getAttribute('data-dropdown-open') === 'true';
            
            dropdownContainers.forEach(otherContainer => {
                if (otherContainer !== container) {
                    otherContainer.setAttribute('data-dropdown-open', 'false');
                    otherContainer.querySelector('.dropdown-content').classList.replace('max-h-[1000px]', 'max-h-0');
                    otherContainer.querySelector('.dropdown-content').classList.replace('opacity-100', 'opacity-0');
                    otherContainer.querySelector('.chevron').classList.remove('rotate-90');
                }
            });

            container.setAttribute('data-dropdown-open', !isOpen);
            
            if (!isOpen) {
                content.classList.replace('max-h-0', 'max-h-[1000px]');
                content.classList.replace('opacity-0', 'opacity-100');
                chevron.classList.add('rotate-90');
            } else {
                content.classList.replace('max-h-[1000px]', 'max-h-0');
                content.classList.replace('opacity-100', 'opacity-0');
                chevron.classList.remove('rotate-90');
            }
        });
    });
});
