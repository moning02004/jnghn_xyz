const DAY = 86400000;
$(document).ready(function() {
    var content = $('.field').html();
    var cost_content = $('.cost-field').html();
    $('.button-p').click(function() {
        $('.field').append(content);
    });
    $('.button-m').click(function() {
        if ($('.field > div').length > 1) {
            $('div').remove('.field > div:last');
        }
    });
    $('.button-cp').click(function() {
        $('.cost-field').append(cost_content);
    });
    $('.button-cm').click(function() {
        if ($('.cost-field > div').length > 1) {
            $('div').remove('.cost-field > div:last');
        }
    });

    var field_array = [];
    for (var i=0; i<$('#contents > div').length; i++) {
        field_array.push($('.field'+i).html());
        $('.button'+i+'-p').click(function() {
            $('.field'+$(this).parent().attr('id')).append(field_array[$(this).parent().attr('id')]);
        });
        $('.button'+i+'-m').click(function() {
            if ($('.field'+$(this).parent().attr('id')+ ' > div').length > 1) {
                console.log($(this).parent().attr('id'));
                $('div').remove('.field'+$(this).parent().attr('id')+' > div:last');
            }
        });
    }

    $('.button-prev').click(function() {
        if (confirm("계속하시겠습니까?")){
            return true;
        }
        return false;
    });

    $('input[name="day_from"]').change(function() {
        let day_to = new Date(new Date($('input[name="day_from"]').val()).getTime() + ($('#contents > div').length-1)*DAY);

        let month = day_to.getMonth() + 1;
        let day = day_to.getDate();
        if (month < 10) month = '0' + month
        if (day < 10) day = '0' + day

        $('input[name="day_to"]').val(day_to.getFullYear() + "-" + month + "-" + day);
    });
});