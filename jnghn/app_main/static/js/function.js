$('document').ready(function() {
    $('.search-icon').click(function() {
        if ($('.search-icon').val() != 'hiddena') {
            $('.search-icon').val('hiddena')
            $('.search-content').removeClass('hiddena');
            $('.search-content').addClass('showa');
        } else {
            $('.search-icon').val('showa')
            $('.search-content').removeClass('showa');
            $('.search-content').addClass('hiddena');
        }
    });

    $('.day-content').find("#"+$('.day-select option:selected').val()).removeClass('hiddena');
    $('.day-select').change(function() {
        console.log($('.day-select option:selected').val());
        console.log($('.day-content').children().parent().html());
        $('.day-content').children().addClass('hiddena');
        $('.day-content').find("#"+$('.day-select option:selected').val()).removeClass('hiddena');
    });
});

function newWindow(fileUrl){
    window.open(fileUrl, "", "width=480, height=600");
    return false;
}