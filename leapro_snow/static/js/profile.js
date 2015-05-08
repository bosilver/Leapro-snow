


$(document).ready(function(){
    lines = want_to_say.split('\n');
    for (var i = 0; i < lines.length; i++) {
        $('#want_to_say').append("<p>"+ lines[i] + "</p>")
    };
    lines = cert.split('\n');
    for (var i = 0; i < lines.length; i++) {
        $('#cert').append("<li>"+ lines[i] + "</li>")
    };

});
