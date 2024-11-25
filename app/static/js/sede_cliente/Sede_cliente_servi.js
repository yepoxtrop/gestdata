document.addEventListener('DOMContentLoaded', function () {
    const hamburgerMenu = document.getElementById('hamburger-menu');
    const menu = document.getElementById('menu');
    const overlay = document.getElementById('overlay');
    const closeMenuBtn = document.getElementById('close-menu');
    const logoutButton = document.getElementById('logout-button');

    function toggleMenu() {
        const isOpen = menu.classList.toggle('open');
        overlay.classList.toggle('show');
        hamburgerMenu.style.display = isOpen ? 'none' : 'block'; 
        logoutButton.style.display = isOpen ? 'none' : 'block';
    }

    hamburgerMenu.addEventListener('click', toggleMenu);
    closeMenuBtn.addEventListener('click', toggleMenu);

    overlay.addEventListener('click', function () {
        menu.classList.remove('open');
        overlay.classList.remove('show');
        hamburgerMenu.style.display = 'block';
        logoutButton.style.display = 'block';
    });

    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') {
            menu.classList.remove('open');
            overlay.classList.remove('show');
            hamburgerMenu.style.display = 'block';
            logoutButton.style.display = 'block';
        }
    });

    window.addEventListener('resize', function () {
        if (window.innerWidth > 1018) {
            menu.classList.remove('open');
            overlay.classList.remove('show');
            hamburgerMenu.style.display = 'block';
            logoutButton.style.display = 'block';
        } else {
            if (menu.classList.contains('open')) {
                logoutButton.style.display = 'none'; 
            } else {
                logoutButton.style.display = 'block';
            }
        }
    });
});
