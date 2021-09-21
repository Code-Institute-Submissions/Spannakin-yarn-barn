if (document.querySelector('#burger')) {
    const burgerIcon = document.querySelector('#burger');
    const navbarMenu = document.querySelector('#navbar-links');

    burgerIcon.addEventListener('click', () => {
        navbarMenu.classList.toggle('is-active')
    });
 }
