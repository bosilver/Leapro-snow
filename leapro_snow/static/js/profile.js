


$(document).ready(function(){

    $('img #profile-img').css({'width':'550px', 'heigh':'550px'})

    var profile = description.split('&')
    for (var i = 0; i < profile.length; i++) {
        if (i == 0) {
            $('#profile-img').attr('src', profile[i])
        }
        else {
            $('#profile'+i).text(profile[i])
        };
    };
});
