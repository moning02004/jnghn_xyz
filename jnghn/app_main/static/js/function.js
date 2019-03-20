$(function() {
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

    $('.day-content').find("#"+$('.day-select option:selected').val()).removeClass('hidden-item');
    $('.day-select').change(function() {
        console.log($('.day-select option:selected').val());
        console.log($('.day-content').find("#"+$('.day-select option:selected').val()).html());
        $('.day-content').children().addClass('hidden-item');
        $('.day-content').find("#"+$('.day-select option:selected').val()).removeClass('hidden-item');
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
    $('.account_book-toggle').click(function() {
        if ($(".account_book-toggle > i").hasClass("fa-toggle-off")){
            $(".account_book-toggle > i").removeClass("fa-toggle-off");
            $(".account_book-toggle > i").addClass("fa-toggle-on");
            console.log($(".table-account tr td:last-child").html());
            $(".table-account tr th:last-child").removeAttr("hidden")
            $(".table-account tr td:last-child").removeAttr("hidden")
        } else {
            $(".account_book-toggle > i").removeClass("fa-toggle-on");
            $(".account_book-toggle > i").addClass("fa-toggle-off");
            $(".table-account tr th:last-child").attr("hidden", "")
            $(".table-account tr td:last-child").attr("hidden", "")
        }
    });
});