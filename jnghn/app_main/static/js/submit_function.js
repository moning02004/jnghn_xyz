$(function() {
    // post submit
    $('input[value="Save"]').click(function() {
      var str = $('textarea').val();
      console.log("STR : " + typeof(str));
      for(var i = 0; i != 10; i++) {
        console.log(str.charAt(i) == "\n");
      }
      console.log("STR : " + str.search("\n"));
      console.log("STR : " + str);

        if (confirm("저장할까요?")){
            if ($('input[name="title"]').val() == "" || $('input[name="day_from"]').val() == "" || $('input[name="where"]').val() == "") {
                alert("내용을 모두 입력하고 저장을 클릭하세요!");
                return false;
            } else if($("input[name=password]").length < 5 && $("input[name=password_check]").val() != $("input[name=password]").val()) {
                alert("설정된 비밀번호가 서로 다르거나 유효하지 않아요!")
                return false;
            }
            return true;
        }
        return false;
    });

    // register button
    $('input[value="Create Account"]').click(function() {
        if ($('input[name="name"]').val() != "" && $('input[name="email"]').val() != "") {
            if ($('.check_username i').hasClass('fa fa-check')) {
                if ($('.input-password i').hasClass('fa-check') && $('.input-re-password i').hasClass('fa-check')) {
                    if (confirm("가입하실건가요?")) {
                        return true;
                    }
                }
            }
        }
        alert("Type the information Correctly! :(");
        return false;
    });
});
