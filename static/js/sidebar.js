$('.menu-btn').on('click', function (e) {
    e.preventDefault();
    $('.menu').toggleClass('menu_active');
    $('.content').toggleClass('content_active');
})

$('.wrapper').on('click', function (e) {
    e.preventDefault();
    $('.menu').removeClass('menu_active');
    $('.content').removeClass('content_active');
})