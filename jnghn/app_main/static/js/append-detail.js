$(document).ready(function() {
    var period = 0;
    $('.adapt-button').click(function() {
        var from = new Date($('input[name="from"]').val());
        var to = new Date($('input[name="to"]').val());
        console.log(from.getDate());
        console.log(to.getDate());

        if (to.getDate() - from.getDate() < 2) period = 2;
        else if (to.getDate() - from.getDate() > 10) period = 10;
        else period = to.getDate() - from.getDate() + 1;
        console.log(period);
    });

    var day_tab = $('.detail-tabs').html();
    var detail_tab = $('.detail-content').html();
});