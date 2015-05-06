



var setup_carousel = function  (carousel) {
    for (var i = 0; i < carousel.length; i++) {
        $('#myCarousel ol').append('<li data-target="#myCarousel" data-slide-to="'+i+'"></li>')
        $('#myCarousel .carousel-inner').append(
            '<div class="item">'+
                '<img src="'+carousel[i].url+'" class="img-responsivex">'+
                '<div class="container">'+
                    '<div class="carousel-caption">'+
                        '<h2>'+ carousel[i].text +'</h2>'+
                    '</div>'+
                '</div>'+
            '</div>'
        )

    };
}
setup_carousel(window.carousel)

$('#myCarousel li:first').addClass('active')
$('.carousel-inner div:first').addClass('active')


jQuery(document).ready(function() {
    $('.carousel').carousel({
        pause: "false",
        interval: 7000
    });

    $('.carousel').css({'margin': 0, 'width': $(window).outerWidth(), 'height': $(window).outerHeight()});
    $('.carousel .item').css({'position': 'fixed', 'width': '100%', 'height': '100%'});
    $('.carousel-inner div.item img').each(function() {
        var imgSrc = $(this).attr('src');
        $(this).parent().css({'background': 'url('+imgSrc+') center center no-repeat', '-webkit-background-size': '100% ', '-moz-background-size': '100%', '-o-background-size': '100%', 'background-size': '100%', '-webkit-background-size': 'cover', '-moz-background-size': 'cover', '-o-background-size': 'cover', 'background-size': 'cover'});
        $(this).remove();
    });

    $(window).on('resize', function() {
        $('.carousel').css({'width': $(window).outerWidth(), 'height': $(window).outerHeight()});
    });
});
