const category_button = document.querySelector('.catalog-menu-list>li');
const sub_menu = document.querySelector('.catalog-sub-menu-list');

category_button.addEventListener('click', function() {  
    sub_menu.classList.toggle('catalog-sub-menu-list-toggle');
});