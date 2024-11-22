const burgerMenu = document.querySelector('#burgerMenu');
const burgerToggle = document.querySelector('#burgerToggle');

burgerToggle.addEventListener('click', () => {
    burgerMenu.classList.toggle('hidden');
});

window.addEventListener('resize', () => {
    if (window.innerWidth >= 1280){
        burgerMenu.classList.add('hidden');
    } 
});