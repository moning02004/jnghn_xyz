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
    $('.button-d').click(function() {
        if (!confirm("되돌릴 수 없는데 계속 할 거에요?")) {
            return false;
        }
        return true;
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
                $('div').remove('.field'+$(this).parent().attr('id')+' > div:last');
            }
        });
    }

    $('.button-prev').click(function() {
        if (confirm("계속할거에요?")){
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

    $('.button-f').click(function() {
        var alphabet = 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ0123456789';
        var correct = [];
        for (var i = 0; i<5; i++) correct.push(alphabet[Math.floor(Math.random()*alphabet.length)]);

        answer = prompt("다음 문자를 입력하시오\n"+ correct.join(""));
        if (answer == correct.join("")) return true;
        return false;
    });
});

function newSubmit() {
    if (confirm("저장할까요?")){
        if ($('input[name="title"]').val() == "" || $('input[name="day_from"]').val() == "" || $('input[name="where"]').val() == "") {
            alert("내용을 모두 입력하고 저장을 클릭하세요");
            return false;
        }
        return true;
    }
    return false;
}