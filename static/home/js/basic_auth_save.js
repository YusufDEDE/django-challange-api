$(document).ready(function () {
  $("#auth_from").submit(function (event) {
    let auth_data = {
      username: $("#username").val(),
      password: $("#password").val(),
    };

    localStorage.setItem("auth_info", JSON.stringify(auth_data, null, ' '));

    iziToast.success({
        title: 'Basic Authentication Save',
        message: 'Success!',
    });

    $('#exampleModal').modal('hide')

    event.preventDefault();
  });
});