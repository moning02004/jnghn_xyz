$('document').ready(function() {

    $('body').contextmenu(function() {
        return false;
    });
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
        console.log($('.day-content').find("#"+$('.day-select option:selected').val()).html());
        $('.day-content').children().addClass('hiddena');
        $('.day-content').find("#"+$('.day-select option:selected').val()).removeClass('hiddena');
    });



    // click the delete button
    $('.button-delete').click(function() {
        if (confirm("삭제하면 복구가 불가능합니다. 정말 삭제하시겠습니까?")) {
            var alphabet = 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789';
            var correct = [];
            for (var i = 0; i<5; i++) correct.push(alphabet[Math.floor(Math.random()*alphabet.length)]);

            answer = prompt("다음 문자를 입력하시오\n"+ correct.join(""));
            if (answer == correct.join("")) return true;
        }
        return false;
    });

    //
    $('.ab-toggle').click(function() {
        if ($(".ab-toggle > i").hasClass("fa-toggle-off")){
            $(".ab-toggle > i").removeClass("fa-toggle-off");
            $(".ab-toggle > i").addClass("fa-toggle-on");
            console.log($(".table-account tr td:last-child").html());
            $(".table-account tr th:last-child").removeAttr("hidden")
            $(".table-account tr td:last-child").removeAttr("hidden")
        } else {
            $(".ab-toggle > i").removeClass("fa-toggle-on");
            $(".ab-toggle > i").addClass("fa-toggle-off");
            $(".table-account tr th:last-child").attr("hidden", "")
            $(".table-account tr td:last-child").attr("hidden", "")
        }
    });
});

function newWindow(fileUrl){
    window.open(fileUrl, "", "width=480, height=600");
    return false;
}