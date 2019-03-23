$(function() {
    //
    $('.auto-select').select();

    // search bar
    $('.search-icon').click(function() {
        if ($('.search-icon').val() != 'hidden-item') {
            $('.search-icon').val('hidden-item')
            $('.search-content').removeClass('hidden-item');
            $('.search-content').addClass('show-item');
        } else {
            $('.search-icon').val('show-item')
            $('.search-content').removeClass('show-item');
            $('.search-content').addClass('hidden-item');
        }
    });

    // plan detail
    $('.day-content').find("#"+$('.day-select option:selected').val()).removeClass('hidden-item');
    $('.day-select').change(function() {
        console.log($('.day-select option:selected').val());
        console.log($('.day-content').find("#"+$('.day-select option:selected').val()).html());
        $('.day-content').children().addClass('hidden-item');
        $('.day-content').find("#"+$('.day-select option:selected').val()).removeClass('hidden-item');
    });
});