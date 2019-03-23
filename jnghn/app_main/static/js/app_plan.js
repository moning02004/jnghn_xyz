const DAY = 86400000;
$(document).ready(function() {
    $('input[name="day_from"]').change(function() {
        let day_to = new Date(new Date($('input[name="day_from"]').val()).getTime() + ($('#contents > div').length-1)*DAY);
        let month = day_to.getMonth() + 1;
        let day = day_to.getDate();
        if (month < 10) month = '0' + month
        if (day < 10) day = '0' + day

        $('input[name="day_to"]').val(day_to.getFullYear() + "-" + month + "-" + day);
    });
});
