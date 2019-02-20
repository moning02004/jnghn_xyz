$(document).ready(function() {
    var content = $('.field').html();
    $('.button-p').click(function() {
        $('.field').append(content);
    });
    $('.button-m').click(function() {
        if ($('.field > div').length > 1) {
            $('div').remove('.field > div:last');
        }
    });
});