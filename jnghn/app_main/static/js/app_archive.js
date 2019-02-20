$(document).ready(function() {
    $(".nation").change(function() {
        console.log($(".nation").val());
        if ($(".nation").val() == "Costa_Rica") {
            $('')
        }
    });
});

function boardSubmitCheck(){
    if ($('.title').val() == "") {
        alert('Type the title')
        return false;
    }
    return true
}