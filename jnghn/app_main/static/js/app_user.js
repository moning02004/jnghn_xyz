$(function() {
    $('.password').keyup(function() {
        var pattern = /^(?=.*[0-9])(?=.*[a-z]).{8,16}/;
        if (pattern.test($('.password').val())){
            $('.input-password i').removeClass('fa fa-exclamation');
            $('.input-password i').addClass('fa fa-check');
            $('.input-password i').css({"color": "rgb(208, 208, 0)"});
        } else {
            $('.input-password i').removeClass('fa fa-check');
            $('.input-password i').addClass('fa fa-exclamation');
            $('.input-password i').css({"color": "red"});
        }
        if ($('.password').val() == $('.re-password').val()){
            $('.input-re-password i').removeClass('fa fa-exclamation');
            $('.input-re-password i').addClass('fa fa-check');
            $('.input-re-password i').css({"color": "rgb(208, 208, 0)"});
        } else {
            $('.input-re-password i').removeClass('fa fa-check');
            $('.input-re-password i').addClass('fa fa-exclamation');
            $('.input-re-password i').css({"color": "red"});
        }
    });
    $('.re-password').keyup(function() {
        var pattern = /^(?=.*[0-9])(?=.*[a-z]).{8,16}/;
        if ($('.password').val() == $('.re-password').val()){
            $('.input-re-password i').removeClass('fa fa-exclamation');
            $('.input-re-password i').addClass('fa fa-check');
            $('.input-re-password i').css({"color": "rgb(208, 208, 0)"});
        } else {
            $('.input-re-password i').removeClass('fa fa-check');
            $('.input-re-password i').addClass('fa fa-exclamation');
            $('.input-re-password i').css({"color": "red"});
        }
    });
    $('input[name="username"]').change(function() {
        $('.check_username i').removeClass('fa-check');
        $('.check_username i').addClass('fa-user');
        $('.check_username i').css("color", "black");
    });
});