$(function() {
    // ============================================================================================================== //
    // ===============<< Plan >>=============== //
    // ======================================== //
    //

    // new page's Back button
    $('.button-prev').click(function() {
        if (confirm("계속할거에요?")){
            return true;
        }
        return false;
    });

    // Plan new page's todo list plus/minus button
    var field_array = [];
    for (var i=0; i<$('#contents > div').length; i++) {
        field_array.push($('.field'+i).html());
        $('.button'+i+'-p').click({param1: ".field" + $('.button'+i+'-p').parent().attr('id'), param2: field_array[$('.button'+i+'-p').parent().attr('id')]}, itemAppend);
        $('.button'+i+'-m').click({param1: ".field" + $('.button'+i+'-m').parent().attr('id')}, itemRemove);
    }

    // In plan/review/drive new page, plus/minus button
    var content = $('.field').html();
    $('.button-p').click({param1: ".field", param2: content}, itemAppend);
    $('.button-m').click({param1: ".field"}, itemRemove);

    $('.button-d').click(function() {
        if (confirm("되돌릴 수 없는데 계속 할 거에요?")) {
            return true;
        }
        return false;
    });

    // plan's finish button
    $('.button-f').click(planFinish);

    // ============================================================================================================== //
    // ===============<< Review>>=============== //
    // ======================================== //
    //
    // In review new page, cost plus/minus button
    var cost_content = $('.cost-field').html();
    $('.button-cp').click({param1: ".cost-field", param2: cost_content}, itemAppend);
    $('.button-cm').click({param1: ".cost-field"}, itemRemove);

    // ============================================================================================================== //
    // ===============<< Others >>=============== //
    // ======================================== //
    //
    // back button
    $('.button-go-back').click(function() {
        window.history.back();
    });
    // delete button
    $('.button-delete').click(planFinish);

    // account edit button
    $('.account_book-toggle').click(function() {
        if ($(".account_book-toggle > i").hasClass("fa-toggle-off")){
            $(".account_book-toggle > i").removeClass("fa-toggle-off");
            $(".account_book-toggle > i").addClass("fa-toggle-on");
            $(".table-account tr th:last-child").removeAttr("hidden");
            $(".table-account tr td:last-child").removeAttr("hidden");
        } else {
            $(".account_book-toggle > i").removeClass("fa-toggle-on");
            $(".account_book-toggle > i").addClass("fa-toggle-off");
            $(".table-account tr th:last-child").attr("hidden", "");
            $(".table-account tr td:last-child").attr("hidden", "");
        }
    });


});
function planFinish() {
    var alphabet = 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789';
    var correct = [];
    for (var i = 0; i<5; i++) correct.push(alphabet[Math.floor(Math.random()*alphabet.length)]);

    answer = prompt("자동 방지입니다. 다음 문자를 입력하시오\n >> "+ correct.join(""));
    if (answer == correct.join("")) return true;
    return false;
}

function itemAppend(event) {
    $(event.data.param1).append(event.data.param2);
}
function itemRemove(event) {
    console.log(event.data.param1);
    if ($(event.data.param1 + ' > div').length > 1) {
        $(event.data.param1 + ' > div').remove(':last');
    }
}