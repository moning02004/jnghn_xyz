$(document).ready(function() {
    $('.password').keyup(function() {
        var pattern = /^(?=.*[0-9])(?=.*[a-z]).{8,16}/;
        if (pattern.test($('.password').val())){
            $('.input-password i').removeClass('fa fa-exclamation');
            $('.input-password i').addClass('fa fa-check');
            $('.input-password i').css({"color": "rgb(208, 208, 0)"});
            $('.password-message').html('Great!');
        } else {
            $('input[name="passwordCheck"]').val('not');
            $('.input-password i').removeClass('fa fa-check');
            $('.input-password i').addClass('fa fa-exclamation');
            $('.input-password i').css({"color": "red"});
            $('.password-message').html('Type the password correctly! (must include [0-9], [a-z])');
        }
        });
    $('.re-password').keyup(function() {
        var pattern = /^(?=.*[0-9])(?=.*[a-z]).{8,16}/;
        if ($('.password').val() == $('.re-password').val()){
            $('.input-re-password i').removeClass('fa fa-exclamation');
            $('.input-re-password i').addClass('fa fa-check');
            $('.input-re-password i').css({"color": "#dd0"});
            $('.re-password-message').html('Great!');
        } else {
            $('input[name="passwordCheck"]').val('not');
            $('.input-re-password i').removeClass('fa fa-check');
            $('.input-re-password i').addClass('fa fa-exclamation');
            $('.input-re-password i').css({"color": "red"});
            $('.re-password-message').html('Not Matched');
        }
    });
    $('.admin-delete').click(function() {
        if (confirm('정말 삭제하시겠습니까?\n(삭제하시면 되돌릴 수 없습니다)')){
            return true;
        }
        return false;
    });
});

function registerCheck() {
    if ($('input[name="usernameCheck"]').val() == "unavailable") {
        alert('Please click the confirm button');
        return false;
    }
    if ($('.password').val() != $('.re-password').val()) {
        alert('Please check password');
        return false
    }
    return true;
}