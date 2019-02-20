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
    $('.delete-button').click(function() {
        if (confirm('정말로 삭제하시겠습니까\n(삭제된 후에는 수정을 취소하셔도 복구할 수 없습니다.)')){
            return true;
        }
        return false;
    });
    $('.comment-field').hide();
    $('.comment-button').click(function() {
        if ($('button[name="showComment"]').val() != "show") {
            $('button[name="showComment"]').val('show');
            $('.comment-field').show();
        } else {
            $('button[name="showComment"]').val('hide');
            $('.comment-field').hide();
        }
    });
});

function newWindow(fileUrl){
    window.open(fileUrl, "", "width=480, height=600");
    return false;
}