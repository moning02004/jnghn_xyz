function checkPassword() {
    if ($('input[name="password1"]').val() != $('input[name="password2"]').val()) return false;
    if ($('input[name="password1"]').val() != "" && $('input[name="password2"]').val() == "") return false;
    if ($('input[name="password1"]').val() == "" && $('input[name="password2"]').val() != "") return false;
    return true
}