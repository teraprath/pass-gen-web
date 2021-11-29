function generate() {
    var form = document.getElementById("form");
    formData = new FormData(form);

    var length = formData.get("slider");

    if (formData.get("digits") == null) {
        var allow_digits = false;
    } else {
        var allow_digits = true;
    }

    if (formData.get("alphabets") == null) {
        var allow_alphabets = false;
    } else {
        var allow_alphabets = true;
    }

    if (formData.get("specialchars") == null) {
        var allow_specialchars = false;
    } else {
        var allow_specialchars = true;
    }

    if (allow_digits == false && allow_alphabets == false && allow_specialchars == false) {
        $("#checkbox-error").show();
        return
    } else {
        $("#checkbox-error").hide();
    }

    var url = "/generate/" + length + "/" + allow_digits + "/" + allow_alphabets + "/" + allow_specialchars;

    $.ajax({
        url: url,
        type: "POST",
        dataType: "json",
        success: function (data) {
            console.log(data)
            $("#password").html(data.password);
            $("#password").css("color", "#cccccc");
            $("#pw-box").show();
        }
    });
}