const json_body = localStorage.getItem('auth_info');

$(document).ready(function () {
    const defaultUserMeGetJSON = {
     "bio": [
      {
       "username": "",
       "first_name": "",
       "last_name": "",
       "email": "",
       "phone": "",
       "about_us": ""
      }
     ]
    }

    $('#userMeGet').text(JSON.stringify(defaultUserMeGetJSON, null, ' '))
    hljs.highlightBlock(document.getElementById('userMeGet'))
})

function make_base_auth(user, password) {
  const token = `${user}:${password}`;
  const hash = btoa(token);
  return `Basic ${hash}`;
}

function getUserBio() {
    const auth_info = JSON.parse(localStorage.getItem('auth_info'))

    if (!auth_info) {
        iziToast.info({
            title: 'Basic Authentication',
            message: 'Request for Basic Authentication Save..',
        });
    }

    const basic_auth_token = make_base_auth(auth_info.username, auth_info.password)

    $.ajax
      ({
        type: "GET",
        url: "/users/me",
        dataType: 'json',
        async: false,
        data: '{}',
        beforeSend: function (xhr){
            xhr.setRequestHeader('Authorization', basic_auth_token);
        },
        success: function (data){
            iziToast.success({
                title: 'GET /users/me',
                message: 'Success Request/Response!',
            });

            $('#userMeGet').text(JSON.stringify(data, null, ' '))

            hljs.highlightBlock(document.getElementById('userMeGet'))
        },
        error: function (err) {
            if (err.status == 403) {
                 iziToast.error({
                    title: 'Auth Error',
                    message: 'Basic Authentication Username or Password Wrong!',
                 });
            }
        }
    });
}