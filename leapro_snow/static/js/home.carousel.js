



var setup_carousel = function  (carousel) {
    for (var i = 0; i < carousel.length; i++) {
        $('#myCarousel ol').append('<li data-target="#myCarousel" data-slide-to="'+i+'"></li>')
        $('#myCarousel .carousel-inner').append(
            '<div class="item fill" style="background-image:url('+carousel[i].url+');">'+
                '<div class="container">'+
                '<div class="carousel-caption">'+
                    '<h2>'+ carousel[i].text +'</h2>'+
                '</div>'+
            '</div>'
        )

    };
}
setup_carousel(window.carousel)

$('#myCarousel li:first').addClass('active')
$('.carousel-inner div:first').addClass('active')

$('.carousel').carousel({
    interval: 5000 //changes the speed
})
